"""
False-positive (FP) analysis for the removal model vs manual annotation — Leeds
Date: 2026-08-03  (updated: + OS Greenspace + OSM landuse/pitch/parking attribution)
Author: Hou

FP = model - manual (area the model calls parking but the manual truth does not).

(1) Boundary-dilation vs standalone split (D = 2, 5, 10 m; 5 m used below).
(2) Category attribution of standalone FP, priority partition (subtract in order):
      building         : OSM building footprints (residual; removal pre-subtracts)
      road_adjacent    : within EXTRA_ROAD m of OSM road buffers (kerbside/on-street)
      osm_parking      : OSM amenity=parking (real parking the manual excluded)
      sports_courts    : OS Greenspace hard sports funcs  ∪  OSM leisure pitch/track/centre
      industrial_yard  : OSM landuse industrial/commercial/retail/railway/depot (storage/depot)
      brownfield_bare  : OSM landuse brownfield/construction/greenfield/landfill
      other            : the rest -> exported for manual sampling (grey hardstanding,
                         bare ground, houses missing from OSM, etc.)

Reads source data read-only. Writes ONLY 0803-tagged outputs in this analysis/ folder.
Caches OSM/reference layers to *_0803.gpkg so re-runs are fast and offline.
Outputs:
  - fp_analysis_summary_0803.csv
  - fp_unclassified_0803.geojson
  - ref_cache_0803.gpkg      (buildings / road_buffer unions - cache)
  - osm_extra_0803.gpkg      (fetched OSM landuse/pitch/parking - cache)
"""
import os, glob, csv
import geopandas as gpd
import pandas as pd
from shapely.ops import unary_union
import warnings; warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MODEL = f"{ROOT}/Parking/calculate/output_files_merged/removal_merged.geojson"
MANUAL = f"{ROOT}/manual/leeds_manual.gpkg"
GRID = f"{ROOT}/manual/leeds_grid.gpkg"
OSM_ROOT = f"{ROOT}/Parking/parking-lot-mapping-tool/output_files/tif_removal"
GREENSPACE = f"{HERE}/OS Open Greenspace (ESRI Shape File) SE/data/SE_GreenspaceSite.shp"
OUT_SUMMARY = f"{HERE}/fp_analysis_summary_0803.csv"
OUT_OTHER = f"{HERE}/fp_unclassified_0803.geojson"
REF_CACHE = f"{HERE}/ref_cache_0803.gpkg"
OSM_CACHE = f"{HERE}/osm_extra_0803.gpkg"

DILATION_D, EXTRA_ROAD, MIN_SAMPLE_M2 = 5.0, 6.0, 100.0
SPORTS_HARD = ["Tennis Court", "Other Sports Facility", "Play Space"]
OSM_GROUPS = {
    "industrial_yard": {"landuse": ["industrial", "commercial", "retail", "railway", "depot"]},
    "brownfield_bare": {"landuse": ["brownfield", "construction", "greenfield", "landfill"]},
    "pitch": {"leisure": ["pitch", "track", "sports_centre"]},
    "osm_parking": {"amenity": ["parking"]},
}


def poly_union(gdf):
    gdf = gdf[gdf.geometry.type.isin(["Polygon", "MultiPolygon"])].copy()
    if not len(gdf):
        return None
    gdf["geometry"] = gdf.geometry.buffer(0)
    return unary_union(gdf.geometry.values)


print("loading model / manual / grid ...")
model = gpd.read_file(MODEL).to_crs(27700); model["geometry"] = model.geometry.buffer(0)
manual = gpd.read_file(MANUAL).to_crs(27700); manual["geometry"] = manual.geometry.buffer(0)
grid = gpd.read_file(GRID).to_crs(27700)
region = unary_union(grid.geometry.values)
model_u = unary_union(model.geometry.values).intersection(region)
manual_u = unary_union(manual.geometry.values).intersection(region)
FP = model_u.difference(manual_u)
fp_area = FP.area
print(f"total FP area = {fp_area/1e6:.4f} km^2")

# ---- reference unions (buildings, road buffers) with cache ----
if os.path.exists(REF_CACHE):
    ref = gpd.read_file(REF_CACHE)
    buildings_u = poly_union(ref[ref["grp"] == "buildings"])
    roads_u = poly_union(ref[ref["grp"] == "roads"])
    print("loaded reference unions from cache")
else:
    print("loading OSM buildings / road buffers (cached tiles) ...")
    def load_union(paths):
        parts = [gpd.read_file(p).to_crs(27700) for p in paths if os.path.getsize(p) > 0]
        parts = [g for g in parts if len(g)]
        g = pd.concat(parts, ignore_index=True); g["geometry"] = g.geometry.buffer(0)
        return unary_union(g.geometry.values)
    buildings_u = load_union(glob.glob(f"{OSM_ROOT}/**/osm_cache/*_osm_buildings.geojson", recursive=True))
    roads_u = load_union(glob.glob(f"{OSM_ROOT}/**/osm_cache/*_osm_road_buffers.geojson", recursive=True))
    gpd.GeoDataFrame({"grp": ["buildings", "roads"]},
                     geometry=[buildings_u, roads_u], crs=27700).to_file(REF_CACHE, driver="GPKG")
    print("cached reference unions")

# ---- greenspace sports ----
gs = gpd.read_file(GREENSPACE).to_crs(27700); gs["geometry"] = gs.geometry.buffer(0)
gs = gs[gs.intersects(region)]
gs_sports_u = poly_union(gs[gs["function"].isin(SPORTS_HARD)])

# ---- extra OSM groups with cache ----
if os.path.exists(OSM_CACHE):
    ex = gpd.read_file(OSM_CACHE)
    osm_u = {g: poly_union(ex[ex["grp"] == g]) for g in OSM_GROUPS}
    print("loaded extra OSM from cache")
else:
    import osmnx as ox
    poly4326 = gpd.GeoSeries([region], crs=27700).to_crs(4326).iloc[0]
    frames, osm_u = [], {}
    for grp, tags in OSM_GROUPS.items():
        try:
            f = ox.features_from_polygon(poly4326, tags).to_crs(27700)
            f = f[f.geometry.type.isin(["Polygon", "MultiPolygon"])][["geometry"]].copy()
            f["grp"] = grp
            frames.append(f); osm_u[grp] = poly_union(f)
            print(f"  fetched {grp}: {len(f)} polygons")
        except Exception as e:
            osm_u[grp] = None; print(f"  {grp}: none ({e})")
    if frames:
        pd.concat(frames, ignore_index=True).to_file(OSM_CACHE, driver="GPKG")
        print("cached extra OSM")

# ---- FP analysis ----
rows = [{"category": "TOTAL_FP", "area_km2": round(fp_area/1e6, 4), "pct_of_FP": 100.0}]
standalone = None
for D in (2.0, 5.0, 10.0):
    dil = FP.intersection(manual_u.buffer(D)); stand = FP.difference(manual_u.buffer(D))
    rows.append({"category": f"dilation_FP_within_{int(D)}m", "area_km2": round(dil.area/1e6, 4), "pct_of_FP": round(100*dil.area/fp_area, 1)})
    rows.append({"category": f"standalone_FP_beyond_{int(D)}m", "area_km2": round(stand.area/1e6, 4), "pct_of_FP": round(100*stand.area/fp_area, 1)})
    if D == DILATION_D:
        standalone = stand
stand_area = standalone.area

sports_u = unary_union([g for g in [gs_sports_u, osm_u.get("pitch")] if g is not None]) if (gs_sports_u or osm_u.get("pitch")) else None
roads_wide = roads_u.buffer(EXTRA_ROAD) if roads_u is not None else None

parts, rem = {}, standalone
def peel(name, layer):
    global rem
    if layer is None or (hasattr(layer, "is_empty") and layer.is_empty):
        parts[name] = None; return
    hit = rem.intersection(layer); parts[name] = hit; rem = rem.difference(layer)

parts["building"] = standalone.intersection(buildings_u) if buildings_u is not None else None
rem = standalone.difference(buildings_u) if buildings_u is not None else standalone
peel("road_adjacent", roads_wide)
peel("osm_parking", osm_u.get("osm_parking"))
peel("sports_courts", sports_u)
peel("industrial_yard", osm_u.get("industrial_yard"))
peel("brownfield_bare", osm_u.get("brownfield_bare"))
other_fp = rem

def add(cat, geom):
    a = geom.area if geom is not None else 0.0
    rows.append({"category": cat, "area_km2": round(a/1e6, 4), "pct_of_FP": round(100*a/fp_area, 1),
                 "pct_of_standalone": round(100*a/stand_area, 1) if stand_area else None})

rows.append({"category": f"--- standalone(>{int(DILATION_D)}m) breakdown ---", "area_km2": round(stand_area/1e6, 4), "pct_of_FP": round(100*stand_area/fp_area, 1)})
for name in ["building", "road_adjacent", "osm_parking", "sports_courts", "industrial_yard", "brownfield_bare"]:
    add(name + "_FP", parts.get(name))
add("other_unexplained_FP", other_fp)

with open(OUT_SUMMARY, "w", newline="") as f:
    cols = ["category", "area_km2", "pct_of_FP", "pct_of_standalone"]
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for r in rows:
        w.writerow({c: r.get(c, "") for c in cols})

if other_fp is not None and not other_fp.is_empty:
    gser = gpd.GeoSeries([other_fp], crs=27700).explode(index_parts=False).reset_index(drop=True)
    gdf = gpd.GeoDataFrame(geometry=gser, crs=27700); gdf["area_m2"] = gdf.geometry.area
    gdf = gdf[gdf["area_m2"] >= MIN_SAMPLE_M2].sort_values("area_m2", ascending=False).reset_index(drop=True)
    gdf.to_file(OUT_OTHER, driver="GeoJSON")
    print(f"exported {len(gdf)} 'other' FP polygons (>= {MIN_SAMPLE_M2:.0f} m2)")

print(f"\nwrote: {OUT_SUMMARY}")
print("\n=== FP ANALYSIS SUMMARY ===")
for r in rows:
    ps = r.get("pct_of_standalone", ""); ps = "" if ps in (None, "") else ps
    print(f"{r['category']:<36} {str(r['area_km2']):>8} km2  {str(r['pct_of_FP']):>5}% FP  {ps:>6}")
