from argparse import ArgumentParser
from pathlib import Path

import geopandas as gpd
import pandas as pd

try:
    from calculate_osm_agreement import (
        MODEL_CRS_IF_MISSING,
        OUTPUT_FILES_DIR,
        TARGET_CRS,
        clean_polygons,
    )
except ModuleNotFoundError:
    from calculate.calculate_osm_agreement import (
        MODEL_CRS_IF_MISSING,
        OUTPUT_FILES_DIR,
        TARGET_CRS,
        clean_polygons,
    )


BASE_DIR = Path(__file__).resolve().parent
FILTERED_OUTPUT_DIR = BASE_DIR / "filtered_output_files"


def parse_args():
    parser = ArgumentParser(
        description="Filter model parking polygons by projected area."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=OUTPUT_FILES_DIR,
        help="Directory containing original model GeoJSON files.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=FILTERED_OUTPUT_DIR,
        help="Directory for filtered GeoJSON files.",
    )
    parser.add_argument(
        "--min-area",
        type=float,
        default=500.0,
        help="Minimum polygon area in square metres.",
    )
    return parser.parse_args()


def find_geojson_files(input_dir):
    return sorted(
        path
        for path in input_dir.rglob("*.geojson")
        if not path.name.startswith(".")
    )


def threshold_label(min_area):
    if float(min_area).is_integer():
        return f"min_{int(min_area)}m2"
    return f"min_{str(min_area).replace('.', '_')}m2"


def output_path_for(input_file, input_dir, output_dir, min_area):
    rel_path = input_file.relative_to(input_dir)
    label = threshold_label(min_area)
    stem = rel_path.stem.replace("_original", "")
    return output_dir / label / rel_path.parent / f"{stem}_{label}.geojson"


def read_input_file(path):
    gdf = gpd.read_file(path)
    if gdf.crs is None:
        gdf = gdf.set_crs(MODEL_CRS_IF_MISSING)
    return gdf


def filter_file(input_file, input_dir, output_dir, min_area):
    polygons = clean_polygons(read_input_file(input_file))
    polygons["area_m2"] = polygons.geometry.area
    filtered = polygons[polygons["area_m2"] >= min_area].copy()

    output_file = output_path_for(input_file, input_dir, output_dir, min_area)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    filtered.to_crs(TARGET_CRS).to_file(output_file, driver="GeoJSON")

    return {
        "input_file": str(input_file),
        "output_file": str(output_file),
        "input_count": len(polygons),
        "output_count": len(filtered),
        "input_area_m2": polygons["area_m2"].sum(),
        "output_area_m2": filtered["area_m2"].sum(),
    }


def main():
    args = parse_args()
    input_dir = args.input_dir.resolve()
    output_dir = args.output_dir.resolve()

    files = find_geojson_files(input_dir)
    if not files:
        raise FileNotFoundError(f"No GeoJSON files found in {input_dir}")

    print(f"Filtering {len(files)} GeoJSON files")
    print(f"Minimum area: {args.min_area} m2")
    print(f"Output directory: {output_dir / threshold_label(args.min_area)}")

    rows = []
    for input_file in files:
        result = filter_file(input_file, input_dir, output_dir, args.min_area)
        rows.append(result)
        print(
            f"{Path(result['input_file']).name}: "
            f"{result['input_count']} -> {result['output_count']} polygons"
        )

    summary = pd.DataFrame(rows)
    summary_file = output_dir / threshold_label(args.min_area) / "filter_summary.csv"
    summary.to_csv(summary_file, index=False)
    print(f"Saved summary: {summary_file}")


if __name__ == "__main__":
    main()
