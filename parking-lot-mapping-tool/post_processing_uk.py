import json
import time
from pathlib import Path

import geopandas as gpd
import pandas as pd
import requests
from shapely.geometry import LineString, MultiPolygon, Polygon, box
from shapely.ops import polygonize, unary_union


TARGET_CRS = "EPSG:27700"
OVERPASS_URLS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.openstreetmap.ru/api/interpreter",
]
OVERPASS_TIMEOUT = 180
OVERPASS_RETRIES = 2
OVERPASS_RETRY_WAIT_SECONDS = 20
OVERPASS_CHUNK_SIZE_M = 1250

EXCLUDED_ROADS = {
    "bridleway",
    "construction",
    "corridor",
    "cycleway",
    "footway",
    "path",
    "pedestrian",
    "platform",
    "proposed",
    "raceway",
    "service",
    "steps",
    "track",
}

ROAD_BUFFERS = {
    "motorway": 14,
    "motorway_link": 9,
    "trunk": 12,
    "trunk_link": 8,
    "primary": 10,
    "primary_link": 7,
    "secondary": 8,
    "secondary_link": 6,
    "tertiary": 7,
    "tertiary_link": 5,
    "unclassified": 5,
    "residential": 5,
    "living_street": 4,
}


def postprocess_prediction_uk(
    prediction_path,
    tif_path,
    output_path,
    cache_dir=None,
    min_area_m2=0,
    allow_missing_osm=True,
):
    """Subtract OSM buildings and buffered UK roads from model polygons."""
    prediction_path = Path(prediction_path)
    tif_path = Path(tif_path)
    output_path = Path(output_path)
    cache_dir = Path(cache_dir or output_path.parent / "osm_cache")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cache_dir.mkdir(parents=True, exist_ok=True)

    model = read_polygons(prediction_path, TARGET_CRS)
    if model.empty:
        write_geojson(model, output_path)
        return output_path

    study_area = raster_bounds(tif_path)
    try:
        buildings, roads = load_masks(study_area, tif_path.stem, cache_dir)
    except RuntimeError as exc:
        if not allow_missing_osm:
            raise
        print(f"OSM removal failed for {tif_path}; saving unfiltered prediction instead.")
        print(exc)
        write_geojson(model.to_crs(TARGET_CRS), output_path)
        return output_path

    cleaned = subtract(subtract(model.to_crs(TARGET_CRS), buildings), roads)
    cleaned["geometry"] = cleaned.geometry.intersection(study_area)
    cleaned = clean_polygons(cleaned, TARGET_CRS)

    if min_area_m2 > 0 and not cleaned.empty:
        cleaned = cleaned[cleaned.geometry.area >= min_area_m2].copy()

    write_geojson(cleaned, output_path)
    return output_path


def load_masks(study_area, stem, cache_dir):
    building_cache = cache_dir / f"{stem}_osm_buildings.geojson"
    road_cache = cache_dir / f"{stem}_osm_road_buffers.geojson"

    if building_cache.exists() and road_cache.exists():
        return read_polygons(building_cache, TARGET_CRS), read_polygons(road_cache, TARGET_CRS)

    data = request_overpass_for_area(study_area)
    buildings = clean_polygons(osm_buildings(data).to_crs(TARGET_CRS), TARGET_CRS)
    roads = road_buffers(osm_roads(data).to_crs(TARGET_CRS))
    if not data.get("partial"):
        write_geojson(buildings, building_cache)
        write_geojson(roads, road_cache)
    return buildings, roads


def request_overpass_for_area(study_area):
    """Query OSM in smaller chunks so large 5km tiles do not time out Overpass."""
    elements = {}
    errors = []
    chunks = split_study_area(study_area, OVERPASS_CHUNK_SIZE_M)

    for index, chunk in enumerate(chunks, start=1):
        try:
            data = request_overpass(overpass_query(wgs84_bbox(chunk)))
        except RuntimeError as exc:
            errors.append(f"chunk {index}/{len(chunks)}: {exc}")
            continue

        for element in data.get("elements", []):
            key = (element.get("type"), element.get("id"))
            if key[0] is None or key[1] is None:
                key = ("missing-id", index, len(elements))
            elements[key] = element

    if errors:
        print("Some Overpass chunks failed; continuing with available OSM data:")
        print("\n".join(errors))

    if not elements and errors:
        raise RuntimeError("All Overpass chunk requests failed:\n" + "\n".join(errors))

    return {"elements": list(elements.values()), "partial": bool(errors)}


def split_study_area(study_area, chunk_size_m):
    min_x, min_y, max_x, max_y = study_area.bounds
    chunks = []

    x = min_x
    while x < max_x:
        y = min_y
        next_x = min(x + chunk_size_m, max_x)
        while y < max_y:
            next_y = min(y + chunk_size_m, max_y)
            chunk = box(x, y, next_x, next_y).intersection(study_area)
            if not chunk.is_empty:
                chunks.append(chunk)
            y = next_y
        x = next_x

    return chunks or [study_area]


def overpass_query(bbox):
    south, west, north, east = bbox
    bbox_text = f"{south:.7f},{west:.7f},{north:.7f},{east:.7f}"
    return f"""
    [out:json][timeout:180];
    (
      way["building"]({bbox_text});
      relation["building"]({bbox_text});
      way["highway"]({bbox_text});
    );
    out tags geom;
    """


def request_overpass(query):
    errors = []
    headers = {"User-Agent": "parking-uk-post-processing/1.0"}
    retry_statuses = {429, 500, 502, 503, 504}

    for attempt in range(1, OVERPASS_RETRIES + 1):
        for url in OVERPASS_URLS:
            try:
                response = requests.post(
                    url,
                    data={"data": query},
                    headers=headers,
                    timeout=OVERPASS_TIMEOUT,
                )
                if response.ok:
                    return response.json()

                errors.append(f"{url}: HTTP {response.status_code}")
                if response.status_code not in retry_statuses:
                    continue
            except requests.RequestException as exc:
                errors.append(f"{url}: {exc}")

        if attempt < OVERPASS_RETRIES:
            time.sleep(OVERPASS_RETRY_WAIT_SECONDS * attempt)

    raise RuntimeError("All Overpass API requests failed:\n" + "\n".join(errors))


def osm_buildings(data):
    rows = []
    for element in data.get("elements", []):
        if "building" not in element.get("tags", {}):
            continue
        geom = osm_polygon(element)
        if geom is not None and not geom.is_empty:
            rows.append(row(element, geom))
    return gdf(rows, "EPSG:4326")


def osm_roads(data):
    rows = []
    for element in data.get("elements", []):
        highway = element.get("tags", {}).get("highway")
        coords = coords_from_nodes(element.get("geometry", []))
        if element.get("type") == "way" and highway and highway not in EXCLUDED_ROADS and len(coords) > 1:
            rows.append(row(element, LineString(coords)))
    return gdf(rows, "EPSG:4326")


def road_buffers(roads):
    if roads.empty:
        return empty_gdf(TARGET_CRS)
    roads = roads.copy()
    roads["geometry"] = roads.apply(
        lambda item: item.geometry.buffer(buffer_width(item), cap_style="flat"),
        axis=1,
    )
    return clean_polygons(roads, TARGET_CRS)


def buffer_width(row):
    width = ROAD_BUFFERS.get(row.get("highway"), 5)
    lanes = parse_lanes(row.get("lanes"))
    return max(width, lanes * 3) if lanes else width


def parse_lanes(value):
    if pd.isna(value):
        return None
    try:
        return max(1, int(float(str(value).replace(";", "|").split("|")[0])))
    except ValueError:
        return None


def osm_polygon(element):
    if element.get("type") == "way":
        coords = coords_from_nodes(element.get("geometry", []))
        return Polygon(coords) if len(coords) >= 4 and coords[0] == coords[-1] else None

    if element.get("type") != "relation":
        return None

    outer, inner = [], []
    for member in element.get("members", []):
        coords = coords_from_nodes(member.get("geometry", []))
        if len(coords) < 2:
            continue
        (inner if member.get("role") == "inner" else outer).append(LineString(coords))

    outer_polygons = list(polygonize(outer))
    if not outer_polygons:
        return None
    geom = unary_union(outer_polygons)
    inner_polygons = list(polygonize(inner))
    return geom.difference(unary_union(inner_polygons)) if inner_polygons else geom


def subtract(base, mask):
    base = clean_polygons(base, TARGET_CRS)
    mask = clean_polygons(mask, TARGET_CRS)
    if base.empty or mask.empty:
        return base
    mask_union = union_all(mask)
    base = base.copy()
    base["geometry"] = base.geometry.apply(lambda geom: safe_difference(geom, mask_union))
    return clean_polygons(base, TARGET_CRS)


def raster_bounds(tif_path):
    import rasterio

    with rasterio.open(tif_path) as src:
        geom = box(src.bounds.left, src.bounds.bottom, src.bounds.right, src.bounds.top)
        return gpd.GeoSeries([geom], crs=src.crs).to_crs(TARGET_CRS).iloc[0]


def wgs84_bbox(geom):
    min_lon, min_lat, max_lon, max_lat = gpd.GeoSeries([geom], crs=TARGET_CRS).to_crs("EPSG:4326").iloc[0].bounds
    return min_lat, min_lon, max_lat, max_lon


def read_polygons(path, crs):
    data = gpd.read_file(path)
    return clean_polygons(data.set_crs(crs) if data.crs is None else data, crs)


def clean_polygons(data, crs):
    if data is None or data.empty:
        return empty_gdf(crs)
    data = data.to_crs(crs) if data.crs and str(data.crs) != str(crs) else data.set_crs(crs, allow_override=True)
    data = data[data.geometry.notna()].copy()
    if data.empty:
        return empty_gdf(crs)
    try:
        data["geometry"] = data.geometry.make_valid()
    except Exception:
        data["geometry"] = data.geometry.buffer(0)
    data = data[data.geometry.notna() & ~data.geometry.is_empty].explode(index_parts=False).reset_index(drop=True)
    return data[data.geometry.geom_type.isin(["Polygon", "MultiPolygon"])].copy()


def safe_difference(geom, mask):
    try:
        return fix_geometry(geom).difference(mask)
    except Exception:
        return fix_geometry(geom.buffer(0).difference(mask.buffer(0)))


def fix_geometry(geom):
    if geom is None or geom.is_empty:
        return None
    try:
        from shapely.validation import make_valid

        return make_valid(geom)
    except Exception:
        return geom.buffer(0)


def coords_from_nodes(nodes):
    return [(node["lon"], node["lat"]) for node in nodes if "lon" in node and "lat" in node]


def row(element, geom):
    tags = element.get("tags", {}).copy()
    return {**tags, "osm_type": element.get("type"), "osm_id": element.get("id"), "geometry": geom}


def union_all(data):
    try:
        return data.geometry.union_all()
    except AttributeError:
        return data.unary_union


def gdf(rows, crs):
    return gpd.GeoDataFrame(rows, geometry="geometry", crs=crs) if rows else empty_gdf(crs)


def empty_gdf(crs):
    return gpd.GeoDataFrame({"geometry": gpd.GeoSeries([], crs=crs)}, geometry="geometry", crs=crs)


def write_geojson(data, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if data.empty:
        path.write_text(json.dumps({"type": "FeatureCollection", "features": []}))
    else:
        data.to_file(path, driver="GeoJSON")
