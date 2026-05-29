from argparse import ArgumentParser
from pathlib import Path
import sys

import geopandas as gpd
import pandas as pd
from shapely.geometry import box

try:
    from calculate_osm_agreement import (
        RESULTS_DIR,
        TARGET_CRS,
        calculate_metrics,
        clean_polygons,
        download_osm_parking,
        read_model,
        surface_parking_only,
    )
    from filter_large_parking_polygons import FILTERED_OUTPUT_DIR, threshold_label
except ModuleNotFoundError:
    from calculate.calculate_osm_agreement import (
        RESULTS_DIR,
        TARGET_CRS,
        calculate_metrics,
        clean_polygons,
        download_osm_parking,
        read_model,
        surface_parking_only,
    )
    from calculate.filter_large_parking_polygons import (
        FILTERED_OUTPUT_DIR,
        threshold_label,
    )


BASE_DIR = Path(__file__).resolve().parent
FILTERED_RESULTS_DIR = BASE_DIR / "filtered_results"


def parse_args():
    parser = ArgumentParser(
        description="Calculate OSM agreement for area-filtered model results."
    )
    parser.add_argument(
        "--min-area",
        type=float,
        default=500.0,
        help="Area threshold folder to read, in square metres.",
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=None,
        help="Directory containing filtered GeoJSON files.",
    )
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=None,
        help="Directory for filtered OSM agreement results.",
    )
    return parser.parse_args()


def default_input_dir(min_area):
    return FILTERED_OUTPUT_DIR / threshold_label(min_area)


def default_results_dir(min_area):
    return FILTERED_RESULTS_DIR / threshold_label(min_area)


def find_filtered_files(input_dir):
    return sorted(
        path
        for path in input_dir.rglob("*.geojson")
        if not path.name.startswith(".")
    )


def filter_by_area(gdf, min_area):
    if gdf.empty:
        return gdf

    filtered = gdf.copy()
    filtered["area_m2"] = filtered.geometry.area
    return filtered[filtered["area_m2"] >= min_area].copy()


def original_result_name(filtered_result_name, min_area):
    label = threshold_label(min_area)
    suffix = f"_{label}"
    if filtered_result_name.endswith(suffix):
        return filtered_result_name[: -len(suffix)]
    return filtered_result_name


def original_osm_cache_file(filtered_result_name, min_area):
    result_name = original_result_name(filtered_result_name, min_area)
    return RESULTS_DIR / result_name / f"{result_name}_osm_parking.gpkg"


def process_filtered_file(model_file, results_dir, min_area):
    result_name = model_file.stem
    result_dir = results_dir / result_name
    result_dir.mkdir(parents=True, exist_ok=True)

    osm_file = result_dir / f"{result_name}_osm_parking.gpkg"
    overlap_file = result_dir / f"{result_name}_overlap.gpkg"
    metrics_file = result_dir / f"{result_name}_osm_agreement_metrics.csv"

    print(f"\nReading filtered model polygons: {model_file}")
    model = clean_polygons(read_model(model_file))

    if model.empty:
        print(f"Skipped empty filtered model layer: {model_file}")
        return None

    study_area = box(*model.total_bounds)
    original_osm_file = original_osm_cache_file(result_name, min_area)
    osm_cache_message = f"Saved: {osm_file}"

    if original_osm_file.exists():
        print(f"Reading full cached OSM parking from original results: {original_osm_file}")
        osm = gpd.read_file(original_osm_file, layer="osm_parking")
        osm_cache_message = f"Used full OSM cache: {original_osm_file}"
    elif osm_file.exists():
        print(f"Reading cached OSM parking: {osm_file}")
        osm = gpd.read_file(osm_file, layer="osm_parking")
        osm_cache_message = f"Used full OSM cache: {osm_file}"
    else:
        print("Downloading OSM amenity=parking features...")
        osm = download_osm_parking(study_area)
        osm = clean_polygons(surface_parking_only(osm))
        osm.to_file(osm_file, layer="osm_parking", driver="GPKG")

    osm = filter_by_area(osm, min_area)

    metrics = calculate_metrics(model, osm, study_area, overlap_file)
    metrics["result_name"] = result_name
    metrics["model_file"] = str(model_file)
    metrics["min_area_m2"] = min_area
    metrics["osm_area_filtered"] = True
    pd.Series(metrics).to_csv(metrics_file, header=False)

    print(pd.Series(metrics))
    print(f"Saved: {metrics_file}")
    print(osm_cache_message)
    print(f"Saved: {overlap_file}")
    return metrics


def main():
    args = parse_args()
    input_dir = (args.input_dir or default_input_dir(args.min_area)).resolve()
    results_dir = (args.results_dir or default_results_dir(args.min_area)).resolve()

    model_files = find_filtered_files(input_dir)
    if not model_files:
        raise FileNotFoundError(
            f"No filtered GeoJSON files found in {input_dir}. "
            "Run filter_large_parking_polygons.py first."
        )

    results_dir.mkdir(parents=True, exist_ok=True)

    all_metrics = []
    for model_file in model_files:
        metrics = process_filtered_file(model_file, results_dir, args.min_area)
        if metrics is not None:
            all_metrics.append(metrics)

    if all_metrics:
        label = threshold_label(args.min_area)
        summary_file = results_dir / f"filtered_osm_agreement_summary_{label}.csv"
        pd.DataFrame(all_metrics).to_csv(summary_file, index=False)
        print(f"\nSaved summary: {summary_file}")


if __name__ == "__main__":
    sys.exit(main())
