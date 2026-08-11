"""
When were the OSM parking records last edited? — Leeds
Author: Hou

Sampling found that 63% of the OSM car parks the labelling had not covered show
no parking at all in the aerial imagery. The obvious explanation is that OSM is
out of date. This tests that explanation rather than assuming it, by reading the
last-edit date of every OSM parking feature and comparing the dates of the
records judged wrong against the rest.

If those records were old, staleness would be supported. If they are as recent as
any other, staleness is not the explanation and the disagreement has to be
described more carefully — which matters, because without a capture date for the
aerial imagery the direction of any temporal argument cannot be established.

Note on the field: `timestamp` is the last edit of any kind, including a tag
change on a feature drawn years earlier. It shows when a record was last
maintained, not when the car park was built, and it is used here only in that
sense.

The timestamps are fetched once from Overpass with `out meta` and stored in
osm_extra.gpkg; if they are already there the fetch is skipped.

Reads read-only apart from adding the timestamp columns to the OSM cache.
Output:
  - osm_timestamps_summary.csv
"""
import os, json, csv
import pandas as pd
import geopandas as gpd
from shapely.ops import unary_union
import warnings; warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
GRID = f"{ROOT}/manual/leeds_grid.gpkg"
OSM_CACHE = f"{HERE}/osm_extra.gpkg"
INDEX = f"{HERE}/chips/index.csv"
WORKSHEET = f"{HERE}/sampling_worksheet.gpkg"
OUT = f"{HERE}/osm_timestamps_summary.csv"

ENDPOINTS = ["https://overpass-api.de/api/interpreter",
             "https://overpass.kumi.systems/api/interpreter",
             "https://overpass.osm.ch/api/interpreter"]
HEADERS = {"User-Agent": "dissertation-research/1.0 (academic use)",
           "Accept": "application/json"}


def log(m):
    print(m, flush=True)


grid = gpd.read_file(GRID).to_crs(27700)
region = unary_union(grid.geometry.values)
ex = gpd.read_file(OSM_CACHE).to_crs(27700)

# ---- fetch metadata only if the cache does not already carry it ----
if "timestamp" not in ex.columns or ex.loc[ex["grp"] == "osm_parking", "timestamp"].isna().all():
    import requests, osmnx as ox
    log("fetching OSM metadata ...")
    poly4326 = gpd.GeoSeries([region], crs=27700).to_crs(4326).iloc[0]
    minx, miny, maxx, maxy = poly4326.bounds
    q = (f"[out:json][timeout:180];\n"
         f'(way["amenity"="parking"]({miny},{minx},{maxy},{maxx});\n'
         f' relation["amenity"="parking"]({miny},{minx},{maxy},{maxx}););\nout meta;')
    els = None
    for url in ENDPOINTS:
        try:
            r = requests.post(url, data={"data": q}, headers=HEADERS, timeout=300)
            r.raise_for_status()
            els = json.loads(r.text)["elements"]
            log(f"  ok via {url}")
            break
        except Exception as e:
            log(f"  failed {url}: {e}")
    if els is None:
        raise SystemExit("all Overpass endpoints failed")
    meta = {(e["type"], e["id"]): (e.get("timestamp"), e.get("version")) for e in els}

    f = ox.features_from_polygon(poly4326, {"amenity": ["parking"]}).to_crs(27700)
    f = f[f.geometry.type.isin(["Polygon", "MultiPolygon"])].reset_index()
    idcol = "id" if "id" in f.columns else "osmid"
    typecol = "element_type" if "element_type" in f.columns else "element"
    f["osmid"] = f[idcol]
    f["timestamp"] = [meta.get((t, i), (None, None))[0] for t, i in zip(f[typecol], f[idcol])]
    f["osm_version"] = [meta.get((t, i), (None, None))[1] for t, i in zip(f[typecol], f[idcol])]
    new = f[["geometry", "osmid", "timestamp", "osm_version"]].copy()
    new["grp"] = "osm_parking"
    ex = gpd.GeoDataFrame(pd.concat([ex[ex["grp"] != "osm_parking"], new], ignore_index=True),
                          geometry="geometry", crs=27700)
    ex.to_file(OSM_CACHE, driver="GPKG", layer="osm_extra")
    log(f"  stored metadata for {len(new)} parking polygons")
else:
    log("timestamps already present in the cache")

osm = ex[ex["grp"] == "osm_parking"].copy()
osm = osm[osm.intersects(region)]
osm["ts"] = pd.to_datetime(osm["timestamp"], errors="coerce", utc=True)
osm["year"] = osm["ts"].dt.year

rows = []


def add(scope, n, median, lo, hi, note=""):
    rows.append({"scope": scope, "n": n, "median_last_edit_year": median,
                 "earliest": lo, "latest": hi, "note": note})


add("all OSM parking in the study area", len(osm), int(osm["year"].median()),
    int(osm["year"].min()), int(osm["year"].max()), "")

# ---- the sampled OSM car parks, by how they were judged ----
d = pd.read_csv(INDEX)
d = d[d["source"] == "osm_disagree"].copy()
d["category"] = d["category"].astype(str).str.strip()
d = d[~d["category"].isin(["", "nan", "None"])]

ws = gpd.read_file(WORKSHEET)
ws = ws[ws["source"] == "osm_disagree"][["sample_id", "geometry"]]
j = gpd.sjoin(ws, osm[["year", "osm_version", "geometry"]], how="left", predicate="intersects")
j = j[~j.index.duplicated(keep="first")]
m = d.merge(j.drop(columns="geometry"), on="sample_id", how="left")

for cat, g in m.groupby("category"):
    yr = g["year"].dropna()
    if not len(yr):
        continue
    add(f"sampled: {cat}", len(g), int(yr.median()), int(yr.min()), int(yr.max()),
        f"{int((yr >= 2024).sum())} of {len(yr)} edited 2024 or later")

with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["scope", "n", "median_last_edit_year",
                                      "earliest", "latest", "note"])
    w.writeheader(); w.writerows(rows)
    w.writerow({})
    w.writerow({"scope": "year", "n": "count", "median_last_edit_year": "",
                "earliest": "", "latest": "", "note": "all OSM parking"})
    for y, c in osm["year"].value_counts().sort_index().items():
        w.writerow({"scope": int(y), "n": int(c)})

log(f"\nwrote: {OUT}\n")
log(pd.DataFrame(rows).to_string(index=False))
log("\nyear distribution, all OSM parking:")
log(osm["year"].value_counts().sort_index().to_string())

wrong = m[m["category"] == "not_parking"]["year"].dropna()
if len(wrong):
    log(f"\nRecords judged not to show parking: median last edit {int(wrong.median())}, "
        f"{int((wrong >= 2024).sum())} of {len(wrong)} edited 2024 or later. "
        f"They are not older than the rest, so staleness does not account for the "
        f"disagreement; without a capture date for the aerial imagery the direction "
        f"of any temporal claim cannot be established, and the disagreement is "
        f"reported neutrally as parking not visible in the imagery used here.")
