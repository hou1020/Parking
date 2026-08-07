"""
Build the stratified sampling worksheet for the unexplained error residuals — Leeds
Author: Hou

Parts of the error taxonomy cannot be attributed automatically, because no
reference layer describes them: grey hardstanding, bare ground, houses absent
from OSM, lorry parks, shaded lots. Those residuals are characterised by
inspecting a sample rather than every polygon, which is standard practice in
remote-sensing accuracy assessment.

Three populations are sampled:
    fp_other      false positives no reference layer explains
    fn_other      whole labelled lots the model essentially missed, as exported
                  by fn_analysis.py. Earlier this was built from FN fragments
                  more than 5 m from a prediction, which had the same flaw as the
                  third population below: 74% of those fragments sat exactly on
                  the 5 m boundary, and a fifth of the area belonged to lots the
                  model had in fact detected, so they were the undrawn edge of a
                  found car park rather than a missed one. Whole lots are sampled
                  instead, so "why was this missed" is a question about a car
                  park rather than about a sliver of one.
    osm_disagree  OSM car parks the labelling has essentially not covered, to
                  check whether they are rule-based exclusions (on-street,
                  multi-storey, private driveways, vehicle storage) or parking
                  that should have been labelled and was missed.

    An earlier version of the third population was built from false-positive
    fragments more than 5 m from labelled parking. Inspection showed that was
    the wrong unit: a third of the sample sat exactly on the 5 m boundary and 12
    of 30 belonged to an OSM polygon that was already largely labelled, so they
    were the parcel margin around a correctly labelled car park. OSM outlines
    follow parcel boundaries rather than the pavement (Qiam et al., 2025), so
    unlabelled OSM area fringing a labelled lot is expected and is not evidence
    of a missing label. Defining the population as whole OSM polygons that the
    labelling has barely touched removes that artefact and makes it a question
    about the ground truth rather than about the model.

Sampling design
    Area, not polygon count, is what the taxonomy reports, and area is spread
    unevenly: for fp_other the 50 largest polygons hold only 27% of the area, so
    inspecting only large ones would bias the result. Each population is
    therefore split into size strata and sampled at random within each, with a
    fixed seed for reproducibility. Stratum totals are written out so the
    sampled proportions can be weighted back up to the full population.

Estimator (applied later, once categories are filled in)
    For stratum h with total area A_h, the estimated area of category c is
        A_h  x  (sampled area in category c / total sampled area in h)
    summed over strata. This is a ratio estimator, so strata that were
    oversampled relative to their size do not distort the totals.

Existing work is never overwritten: if the worksheet already exists and a
population already has categories filled in, that population's rows are carried
over unchanged and only the untouched populations are redrawn.

Reads read-only apart from the outputs below, in this folder.
Outputs:
  - sampling_worksheet.gpkg   : polygons to inspect, with empty category / note
                                fields to fill in QGIS
  - sampling_worksheet.csv    : the same table without geometry, for reference
  - sampling_strata.csv       : population and sample sizes per stratum, needed
                                to weight the results back up
"""
import os
import numpy as np
import pandas as pd
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
FP_OTHER = f"{HERE}/fp_unclassified.geojson"
FN_OTHER = f"{HERE}/fn_unclassified.geojson"

OUT_GPKG = f"{HERE}/sampling_worksheet.gpkg"
OUT_CSV = f"{HERE}/sampling_worksheet.csv"
OUT_STRATA = f"{HERE}/sampling_strata.csv"

SEED = 42
MIN_AREA = 100.0                     # ignore slivers below this
MAX_LABELLED = 0.10                  # "essentially unlabelled" OSM car park
BREAKS = [100, 300, 1000, 1e12]      # small / medium / large
LABELS = ["small_100_300", "medium_300_1k", "large_1k+"]
# how many polygons to inspect per stratum
N_PER_STRATUM = {
    "fp_other":     {"small_100_300": 20, "medium_300_1k": 25, "large_1k+": 25},
    "fn_other":     {"small_100_300": 10, "medium_300_1k": 15, "large_1k+": 20},
    "osm_disagree": {"small_100_300": 5,  "medium_300_1k": 10, "large_1k+": 15},
}

# Category lists are fixed before inspection so that classes are not invented
# to fit what has already been seen.
CATEGORIES = {
    "fp_other": "grey_hardstanding | bare_ground | goods_yard | sports_court | "
                "building_house | on_street | real_parking_missed | other",
    "fn_other": "lorry_van_lot | unusual_surface | shaded_occluded | small_irregular | "
                "rooftop | other",
    "osm_disagree": "on_street | multi_storey | private_driveway | vehicle_storage | "
                    "not_parking | real_parking_missed | other",
}


def dissolve(gdf, region=None):
    g = gdf.to_crs(27700).copy()
    g = g[g.geometry.type.isin(["Polygon", "MultiPolygon"])]
    g["geometry"] = g.geometry.buffer(0)
    u = unary_union(g.geometry.values)
    if region is not None:
        u = u.intersection(region)
    return gpd.GeoDataFrame(geometry=gpd.GeoSeries([u], crs=27700), crs=27700
                            ).explode(index_parts=False).reset_index(drop=True)


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


log("loading populations ...")
grid = gpd.read_file(GRID).to_crs(27700)
region = unary_union(grid.geometry.values)

pops = {
    "fp_other": gpd.read_file(FP_OTHER).to_crs(27700),
    "fn_other": gpd.read_file(FN_OTHER).to_crs(27700),
}

# build the omission-check population: whole OSM car parks the labelling has
# barely covered. Kept at polygon level so that the parcel margin around a
# correctly labelled lot is not mistaken for a missing label.
log("building osm_disagree population ...")
manual_raw = gpd.read_file(MANUAL).to_crs(27700)
manual_raw["geometry"] = manual_raw.geometry.buffer(0)
manual_u = unary_union(manual_raw.geometry.values).intersection(region)

ex = gpd.read_file(OSM_CACHE).to_crs(27700)
osm = ex[ex["grp"] == "osm_parking"].copy()
osm = osm[osm.geometry.type.isin(["Polygon", "MultiPolygon"])]
osm["geometry"] = osm.geometry.buffer(0)
osm = osm[osm.intersects(region)].reset_index(drop=True)
osm["_area"] = osm.geometry.area
osm["labelled_frac"] = osm.geometry.intersection(manual_u).area / osm["_area"]
pops["osm_disagree"] = osm[osm["labelled_frac"] <= MAX_LABELLED][
    ["labelled_frac", "geometry"]].reset_index(drop=True)

rng = np.random.default_rng(SEED)
sample_rows, strata_rows = [], []

for src, gdf in pops.items():
    g = gdf.copy()
    g["area_m2"] = g.geometry.area
    g = g[g["area_m2"] >= MIN_AREA].reset_index(drop=True)
    g["stratum"] = pd.cut(g["area_m2"], bins=BREAKS, labels=LABELS, right=False)

    for stratum in LABELS:
        sub = g[g["stratum"] == stratum]
        n_pop, a_pop = len(sub), float(sub["area_m2"].sum())
        n_take = min(N_PER_STRATUM[src][stratum], n_pop)
        strata_rows.append({"source": src, "stratum": stratum,
                            "n_population": n_pop, "area_population_m2": round(a_pop, 1),
                            "n_sampled": n_take})
        if n_take == 0:
            continue
        idx = rng.choice(sub.index.values, size=n_take, replace=False)
        for i in idx:
            geom = sub.loc[i, "geometry"]
            c = geom.centroid
            cell = grid[grid.contains(c)]
            cell_id = (f"c{int(cell.iloc[0]['col_index'])}r{int(cell.iloc[0]['row_index'])}"
                       if len(cell) else "")
            sample_rows.append({
                "sample_id": f"{src[:2]}_{stratum[0]}_{len(sample_rows)+1:03d}",
                "source": src, "stratum": stratum,
                "area_m2": round(float(sub.loc[i, "area_m2"]), 1),
                # share of this OSM car park already covered by manual labels;
                # only meaningful for the osm_disagree population
                "labelled_frac": (round(float(sub.loc[i, "labelled_frac"]), 3)
                                  if "labelled_frac" in sub.columns else None),
                "cell": cell_id,
                "centroid_x": round(c.x, 1), "centroid_y": round(c.y, 1),
                "category": "", "conf": None, "note": "",
                "options": CATEGORIES[src],
                "geometry": geom,
            })

samp = gpd.GeoDataFrame(sample_rows, crs=27700)

# carry over any population whose rows have already been worked on, so that
# regenerating the worksheet cannot destroy completed inspection
if os.path.exists(OUT_GPKG):
    prev = gpd.read_file(OUT_GPKG)
    cat = prev["category"].astype(str).str.strip()
    done = set(prev.loc[cat.ne("") & cat.ne("None") & cat.ne("nan"), "source"].unique())
    if done:
        keep = prev[prev["source"].isin(done)]
        samp = gpd.GeoDataFrame(
            pd.concat([keep, samp[~samp["source"].isin(done)]], ignore_index=True),
            geometry="geometry", crs=27700)
        strata_rows = [r for r in strata_rows if r["source"] not in done]
        prev_st = pd.read_csv(OUT_STRATA) if os.path.exists(OUT_STRATA) else None
        if prev_st is not None:
            strata_rows = (prev_st[prev_st["source"].isin(done)].to_dict("records")
                           + strata_rows)
        log(f"kept existing rows for: {', '.join(sorted(done))}")
samp.to_file(OUT_GPKG, driver="GPKG", layer="sampling_worksheet")
samp.drop(columns="geometry").to_csv(OUT_CSV, index=False)
pd.DataFrame(strata_rows).to_csv(OUT_STRATA, index=False)

log(f"\nwrote: {OUT_GPKG}\nwrote: {OUT_CSV}\nwrote: {OUT_STRATA}")
log("\n=== STRATA ===")
st = pd.DataFrame(strata_rows)
st["area_population_km2"] = (st["area_population_m2"]/1e6).round(4)
st["pct_sampled"] = (100*st["n_sampled"]/st["n_population"].replace(0, np.nan)).round(1)
print(st[["source", "stratum", "n_population", "area_population_km2",
          "n_sampled", "pct_sampled"]].to_string(index=False))
log(f"\ntotal polygons to inspect: {len(samp)}")
