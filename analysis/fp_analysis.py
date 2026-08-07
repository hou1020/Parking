"""
False-positive (FP) analysis for the removal model vs manual annotation — Leeds
Author: Hou

FP = model - manual (area the model calls parking but the manual truth does not).

(1) Dilation vs standalone split
    dilation FP   = FP within D metres of a true parking area
                    -> the model found the lot but drew it too large
    standalone FP = the rest -> parking detected where there is none
    Reported at D = 2, 5, 10 m; D = 5 m is used below.

(2) Attribution of standalone FP — reported two ways
    (a) Exclusive partition. Each square metre is assigned to one category only,
        so the shares sum to 100%. Layers are peeled off in order of how
        specific the evidence is, from precise features to broad land-use
        blankets, so a category is only credited with area that no more precise
        layer can explain:
            buildings      precise footprints
            osm_parking    precise parking polygons (a definition difference:
                           OSM calls it parking, the manual rules do not)
            sports_courts  precise facility polygons (OS Greenspace + OSM pitch)
            road_adjacent  proximity rule, road buffer widened by EXTRA_ROAD m
            brownfield     land-use polygons, moderate extent
            industrial     land-use polygons, broadest extent, so peeled last
            other          unexplained; exported for manual sampling
    (b) Unordered overlap. Each layer's raw overlap with all FP, computed
        independently. Categories may overlap and need not sum to 100%, but the
        numbers do not depend on the peeling order, so they show each layer's
        explanatory reach on its own terms.

    Both are reported because the exclusive shares depend on an ordering choice,
    whereas the unordered overlaps do not.

Caveat on interpretation: attribution is by location, not by inspection. FP on
OSM industrial land is "FP located on industrial or commercial land", which is
not the same as confirming each patch is a storage yard — real car parks also
sit on commercial and retail land.

Note: removal_merged already had OSM buildings and road buffers subtracted, so
building FP is residual (where OSM was incomplete) and the road buffer must be
widened to catch kerbside FP lying just outside the removed carriageway.

Reads source data read-only. Writes only the outputs below, in this folder.
Outputs:
  - fp_analysis_summary.csv     : exclusive partition + unordered overlaps
  - fp_unclassified.geojson     : "other" FP polygons (>= MIN_SAMPLE_M2) for sampling
  - ref_cache.gpkg              : cached OSM building / road-buffer unions
  - osm_extra.gpkg              : cached OSM land-use, pitch and parking polygons
"""
import os, glob, csv
import geopandas as gpd
import pandas as pd
from shapely.ops import unary_union
import warnings; warnings.filterwarnings("ignore")


def log(m):
    print(m, flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MODEL = f"{ROOT}/Parking/calculate/output_files_merged/removal_merged.geojson"
MANUAL = f"{ROOT}/manual/leeds_manual.gpkg"
GRID = f"{ROOT}/manual/leeds_grid.gpkg"
OSM_ROOT = f"{ROOT}/Parking/parking-lot-mapping-tool/output_files/tif_removal"
GREENSPACE = f"{HERE}/OS Open Greenspace (ESRI Shape File) SE/data/SE_GreenspaceSite.shp"
OUT_SUMMARY = f"{HERE}/fp_analysis_summary.csv"
OUT_OTHER = f"{HERE}/fp_unclassified.geojson"
REF_CACHE = f"{HERE}/ref_cache.gpkg"
OSM_CACHE = f"{HERE}/osm_extra.gpkg"

DILATION_D, EXTRA_ROAD, MIN_SAMPLE_M2 = 5.0, 6.0, 100.0
SPORTS_HARD = ["Tennis Court", "Other Sports Facility", "Play Space"]
OSM_GROUPS = {
    "industrial_yard": {"landuse": ["industrial", "commercial", "retail", "railway", "depot"]},
    "brownfield_bare": {"landuse": ["brownfield", "construction", "greenfield", "landfill"]},
    "pitch": {"leisure": ["pitch", "track", "sports_centre"]},
    "osm_parking": {"amenity": ["parking"]},
}


# ---------- geometry helpers (shared with fn_analysis.py) ----------
def dissolve(gdf, region=None):
    """Clean, merge and explode a layer into disjoint parts."""
    g = gdf.to_crs(27700).copy()
    g = g[g.geometry.type.isin(["Polygon", "MultiPolygon"])]
    if not len(g):
        return gpd.GeoDataFrame(geometry=gpd.GeoSeries([], crs=27700), crs=27700)
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


# ---------- load ----------
log("loading model / manual / grid ...")
grid = gpd.read_file(GRID).to_crs(27700)
region = unary_union(grid.geometry.values)
model = dissolve(gpd.read_file(MODEL), region)
manual = dissolve(gpd.read_file(MANUAL), region)

FP = minus(model, manual)
fp_area = area(FP)
log(f"total FP area = {fp_area/1e6:.4f} km2")

# reference layers: buildings and road buffers (cached)
if os.path.exists(REF_CACHE):
    ref = gpd.read_file(REF_CACHE).to_crs(27700)
    buildings = as_parts(ref[ref["grp"] == "buildings"])   # cache is already dissolved
    roads = as_parts(ref[ref["grp"] == "roads"])
    log("loaded reference unions from cache")
else:
    log("merging cached OSM building / road-buffer tiles ...")

    def load_tiles(paths):
        parts = [gpd.read_file(p).to_crs(27700) for p in paths if os.path.getsize(p) > 0]
        parts = [g for g in parts if len(g)]
        return dissolve(pd.concat(parts, ignore_index=True))

    buildings = load_tiles(glob.glob(f"{OSM_ROOT}/**/osm_cache/*_osm_buildings.geojson", recursive=True))
    roads = load_tiles(glob.glob(f"{OSM_ROOT}/**/osm_cache/*_osm_road_buffers.geojson", recursive=True))
    gpd.GeoDataFrame({"grp": ["buildings", "roads"]},
                     geometry=[unary_union(buildings.geometry.values),
                               unary_union(roads.geometry.values)],
                     crs=27700).to_file(REF_CACHE, driver="GPKG")
    log("cached reference unions")

roads_wide = buffered(roads, EXTRA_ROAD)

# OS Greenspace sports facilities
gs = gpd.read_file(GREENSPACE).to_crs(27700)
gs_sports = dissolve(gs[gs["function"].isin(SPORTS_HARD)], region)

# extra OSM layers (cached)
if os.path.exists(OSM_CACHE):
    ex = gpd.read_file(OSM_CACHE).to_crs(27700)
    # this cache holds raw fetched polygons, which can overlap, so it must be
    # dissolved (unlike ref_cache.gpkg, which was stored already merged)
    osm = {g: dissolve(ex[ex["grp"] == g]) for g in OSM_GROUPS}
    log("loaded extra OSM from cache")
else:
    import osmnx as ox
    poly4326 = gpd.GeoSeries([region], crs=27700).to_crs(4326).iloc[0]
    frames, osm = [], {}
    for grp, tags in OSM_GROUPS.items():
        try:
            f = ox.features_from_polygon(poly4326, tags).to_crs(27700)
            f = f[f.geometry.type.isin(["Polygon", "MultiPolygon"])].reset_index()
            # keep the OSM id so each feature can be traced back, and its last-edit
            # date, which is needed to tell a stale OSM record from stale imagery
            idcol = "id" if "id" in f.columns else "osmid"
            keep = {"geometry": f.geometry, "grp": grp, "osmid": f[idcol]}
            f = gpd.GeoDataFrame(keep, geometry="geometry", crs=27700)
            frames.append(f)
            osm[grp] = dissolve(f)
            log(f"  fetched {grp}: {len(f)} polygons")
        except Exception as e:
            osm[grp] = None
            log(f"  {grp}: none ({e})")
    if frames:
        pd.concat(frames, ignore_index=True).to_file(OSM_CACHE, driver="GPKG")
        log("cached extra OSM")

sports = dissolve(pd.concat([gs_sports, osm["pitch"]], ignore_index=True)) \
    if osm.get("pitch") is not None and len(osm["pitch"]) else gs_sports

# ---------- (1) dilation vs standalone ----------
rows = [{"category": "TOTAL_FP", "area_km2": round(fp_area/1e6, 4), "pct_of_FP": 100.0}]
standalone = None
for D in (2.0, 5.0, 10.0):
    log(f"  dilation split at {D:.0f} m ...")
    buf = buffered(manual, D)
    dil = inter(FP, buf)
    stand = minus(FP, buf)
    rows.append({"category": f"dilation_FP_within_{int(D)}m", "area_km2": round(area(dil)/1e6, 4),
                 "pct_of_FP": round(100*area(dil)/fp_area, 1)})
    rows.append({"category": f"standalone_FP_beyond_{int(D)}m", "area_km2": round(area(stand)/1e6, 4),
                 "pct_of_FP": round(100*area(stand)/fp_area, 1)})
    if D == DILATION_D:
        standalone = stand
stand_area = area(standalone)

# ---------- (2a) exclusive partition, most specific evidence first ----------
PEEL_ORDER = [
    ("building", buildings),
    ("osm_parking", osm.get("osm_parking")),
    ("sports_courts", sports),
    ("road_adjacent", roads_wide),
    ("brownfield_bare", osm.get("brownfield_bare")),
    ("industrial_yard", osm.get("industrial_yard")),
]

log("attributing standalone FP (exclusive partition) ...")
excl, rem = {}, standalone
for name, layer in PEEL_ORDER:
    if layer is None or not len(layer):
        excl[name] = 0.0
        continue
    hit = inter(rem, layer)
    excl[name] = area(hit)
    rem = minus(rem, layer)
    log(f"  {name}: {excl[name]/1e6:.4f} km2")
other_fp = rem
excl["other_unexplained"] = area(other_fp)

rows.append({"category": f"--- standalone(>{int(DILATION_D)}m), exclusive partition ---",
             "area_km2": round(stand_area/1e6, 4), "pct_of_FP": round(100*stand_area/fp_area, 1)})
for name, _ in PEEL_ORDER:
    a = excl[name]
    rows.append({"category": f"{name}_FP", "area_km2": round(a/1e6, 4),
                 "pct_of_FP": round(100*a/fp_area, 1),
                 "pct_of_standalone": round(100*a/stand_area, 1) if stand_area else None})
a = excl["other_unexplained"]
rows.append({"category": "other_unexplained_FP", "area_km2": round(a/1e6, 4),
             "pct_of_FP": round(100*a/fp_area, 1),
             "pct_of_standalone": round(100*a/stand_area, 1) if stand_area else None})

# ---------- (2b) unordered overlaps, independent of peeling order ----------
log("computing unordered overlaps ...")
rows.append({"category": "--- unordered overlap with ALL FP (may overlap; need not sum to 100%) ---",
             "area_km2": "", "pct_of_FP": ""})
for name, layer in PEEL_ORDER:
    if layer is None or not len(layer):
        continue
    a = area(inter(FP, layer))
    rows.append({"category": f"overlap_{name}", "area_km2": round(a/1e6, 4),
                 "pct_of_FP": round(100*a/fp_area, 1)})

with open(OUT_SUMMARY, "w", newline="") as f:
    cols = ["category", "area_km2", "pct_of_FP", "pct_of_standalone"]
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for r in rows:
        w.writerow({c: r.get(c, "") for c in cols})

if len(other_fp):
    o = other_fp.copy()
    o["area_m2"] = o.geometry.area
    o = o[o["area_m2"] >= MIN_SAMPLE_M2].sort_values("area_m2", ascending=False).reset_index(drop=True)
    o.to_file(OUT_OTHER, driver="GeoJSON")
    log(f"exported {len(o)} 'other' FP polygons (>= {MIN_SAMPLE_M2:.0f} m2) for sampling")

log(f"\nwrote: {OUT_SUMMARY}\nwrote: {OUT_OTHER}")
log("\n=== FP ANALYSIS SUMMARY ===")
for r in rows:
    ps = r.get("pct_of_standalone", ""); ps = "" if ps in (None, "") else ps
    log(f"{r['category']:<40} {str(r['area_km2']):>8} km2  {str(r['pct_of_FP']):>5}% FP  {ps:>6}")
