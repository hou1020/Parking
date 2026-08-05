"""
OSM parking as a reference layer — Leeds
Author: Hou

Compares OSM amenity=parking with the manual ground truth and with the model's
false positives, to establish two things:

  (1) How incomplete OSM parking is. OSM is the obvious existing source of UK
      parking geometry, so the size of the gap between OSM and the labelled
      ground truth is direct evidence for the data gap this study addresses.

  (2) Why some false positives coincide with OSM parking. Qiam et al. (2025)
      note that OSM polygons follow parcel boundaries rather than the parking
      pavement, so OSM outlines are wider than the surface a model detects.
      Splitting FP ∩ OSM by distance to labelled parking separates that
      geometric effect from genuine disagreement about what counts as parking.

Areas are computed on the validation grid (EPSG:27700).

Reads source data read-only. Writes only the output below, in this folder.
Output:
  - osm_comparison_summary.csv
"""
import os, csv
import geopandas as gpd
from shapely.ops import unary_union
import warnings; warnings.filterwarnings("ignore")


def log(m):
    print(m, flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MODEL = f"{ROOT}/Parking/calculate/output_files_merged/removal_merged.geojson"
MANUAL = f"{ROOT}/manual/leeds_manual.gpkg"
GRID = f"{ROOT}/manual/leeds_grid.gpkg"
OSM_CACHE = f"{HERE}/osm_extra.gpkg"
OUT = f"{HERE}/osm_comparison_summary.csv"

DISTANCES = (5.0, 10.0, 25.0)


def dissolve(gdf, region=None):
    g = gdf.to_crs(27700).copy()
    g = g[g.geometry.type.isin(["Polygon", "MultiPolygon"])]
    g["geometry"] = g.geometry.buffer(0)
    u = unary_union(g.geometry.values)
    if region is not None:
        u = u.intersection(region)
    out = gpd.GeoDataFrame(geometry=gpd.GeoSeries([u], crs=27700), crs=27700)
    return out.explode(index_parts=False).reset_index(drop=True)


def area(g):
    return float(g.geometry.area.sum()) if len(g) else 0.0


def inter(a, b):
    return gpd.overlay(a[["geometry"]], b[["geometry"]], how="intersection",
                       keep_geom_type=True) if len(a) and len(b) else a.iloc[0:0]


def minus(a, b):
    return gpd.overlay(a[["geometry"]], b[["geometry"]], how="difference",
                       keep_geom_type=True) if len(a) and len(b) else a


def buffered(g, d):
    u = unary_union(g.geometry.buffer(d).values)
    return gpd.GeoDataFrame(geometry=gpd.GeoSeries([u], crs=27700), crs=27700
                            ).explode(index_parts=False).reset_index(drop=True)


log("loading layers ...")
grid = gpd.read_file(GRID).to_crs(27700)
region = unary_union(grid.geometry.values)
model = dissolve(gpd.read_file(MODEL), region)
manual_raw = gpd.read_file(MANUAL).to_crs(27700)
manual = dissolve(manual_raw, region)
ex = gpd.read_file(OSM_CACHE).to_crs(27700)
osm_raw = ex[ex["grp"] == "osm_parking"]
osm = dissolve(osm_raw, region)

rows = []


def add(measure, value, unit, note=""):
    rows.append({"measure": measure, "value": value, "unit": unit, "note": note})
    log(f"  {measure:<40} {value:>9} {unit}")


log("\n--- layer extents ---")
add("manual labelled parking", round(area(manual)/1e6, 4), "km2", "ground truth")
add("model predicted parking", round(area(model)/1e6, 4), "km2", "removal output")
add("OSM amenity=parking", round(area(osm)/1e6, 4), "km2", "")
add("OSM as share of manual", round(100*area(osm)/area(manual), 1), "%", "")

o_raw = osm_raw[osm_raw.geometry.type.isin(["Polygon", "MultiPolygon"])]
o_raw = o_raw[o_raw.intersects(region)]
add("OSM polygons in region", len(o_raw), "count", "")
add("manual polygons", len(manual_raw), "count", "")
add("OSM median polygon area", round(float(o_raw.geometry.area.median()), 0), "m2", "")
add("manual median polygon area", round(float(manual_raw.geometry.area.median()), 0), "m2", "")

log("\n--- OSM vs manual agreement ---")
both = area(inter(osm, manual))
osm_only = area(minus(osm, manual))
man_only = area(minus(manual, osm))
add("OSM and manual agree", round(both/1e6, 4), "km2", f"{100*both/area(osm):.1f}% of OSM")
add("OSM only (manual says no)", round(osm_only/1e6, 4), "km2", "")
add("manual only (missing from OSM)", round(man_only/1e6, 4), "km2",
    f"{100*man_only/area(manual):.1f}% of labelled parking absent from OSM")

log("\n--- false positives coinciding with OSM parking ---")
FP = minus(model, manual)
fp_area = area(FP)
fp_osm = inter(FP, osm)
add("FP total", round(fp_area/1e6, 4), "km2", "")
add("FP on OSM parking", round(area(fp_osm)/1e6, 4), "km2",
    f"{100*area(fp_osm)/fp_area:.1f}% of FP")
for D in DISTANCES:
    buf = buffered(manual, D)
    near = area(inter(fp_osm, buf))
    far = area(minus(fp_osm, buf))
    add(f"  of which within {D:.0f} m of manual", round(near/1e6, 4), "km2",
        f"{100*near/area(fp_osm):.1f}% - parcel vs pavement geometry")
    add(f"  of which beyond {D:.0f} m of manual", round(far/1e6, 4), "km2",
        f"{100*far/area(fp_osm):.1f}% - genuine disagreement")

with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["measure", "value", "unit", "note"])
    w.writeheader(); w.writerows(rows)
log(f"\nwrote: {OUT}")
