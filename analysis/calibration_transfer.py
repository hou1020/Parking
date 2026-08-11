"""
Does the calibration factor transfer? — Leeds
Author: Hou

The model over-predicts parking area by half, but the bias is measurable: for a
map with precision p and recall r, predicted area A relates to true area T as
A x p = TP = T x r, so T = A x (p/r). Applied to the cells the factor was fitted
on this is an identity and carries no information. The question that matters for
using the model anywhere else is whether a factor fitted on one part of the city
predicts another part, and at what spatial grain it stops working.

Three hold-out schemes, each fitting p/r on a training set of cells and applying
it to cells the fit never saw:

    random half   200 random splits of the cells into equal halves. Tests
                  transfer to a comparable area of the same city.
    distance band leave one distance band out. Tests transfer across the urban
                  gradient, which is the harder case, since parking density and
                  built form both change with distance from the centre.
    leave one out fit on all but one cell, predict that cell. Tests the finest
                  grain the estimator could be used at.

Error is reported as (calibrated prediction - labelled area) / labelled area for
the held-out set.

Note what the factor reduces to. With p = TP/A and r = TP/T, the ratio p/r is
exactly T/A: the labelled area of the training cells divided by their predicted
area. The estimator therefore needs only a labelled total area on a sample of
cells, not a full per-object error analysis — which is what makes calibrating it
in a second city affordable. Precision and recall are not thrown away by saying
so; they are what establishes that the bias is systematic rather than noise, and
the hold-out test below is what establishes the grain at which it holds.

Two implementation points. Per-cell true positives are recovered as
TP = precision x model area, and p and r are then aggregated micro, as
sum(TP)/sum(model) and sum(TP)/sum(manual); averaging per-cell precision directly
would give the macro figure (0.5136 rather than 0.5708) and a factor to match.
One cell contains no labelled parking, so it has no defined relative error and is
excluded from the leave-one-out scheme, leaving 99; this is the same cell that
makes recall undefined in the per-cell table. Relative error is unstable where
the denominator is small, which inflates the leave-one-out mean above its median;
a median absolute error in km2 is reported alongside for that scheme.

Reads read-only. Writes only the outputs below.
Outputs:
  - calibration_transfer_summary.csv
  - calibration_transfer.png
"""
import os, csv
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
PERCELL = f"{HERE}/accuracy_vs_distance.csv"
OUT_CSV = f"{HERE}/calibration_transfer_summary.csv"
OUT_FIG = f"{HERE}/calibration_transfer.png"

N_SPLITS = 200
SEED = 42
BANDS = [0, 1, 2, 3, 4, 99]
BAND_LABELS = ["<1", "1-2", "2-3", "3-4", ">4"]


def log(m):
    print(m, flush=True)


d = pd.read_csv(PERCELL)
# recover per-cell true positives, then aggregate micro
d["tp_m2"] = d["prec_all"].fillna(0) * d["model_m2"]
d["band_km"] = pd.cut(d["dist_km"], bins=BANDS, labels=BAND_LABELS)


def factor(df):
    """Micro-aggregated p/r over a set of cells."""
    tp, mod, man = df["tp_m2"].sum(), df["model_m2"].sum(), df["manual_all_m2"].sum()
    if mod == 0 or man == 0:
        return np.nan
    return (tp / mod) / (tp / man)          # = manual/model, by construction


def rel_error(train, test):
    """Relative error of the calibrated estimate on held-out cells."""
    f = factor(train)
    if not np.isfinite(f) or test["manual_all_m2"].sum() == 0:
        return np.nan
    pred = test["model_m2"].sum() * f
    return (pred - test["manual_all_m2"].sum()) / test["manual_all_m2"].sum()


def abs_error_km2(train, test):
    """Signed error of the calibrated estimate in km2, for when the relative
    error has a small and unstable denominator."""
    f = factor(train)
    if not np.isfinite(f):
        return np.nan
    return (test["model_m2"].sum() * f - test["manual_all_m2"].sum()) / 1e6


f_all = factor(d)
log(f"cells: {len(d)}")
log(f"whole-area factor p/r = {f_all:.4f}   "
    f"(model {d['model_m2'].sum()/1e6:.4f} -> {d['model_m2'].sum()*f_all/1e6:.4f} km2, "
    f"labelled {d['manual_all_m2'].sum()/1e6:.4f} km2)")

rows = []


def add(scheme, errs, n, note="", pct_cols=True):
    """pct_cols=False where there are too few tests for a share to mean anything;
    the individual errors are reported instead."""
    e = np.array([x for x in errs if np.isfinite(x)]) * 100
    rows.append({"scheme": scheme, "n_tests": len(e),
                 "mean_error_pct": round(float(e.mean()), 1),
                 "sd_pct": round(float(e.std(ddof=1)), 1) if len(e) > 1 else None,
                 "median_error_pct": round(float(np.median(e)), 1),
                 "p05_pct": round(float(np.percentile(e, 5)), 1),
                 "p95_pct": round(float(np.percentile(e, 95)), 1),
                 "within_10pct": round(100 * float((np.abs(e) <= 10).mean()), 0) if pct_cols else None,
                 "within_25pct": round(100 * float((np.abs(e) <= 25).mean()), 0) if pct_cols else None,
                 "cells_held_out": n, "note": note})
    return e


rng = np.random.default_rng(SEED)
idx = d.index.to_numpy()

# 1 random half split
errs = []
for _ in range(N_SPLITS):
    perm = rng.permutation(idx)
    half = len(perm) // 2
    errs.append(rel_error(d.loc[perm[:half]], d.loc[perm[half:]]))
e_half = add("random half split", errs, len(idx) // 2, f"{N_SPLITS} splits")

# 2 leave one distance band out
errs, band_rows = [], []
for b in BAND_LABELS:
    test = d[d["band_km"] == b]
    if not len(test):
        continue
    err = rel_error(d[d["band_km"] != b], test)
    errs.append(err)
    band_rows.append({"band": b, "n_cells": len(test),
                      "error_pct": round(100 * err, 1) if np.isfinite(err) else None})
e_band = add("leave one distance band out", errs, None,
             "only 5 tests, so no share is quoted; see the per-band errors below. "
             "the <1 km band holds only 2 cells",
             pct_cols=False)

# 3 leave one cell out, excluding the cell with no labelled parking
usable = d[d["manual_all_m2"] > 0]
errs = [rel_error(usable.drop(i), usable.loc[[i]]) for i in usable.index]
abs_km2 = np.array([abs_error_km2(usable.drop(i), usable.loc[[i]]) for i in usable.index])
e_loo = add("leave one cell out", errs, 1,
            f"n = {len(usable)}; the cell with no labelled parking is excluded. "
            f"the mean sits above the median because relative error is unstable "
            f"where a cell holds little parking; median absolute error "
            f"{np.median(np.abs(abs_km2)):.4f} km2 per cell against a mean labelled "
            f"{usable['manual_all_m2'].mean()/1e6:.4f} km2")

with open(OUT_CSV, "w", newline="") as f:
    cols = ["scheme", "n_tests", "mean_error_pct", "sd_pct", "median_error_pct",
            "p05_pct", "p95_pct", "within_10pct", "within_25pct", "cells_held_out", "note"]
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    w.writerow({})
    w.writerow({"scheme": "whole-area factor p/r", "mean_error_pct": round(f_all, 4)})
    w.writerow({})
    w.writerow({"scheme": "by distance band", "n_tests": "n_cells", "mean_error_pct": "error_pct"})
    for b in band_rows:
        w.writerow({"scheme": b["band"], "n_tests": b["n_cells"], "mean_error_pct": b["error_pct"]})

log(f"\nwrote: {OUT_CSV}\n")
log(pd.DataFrame(rows)[["scheme", "n_tests", "mean_error_pct", "sd_pct",
                        "p05_pct", "p95_pct", "within_25pct"]].to_string(index=False))
log("\nby distance band:")
log(pd.DataFrame(band_rows).to_string(index=False))

fig, ax = plt.subplots(1, 3, figsize=(14, 4))
for a, e, t in [(ax[0], e_half, "Random half split"),
                (ax[1], e_band, "Leave one distance band out"),
                (ax[2], e_loo, "Leave one cell out")]:
    a.hist(e, bins=min(25, max(5, len(e) // 3)), color="#4878a8", edgecolor="white")
    a.axvline(0, color="black", lw=1)
    a.axvline(np.median(e), color="crimson", lw=1.4,
              label=f"median {np.median(e):+.1f}%")
    a.set_xlabel("error of calibrated estimate (%)")
    a.set_ylabel("held-out sets"); a.set_title(t)
    a.legend(fontsize=8); a.grid(alpha=.3)
fig.suptitle("Transferability of the calibration factor, Leeds")
fig.tight_layout(); fig.savefig(OUT_FIG, dpi=150)
log(f"\nwrote: {OUT_FIG}")
