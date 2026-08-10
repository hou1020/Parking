"""
Cut an image chip for every sampling-worksheet polygon — Leeds
Author: Hou

The samples have to be judged against the Digimap aerial tiles, because those are
what the model actually saw. One small chip per sample is quicker to work through
than navigating a mosaic in QGIS, and keeps the full 0.25 m resolution, so bay
markings and vehicle arrangement stay as legible as in the source. The whole set
is a few tens of megabytes.

Each chip carries the sampled polygon in red, the model's prediction in blue and
any other labelled parking nearby in yellow, so it answers its own question
without any panning or layer switching.

An index CSV is written alongside with the same fields as the worksheet, plus the
chip path. Categories can be typed into that CSV while flipping through the
images, and merged back into the worksheet afterwards.

Source imagery is read read-only and never modified.
Outputs:
  - chips/<source>/<sample_id>.png
  - chips/index.csv
"""
import os, glob, re, csv
import geopandas as gpd
from PIL import Image, ImageDraw
import warnings; warnings.filterwarnings("ignore")

Image.MAX_IMAGE_PIXELS = None

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
WORKSHEET = f"{HERE}/sampling_worksheet.gpkg"
MODEL = f"{ROOT}/Parking/calculate/output_files_merged/removal_merged.geojson"
MANUAL = f"{ROOT}/manual/leeds_manual.gpkg"
OUT_DIR = f"{HERE}/chips"

PX, TILE_PX = 0.25, 4000
TILE_M = int(TILE_PX * PX)
MARGIN_M = 30          # ground margin around the polygon
MAX_SIDE_PX = 1400     # cap, so a very large lot still yields a small file
OUTLINE = (255, 40, 40)      # the sampled polygon
MODEL_COL = (60, 140, 255)   # what the model predicted
MANUAL_COL = (255, 220, 40)  # other labelled parking nearby
OPEN_LIMIT = 6               # source images held open at once


def log(m):
    print(m, flush=True)


def tile_key(path):
    m = re.match(r"se(\d{2})(\d{2})_rgb_250_\d+\.tif", os.path.basename(path))
    return (400000 + int(m.group(1)) * 1000, 400000 + int(m.group(2)) * 1000) if m else None


log("indexing imagery ...")
tiles = {}
for p in glob.glob(f"{ROOT}/**/*_rgb_250_*.tif", recursive=True):
    k = tile_key(p)
    if k:
        tiles.setdefault(k, p)
log(f"  {len(tiles)} tiles")

ws = gpd.read_file(WORKSHEET).to_crs(27700)
model = gpd.read_file(MODEL).to_crs(27700)
manual = gpd.read_file(MANUAL).to_crs(27700)
log(f"  {len(ws)} worksheet polygons")

os.makedirs(OUT_DIR, exist_ok=True)
_open = {}


def read_window(minx, miny, maxx, maxy):
    """Mosaic the requested ground window out of the source tiles."""
    w = int(round((maxx - minx) / PX))
    h = int(round((maxy - miny) / PX))
    canvas = Image.new("RGB", (w, h), (20, 20, 20))
    for gx in range(int(minx // TILE_M) * TILE_M, int(maxx // TILE_M) * TILE_M + TILE_M, TILE_M):
        for gy in range(int(miny // TILE_M) * TILE_M, int(maxy // TILE_M) * TILE_M + TILE_M, TILE_M):
            path = tiles.get((gx, gy))
            if not path:
                continue
            if path not in _open:
                if len(_open) >= OPEN_LIMIT:
                    _open.pop(next(iter(_open))).close()
                _open[path] = Image.open(path)
            im = _open[path]
            ox0, oy0 = max(minx, gx), max(miny, gy)
            ox1, oy1 = min(maxx, gx + TILE_M), min(maxy, gy + TILE_M)
            if ox1 <= ox0 or oy1 <= oy0:
                continue
            src = (int(round((ox0 - gx) / PX)), int(round((gy + TILE_M - oy1) / PX)),
                   int(round((ox1 - gx) / PX)), int(round((gy + TILE_M - oy0) / PX)))
            canvas.paste(im.crop(src), (int(round((ox0 - minx) / PX)),
                                        int(round((maxy - oy1) / PX))))
    return canvas


def draw_poly(dr, geom, minx, maxy, scale, colour, width):
    polys = geom.geoms if geom.geom_type == "MultiPolygon" else [geom]
    for poly in polys:
        for ring in [poly.exterior] + list(poly.interiors):
            # coords may carry a Z value, so take only the first two
            pts = [((c[0] - minx) / PX * scale, (maxy - c[1]) / PX * scale)
                   for c in ring.coords]
            dr.line(pts + [pts[0]], fill=colour, width=width)


rows = []
for n, (_, r) in enumerate(ws.iterrows(), 1):
    g = r.geometry
    x0, y0, x1, y1 = g.bounds
    minx, miny = x0 - MARGIN_M, y0 - MARGIN_M
    maxx, maxy = x1 + MARGIN_M, y1 + MARGIN_M
    img = read_window(minx, miny, maxx, maxy)

    scale = min(1.0, MAX_SIDE_PX / max(img.size))
    if scale < 1.0:
        img = img.resize((max(1, int(img.width * scale)),
                          max(1, int(img.height * scale))), Image.LANCZOS)
    dr = ImageDraw.Draw(img)
    # context first, sampled polygon last so it stays on top
    for layer, colour in [(manual, MANUAL_COL), (model, MODEL_COL)]:
        for geom in layer[layer.intersects(g.buffer(MARGIN_M))].geometry.values:
            if not geom.is_empty:
                draw_poly(dr, geom, minx, maxy, scale, colour, 2)
    draw_poly(dr, g, minx, maxy, scale, OUTLINE, 3)

    sub = os.path.join(OUT_DIR, str(r["source"]))
    os.makedirs(sub, exist_ok=True)
    out = os.path.join(sub, f"{r['sample_id']}.png")
    img.save(out, optimize=True)

    rows.append({k: r[k] for k in ws.columns if k != "geometry"})
    rows[-1]["chip"] = os.path.relpath(out, HERE)
    if n % 20 == 0 or n == len(ws):
        log(f"  {n}/{len(ws)} chips")

with open(f"{OUT_DIR}/index.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)

size = sum(os.path.getsize(os.path.join(dp, fn))
           for dp, _, fns in os.walk(OUT_DIR) for fn in fns)
log(f"\nwrote {len(rows)} chips, {size/1e6:.1f} MB, into {OUT_DIR}")
log("red = sampled polygon, blue = model prediction, yellow = other labelled parking")
