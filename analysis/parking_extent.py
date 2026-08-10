"""
How much land is surface parking, and where — Leeds
Author: Hou

Answers RQ3 from what the validation already produced: the extent and internal
distribution of surface parking in the study area, reported with the uncertainty
the accuracy assessment established.

Three things are reported.

  Extent      Labelled and predicted parking as a share of the 100 km2 study
              area. The predicted figure is an upper bound: the model over-
              predicts by roughly half.

  Distribution
              Parking share by distance band from the city centre, and the
              per-cell distribution, so the internal pattern is visible rather
              than only the total.

  Calibration The reason the over-prediction matters less than it appears. For a
              map with measured precision p and recall r, the predicted area A
              relates to the true area T as A x p = TP = T x r, so T = A x p/r.
              In Leeds this is an identity, since p and r were measured there.
              Its value is that the bias is a measurable, correctable quantity
              rather than noise: the factor can in principle be carried to other
              cities, though whether it transfers is untested and is left as
              further work.

Scope note: this quantifies extent and pattern only. It does not assess whether
any site could or should be developed.

Reads read-only. Writes only the outputs below.
Outputs:
  - parking_extent_summary.csv   : extent, by distance band and overall
  - parking_extent.png           : per-cell parking share, map and distribution
"""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
PERCELL = f"{HERE}/accuracy_vs_distance.csv"     # per-cell metrics + distance
OUT_CSV = f"{HERE}/parking_extent_summary.csv"
OUT_FIG = f"{HERE}/parking_extent.png"

CELL_KM2 = 1.0
BANDS = [0, 1, 2, 3, 4, 99]
BAND_LABELS = ["<1", "1-2", "2-3", "3-4", ">4"]
# measured on the validation grid
PRECISION, RECALL = 0.5708, 0.8543


def log(m):
    print(m, flush=True)


d = pd.read_csv(PERCELL)
d["manual_km2"] = d["manual_all_m2"] / 1e6
d["model_km2"] = d["model_m2"] / 1e6
d["manual_share"] = 100 * d["manual_km2"] / CELL_KM2
d["model_share"] = 100 * d["model_km2"] / CELL_KM2
d["band_km"] = pd.cut(d["dist_km"], bins=BANDS, labels=BAND_LABELS)

area_km2 = len(d) * CELL_KM2
man_tot, mod_tot = d["manual_km2"].sum(), d["model_km2"].sum()
calib = PRECISION / RECALL

rows = []


def add(scope, n, man, mod, note=""):
    rows.append({"scope": scope, "n_cells": n, "area_km2": round(n * CELL_KM2, 1),
                 "labelled_km2": round(man, 4),
                 "labelled_pct_of_area": round(100 * man / (n * CELL_KM2), 2),
                 "predicted_km2": round(mod, 4),
                 "predicted_pct_of_area": round(100 * mod / (n * CELL_KM2), 2),
                 "calibrated_km2": round(mod * calib, 4),
                 "calibrated_pct_of_area": round(100 * mod * calib / (n * CELL_KM2), 2),
                 "note": note})


add("whole study area", len(d), man_tot, mod_tot, "100 x 1 km2 cells")
for lab, g in d.groupby("band_km", observed=True):
    add(f"{lab} km from centre", len(g), g["manual_km2"].sum(), g["model_km2"].sum(),
        "few cells, read with caution" if len(g) < 5 else "")

out = pd.DataFrame(rows)
out.to_csv(OUT_CSV, index=False)
log(f"wrote: {OUT_CSV}\n")
log("=== EXTENT ===")
log(out[["scope", "n_cells", "labelled_km2", "labelled_pct_of_area",
         "predicted_km2", "predicted_pct_of_area", "calibrated_km2"]].to_string(index=False))

log(f"\n=== CALIBRATION ===")
log(f"measured precision {PRECISION:.4f}, recall {RECALL:.4f}")
log(f"factor p/r = {calib:.4f}")
log(f"predicted {mod_tot:.4f} km2  x {calib:.4f}  = {mod_tot*calib:.4f} km2")
log(f"labelled                                    {man_tot:.4f} km2")
log(f"over-prediction before calibration: {mod_tot/man_tot:.2f}x")

log(f"\n=== PER-CELL DISTRIBUTION (labelled parking share, % of cell) ===")
log(d["manual_share"].describe().round(2).to_string())
q = d["manual_share"].quantile([.5, .75, .9, .95]).round(2)
top = d.nlargest(5, "manual_share")[["col_index", "row_index", "dist_km", "manual_share"]]
log(f"\ncells above 10% parking: {(d['manual_share'] > 10).sum()}")
log("highest cells:")
log(top.round(2).to_string(index=False))

# ---- figure ----
fig, ax = plt.subplots(1, 3, figsize=(15, 4.4))

piv = d.pivot(index="row_index", columns="col_index", values="manual_share")
im = ax[0].imshow(piv.values, origin="lower", cmap="YlOrRd")
ax[0].set_title("Labelled parking, % of each km² cell")
ax[0].set_xlabel("column"); ax[0].set_ylabel("row")
fig.colorbar(im, ax=ax[0], fraction=0.046)

ax[1].scatter(d["dist_km"], d["manual_share"], s=26, alpha=.75, label="labelled")
ax[1].scatter(d["dist_km"], d["model_share"], s=18, alpha=.45, label="predicted")
band = d.groupby("band_km", observed=True)["manual_share"].mean()
centres = [0.5, 1.5, 2.5, 3.5, 5.5]
ax[1].plot(centres[:len(band)], band.values, color="crimson", lw=1.6, marker="o",
           label="band mean, labelled")
ax[1].set_xlabel("distance from city centre (km)")
ax[1].set_ylabel("parking share of cell (%)")
ax[1].set_title("Parking share vs distance"); ax[1].legend(fontsize=8); ax[1].grid(alpha=.3)

ax[2].hist(d["manual_share"], bins=20, color="#4878a8", edgecolor="white")
ax[2].axvline(d["manual_share"].mean(), color="crimson", lw=1.4,
              label=f"mean {d['manual_share'].mean():.1f}%")
ax[2].set_xlabel("parking share of cell (%)"); ax[2].set_ylabel("cells")
ax[2].set_title("Distribution across cells"); ax[2].legend(fontsize=8); ax[2].grid(alpha=.3)

fig.suptitle("Extent and distribution of surface parking, Leeds study area (100 km²)")
fig.tight_layout()
fig.savefig(OUT_FIG, dpi=150)
log(f"\nwrote: {OUT_FIG}")
