"""
Model accuracy vs location — Leeds
Author: Hou

Tests whether the model's per-cell accuracy varies with position in the city,
and whether any such pattern is really a distance effect or simply reflects how
much parking a cell contains.

Steps
  1. Distance from each 1 km2 grid cell centroid to the city centre.
  2. Join to the per-cell validation metrics (validation_percell.csv).
  3. Correlations (Pearson and Spearman) of distance with precision / recall /
     IoU, and of parking amount with the same, plus partial correlations of
     distance controlling for parking amount (and vice versa).
  4. Metrics averaged over distance bands.
  5. Scatter figure.

City centre is defined by a landmark coordinate (Leeds City Square), given in
WGS84 below and projected to British National Grid, so it can be checked and
changed in one place.

Reads read-only. Writes only the outputs below, in this folder.
Outputs:
  - accuracy_vs_distance.csv          : per-cell distance + metrics
  - accuracy_vs_distance_summary.csv  : correlations and distance bands
  - accuracy_vs_distance.png          : scatter figure
"""
import os
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
GRID = f"{ROOT}/manual/leeds_grid.gpkg"
PERCELL = f"{HERE}/validation_percell.csv"

OUT_CELLS = f"{HERE}/accuracy_vs_distance.csv"
OUT_SUMMARY = f"{HERE}/accuracy_vs_distance_summary.csv"
OUT_FIG = f"{HERE}/accuracy_vs_distance.png"

# City centre: Leeds City Square (WGS84). Change here if a different centre is wanted.
CENTRE_LATLON = (53.7965, -1.5486)
BANDS = [0, 1, 2, 3, 4, 99]
BAND_LABELS = ["<1", "1-2", "2-3", "3-4", ">4"]

centre = gpd.GeoSeries([Point(CENTRE_LATLON[1], CENTRE_LATLON[0])], crs=4326).to_crs(27700).iloc[0]
print(f"city centre (BNG): E {centre.x:.0f}  N {centre.y:.0f}")

grid = gpd.read_file(GRID).to_crs(27700)
cen = grid.geometry.centroid
grid["dist_km"] = cen.distance(centre) / 1000.0
grid["col_index"] = grid["col_index"].astype(int)
grid["row_index"] = grid["row_index"].astype(int)

pc = pd.read_csv(PERCELL)
df = grid[["col_index", "row_index", "dist_km"]].merge(pc, on=["col_index", "row_index"], how="inner")
df["parking_share"] = df["manual_all_m2"] / 1e6          # cell is 1 km2
df["model_over_manual"] = df["model_m2"] / df["manual_all_m2"].replace(0, np.nan)
df = df.sort_values("dist_km").reset_index(drop=True)
df.to_csv(OUT_CELLS, index=False)
print(f"cells: {len(df)}, distance range {df.dist_km.min():.2f}-{df.dist_km.max():.2f} km")

METRICS = ["prec_all", "rec_all", "iou_all"]


def partial_corr(x, y, z):
    """Correlation of x and y after removing the linear effect of z."""
    ok = np.isfinite(x) & np.isfinite(y) & np.isfinite(z)
    x, y, z = x[ok], y[ok], z[ok]
    rx = x - np.polyval(np.polyfit(z, x, 1), z)
    ry = y - np.polyval(np.polyfit(z, y, 1), z)
    return stats.pearsonr(rx, ry)


rows = []
d = df["dist_km"].to_numpy()
p = df["parking_share"].to_numpy()
for m in METRICS:
    v = df[m].to_numpy(dtype=float)
    ok = np.isfinite(v)
    pr, pp = stats.pearsonr(d[ok], v[ok])
    sr, sp = stats.spearmanr(d[ok], v[ok])
    rows.append({"test": f"distance vs {m}", "n": int(ok.sum()),
                 "pearson_r": round(pr, 3), "pearson_p": round(pp, 4),
                 "spearman_r": round(sr, 3), "spearman_p": round(sp, 4)})
    pr2, pp2 = stats.pearsonr(p[ok], v[ok])
    sr2, sp2 = stats.spearmanr(p[ok], v[ok])
    rows.append({"test": f"parking_share vs {m}", "n": int(ok.sum()),
                 "pearson_r": round(pr2, 3), "pearson_p": round(pp2, 4),
                 "spearman_r": round(sr2, 3), "spearman_p": round(sp2, 4)})
    r3, p3 = partial_corr(d, v, p)
    rows.append({"test": f"distance vs {m} | controlling parking_share", "n": int(ok.sum()),
                 "pearson_r": round(r3, 3), "pearson_p": round(p3, 4),
                 "spearman_r": "", "spearman_p": ""})
    r4, p4 = partial_corr(p, v, d)
    rows.append({"test": f"parking_share vs {m} | controlling distance", "n": int(ok.sum()),
                 "pearson_r": round(r4, 3), "pearson_p": round(p4, 4),
                 "spearman_r": "", "spearman_p": ""})

# distance vs parking amount itself
r5, p5 = stats.pearsonr(d, p)
s5, sp5 = stats.spearmanr(d, p)
rows.append({"test": "distance vs parking_share", "n": len(d),
             "pearson_r": round(r5, 3), "pearson_p": round(p5, 4),
             "spearman_r": round(s5, 3), "spearman_p": round(sp5, 4)})

corr_df = pd.DataFrame(rows)

df["band_km"] = pd.cut(df["dist_km"], bins=BANDS, labels=BAND_LABELS)
band = df.groupby("band_km", observed=True).agg(
    n_cells=("dist_km", "size"),
    mean_dist_km=("dist_km", "mean"),
    manual_km2=("manual_all_m2", lambda s: s.sum()/1e6),
    model_km2=("model_m2", lambda s: s.sum()/1e6),
    mean_parking_share=("parking_share", "mean"),
    mean_precision=("prec_all", "mean"),
    mean_recall=("rec_all", "mean"),
    mean_iou=("iou_all", "mean"),
).round(3).reset_index()

with open(OUT_SUMMARY, "w") as f:
    f.write("# correlations\n")
    corr_df.to_csv(f, index=False)
    f.write("\n# distance bands (km from city centre)\n")
    band.to_csv(f, index=False)

fig, ax = plt.subplots(2, 2, figsize=(11, 8))
for a, m, t in [(ax[0, 0], "prec_all", "Precision"), (ax[0, 1], "rec_all", "Recall"),
                (ax[1, 0], "iou_all", "IoU")]:
    a.scatter(df["dist_km"], df[m], s=26, alpha=0.75, edgecolor="none")
    ok = np.isfinite(df[m])
    if ok.sum() > 2:
        z = np.polyfit(df["dist_km"][ok], df[m][ok], 1)
        xs = np.linspace(df["dist_km"].min(), df["dist_km"].max(), 50)
        a.plot(xs, np.polyval(z, xs), lw=1.4, color="crimson")
    a.set_xlabel("distance from city centre (km)"); a.set_ylabel(t)
    a.set_title(f"{t} vs distance"); a.grid(alpha=.3)
ax[1, 1].scatter(df["parking_share"]*100, df["iou_all"], s=26, alpha=0.75,
                 c=df["dist_km"], cmap="viridis", edgecolor="none")
ax[1, 1].set_xlabel("parking share of cell (%)"); ax[1, 1].set_ylabel("IoU")
ax[1, 1].set_title("IoU vs parking amount (colour = distance)"); ax[1, 1].grid(alpha=.3)
fig.suptitle("Per-cell model accuracy vs location, Leeds (1 km² cells)")
fig.tight_layout()
fig.savefig(OUT_FIG, dpi=150)

print(f"\nwrote: {OUT_CELLS}\nwrote: {OUT_SUMMARY}\nwrote: {OUT_FIG}")
print("\n=== CORRELATIONS ===")
print(corr_df.to_string(index=False))
print("\n=== DISTANCE BANDS ===")
print(band.to_string(index=False))
