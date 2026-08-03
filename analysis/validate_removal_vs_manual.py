"""
Model (removal_merged) vs manual annotation validation — Leeds
Date: 2026-07-28
Author: Hou

Manual annotation is complete for the whole grid; every 1 km2 cell is scored.
Compares the post-processed model output (removal_merged.geojson) against the
manual ground truth (leeds_manual.gpkg) on the validation grid (leeds_grid.gpkg).
Metrics are area-based (EPSG:27700, metres).

Two ground-truth variants are reported:
  - all         : all manual polygons (confidence 1, 2, 3)
  - c23         : confidence 2-3 only (main-validation subset)

Reads only; writes ONLY the two dated output CSVs below. Source data untouched.

Outputs (in Parking/):
  - validation_percell_0728.csv   : per grid cell metrics (both variants)
  - validation_summary_0728.csv   : overall (area-weighted) + mean-of-cells, both variants

Metric definitions (by area):
  TP = model ∩ manual ; FP = model − manual ; FN = manual − model
  precision = TP/(TP+FP) ; recall = TP/(TP+FN) ; IoU = TP/(TP+FP+FN)
"""
import os, csv
from statistics import mean
import geopandas as gpd
from shapely.ops import unary_union
import warnings; warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.dirname(HERE)
MODEL = f"{B}/Parking/calculate/output_files_merged/removal_merged.geojson"
MANUAL = f"{B}/manual/leeds_manual.gpkg"
GRID = f"{B}/manual/leeds_grid.gpkg"
OUT_PERCELL = f"{HERE}/validation_percell_0728.csv"
OUT_SUMMARY = f"{HERE}/validation_summary_0728.csv"

model = gpd.read_file(MODEL).to_crs(27700)
manual = gpd.read_file(MANUAL).to_crs(27700)
grid = gpd.read_file(GRID).to_crs(27700)
for g in (model, manual):
    g["geometry"] = g.geometry.buffer(0)

model_u = unary_union(model.geometry.values)
manual_all_u = unary_union(manual.geometry.values)
man23 = manual[manual["confidence"].fillna(0) >= 2]
manual_c23_u = unary_union(man23.geometry.values) if len(man23) else None


def metrics(mod, man):
    tp = mod.intersection(man).area
    fp = mod.difference(man).area
    fn = man.difference(mod).area
    prec = tp / (tp + fp) if tp + fp > 0 else None
    rec = tp / (tp + fn) if tp + fn > 0 else None
    iou = tp / (tp + fp + fn) if tp + fp + fn > 0 else None
    return tp, fp, fn, prec, rec, iou


def rnd(x, n=4):
    return None if x is None else round(x, n)


# ---------- per cell ----------
percell = []
for _, c in grid.iterrows():
    cg = c.geometry
    mod_c = model_u.intersection(cg)
    man_all = manual_all_u.intersection(cg)
    man_c23 = manual_c23_u.intersection(cg) if manual_c23_u is not None else None
    _, _, _, pa, ra, ia = metrics(mod_c, man_all)
    if man_c23 is not None:
        _, _, _, pc, rc, ic = metrics(mod_c, man_c23)
        m23a = round(man_c23.area, 1)
    else:
        pc = rc = ic = None; m23a = 0.0
    percell.append({
        "col_index": int(c["col_index"]), "row_index": int(c["row_index"]),
        "model_m2": round(mod_c.area, 1),
        "manual_all_m2": round(man_all.area, 1),
        "prec_all": rnd(pa), "rec_all": rnd(ra), "iou_all": rnd(ia),
        "manual_c23_m2": m23a,
        "prec_c23": rnd(pc), "rec_c23": rnd(rc), "iou_c23": rnd(ic),
    })
percell.sort(key=lambda r: (r["col_index"], r["row_index"]))
with open(OUT_PERCELL, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(percell[0].keys()))
    w.writeheader(); w.writerows(percell)


# ---------- summary ----------
region = unary_union(grid.geometry.values)
mod_r = model_u.intersection(region)


def overall_row(man_union, label):
    man_r = man_union.intersection(region)
    tp, fp, fn, prec, rec, iou = metrics(mod_r, man_r)
    return {
        "metric": label,
        "manual_km2": rnd(man_r.area / 1e6), "model_km2": rnd(mod_r.area / 1e6),
        "model_over_manual_ratio": rnd(mod_r.area / man_r.area, 3) if man_r.area else None,
        "tp_km2": rnd(tp / 1e6), "fp_km2": rnd(fp / 1e6), "fn_km2": rnd(fn / 1e6),
        "precision": rnd(prec), "recall": rnd(rec), "iou": rnd(iou),
    }


def mean_row(pk, rk, ik, label):
    def m(key):
        vals = [r[key] for r in percell if r[key] is not None]
        return round(mean(vals), 4) if vals else None
    return {"metric": label, "manual_km2": "", "model_km2": "",
            "model_over_manual_ratio": "", "tp_km2": "", "fp_km2": "", "fn_km2": "",
            "precision": m(pk), "recall": m(rk), "iou": m(ik)}


summary = [overall_row(manual_all_u, "overall_area_weighted_all")]
if manual_c23_u is not None:
    summary.append(overall_row(manual_c23_u, "overall_area_weighted_c23"))
summary.append(mean_row("prec_all", "rec_all", "iou_all", "mean_of_cells_all"))
summary.append(mean_row("prec_c23", "rec_c23", "iou_c23", "mean_of_cells_c23"))
with open(OUT_SUMMARY, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(summary[0].keys()))
    w.writeheader(); w.writerows(summary)


# ---------- print ----------
print(f"cells scored: {len(percell)} | manual polys: {len(manual)} (conf2-3: {len(man23)})")
print(f"wrote: {OUT_PERCELL}\nwrote: {OUT_SUMMARY}")
print("\n=== SUMMARY ===")
hdr = ["metric", "manual_km2", "model_km2", "model_over_manual_ratio",
       "tp_km2", "fp_km2", "fn_km2", "precision", "recall", "iou"]
print(" | ".join(hdr))
for s in summary:
    print(" | ".join(str(s[h]) for h in hdr))
print("\n=== PER CELL (all-confidence metrics) ===")
print(f"{'col':>3} {'row':>3} {'manual_all':>10} {'model_m2':>10} {'prec':>6} {'rec':>6} {'IoU':>6}")
for r in percell:
    p = "  -  " if r["prec_all"] is None else f"{r['prec_all']:>6.3f}"
    rc = "  -  " if r["rec_all"] is None else f"{r['rec_all']:>6.3f}"
    io = "  -  " if r["iou_all"] is None else f"{r['iou_all']:>6.3f}"
    print(f"{r['col_index']:>3} {r['row_index']:>3} {r['manual_all_m2']:>10.0f} {r['model_m2']:>10.0f} {p} {rc} {io}")
