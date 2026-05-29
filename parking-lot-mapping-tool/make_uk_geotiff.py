from pathlib import Path

import numpy as np
from PIL import Image
from PIL.TiffImagePlugin import ImageFileDirectory_v2


ROOT = Path(__file__).resolve().parent
INPUT_DIR = ROOT / "files" / "leeds"
OUTPUT_DIR = ROOT / "files" / "leeds_tif"


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


def convert_to_geotiff(image_path, output_dir):
    world_path = image_path.with_suffix(".jgw")
    output_path = output_dir / f"{image_path.stem}.tif"

    if not world_path.exists():
        raise FileNotFoundError(f"Missing world file: {world_path}")

    transform = read_world_file(world_path)

    with Image.open(image_path) as image:
        image = image.convert("RGB")
        array = np.asarray(image)

    Image.fromarray(array).save(
        output_path,
        format="TIFF",
        tiffinfo=geotiff_tags(transform),
        compression="tiff_lzw",
    )

    print(f"Created GeoTIFF: {output_path}")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    image_paths = sorted(INPUT_DIR.glob("*.jpg"))
    if not image_paths:
        raise FileNotFoundError(f"No jpg files found in {INPUT_DIR}")

    for image_path in image_paths:
        convert_to_geotiff(image_path, OUTPUT_DIR)

    print(f"Finished converting {len(image_paths)} files.")


if __name__ == "__main__":
    main()
