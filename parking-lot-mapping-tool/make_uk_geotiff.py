from pathlib import Path
import argparse

from PIL import Image
from PIL.TiffImagePlugin import ImageFileDirectory_v2


ROOT = Path(__file__).resolve().parent
DEFAULT_INPUT_DIR = ROOT / "files" / "aerial"
DEFAULT_OUTPUT_DIR = ROOT / "files" / "tif"


def read_world_file(path):
    a, d, b, e, c, f = [float(line.strip()) for line in path.read_text().splitlines()]

    # jgw 里的 c/f 是像素中心点坐标；GeoTIFF 需要左上角坐标。
    return {
        "pixel_width": abs(a),
        "pixel_height": abs(e),
        "top_left_x": c - (a / 2) - (b / 2),
        "top_left_y": f - (d / 2) - (e / 2),
    }


def geotiff_tags(transform):
    tags = ImageFileDirectory_v2()

    tags[33550] = (transform["pixel_width"], transform["pixel_height"], 0.0)
    tags[33922] = (0.0, 0.0, 0.0, transform["top_left_x"], transform["top_left_y"], 0.0)
    tags[34735] = (
        1, 1, 0, 4,
        1024, 0, 1, 1,      # 投影坐标
        1025, 0, 1, 1,      # 像素代表面积
        3072, 0, 1, 27700,  # EPSG:27700 British National Grid
        3076, 0, 1, 9001,   # 单位：米
    )

    return tags


def output_dir_for_image(image_path, input_dir, output_dir):
    relative = image_path.relative_to(input_dir)
    download_name = relative.parts[0]

    # Getmapping downloads store tiles as <download>/<5km-part>/se/*.jpg.
    if len(relative.parts) >= 4 and image_path.parent.name.lower() == "se":
        part_name = image_path.parent.parent.name
    elif len(relative.parts) >= 3:
        part_name = image_path.parent.name
    else:
        part_name = "tiles"

    return output_dir / download_name / part_name


def find_images(input_dir):
    return sorted(
        path
        for path in input_dir.rglob("*.jpg")
        if path.with_suffix(".jgw").exists()
    )


def convert_to_geotiff(image_path, input_dir, output_dir, compression, jpeg_quality, overwrite):
    world_path = image_path.with_suffix(".jgw")
    image_output_dir = output_dir_for_image(image_path, input_dir, output_dir)
    output_path = image_output_dir / f"{image_path.stem}.tif"

    if not world_path.exists():
        raise FileNotFoundError(f"Missing world file: {world_path}")
    if output_path.exists() and not overwrite:
        print(f"Skipped existing GeoTIFF: {output_path}")
        return False

    transform = read_world_file(world_path)
    image_output_dir.mkdir(parents=True, exist_ok=True)

    with Image.open(image_path) as image:
        image = image.convert("RGB")
        save_kwargs = {
            "format": "TIFF",
            "tiffinfo": geotiff_tags(transform),
            "compression": compression,
        }
        if compression == "jpeg":
            save_kwargs["quality"] = jpeg_quality

        image.save(output_path, **save_kwargs)

    print(f"Created GeoTIFF: {output_path}")
    return True


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert all aerial JPG/JGW tiles under files/aerial into GeoTIFFs."
    )
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_INPUT_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--compression",
        choices=("jpeg", "tiff_lzw", "raw"),
        default="jpeg",
        help="TIFF compression. JPEG keeps aerial RGB tiles compact.",
    )
    parser.add_argument(
        "--jpeg-quality",
        type=int,
        default=75,
        help="JPEG quality used when --compression=jpeg.",
    )
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    input_dir = args.input_dir.resolve()
    output_dir = args.output_dir.resolve()

    output_dir.mkdir(parents=True, exist_ok=True)

    image_paths = find_images(input_dir)
    if not image_paths:
        raise FileNotFoundError(f"No jpg files with matching jgw files found in {input_dir}")

    converted = 0
    for image_path in image_paths:
        if convert_to_geotiff(
            image_path,
            input_dir,
            output_dir,
            args.compression,
            args.jpeg_quality,
            args.overwrite,
        ):
            converted += 1

    print(f"Finished converting {converted} of {len(image_paths)} files.")


if __name__ == "__main__":
    main()
