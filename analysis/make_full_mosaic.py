"""
Mosaic the Digimap aerial tiles into one GeoTIFF for QGIS — Leeds
Author: Hou

Writes a single tiled BigTIFF covering all the model-input tiles at their native
0.25 m, with Deflate compression so QGIS does not need libjpeg. The originals are
read only.

The file is large, so it is written tile by tile through a generator rather than
assembled in memory: peak memory stays in the tens of megabytes instead of the
6.7 GB the whole array would take. Free disk space is checked as the write
proceeds and the run aborts, removing the partial file, if headroom falls below
MIN_FREE_GB — filling the disk is worse than not having the mosaic.

Set AREA to limit the output to part of the grid if the full extent is too large.

Outputs:
  - digimap_full.tif   : load this in QGIS
"""
import os, glob, re, shutil, sys
import numpy as np
from PIL import Image
import tifffile
import warnings; warnings.filterwarnings("ignore")

Image.MAX_IMAGE_PIXELS = None

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = f"{HERE}/digimap_full.tif"

PX, TILE_PX = 0.25, 4000
TILE_M = int(TILE_PX * PX)
OUT_TILE = 512                # output tile size in pixels
MIN_FREE_GB = 0.7             # abort if free space drops below this
AREA = None                   # (minx, miny, maxx, maxy) in BNG, or None for all
OPEN_LIMIT = 8                # source images held open at once


def log(m):
    print(m, flush=True)


def free_gb():
    return shutil.disk_usage(HERE).free / 1e9


def tile_key(path):
    m = re.match(r"se(\d{2})(\d{2})_rgb_250_\d+\.tif", os.path.basename(path))
    return (400000 + int(m.group(1)) * 1000, 400000 + int(m.group(2)) * 1000) if m else None


log("indexing source tiles ...")
src = {}
for p in glob.glob(f"{ROOT}/**/*_rgb_250_*.tif", recursive=True):
    if os.path.abspath(p) == os.path.abspath(OUT):
        continue
    k = tile_key(p)
    if k:
        src.setdefault(k, p)
if AREA:
    x0, y0, x1, y1 = AREA
    src = {(x, y): p for (x, y), p in src.items()
           if x + TILE_M > x0 and x < x1 and y + TILE_M > y0 and y < y1}
if not src:
    sys.exit("no tiles found")

xs = [x for x, _ in src]
ys = [y for _, y in src]
minx, maxx = min(xs), max(xs) + TILE_M
miny, maxy = min(ys), max(ys) + TILE_M
W, H = int((maxx - minx) / PX), int((maxy - miny) / PX)
log(f"  {len(src)} tiles -> {W} x {H} px, {minx}-{maxx} E, {miny}-{maxy} N")
log(f"  free disk before: {free_gb():.2f} GB")

_open = {}


def source_image(key):
    path = src[key]
    if path not in _open:
        if len(_open) >= OPEN_LIMIT:
            _open.pop(next(iter(_open))).close()
        _open[path] = Image.open(path).convert("RGB")
    return _open[path]


def tiles():
    """Yield output tiles in row-major order, reading only what each needs."""
    ny, nx = (H + OUT_TILE - 1) // OUT_TILE, (W + OUT_TILE - 1) // OUT_TILE
    checked = 0
    for ty in range(ny):
        for tx in range(nx):
            buf = np.zeros((OUT_TILE, OUT_TILE, 3), np.uint8)
            # ground window of this output tile
            gx0 = minx + tx * OUT_TILE * PX
            gy1 = maxy - ty * OUT_TILE * PX
            gx1, gy0 = gx0 + OUT_TILE * PX, gy1 - OUT_TILE * PX
            for kx in range(int(gx0 // TILE_M) * TILE_M, int(gx1 // TILE_M) * TILE_M + TILE_M, TILE_M):
                for ky in range(int(gy0 // TILE_M) * TILE_M, int(gy1 // TILE_M) * TILE_M + TILE_M, TILE_M):
                    if (kx, ky) not in src:
                        continue
                    ox0, oy0 = max(gx0, kx), max(gy0, ky)
                    ox1, oy1 = min(gx1, kx + TILE_M), min(gy1, ky + TILE_M)
                    if ox1 <= ox0 or oy1 <= oy0:
                        continue
                    im = source_image((kx, ky))
                    crop = im.crop((int(round((ox0 - kx) / PX)),
                                    int(round((ky + TILE_M - oy1) / PX)),
                                    int(round((ox1 - kx) / PX)),
                                    int(round((ky + TILE_M - oy0) / PX))))
                    r0 = int(round((gy1 - oy1) / PX))
                    c0 = int(round((ox0 - gx0) / PX))
                    a = np.asarray(crop, np.uint8)
                    buf[r0:r0 + a.shape[0], c0:c0 + a.shape[1]] = a
            yield buf
            checked += 1
            if checked % 500 == 0:
                f = free_gb()
                log(f"  {checked}/{nx*ny} output tiles, free {f:.2f} GB")
                if f < MIN_FREE_GB:
                    raise RuntimeError(f"aborting: only {f:.2f} GB free")


# GeoTIFF tags: pixel scale, tiepoint, and the minimum geokeys for EPSG:27700
extratags = [
    (33550, 12, 3, (PX, PX, 0.0), True),
    (33922, 12, 6, (0.0, 0.0, 0.0, float(minx), float(maxy), 0.0), True),
    (34735, 3, 20, (1, 1, 0, 4, 1024, 0, 1, 1, 1025, 0, 1, 1, 3072, 0, 1, 27700,
                    3076, 0, 1, 9001), True),
]

log("writing ...")
try:
    with tifffile.TiffWriter(OUT, bigtiff=True) as tw:
        tw.write(tiles(), shape=(H, W, 3), dtype=np.uint8,
                 tile=(OUT_TILE, OUT_TILE), photometric="rgb",
                 compression="deflate", extratags=extratags)
except Exception as e:
    if os.path.exists(OUT):
        os.remove(OUT)
    log(f"FAILED, partial file removed: {e}")
    sys.exit(1)

log(f"\nwrote: {OUT}  ({os.path.getsize(OUT)/1e9:.2f} GB)")
log(f"free disk after: {free_gb():.2f} GB")
