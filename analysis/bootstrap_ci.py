"""
Confidence intervals for the sampled estimates — Leeds
Author: Hou

sampling_results.py scales the inspected chips back to their populations with a
stratified ratio estimator, but reports point estimates only. The good practice
this study follows asks for the uncertainty as well (Olofsson et al., 2014), and
without it there is no way to tell whether the corrected accuracy figures of
§4.6 would survive a different draw of 142 polygons. This supplies that.

Method
    The estimator is the one already in use: for stratum h of known population
    area A_h,
        A_c = sum_h A_h * (sampled area in category c) / (total sampled area)

    Uncertainty arises from having inspected a sample rather than the whole
    population, so the inspected polygons are resampled with replacement WITHIN
    each stratum, n_h at a time, and the estimator recomputed. Each population
    is resampled once per replicate and every quantity derived from that same
    resample, so categories drawn from one sample stay correlated. That matters
    here: the prediction-side and definitional corrections both come from
    fp_other, and their shares cannot move independently.

Finite population correction
    A plain bootstrap assumes a small sample from a large population, which is
    false in several strata. The largest missed-lot stratum was inspected in
    full, 17 of 17: it was counted, not sampled, and has no sampling variance at
    all. Each replicate's deviation from the observed share is therefore scaled
    by sqrt(1 - f_h), f_h = n_h / N_h. At f_h = 1 the scale is zero and the
    stratum contributes nothing to the spread, which is correct for a census;
    at f_h near zero the deviation passes through unchanged.

What the intervals cover
    Sampling variance only. They do not cover adjudication error, since every
    chip was judged once by one person, and they do not cover the sampling
    frame's exclusion of polygons below 100 m2 (11.7% of the unexplained-FP
    population), which is a coverage limit rather than a variance.

Reads the inspected chips and the strata table read-only. Writes only the two
outputs below, in this folder.
Outputs:
  - bootstrap_ci_results.csv      : sampling_results.csv with 95% intervals
  - bootstrap_ci_corrections.csv  : sampling_corrections.csv with 95% intervals
"""
import os, csv
import numpy as np
import pandas as pd
import warnings; warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = f"{HERE}/chips/index.csv"
STRATA = f"{HERE}/sampling_strata.csv"
POINT = f"{HERE}/sampling_results.csv"
OUT_RESULTS = f"{HERE}/bootstrap_ci_results.csv"
OUT_CORR = f"{HERE}/bootstrap_ci_corrections.csv"

B, SEED = 5000, 42
# headline areas from validate_removal_vs_manual.py, km2
MANUAL, MODEL, TP = 3.2597, 4.8785, 2.7848
# spellings seen in the filled worksheet, mapped to the defined categories
FIXES = {"irrgular_layout": "irregular_layout", "no_obivious_reason": "no_obvious_reason",
         "irregular_surface": "unusual_surface"}


def log(m):
    print(m, flush=True)


d = pd.read_csv(INDEX)
d["category"] = d["category"].astype(str).str.strip().replace(FIXES)
d = d[~d["category"].isin(["", "nan", "None"])]
strata = pd.read_csv(STRATA)
rng = np.random.default_rng(SEED)

pops = {src: (g, strata[strata["source"] == src].set_index("stratum"))
        for src, g in d.groupby("source")}


def estimate(g, st, resample):
    """Estimated area per category, km2. resample=False gives the point estimate."""
    est = {}
    for stratum, gg in g.groupby("stratum"):
        if stratum not in st.index:
            continue
        A_h = st.loc[stratum, "area_population_m2"]
        f_h = st.loc[stratum, "n_sampled"] / st.loc[stratum, "n_population"]
        scale = np.sqrt(max(0.0, 1.0 - f_h))          # 0 where the stratum is a census
        a, cats = gg["area_m2"].to_numpy(), gg["category"].to_numpy()
        tot = a.sum()
        idx = rng.integers(0, len(a), len(a)) if resample else np.arange(len(a))
        ba, bc = a[idx], cats[idx]
        btot = ba.sum()
        for cat in set(cats):
            p = a[cats == cat].sum() / tot
            if resample and btot > 0:
                p = p + scale * (ba[bc == cat].sum() / btot - p)
            est[cat] = est.get(cat, 0.0) + A_h * max(0.0, p) / 1e6
    return est


log(f"inspected: {len(d)} polygons across {len(pops)} populations")
point = {src: estimate(g, st, False) for src, (g, st) in pops.items()}

# the point estimates must reproduce sampling_results.py exactly
ref = pd.read_csv(POINT)
worst = max(abs(point[r["source"]].get(r["category"], 0.0) - r["est_area_km2"])
            for _, r in ref.iterrows() if r["category"] != "TOTAL")
log(f"point estimates match sampling_results.csv to {worst:.6f} km2")

draws = {src: [] for src in pops}
corr = []
for _ in range(B):
    rep = {src: estimate(g, st, True) for src, (g, st) in pops.items()}
    for src in pops:
        draws[src].append(rep[src])
    mism = rep["fn_other"].get("not_parking_in_digimap", 0.0)
    miss = rep["fp_other"].get("real_parking_missed", 0.0)
    defn = rep["fp_other"].get("on_street", 0.0) + rep["fp_other"].get("private_driveway", 0.0)
    man2 = MANUAL - mism
    tp3, man3, mod4 = TP + miss, man2 + miss, MODEL - defn
    corr.append({
        "mismatch": mism, "missed": miss, "definitional": defn,
        "2_precision": TP / MODEL, "2_recall": TP / man2,
        "2_iou": TP / (MODEL + man2 - TP),
        "3_precision": tp3 / MODEL, "3_recall": tp3 / man3,
        "3_iou": tp3 / (MODEL + man3 - tp3),
        "4_precision": tp3 / mod4, "4_recall": tp3 / man3,
        "4_iou": tp3 / (mod4 + man3 - tp3),
    })

ci = lambda v: (float(np.percentile(v, 2.5)), float(np.percentile(v, 97.5)))

rows = []
for src, (g, st) in pops.items():
    pop = st["area_population_m2"].sum() / 1e6
    for cat, a in sorted(point[src].items(), key=lambda kv: -kv[1]):
        lo, hi = ci([r.get(cat, 0.0) for r in draws[src]])
        n = int((g["category"] == cat).sum())
        rows.append({"source": src, "category": cat, "n_sampled": n,
                     "est_area_km2": round(a, 4),
                     "ci_lo_km2": round(lo, 4), "ci_hi_km2": round(hi, 4),
                     "pct_of_population": round(100 * a / pop, 1),
                     "pct_ci_lo": round(100 * lo / pop, 1),
                     "pct_ci_hi": round(100 * hi / pop, 1),
                     "note": "stratum inspected in full, no sampling variance"
                             if hi - lo < 1e-9 else ""})
pd.DataFrame(rows).to_csv(OUT_RESULTS, index=False)

c = pd.DataFrame(corr)

# point estimates of the four variants, from the unresampled estimates, so the
# table carries the same numbers as sampling_corrections.csv and the interval
# is attached to them rather than to the bootstrap mean
# rounded to 4 dp first, as sampling_results.py does, so the two agree exactly
pm = round(point["fn_other"].get("not_parking_in_digimap", 0.0), 4)
pmi = round(point["fp_other"].get("real_parking_missed", 0.0), 4)
pdf = round(point["fp_other"].get("on_street", 0.0), 4) + \
      round(point["fp_other"].get("private_driveway", 0.0), 4)
_man2 = MANUAL - pm
_tp3, _man3, _mod4 = TP + pmi, _man2 + pmi, MODEL - pdf
PT = {
    "2": (TP / MODEL, TP / _man2, TP / (MODEL + _man2 - TP)),
    "3": (_tp3 / MODEL, _tp3 / _man3, _tp3 / (MODEL + _man3 - _tp3)),
    "4": (_tp3 / _mod4, _tp3 / _man3, _tp3 / (_mod4 + _man3 - _tp3)),
}
PT_INPUT = {"mismatch": pm, "missed": pmi, "definitional": pdf}

crows = []
for v, lab in [("1", "1 as measured"), ("2", "2 + reference side"),
               ("3", "3 + prediction side"), ("4", "4 effective")]:
    if v == "1":
        crows.append({"variant": lab, "precision": 0.5708, "recall": 0.8543, "iou": 0.5202,
                      "note": "no sampled input, so no interval"})
        continue
    row = {"variant": lab}
    for m, pt in zip(("precision", "recall", "iou"), PT[v]):
        lo, hi = ci(c[f"{v}_{m}"])
        row[m] = round(pt, 4)
        row[f"{m}_lo"] = round(lo, 4)
        row[f"{m}_hi"] = round(hi, 4)
    crows.append(row)
for k, lab in [("mismatch", "input: reference side, not parking in Digimap"),
               ("missed", "input: prediction side, parking never labelled"),
               ("definitional", "input: on-street + private driveways")]:
    lo, hi = ci(c[k])
    crows.append({"variant": lab, "precision": round(PT_INPUT[k], 4),
                  "precision_lo": round(lo, 4), "precision_hi": round(hi, 4),
                  "note": "km2, not a ratio"})
cols = ["variant", "precision", "precision_lo", "precision_hi", "recall", "recall_lo",
        "recall_hi", "iou", "iou_lo", "iou_hi", "note"]
with open(OUT_CORR, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for r in crows:
        w.writerow({k: r.get(k, "") for k in cols})

log(f"\nwrote: {OUT_RESULTS}\nwrote: {OUT_CORR}")
log(f"\n=== ESTIMATES, 95% interval, B = {B} ===")
for src in pops:
    log(f"\n{src}")
    for r in [r for r in rows if r["source"] == src]:
        flag = "  <- single stratum, censused" if r["note"] else ("  <- n <= 2" if r["n_sampled"] <= 2 else "")
        log(f"  {r['category']:<26}{r['n_sampled']:>3} {r['est_area_km2']:>8.4f} "
            f"[{r['ci_lo_km2']:.4f}, {r['ci_hi_km2']:.4f}]  "
            f"{r['pct_of_population']:>5.1f}% [{r['pct_ci_lo']:.1f}, {r['pct_ci_hi']:.1f}]{flag}")

log(f"\n=== HEADLINE METRICS ===")
for r in crows[:4]:
    if "precision_lo" not in r:
        log(f"  {r['variant']:<22} P {r['precision']:.4f}          R {r['recall']:.4f}")
    else:
        log(f"  {r['variant']:<22} P {r['precision']:.4f} [{r['precision_lo']:.4f}, {r['precision_hi']:.4f}]"
            f"  R {r['recall']:.4f} [{r['recall_lo']:.4f}, {r['recall_hi']:.4f}]"
            f"  IoU {r['iou']:.4f} [{r['iou_lo']:.4f}, {r['iou_hi']:.4f}]")
lo4 = crows[3]["precision_lo"]
log(f"\n  variant 4 precision lower bound {lo4:.4f} vs measured 0.5708: "
    f"{'overlaps, the gain is not separable from sampling noise' if lo4 <= 0.5708 else 'does not reach it, the gain is not a sampling artefact'}")
