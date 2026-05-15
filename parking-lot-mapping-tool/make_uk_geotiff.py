from pathlib import Path

import numpy as np
from PIL import Image
from PIL.TiffImagePlugin import ImageFileDirectory_v2


ROOT = Path(__file__).resolve().parent
IMAGE_PATH = ROOT / "files" / "uk" / "nt2774_rgb_250_05.jpg"
WORLD_PATH = ROOT / "files" / "uk" / "nt2774_rgb_250_05.jgw"
OUTPUT_PATH = ROOT / "files" / "nt2774_rgb_250_05.tif"


def read_world_file(path):
    a, d, b, e, c, f = [float(line.strip()) for line in path.read_text().splitlines()]

    # Convert from pixel centre coordinates to upper-left corner coordinates.
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
        1024, 0, 1, 1,      # GTModelTypeGeoKey: projected
        1025, 0, 1, 1,      # GTRasterTypeGeoKey: pixel is area
        3072, 0, 1, 27700,  # ProjectedCSTypeGeoKey: British National Grid
        3076, 0, 1, 9001,   # ProjLinearUnitsGeoKey: metre
    )

    return tags


transform = read_world_file(WORLD_PATH)

with Image.open(IMAGE_PATH) as image:
    image = image.convert("RGB")
    array = np.asarray(image)

Image.fromarray(array).save(
    OUTPUT_PATH,
    format="TIFF",
    tiffinfo=geotiff_tags(transform),
    compression="tiff_lzw",
)

print(f"Created GeoTIFF: {OUTPUT_PATH}")
