"""
Turn the inspected samples into area-weighted estimates — Leeds
Author: Hou

The residual error categories were characterised by stratified random sampling
rather than by inspecting every polygon. This applies the ratio estimator to
scale what was seen back up to each population, and reports what the results
imply for the headline accuracy figures.

Estimator
    For stratum h with total population area A_h, the estimated area of category
    c is  A_h x (sampled area in c / total sampled area in h), summed over strata.
    Weighting by stratum area means the deliberate oversampling of large polygons
    does not distort the totals.

Corrections
    Four variants are reported cumulatively, so that every step remains visible
    and the uncorrected figures are never lost.

    1  as measured
       The labels exactly as drawn.

    2  + reference side (not_parking_in_digimap)
       Labelling was drawn on a satellite basemap while the model consumed
       Digimap aerial tiles, so some labelled lots are not parking in the imagery
       the model was given. The model is right to omit them and they are not
       detection failures, so their estimated area leaves the reference. This
       correction is confined to the missed-lot population by construction: a lot
       absent from the model's input imagery cannot be partially detected, so
       every lot found even in part demonstrably exists in that imagery.

    3  + prediction side (real_parking_missed)
       The mirror case: parking that is present in the Digimap imagery and meets
       the annotation rules, which the model found and the labelling did not
       record. That area belongs in the reference and counts as a true positive,
       whether it was an omission or was built after the basemap was captured.

    4  effective, excluding definitional differences
       on_street and private_driveway are real parking that the annotation rules
       deliberately exclude. The model is not wrong to see them; the disagreement
       is definitional. Removing them from the prediction rather than counting
       them as errors gives an effective precision, the accuracy attributable to
       the model rather than to where the scope boundary was drawn.

    The osm_disagree population also contains omitted parking, estimated
    separately below. It is not folded into these metrics: that population is
    defined by OSM coverage rather than by model behaviour, and some of it would
    overlap the prediction-side correction already applied.

Reads the filled worksheet read-only. Writes only the outputs below.
Outputs:
  - sampling_results.csv        : estimated area and share per category
  - sampling_corrections.csv    : headline metrics, uncorrected and at each
                                  correction step
"""
import os, csv
import pandas as pd
import geopandas as gpd
import warnings; warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = f"{HERE}/chips/index.csv"
WORKSHEET = f"{HERE}/sampling_worksheet.gpkg"
STRATA = f"{HERE}/sampling_strata.csv"
OUT_RESULTS = f"{HERE}/sampling_results.csv"
OUT_CORR = f"{HERE}/sampling_corrections.csv"

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
log(f"inspected: {len(d)} polygons")
log(d.groupby("source").size().to_string())

rows = []
for src, g in d.groupby("source"):
    st = strata[strata["source"] == src].set_index("stratum")
    pop_area = st["area_population_m2"].sum()
    est = {}
    for stratum, gg in g.groupby("stratum"):
        if stratum not in st.index:
            continue
        A_h = st.loc[stratum, "area_population_m2"]
        tot = gg["area_m2"].sum()
        for cat, ggg in gg.groupby("category"):
            est[cat] = est.get(cat, 0.0) + A_h * ggg["area_m2"].sum() / tot
    for cat, a in sorted(est.items(), key=lambda kv: -kv[1]):
        rows.append({"source": src, "category": cat,
                     "n_sampled": int((g["category"] == cat).sum()),
                     "est_area_km2": round(a / 1e6, 4),
                     "pct_of_population": round(100 * a / pop_area, 1)})
    rows.append({"source": src, "category": "TOTAL", "n_sampled": len(g),
                 "est_area_km2": round(pop_area / 1e6, 4), "pct_of_population": 100.0})

res = pd.DataFrame(rows)
res.to_csv(OUT_RESULTS, index=False)
log(f"\nwrote: {OUT_RESULTS}")
for src in res["source"].unique():
    log(f"\n=== {src} ===")
    log(res[res["source"] == src].to_string(index=False))

# ---- corrected headline metrics ----
def est(source, categories):
    """Estimated area, km2, for one or more categories of a population."""
    sel = res[(res["source"] == source) & (res["category"].isin(categories))]
    return float(sel["est_area_km2"].sum())


mismatch = est("fn_other", ["not_parking_in_digimap"])          # leaves the reference
missed = est("fp_other", ["real_parking_missed"])               # joins the reference
definitional = est("fp_other", ["on_street", "private_driveway"])  # out of scope
osm_omitted = est("osm_disagree", ["real_parking_missed"])      # reported, not folded in

corr = []


def metrics(tp, model, manual, label, note=""):
    fp, fn = model - tp, manual - tp
    corr.append({"variant": label,
                 "tp_km2": round(tp, 4), "manual_km2": round(manual, 4),
                 "model_km2": round(model, 4),
                 "precision": round(tp / (tp + fp), 4),
                 "recall": round(tp / (tp + fn), 4),
                 "iou": round(tp / (tp + fp + fn), 4),
                 "note": note})


# 1 uncorrected
metrics(TP, MODEL, MANUAL, "1 as measured",
        "labels exactly as drawn on the satellite basemap")
# 2 reference side: labelled area that is not parking in the model's imagery
man2 = MANUAL - mismatch
metrics(TP, MODEL, man2, "2 + reference side",
        f"-{mismatch:.4f} km2 not parking in the Digimap imagery")
# 3 prediction side: parking present in that imagery but never labelled
tp3, man3 = TP + missed, man2 + missed
metrics(tp3, MODEL, man3, "3 + prediction side",
        f"+{missed:.4f} km2 real parking the labelling did not record")
# 4 effective: definitional exclusions removed from the prediction
metrics(tp3, MODEL - definitional, man3, "4 effective",
        f"-{definitional:.4f} km2 on-street and private driveways, excluded by rule")

pd.DataFrame(corr).to_csv(OUT_CORR, index=False)
log(f"\nwrote: {OUT_CORR}")
log("\n=== HEADLINE METRICS (cumulative) ===")
log(pd.DataFrame(corr).drop(columns="note").to_string(index=False))
log("\nadjustments, km2 (share of labelled area):")
log(f"  reference side, not parking in Digimap  -{mismatch:.4f}  ({100*mismatch/MANUAL:.1f}%)")
log(f"  prediction side, parking never labelled +{missed:.4f}  ({100*missed/MANUAL:.1f}%)")
log(f"  definitional, on-street + driveways      {definitional:.4f}  ({100*definitional/MANUAL:.1f}%)")
log(f"\nreported separately, not folded in:")
log(f"  omitted parking found via OSM             {osm_omitted:.4f} km2")
