"""
False-negative (FN) analysis for the removal model vs manual annotation — Leeds
Author: Hou

FN = manual - model (real parking the final map misses).

(1) Geometric split: erosion vs standalone
    erosion FN    = FN lying within D metres of a predicted parking area
    standalone FN = the rest
    Reported at D = 2, 5, 10 m. This describes where the missed area sits, but
    distance alone does not establish whether a lot was found: on a large lot
    that the model detected only in the middle, the outer ring lies well beyond
    D and would be counted as standalone even though the lot was detected. The
    classification in (2) is therefore done per lot, not per fragment.

(2) Object-level split: was the LOT found at all?
    Each labelled lot has a detection rate, covered fraction = (lot ∩ model)/lot.
    FN area is assigned by the state of the lot it belongs to:
      whole_lot_missed    lot coverage <= MISSED_COV, the model did not find it
      partly_detected     coverage between MISSED_COV and DETECTED_COV
      fringe_of_detected  coverage > DETECTED_COV, the lot was found but drawn
                          too small, so this FN is an outline error, not a miss

(3) Attribution of whole_lot_missed FN (priority partition, subtracted in order):
    postproc_removed : FN the ORIGINAL (pre-removal) model DID detect
                       -> lost to OSM building/road subtraction: a pipeline
                          artefact, not a model failure
    rooftop_tagged   : remaining FN on lots tagged "rooftop" in notes
    inside_buildings : remaining FN inside OSM building footprints
                       (rooftop-like but untagged)
    other            : the rest -> lots the model genuinely did not see

(4) Per-polygon detection rate
    For each manual polygon: covered fraction = (polygon ∩ model) / polygon,
    summarised by size class and by confidence, to test whether small or
    low-confidence lots are missed more often.

Implementation note: all pairwise geometry work uses GeoPandas overlay, which is
vectorised and spatially indexed. Because every reference layer is dissolved
first, its parts are disjoint, so intersection areas can simply be summed.

Reads source data read-only. Writes only the outputs below, in this folder.
Outputs:
  - fn_analysis_summary.csv
  - fn_detection_by_class.csv
  - fn_unclassified.geojson  : WHOLE LOTS the model essentially missed and that
                               no other explanation covers, for sampling. Whole
                               lots are exported rather than FN fragments, so
                               that "why was this missed" is a question about a
                               car park rather than about a sliver of one.
"""
import os, csv
import geopandas as gpd
import pandas as pd
from shapely.ops import unary_union
import warnings; warnings.filterwarnings("ignore")


def log(m):
    print(m, flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MODEL_REMOVAL = f"{ROOT}/Parking/calculate/output_files_merged/removal_merged.geojson"
MODEL_ORIGINAL = f"{ROOT}/Parking/calculate/output_files_merged/original_merged.geojson"
MANUAL = f"{ROOT}/manual/leeds_manual.gpkg"
GRID = f"{ROOT}/manual/leeds_grid.gpkg"
REF_CACHE = f"{HERE}/ref_cache.gpkg"

OUT_SUMMARY = f"{HERE}/fn_analysis_summary.csv"
OUT_CLASSES = f"{HERE}/fn_detection_by_class.csv"
OUT_OTHER = f"{HERE}/fn_unclassified.geojson"

EROSION_D = 5.0
MISSED_COV = 0.10        # lot coverage at or below this = not found
DETECTED_COV = 0.70      # lot coverage above this = found, outline too small
MIN_SAMPLE_M2 = 100.0
SIZE_BINS = [0, 200, 500, 1000, 2500, 5000, 1e9]
SIZE_LABELS = ["<200", "200-500", "500-1k", "1k-2.5k", "2.5k-5k", ">5k"]


def dissolve(path_or_gdf, region=None):
    """Load, clean and merge a layer into disjoint parts."""
    g = path_or_gdf if isinstance(path_or_gdf, gpd.GeoDataFrame) else gpd.read_file(path_or_gdf)
    g = g.to_crs(27700).copy()
    g["geometry"] = g.geometry.buffer(0)
    u = unary_union(g.geometry.values)
    if region is not None:
        u = u.intersection(region)
    out = gpd.GeoDataFrame(geometry=gpd.GeoSeries([u], crs=27700), crs=27700)
    return out.explode(index_parts=False).reset_index(drop=True)


def as_parts(gdf):
    """Explode a layer that is already dissolved. Cheaper than dissolve(),
    which would re-clean and re-merge geometry that is already disjoint."""
    g = gdf.to_crs(27700)[["geometry"]].copy()
    return g.explode(index_parts=False).reset_index(drop=True)


def area(gdf):
    return float(gdf.geometry.area.sum()) if len(gdf) else 0.0


def inter(a, b):
    if not len(a) or not len(b):
        return a.iloc[0:0]
    return gpd.overlay(a[["geometry"]], b[["geometry"]], how="intersection", keep_geom_type=True)


def minus(a, b):
    if not len(a) or not len(b):
        return a
    return gpd.overlay(a[["geometry"]], b[["geometry"]], how="difference", keep_geom_type=True)


def buffered(gdf, d):
    """Buffer then dissolve: buffers of neighbouring parts overlap, and
    overlapping pieces would otherwise be counted twice."""
    if not len(gdf):
        return gdf
    u = unary_union(gdf.geometry.buffer(d).values)
    out = gpd.GeoDataFrame(geometry=gpd.GeoSeries([u], crs=27700), crs=27700)
    return out.explode(index_parts=False).reset_index(drop=True)


log("loading layers ...")
grid = gpd.read_file(GRID).to_crs(27700)
region = unary_union(grid.geometry.values)

removal = dissolve(MODEL_REMOVAL, region)
original = dissolve(MODEL_ORIGINAL, region)
manual_raw = gpd.read_file(MANUAL).to_crs(27700)
manual_raw["geometry"] = manual_raw.geometry.buffer(0)
manual = dissolve(manual_raw, region)

ref = gpd.read_file(REF_CACHE).to_crs(27700)
buildings = as_parts(ref[ref["grp"] == "buildings"])   # cache is already dissolved

roof_mask = manual_raw["notes"].astype(str).str.contains("roof", case=False, na=False)
rooftop = dissolve(manual_raw[roof_mask], region) if roof_mask.any() else manual.iloc[0:0]

log("computing FN ...")
FN = minus(manual, removal)
fn_area = area(FN)
log(f"total FN = {fn_area/1e6:.4f} km2 "
    f"({100*fn_area/area(manual):.1f}% of manual), {len(FN)} parts")

rows = [{"category": "TOTAL_FN", "area_km2": round(fn_area/1e6, 4), "pct_of_FN": 100.0}]

# ---- (1) erosion vs standalone ----
standalone = None
for D in (2.0, 5.0, 10.0):
    log(f"  erosion split at {D:.0f} m ...")
    buf = buffered(removal, D)
    ero = inter(FN, buf)
    stand = minus(FN, buf)
    rows.append({"category": f"erosion_FN_within_{int(D)}m", "area_km2": round(area(ero)/1e6, 4),
                 "pct_of_FN": round(100*area(ero)/fn_area, 1)})
    rows.append({"category": f"standalone_FN_beyond_{int(D)}m", "area_km2": round(area(stand)/1e6, 4),
                 "pct_of_FN": round(100*area(stand)/fn_area, 1)})
    if D == EROSION_D:
        standalone = stand
stand_area = area(standalone)

# ---- (2) object-level split: was the lot found at all? ----
log("classifying lots by detection rate ...")
lots = manual_raw.reset_index(drop=True).copy()
lots["lot_id"] = lots.index
lots["lot_area"] = lots.geometry.area


def coverage(target):
    """Fraction of each labelled lot covered by a layer."""
    h = gpd.overlay(lots[["lot_id", "geometry"]], target[["geometry"]],
                    how="intersection", keep_geom_type=True)
    c = h.assign(a=h.geometry.area).groupby("lot_id")["a"].sum()
    return lots["lot_id"].map(c).fillna(0.0) / lots["lot_area"]


lots["cov"] = coverage(removal)
lots["cov_original"] = coverage(original)

groups = {
    "whole_lot_missed":   lots["cov"] <= MISSED_COV,
    "partly_detected":    (lots["cov"] > MISSED_COV) & (lots["cov"] <= DETECTED_COV),
    "fringe_of_detected": lots["cov"] > DETECTED_COV,
}
rows.append({"category": "--- FN by state of the lot it belongs to ---",
             "area_km2": round(fn_area/1e6, 4), "pct_of_FN": 100.0})
fn_by_group = {}
for name, mask in groups.items():
    if not mask.any():
        fn_by_group[name] = FN.iloc[0:0]; continue
    g = dissolve(lots[mask], region)
    part = inter(FN, g)
    fn_by_group[name] = part
    log(f"  {name}: {len(lots[mask])} lots, FN {area(part)/1e6:.4f} km2")
    rows.append({"category": f"{name}_FN", "area_km2": round(area(part)/1e6, 4),
                 "pct_of_FN": round(100*area(part)/fn_area, 1),
                 "n_lots": int(mask.sum())})

# ---- (3) attribution of the FN on lots the model did not find ----
log("attributing whole_lot_missed FN ...")
missed_fn = fn_by_group["whole_lot_missed"]
missed_area = area(missed_fn)
parts, rem = {}, missed_fn
for name, layer in [("postproc_removed", original),
                    ("rooftop_tagged", rooftop),
                    ("inside_buildings", buildings)]:
    hit = inter(rem, layer)
    parts[name] = area(hit)
    rem = minus(rem, layer)
    log(f"  {name}: {parts[name]/1e6:.4f} km2")
other = rem
parts["other"] = area(other)

rows.append({"category": "--- whole_lot_missed breakdown ---",
             "area_km2": round(missed_area/1e6, 4),
             "pct_of_FN": round(100*missed_area/fn_area, 1)})
for k, label in [("postproc_removed", "postproc_removed_FN"), ("rooftop_tagged", "rooftop_tagged_FN"),
                 ("inside_buildings", "inside_buildings_FN"), ("other", "other_genuine_miss_FN")]:
    a = parts[k]
    rows.append({"category": label, "area_km2": round(a/1e6, 4),
                 "pct_of_FN": round(100*a/fn_area, 1),
                 "pct_of_missed": round(100*a/missed_area, 1) if missed_area else None})

with open(OUT_SUMMARY, "w", newline="") as f:
    cols = ["category", "area_km2", "pct_of_FN", "n_lots", "pct_of_missed"]
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for r in rows:
        w.writerow({c: r.get(c, "") for c in cols})

# ---- (3) per-polygon detection rate ----
log("computing per-polygon detection rate ...")
m = lots.copy()
m["area_m2"] = m["lot_area"]
m["detect_rate"] = m["cov"]
m["covered_m2"] = m["cov"] * m["lot_area"]
m["size_class"] = pd.cut(m["area_m2"], bins=SIZE_BINS, labels=SIZE_LABELS)

class_rows = []
for grp, col in [("size", "size_class"), ("confidence", "confidence")]:
    for lab, sub in m.groupby(col, observed=True):
        class_rows.append({"group": grp, "class": str(lab), "n": len(sub),
                           "total_area_m2": round(sub["area_m2"].sum(), 1),
                           "mean_detect_rate": round(sub["detect_rate"].mean(), 3),
                           "area_weighted_rate": round(sub["covered_m2"].sum()/sub["area_m2"].sum(), 3),
                           "pct_fully_missed": round(100*(sub["detect_rate"] < 0.05).mean(), 1)})

with open(OUT_CLASSES, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(class_rows[0].keys()))
    w.writeheader(); w.writerows(class_rows)

# ---- export: whole lots the model missed, with no other explanation ----
unexplained = lots[groups["whole_lot_missed"]
                   & (lots["cov_original"] <= MISSED_COV)     # not a post-processing loss
                   & (~roof_mask.values)                       # not a tagged rooftop
                   & (lots["lot_area"] >= MIN_SAMPLE_M2)].copy()
keep = ["lot_id", "lot_area", "cov", "cov_original", "confidence", "notes", "geometry"]
out = gpd.GeoDataFrame(unexplained[keep], geometry="geometry", crs=27700)
out = out.rename(columns={"lot_area": "area_m2"}).sort_values("area_m2", ascending=False)
out.reset_index(drop=True).to_file(OUT_OTHER, driver="GeoJSON")
log(f"exported {len(out)} whole lots the model missed (>= {MIN_SAMPLE_M2:.0f} m2), "
    f"{out['area_m2'].sum()/1e6:.4f} km2")

log(f"\nwrote: {OUT_SUMMARY}\nwrote: {OUT_CLASSES}\nwrote: {OUT_OTHER}")

log("\n=== FN SUMMARY ===")
for r in rows:
    ps = r.get("pct_of_missed", ""); ps = "" if ps in (None, "") else ps
    log(f"{r['category']:<36} {str(r['area_km2']):>8} km2  {str(r['pct_of_FN']):>5}% FN  {ps:>6}")

log("\n=== DETECTION RATE BY CLASS ===")
log(f"{'group':<12}{'class':<10}{'n':>6}{'mean_rate':>11}{'area_wt':>9}{'%missed':>9}")
for r in class_rows:
    log(f"{r['group']:<12}{r['class']:<10}{r['n']:>6}{r['mean_detect_rate']:>11}"
        f"{r['area_weighted_rate']:>9}{r['pct_fully_missed']:>9}")
