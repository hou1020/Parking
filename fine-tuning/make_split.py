"""
Spatial train/test split of the 100 validation cells — Leeds fine-tuning experiment
Author: Hou

Adjacent 512 px patches share the same car parks, so a patch-level random split leaks the
test set into training. The split is therefore made at cell level. Each Digimap GeoTIFF is
exactly one OS 1 km square and exactly one validation cell, so patches never cross a cell
boundary and a cell-level split is airtight.

Two things are balanced across the halves, because both are known from the main analysis to
drive measured accuracy:

    distance from the city centre   the urban gradient; parking share falls with it
    labelled parking area           the strongest single predictor of per-cell precision
                                    (r = +0.54 controlling for distance)

Within each distance band cells are ordered by labelled area and assigned by constrained
greedy balancing: each half has a cell-count quota and the next cell goes to the currently
smaller labelled-area total. Without this, a fine-tuning "improvement" could be nothing
more than the test half being easier than the training half.

Reads read-only. Writes only into this folder.
Outputs:
  - split.csv
  - split.png
"""
import os
import geopandas as gpd
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import warnings; warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
GRID = f"{ROOT}/manual/leeds_grid.gpkg"
MANUAL = f"{ROOT}/manual/leeds_manual.gpkg"
OUT_CSV = f"{HERE}/split.csv"
OUT_FIG = f"{HERE}/split.png"

CENTRE = (429832.0, 433449.0)          # Leeds City Square, EPSG:27700
BANDS = [0, 1, 2, 3, 4, 99]
BAND_LABELS = ["<1", "1-2", "2-3", "3-4", ">4"]
INK, TRAIN_C, TEST_C = "#1f2933", "#4878a8", "#c9412e"


def log(m):
    print(m, flush=True)


log("reading layers ...")
grid = gpd.read_file(GRID).to_crs(27700)
man = gpd.read_file(MANUAL).to_crs(27700)
man["geometry"] = man.geometry.buffer(0)

# labelled area per cell, from the dissolved reference so overlaps are not double counted
man_u = gpd.GeoDataFrame(geometry=[man.geometry.union_all()], crs=27700)
joined = gpd.overlay(grid[["id", "geometry"]], man_u, how="intersection")
area_by_cell = joined.dissolve("id").geometry.area

grid["manual_m2"] = grid["id"].map(area_by_cell).fillna(0.0)
cen = grid.geometry.centroid
grid["dist_km"] = np.hypot(cen.x - CENTRE[0], cen.y - CENTRE[1]) / 1000.0
grid["band"] = pd.cut(grid["dist_km"], bins=BANDS, labels=BAND_LABELS)
grid["cell"] = "c" + grid["col_index"].astype(str) + "r" + grid["row_index"].astype(str)

# Within each band, walk cells from largest labelled area down and give each to whichever
# half currently holds less labelled area, subject to neither half taking more than half the
# cells in that band. Balancing counts alone (simple alternation) leaves the halves ~11%
# apart on labelled area, because the ordering hands the largest cell of every band to the
# same side. Where a band has an odd number of cells the spare alternates between halves.
grid["split"] = ""
spare = 0
for b in BAND_LABELS:
    sel = grid.index[grid["band"] == b]
    order = grid.loc[sel].sort_values("manual_m2", ascending=False).index
    cap = {"train": len(sel) // 2, "test": len(sel) // 2}
    if len(sel) % 2:
        cap["train" if spare % 2 == 0 else "test"] += 1
        spare += 1
    got = {"train": 0.0, "test": 0.0}
    n = {"train": 0, "test": 0}
    for i in order:
        allowed = [s for s in ("train", "test") if n[s] < cap[s]]
        s = min(allowed, key=lambda k: got[k])
        grid.loc[i, "split"] = s
        got[s] += grid.loc[i, "manual_m2"]
        n[s] += 1

cols = ["cell", "id", "col_index", "row_index", "left", "bottom", "right", "top",
        "dist_km", "band", "manual_m2", "split"]
out = grid[cols].copy()
out["dist_km"] = out["dist_km"].round(3)
out["manual_m2"] = out["manual_m2"].round(1)
out.sort_values(["split", "cell"]).to_csv(OUT_CSV, index=False)
log(f"wrote: {OUT_CSV}")

log("\nbalance check")
summary = out.groupby("split").agg(cells=("cell", "size"),
                                   labelled_km2=("manual_m2", lambda s: s.sum() / 1e6),
                                   mean_dist_km=("dist_km", "mean"))
log(summary.round(4).to_string())
log("\ncells per distance band")
log(pd.crosstab(out["band"], out["split"]).to_string())

fig, ax = plt.subplots(figsize=(6.6, 6.8))
for s, c in [("train", TRAIN_C), ("test", TEST_C)]:
    grid[grid["split"] == s].plot(ax=ax, facecolor=c, alpha=.35, edgecolor=c, lw=.8)
man.plot(ax=ax, facecolor=INK, edgecolor="none", zorder=3)
ax.plot(*CENTRE, marker="o", ms=7, mfc="white", mec=INK, mew=1.6, zorder=4)
ax.legend(handles=[
    Line2D([], [], color=TRAIN_C, lw=8, alpha=.5, label=f"train ({(out.split=='train').sum()} cells)"),
    Line2D([], [], color=TEST_C, lw=8, alpha=.5, label=f"held out ({(out.split=='test').sum()} cells)"),
    Line2D([], [], color=INK, lw=6, label="labelled parking"),
], loc="upper left", fontsize=8, frameon=True, framealpha=.95)
ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
for sp in ax.spines.values():
    sp.set_visible(False)
ax.set_title("Cell-level split, balanced on distance and labelled area",
             fontsize=10, color=INK, pad=10)
fig.tight_layout(); fig.savefig(OUT_FIG, dpi=200, bbox_inches="tight", facecolor="white")
log(f"\nwrote: {OUT_FIG}")
