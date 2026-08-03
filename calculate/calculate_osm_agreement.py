from pathlib import Path
import sys
import time

from argparse import ArgumentParser
import geopandas as gpd
import pandas as pd
import requests
from shapely.geometry import LineString, MultiPolygon, Polygon, box
from shapely.ops import polygonize, unary_union


# ===================== 路径和参数 =====================

BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent

OUTPUT_FILES_DIR = PROJECT_DIR / "parking-lot-mapping-tool" / "output_files"
RESULTS_DIR = BASE_DIR / "results"

TARGET_CRS = "EPSG:27700"

# 如果模型输出文件缺少 CRS，就按 EPSG:27700 处理。
MODEL_CRS_IF_MISSING = "EPSG:27700"

OVERPASS_URLS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.openstreetmap.ru/api/interpreter",
]
OVERPASS_TIMEOUT_SECONDS = 45
OVERPASS_RETRIES = 1
OVERPASS_RETRY_WAIT_SECONDS = 10


def parse_args():
    parser = ArgumentParser(
        description="Calculate OSM parking agreement and write one summary table."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=OUTPUT_FILES_DIR,
        help="Directory containing model output GeoJSON files.",
    )
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=RESULTS_DIR,
        help="Directory for the summary CSV.",
    )
    parser.add_argument(
        "--save-layers",
        action="store_true",
        help="Also save per-file OSM parking, overlap GPKG, and metrics CSV outputs.",
    )
    parser.add_argument(
        "--stop-on-error",
        action="store_true",
        help="Stop on the first file-level error instead of recording it in the summary.",
    )
    return parser.parse_args()


# ===================== 数据清洗 =====================

def clean_polygons(gdf):
    """统一投影、修复几何，并只保留 polygon/multipolygon。"""
    gdf = gdf.to_crs(TARGET_CRS)
    gdf = gdf[gdf.geometry.notna()].copy()

    try:
        gdf["geometry"] = gdf.geometry.make_valid()
    except Exception:
        gdf["geometry"] = gdf.geometry.buffer(0)

    gdf = gdf[~gdf.geometry.is_empty].copy()
    gdf = gdf.explode(index_parts=False).reset_index(drop=True)
    return gdf[gdf.geometry.geom_type.isin(["Polygon", "MultiPolygon"])].copy()


def read_model(path):
    """读取一个模型输出 GeoJSON。"""
    model = gpd.read_file(path)
    if model.crs is None:
        model = model.set_crs(MODEL_CRS_IF_MISSING)
    return model


def surface_parking_only(osm):
    """排除非地面停车场，例如地下、多层、屋顶停车场。"""
    if osm.empty or "parking" not in osm.columns:
        return osm

    exclude = {"multi-storey", "underground", "rooftop"}
    return osm[~osm["parking"].astype(str).isin(exclude)].copy()


# ===================== OSM 下载 =====================

def download_osm_parking(study_area_27700):
    """用 Overpass API 下载研究范围内 amenity=parking 的 OSM 要素。"""
    study_area_wgs84 = gpd.GeoSeries([study_area_27700], crs=TARGET_CRS).to_crs(
        "EPSG:4326"
    ).iloc[0]

    query = build_overpass_query(study_area_wgs84)
    data = request_overpass(query)
    return overpass_json_to_gdf(data)


def build_overpass_query(polygon_wgs84):
    """生成 Overpass 查询；poly 参数需要 lat lon 顺序。"""
    if polygon_wgs84.geom_type == "MultiPolygon":
        polygon_wgs84 = max(polygon_wgs84.geoms, key=lambda g: g.area)

    coords = polygon_wgs84.exterior.coords
    poly_text = " ".join(f"{lat:.7f} {lon:.7f}" for lon, lat in coords)

    return f"""
    [out:json][timeout:180];
    (
      way["amenity"="parking"](poly:"{poly_text}");
      relation["amenity"="parking"](poly:"{poly_text}");
    );
    out tags geom;
    """


def request_overpass(query):
    """依次尝试几个 Overpass 镜像，避免单个服务不可用。"""
    errors = []
    headers = {"User-Agent": "parking-osm-agreement/1.0"}

    for attempt in range(1, OVERPASS_RETRIES + 1):
        for url in OVERPASS_URLS:
            try:
                response = requests.post(
                    url,
                    data={"data": query},
                    headers=headers,
                    timeout=OVERPASS_TIMEOUT_SECONDS,
                )
                if response.ok:
                    return response.json()
                errors.append(f"{url}: HTTP {response.status_code}")
            except requests.RequestException as exc:
                errors.append(f"{url}: {exc}")

        if attempt < OVERPASS_RETRIES:
            time.sleep(OVERPASS_RETRY_WAIT_SECONDS * attempt)

    raise RuntimeError("All Overpass API requests failed:\n" + "\n".join(errors))


def overpass_json_to_gdf(data):
    """把 Overpass JSON 转成 GeoDataFrame。"""
    rows = []

    for element in data.get("elements", []):
        geom = osm_element_to_polygon(element)
        if geom is None or geom.is_empty:
            continue

        tags = element.get("tags", {}).copy()
        tags["osm_type"] = element.get("type")
        tags["osm_id"] = element.get("id")
        rows.append({**tags, "geometry": geom})

    if not rows:
        return empty_osm_gdf()

    return gpd.GeoDataFrame(rows, geometry="geometry", crs="EPSG:4326")


def empty_osm_gdf():
    """返回一个带 geometry 列的空 OSM parking 图层。"""
    return gpd.GeoDataFrame(
        {"amenity": pd.Series(dtype="object"),
         "parking": pd.Series(dtype="object"),
         "osm_type": pd.Series(dtype="object"),
         "osm_id": pd.Series(dtype="Int64")},
        geometry=gpd.GeoSeries([], crs="EPSG:4326"),
        crs="EPSG:4326",
    )


def osm_element_to_polygon(element):
    """把 OSM way/relation 转成 shapely polygon。"""
    if element.get("type") == "way":
        coords = node_coords(element.get("geometry", []))
        if len(coords) >= 4 and coords[0] == coords[-1]:
            return Polygon(coords)
        return None

    if element.get("type") != "relation":
        return None

    outer_lines = []
    inner_lines = []
    for member in element.get("members", []):
        coords = node_coords(member.get("geometry", []))
        if len(coords) < 2:
            continue

        line = LineString(coords)
        if member.get("role") == "inner":
            inner_lines.append(line)
        else:
            outer_lines.append(line)

    if not outer_lines:
        return None

    outer = list(polygonize(outer_lines))
    inner = list(polygonize(inner_lines))
    if not outer:
        return None

    geom = unary_union(outer)
    if inner:
        geom = geom.difference(unary_union(inner))

    if isinstance(geom, (Polygon, MultiPolygon)):
        return geom
    return None


def node_coords(nodes):
    """Overpass 节点坐标是 lon/lat，正好是 shapely 需要的 x/y 顺序。"""
    return [(node["lon"], node["lat"]) for node in nodes if "lon" in node and "lat" in node]


# ===================== 指标计算 =====================

def union_geom(gdf):
    """合并同一图层的所有面，避免重叠部分被重复计算。"""
    try:
        return gdf.geometry.union_all()
    except AttributeError:
        return gdf.unary_union


def clip_to_study_area(gdf, study_area):
    """把图层裁剪到同一个研究范围。"""
    clipped = gdf.copy()
    clipped["geometry"] = clipped.geometry.intersection(study_area)
    return clean_polygons(clipped)


def calculate_metrics(model, osm, study_area, overlap_file=None):
    model_geom = union_geom(clip_to_study_area(model, study_area))
    osm_geom = union_geom(clip_to_study_area(osm, study_area))

    overlap_geom = model_geom.intersection(osm_geom)
    union_area = model_geom.union(osm_geom).area

    model_area = model_geom.area
    osm_area = osm_geom.area
    overlap_area = overlap_geom.area

    metrics = {
        "model_area_m2": model_area,
        "osm_area_m2": osm_area,
        "overlap_area_m2": overlap_area,
        "union_area_m2": union_area,
        "precision_like": overlap_area / model_area if model_area > 0 else None,
        "recall_like": overlap_area / osm_area if osm_area > 0 else None,
        "iou": overlap_area / union_area if union_area > 0 else None,
    }

    if overlap_file is not None:
        gpd.GeoDataFrame(
            {"layer": ["model_osm_overlap"]},
            geometry=[overlap_geom],
            crs=TARGET_CRS,
        ).to_file(overlap_file, layer="overlap", driver="GPKG")

    return metrics


# ===================== 主程序 =====================

def find_model_files(input_dir):
    """查找 output_files 里的所有模型结果文件。"""
    return sorted(
        path for path in input_dir.rglob("*.geojson")
        if should_include_model_file(path)
    )


def should_include_model_file(path):
    if path.name.startswith("."):
        return False
    if path.name.endswith("_merged.geojson"):
        return False
    if "osm_cache" in path.parts:
        return False
    return True


def process_model_file(model_file, results_dir, save_layers=False):
    """计算单个模型结果与 OSM parking 的重叠指标。"""
    result_name = model_file.stem.replace("_original", "")
    result_dir = results_dir / result_name

    osm_file = result_dir / f"{result_name}_osm_parking.gpkg"
    overlap_file = result_dir / f"{result_name}_overlap.gpkg"
    metrics_file = result_dir / f"{result_name}_osm_agreement_metrics.csv"

    print(f"\nReading model polygons: {model_file}")
    model = clean_polygons(read_model(model_file))

    if model.empty:
        print(f"Skipped empty model layer: {model_file}")
        return None

    # 这里使用模型结果的外接矩形作为研究范围。
    # 如果论文需要更严谨，可以改成影像 tile 边界或研究区边界。
    study_area = box(*model.total_bounds)

    if save_layers:
        result_dir.mkdir(parents=True, exist_ok=True)

    if save_layers and osm_file.exists():
        print(f"Reading cached OSM parking: {osm_file}")
        osm = gpd.read_file(osm_file, layer="osm_parking")
    else:
        print("Downloading OSM amenity=parking features...")
        osm = download_osm_parking(study_area)
        osm = clean_polygons(surface_parking_only(osm))
        if save_layers:
            osm.to_file(osm_file, layer="osm_parking", driver="GPKG")

    metrics = calculate_metrics(
        model,
        osm,
        study_area,
        overlap_file if save_layers else None,
    )
    metrics["result_name"] = result_name
    metrics["model_file"] = str(model_file)
    if save_layers:
        pd.Series(metrics).to_csv(metrics_file, header=False)

    print(pd.Series(metrics))
    if save_layers:
        print(f"Saved: {metrics_file}")
        print(f"Saved: {osm_file}")
        print(f"Saved: {overlap_file}")
    return metrics


def main():
    args = parse_args()
    input_dir = args.input_dir.resolve()
    results_dir = args.results_dir.resolve()

    model_files = find_model_files(input_dir)
    if not model_files:
        raise FileNotFoundError(f"No GeoJSON result files found in {input_dir}")

    results_dir.mkdir(parents=True, exist_ok=True)

    summary_file = results_dir / "osm_agreement_summary.csv"
    current_model_files = {str(path) for path in model_files}
    if summary_file.exists():
        previous_rows = pd.read_csv(summary_file).to_dict("records")
        all_metrics = [
            row for row in previous_rows
            if row.get("model_file") in current_model_files and row.get("status") == "ok"
        ]
    else:
        all_metrics = []

    completed = {row.get("model_file") for row in all_metrics}

    for model_file in model_files:
        if str(model_file) in completed:
            print(f"Skipping completed file: {model_file}")
            continue

        try:
            metrics = process_model_file(model_file, results_dir, save_layers=args.save_layers)
            if metrics is None:
                continue
            metrics["status"] = "ok"
            metrics["error"] = ""
        except Exception as exc:
            if args.stop_on_error:
                raise
            print(f"Failed: {model_file}\n{exc}")
            metrics = {
                "result_name": model_file.stem.replace("_original", ""),
                "model_file": str(model_file),
                "model_area_m2": None,
                "osm_area_m2": None,
                "overlap_area_m2": None,
                "union_area_m2": None,
                "precision_like": None,
                "recall_like": None,
                "iou": None,
                "status": "failed",
                "error": repr(exc),
            }

        all_metrics = [
            row for row in all_metrics if row.get("model_file") != str(model_file)
        ] + [metrics]
        pd.DataFrame(all_metrics).to_csv(summary_file, index=False)
        print(f"Saved summary: {summary_file}")


if __name__ == "__main__":
    sys.exit(main())
