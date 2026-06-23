from argparse import ArgumentParser
from pathlib import Path
import sys

import geopandas as gpd
import pandas as pd
from shapely.geometry import box

try:
    from calculate_osm_agreement import (
        MODEL_CRS_IF_MISSING,
        TARGET_CRS,
        clean_polygons,
        clip_to_study_area,
        read_model,
        union_geom,
    )
except ModuleNotFoundError:
    from calculate.calculate_osm_agreement import (
        MODEL_CRS_IF_MISSING,
        TARGET_CRS,
        clean_polygons,
        clip_to_study_area,
        read_model,
        union_geom,
    )


BASE_DIR = Path(__file__).resolve().parent

DEFAULT_MODEL_FILE = (
    BASE_DIR / "output_files_merged" / "leeds_original_merged.geojson"
)
DEFAULT_MANUAL_FILE = BASE_DIR / "manual" / "leeds_manual_validation.gpkg"
DEFAULT_MANUAL_LAYER = "leeds_manual_validation"
DEFAULT_RESULTS_DIR = BASE_DIR / "manual_results"


def parse_args():
    parser = ArgumentParser(
        description=(
            "Calculate agreement between merged model parking polygons and "
            "manual parking validation polygons."
        )
    )
    parser.add_argument(
        "--model-file",
        type=Path,
        default=DEFAULT_MODEL_FILE,
        help="Model GeoJSON to evaluate.",
    )
    parser.add_argument(
        "--manual-file",
        type=Path,
        default=DEFAULT_MANUAL_FILE,
        help="Manual validation GeoPackage.",
    )
    parser.add_argument(
        "--manual-layer",
        default=DEFAULT_MANUAL_LAYER,
        help="Layer name inside the manual validation GeoPackage.",
    )
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=DEFAULT_RESULTS_DIR,
        help="Directory for metrics CSV and comparison GeoPackage outputs.",
    )
    parser.add_argument(
        "--study-area",
        choices=["combined_bounds", "model_bounds", "manual_bounds"],
        default="combined_bounds",
        help=(
            "Bounding box used to clip both layers before area calculation. "
            "combined_bounds keeps all model and manual polygons."
        ),
    )
    return parser.parse_args()


def read_manual(path, layer):
    manual = gpd.read_file(path, layer=layer)
    if manual.crs is None:
        manual = manual.set_crs(MODEL_CRS_IF_MISSING)
    return manual


def bounds_to_box(*gdfs):
    bounds = [gdf.total_bounds for gdf in gdfs if not gdf.empty]
    if not bounds:
        raise ValueError("Cannot build study area from empty layers.")

    minx = min(bound[0] for bound in bounds)
    miny = min(bound[1] for bound in bounds)
    maxx = max(bound[2] for bound in bounds)
    maxy = max(bound[3] for bound in bounds)
    return box(minx, miny, maxx, maxy)


def choose_study_area(model, manual, source):
    if source == "model_bounds":
        return box(*model.total_bounds)
    if source == "manual_bounds":
        return box(*manual.total_bounds)
    return bounds_to_box(model, manual)


def write_layer(gpkg_file, layer, geom):
    if geom.is_empty:
        gdf = gpd.GeoDataFrame(
            {"layer": pd.Series(dtype="object")},
            geometry=gpd.GeoSeries([], crs=TARGET_CRS),
            crs=TARGET_CRS,
        )
    else:
        gdf = gpd.GeoDataFrame({"layer": [layer]}, geometry=[geom], crs=TARGET_CRS)

    gdf.to_file(gpkg_file, layer=layer, driver="GPKG")


def calculate_manual_metrics(model, manual, study_area, comparison_file):
    model_geom = union_geom(clip_to_study_area(model, study_area))
    manual_geom = union_geom(clip_to_study_area(manual, study_area))

    overlap_geom = model_geom.intersection(manual_geom)
    model_only_geom = model_geom.difference(manual_geom)
    manual_only_geom = manual_geom.difference(model_geom)

    model_area = model_geom.area
    manual_area = manual_geom.area
    overlap_area = overlap_geom.area
    model_only_area = model_only_geom.area
    manual_only_area = manual_only_geom.area
    union_area = model_geom.union(manual_geom).area

    metrics = {
        "model_area_m2": model_area,
        "manual_area_m2": manual_area,
        "overlap_area_m2": overlap_area,
        "model_only_area_m2": model_only_area,
        "manual_only_area_m2": manual_only_area,
        "union_area_m2": union_area,
        "accuracy_like": overlap_area / model_area if model_area > 0 else None,
        "precision_like": overlap_area / model_area if model_area > 0 else None,
        "recall_like": overlap_area / manual_area if manual_area > 0 else None,
        "iou": overlap_area / union_area if union_area > 0 else None,
    }

    write_layer(comparison_file, "model_manual_overlap", overlap_geom)
    write_layer(comparison_file, "model_only", model_only_geom)
    write_layer(comparison_file, "manual_only", manual_only_geom)

    return metrics


def process_manual_agreement(
    model_file,
    manual_file,
    manual_layer,
    results_dir,
    study_area_source,
):
    result_name = model_file.stem
    results_dir.mkdir(parents=True, exist_ok=True)

    metrics_file = results_dir / f"{result_name}_manual_agreement_metrics.csv"
    comparison_file = results_dir / f"{result_name}_manual_comparison.gpkg"
    summary_file = results_dir / "manual_agreement_summary.csv"
    if comparison_file.exists():
        comparison_file.unlink()

    print(f"Reading model polygons: {model_file}")
    model = clean_polygons(read_model(model_file))
    if model.empty:
        raise ValueError(f"Model layer is empty: {model_file}")

    print(f"Reading manual validation polygons: {manual_file}, layer={manual_layer}")
    manual = clean_polygons(read_manual(manual_file, manual_layer))
    if manual.empty:
        raise ValueError(f"Manual validation layer is empty: {manual_file}")

    study_area = choose_study_area(model, manual, study_area_source)
    metrics = calculate_manual_metrics(model, manual, study_area, comparison_file)
    metrics.update(
        {
            "result_name": result_name,
            "model_file": str(model_file),
            "manual_file": str(manual_file),
            "manual_layer": manual_layer,
            "study_area": study_area_source,
        }
    )

    pd.Series(metrics).to_csv(metrics_file, header=False)
    pd.DataFrame([metrics]).to_csv(summary_file, index=False)

    print(pd.Series(metrics))
    print(f"Saved: {metrics_file}")
    print(f"Saved: {summary_file}")
    print(f"Saved: {comparison_file}")
    return metrics


def main():
    args = parse_args()
    process_manual_agreement(
        args.model_file.resolve(),
        args.manual_file.resolve(),
        args.manual_layer,
        args.results_dir.resolve(),
        args.study_area,
    )


if __name__ == "__main__":
    sys.exit(main())
