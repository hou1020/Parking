"""
Post-processing ablation and rooftop case study — Leeds
Author: Hou

Part 1 — Ablation of the post-processing steps (2x2 factorial)
    Each variant subtracts a different combination of reference layers from the
    same raw model output, so the effect of each step can be read off directly:
        A  original                     neither layer removed
        B  original - buildings         buildings only
        C  original - roads             roads only
        D  original - buildings - roads both (reconstructed)
        D* removal                      the pipeline's own output, for comparison
    D and D* should agree closely; any gap reflects the pipeline subtracting the
    layers tile by tile rather than in one pass, and is reported as a check.

Part 2 — Counter-test: can other reference layers clean the map further? (factorial)
    Each land-use layer that explains many false positives is subtracted from
    the pipeline output on its own, then all together:
        E  removal - sports             OS Greenspace hard sports functions
        F  removal - industrial         OSM industrial/commercial/retail land
        G  removal - roads_wide         road buffers widened by EXTRA_ROAD m
        H  removal - all three          combined

Ordering note: subtraction is commutative here, since (X - A) - B = X - (A ∪ B),
so no variant depends on the order in which layers are removed. Order only
matters where a category is assigned exclusively, as in the false-positive
attribution (fp_analysis.py).

Part 3 — Rooftop case study
    Rooftop parking is labelled in the manual data (notes = "rooftop"). Because
    it sits on top of buildings, subtracting building footprints necessarily
    deletes it. This quantifies how much the original model found, how much
    survived post-processing, and how much lies inside OSM buildings.

Metrics are area-based on the validation grid (EPSG:27700):
    TP = model ∩ manual ; FP = model − manual ; FN = manual − model
    precision = TP/(TP+FP) ; recall = TP/(TP+FN) ; IoU = TP/(TP+FP+FN)

Note: B and C reconstruct the removal steps from the cached OSM layers, so they
approximate rather than exactly reproduce the pipeline's per-tile subtraction.

Reads source data read-only. Writes only the outputs below, in this folder.
Outputs:
  - ablation_summary.csv
  - rooftop_summary.csv
"""
import os, csv
import geopandas as gpd
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
OSM_CACHE = f"{HERE}/osm_extra.gpkg"
GREENSPACE = f"{HERE}/OS Open Greenspace (ESRI Shape File) SE/data/SE_GreenspaceSite.shp"

OUT_ABLATION = f"{HERE}/ablation_summary.csv"
OUT_ROOFTOP = f"{HERE}/rooftop_summary.csv"

EXTRA_ROAD = 6.0
SPORTS_HARD = ["Tennis Court", "Other Sports Facility", "Play Space"]


def dissolve(gdf, region=None):
    """Clean, merge and explode a layer into disjoint parts."""
    g = gdf.to_crs(27700).copy()
    g["geometry"] = g.geometry.buffer(0)
    u = unary_union(g.geometry.values)
    if region is not None:
        u = u.intersection(region)
    out = gpd.GeoDataFrame(geometry=gpd.GeoSeries([u], crs=27700), crs=27700)
    return out.explode(index_parts=False).reset_index(drop=True)


def load(path, region=None):
    return dissolve(gpd.read_file(path), region)


def area(gdf):
    return float(gdf.geometry.area.sum()) if len(gdf) else 0.0


def minus(a, b):
    if not len(a) or not len(b):
        return a
    return gpd.overlay(a[["geometry"]], b[["geometry"]], how="difference", keep_geom_type=True)


def inter(a, b):
    if not len(a) or not len(b):
        return a.iloc[0:0]
    return gpd.overlay(a[["geometry"]], b[["geometry"]], how="intersection", keep_geom_type=True)


def buffered(gdf, d):
    """Buffer then dissolve, so overlapping buffers are not double counted."""
    u = unary_union(gdf.buffer(d).values)
    out = gpd.GeoDataFrame(geometry=gpd.GeoSeries([u], crs=27700), crs=27700)
    return out.explode(index_parts=False).reset_index(drop=True)


log("loading layers ...")
grid = gpd.read_file(GRID).to_crs(27700)
region = unary_union(grid.geometry.values)

removal = load(MODEL_REMOVAL, region)
original = load(MODEL_ORIGINAL, region)

manual_raw = gpd.read_file(MANUAL).to_crs(27700)
manual_raw["geometry"] = manual_raw.geometry.buffer(0)
manual = dissolve(manual_raw, region)
man_area = area(manual)

ref = gpd.read_file(REF_CACHE).to_crs(27700)
ref["geometry"] = ref.geometry.buffer(0)
buildings = dissolve(ref[ref["grp"] == "buildings"])
roads = dissolve(ref[ref["grp"] == "roads"])
roads_wide = buffered(roads.geometry, EXTRA_ROAD)

ex = gpd.read_file(OSM_CACHE).to_crs(27700)
ex["geometry"] = ex.geometry.buffer(0)
industrial = dissolve(ex[ex["grp"] == "industrial_yard"])

gs = gpd.read_file(GREENSPACE).to_crs(27700)
gs["geometry"] = gs.geometry.buffer(0)
sports = dissolve(gs[gs["function"].isin(SPORTS_HARD)], region)

log(f"manual = {man_area/1e6:.3f} km2")


def score(model, label, note=""):
    tp = area(inter(model, manual))
    fp = area(model) - tp
    fn = man_area - tp
    prec = tp / (tp + fp) if tp + fp else 0.0
    rec = tp / (tp + fn) if tp + fn else 0.0
    iou = tp / (tp + fp + fn) if tp + fp + fn else 0.0
    row = {"variant": label, "model_km2": round(area(model)/1e6, 4),
           "tp_km2": round(tp/1e6, 4), "fp_km2": round(fp/1e6, 4), "fn_km2": round(fn/1e6, 4),
           "precision": round(prec, 4), "recall": round(rec, 4), "iou": round(iou, 4),
           "note": note}
    log(f"  {label:<44} P={prec:.3f} R={rec:.3f} IoU={iou:.3f}")
    return row


log("\nPart 1 — post-processing ablation (2x2 factorial on the raw output)")
both = minus(minus(original, buildings), roads)
rows = [
    score(original, "A. original", "neither layer removed"),
    score(minus(original, buildings), "B. original - buildings", "buildings only"),
    score(minus(original, roads), "C. original - roads", "roads only"),
    score(both, "D. original - buildings - roads", "both, reconstructed"),
    score(removal, "D*. removal (pipeline output)", "both, as produced by the pipeline"),
]
gap = abs(area(both) - area(removal)) / area(removal) * 100
log(f"  reconstruction check: |D - D*| = {gap:.1f}% of D* area")

log("\nPart 2 — counter-test: land-use layers as extra filters (each alone, then combined)")
all_three = minus(minus(minus(removal, sports), industrial), roads_wide)
rows += [
    score(minus(removal, sports), "E. removal - sports", "OS Greenspace sports"),
    score(minus(removal, industrial), "F. removal - industrial", "OSM industrial/commercial"),
    score(minus(removal, roads_wide), "G. removal - roads_wide", f"road buffers +{EXTRA_ROAD:.0f} m"),
    score(all_three, "H. removal - all three", "sports + industrial + roads_wide"),
]

with open(OUT_ABLATION, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)

log("\nPart 3 — rooftop case study")
roof_mask = manual_raw["notes"].astype(str).str.contains("roof", case=False, na=False)
roof = dissolve(manual_raw[roof_mask], region)
nonroof = dissolve(manual_raw[~roof_mask], region)
roof_area = area(roof)

cov_orig = area(inter(original, roof))
cov_rem = area(inter(removal, roof))
in_build = area(inter(roof, buildings))
lost = area(minus(inter(original, roof), removal))

rrows = [
    {"measure": "rooftop polygons", "value": int(roof_mask.sum()), "unit": "count"},
    {"measure": "rooftop labelled area", "value": round(roof_area/1e6, 4), "unit": "km2"},
    {"measure": "rooftop share of manual", "value": round(100*roof_area/man_area, 2), "unit": "%"},
    {"measure": "recall on rooftop, original", "value": round(cov_orig/roof_area, 3), "unit": "ratio"},
    {"measure": "recall on rooftop, removal", "value": round(cov_rem/roof_area, 3), "unit": "ratio"},
    {"measure": "recall on non-rooftop, original",
     "value": round(area(inter(original, nonroof))/area(nonroof), 3), "unit": "ratio"},
    {"measure": "recall on non-rooftop, removal",
     "value": round(area(inter(removal, nonroof))/area(nonroof), 3), "unit": "ratio"},
    {"measure": "rooftop inside OSM buildings", "value": round(100*in_build/roof_area, 1), "unit": "%"},
    {"measure": "detected by original then removed", "value": round(100*lost/roof_area, 1), "unit": "%"},
]
with open(OUT_ROOFTOP, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["measure", "value", "unit"])
    w.writeheader(); w.writerows(rrows)

log(f"\nwrote: {OUT_ABLATION}\nwrote: {OUT_ROOFTOP}")
log("\n=== ROOFTOP ===")
for r in rrows:
    log(f"  {r['measure']:<38} {r['value']:>8} {r['unit']}")
