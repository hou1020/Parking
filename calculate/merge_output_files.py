from argparse import ArgumentParser
import csv
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent
OUTPUT_FILES_DIR = PROJECT_DIR / "parking-lot-mapping-tool" / "output_files"
MERGED_OUTPUT_DIR = BASE_DIR / "output_files_merged"


def parse_args():
    parser = ArgumentParser(
        description="Merge GeoJSON files in each output_files subfolder."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=OUTPUT_FILES_DIR,
        help="Directory containing model output GeoJSON folders.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=MERGED_OUTPUT_DIR,
        help="Directory for merged GeoJSON files.",
    )
    return parser.parse_args()


def find_geojson_files(input_dir):
    return sorted(
        path
        for path in input_dir.rglob("*.geojson")
        if not path.name.startswith(".")
    )


def group_files_by_folder(files, input_dir):
    groups = {}
    for path in files:
        folder = path.parent.relative_to(input_dir)
        if folder == Path("."):
            folder = Path(input_dir.name)
        groups.setdefault(folder, []).append(path)
    return groups


def read_feature_collection(path):
    with path.open(encoding="utf-8") as file:
        data = json.load(file)

    if data.get("type") != "FeatureCollection":
        raise ValueError(f"Expected FeatureCollection in {path}")

    return data


def output_file_for(folder, output_dir):
    safe_name = "_".join(folder.parts)
    return output_dir / f"{safe_name}_merged.geojson"


def merge_group(folder, files, output_dir):
    merged = {
        "type": "FeatureCollection",
        "name": f"{'_'.join(folder.parts)}_merged",
        "features": [],
    }

    for path in files:
        data = read_feature_collection(path)
        if "crs" in data and "crs" not in merged:
            merged["crs"] = data["crs"]

        for feature in data.get("features", []):
            feature = dict(feature)
            properties = dict(feature.get("properties") or {})
            properties["source_folder"] = str(folder)
            properties["source_file"] = path.name
            feature["properties"] = properties
            merged["features"].append(feature)

    output_file = output_file_for(folder, output_dir)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", encoding="utf-8") as file:
        json.dump(merged, file, ensure_ascii=False)

    return {
        "folder": str(folder),
        "input_files": len(files),
        "features": len(merged["features"]),
        "output_file": str(output_file),
    }


def main():
    args = parse_args()
    input_dir = args.input_dir.resolve()
    output_dir = args.output_dir.resolve()

    files = find_geojson_files(input_dir)
    if not files:
        raise FileNotFoundError(f"No GeoJSON files found in {input_dir}")

    groups = group_files_by_folder(files, input_dir)
    print(f"Found {len(files)} GeoJSON files in {len(groups)} folder(s)")
    print(f"Output directory: {output_dir}")

    rows = []
    for folder, folder_files in sorted(groups.items()):
        result = merge_group(folder, folder_files, output_dir)
        rows.append(result)
        print(
            f"{result['folder']}: merged {result['input_files']} file(s), "
            f"{result['features']} feature(s)"
        )

    summary_file = output_dir / "merge_summary.csv"
    with summary_file.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["folder", "input_files", "features", "output_file"]
        )
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved summary: {summary_file}")


if __name__ == "__main__":
    main()
