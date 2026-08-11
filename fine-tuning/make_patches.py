"""
Build aligned image/mask patch pairs — Leeds fine-tuning experiment
Author: Hou

The training masks must sit on exactly the same 512 px grid the inference pipeline cuts, or
the model is trained against displaced supervision. That failure is silent: nothing raises,
the masks simply disagree with the imagery by some fraction of a patch and the experiment
quietly underperforms. The tiling here therefore reproduces functions.split_images literally

    for i in range(0, h, 512):
        for j in range(0, w, 512):
            tile = img[i:i+512, j:j+512]        # zero-padded at the right and bottom edges

and derives every mask from the same GeoTIFF tie point and pixel scale as the image it
accompanies.

Two guards against silent misalignment:

    1. The rasterised parking area is summed over every patch and compared against the
       dissolved vector area of the reference. These are computed by completely different
       routes -- one through the tie point and PIL polygon filling, the other through
       shapely -- so agreement to a fraction of a percent means the geotransform is right.
       Disagreement means stop and fix it before training anything.
    2. Padding is recorded per patch as valid_h / valid_w rather than being trimmed. Each
       4000 px tile gives 8 columns of patches, the last holding only 416 real pixels, and
       counting predictions in the padded remainder as false positives would bias the
       evaluation against both models unequally.

Negatives are sampled in the training split only, at --neg-ratio times the number of patches
containing parking. The test split keeps every patch, including empty ones: dropping them
would inflate precision by removing exactly the places where a model over-predicts.

Reads read-only. Writes only into this folder.
Outputs:
  - patches/train/Masks/*.png and patches/test/Masks/*.png
  - optional image PNGs with --materialize-images (normally read from source TIFFs instead)
  - patch_index.csv
"""
import os, csv, glob, shutil, argparse
import numpy as np
import pandas as pd
import geopandas as gpd
import tifffile
from PIL import Image, ImageDraw
from shapely.geometry import box
import warnings; warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
TIF_GLOB = f"{ROOT}/Parking/parking-lot-mapping-tool/files/tif/**/*.tif"
MANUAL = f"{ROOT}/manual/leeds_manual.gpkg"
SPLIT = f"{HERE}/split.csv"
PATCH_DIR = f"{HERE}/patches"
OUT_INDEX = f"{HERE}/patch_index.csv"

PATCH = 512
TILE_M = 1000.0


def log(m):
    print(m, flush=True)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--neg-ratio", type=float, default=1.0,
                   help="empty training patches to keep, as a multiple of the parking ones")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--limit", type=int, default=0, help="stop after N tiles, for a smoke test")
    p.add_argument("--materialize-images", action="store_true",
                   help="also write image PNGs; requires many GB and is normally unnecessary")
    return p.parse_args()


def geo_reference(page):
    """Top-left world coordinate and pixel size, from the GeoTIFF tags."""
    sx, sy, _ = page.tags["ModelPixelScaleTag"].value
    tp = page.tags["ModelTiepointTag"].value
    return tp[3], tp[4], sx, sy


def rasterise(geoms, px0, py0, sx, sy, size):
    """Burn polygons into a size x size uint8 mask, 1 = parking, holes back to 0."""
    img = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(img)
    for g in geoms:
        parts = g.geoms if g.geom_type == "MultiPolygon" else [g]
        for poly in parts:
            ext = [((x - px0) / sx, (py0 - y) / sy) for x, y in poly.exterior.coords]
            if len(ext) >= 3:
                draw.polygon(ext, fill=1)
            for ring in poly.interiors:
                inn = [((x - px0) / sx, (py0 - y) / sy) for x, y in ring.coords]
                if len(inn) >= 3:
                    draw.polygon(inn, fill=0)
    return np.array(img, dtype=np.uint8)


def main():
    args = parse_args()
    rng = np.random.default_rng(args.seed)

    split = pd.read_csv(SPLIT)
    by_corner = {(int(r.left), int(r.bottom)): r for r in split.itertuples()}
    log(f"split: {len(split)} cells")

    man = gpd.read_file(MANUAL).to_crs(27700)
    man["geometry"] = man.geometry.buffer(0)
    dissolved = man.geometry.union_all()
    vector_km2 = dissolved.area / 1e6
    parts = gpd.GeoSeries(
        list(dissolved.geoms) if dissolved.geom_type == "MultiPolygon" else [dissolved],
        crs=27700)
    sindex = parts.sindex
    log(f"reference: {len(parts)} dissolved parts, {vector_km2:.4f} km²")

    if os.path.isdir(PATCH_DIR):
        shutil.rmtree(PATCH_DIR)
    for s in ("train", "test"):
        for k in ("Images", "Masks"):
            os.makedirs(f"{PATCH_DIR}/{s}/{k}", exist_ok=True)

    tifs = sorted(glob.glob(TIF_GLOB, recursive=True))
    basenames = [os.path.basename(p) for p in tifs]
    if len(basenames) != len(set(basenames)):
        raise SystemExit("duplicate GeoTIFF basenames would make patch_index.csv ambiguous")
    if args.limit:
        tifs = tifs[:args.limit]
    log(f"tiles: {len(tifs)}\n")

    def patch_geometry(path):
        """Tie point, pixel size and tile extent, without decoding any pixels."""
        with tifffile.TiffFile(path) as tf:
            page = tf.pages[0]
            return (*geo_reference(page), page.imagelength, page.imagewidth)

    def mask_for(x0, y0, sx, sy, i, j, vh, vw):
        px0, py0 = x0 + j * sx, y0 - i * sy
        bbox = box(px0, py0 - PATCH * sy, px0 + PATCH * sx, py0)
        hits = list(sindex.query(bbox, predicate="intersects"))
        m = (rasterise([parts.iloc[k] for k in hits], px0, py0, sx, sy, PATCH)
             if len(hits) else np.zeros((PATCH, PATCH), np.uint8))
        m[vh:, :] = 0
        m[:, vw:] = 0
        return m, px0, py0

    # Pass 1 indexes every patch from geometry alone. Holding 6,400 image and mask arrays in
    # memory to decide the sampling afterwards would need several gigabytes, so nothing is
    # kept here; masks are cheap to rebuild once the keep set is known.
    log("pass 1: indexing patches from geometry ...")
    rows, raster_m2, covered, covered_cells = [], 0.0, [], []
    for n, path in enumerate(tifs, 1):
        x0, y0, sx, sy, h, w = patch_geometry(path)
        corner = (int(round(x0)), int(round(y0 - TILE_M)))
        if corner not in by_corner:
            log(f"  [skip] {os.path.basename(path)} at {corner} is outside the grid")
            continue
        rec = by_corner[corner]
        if rec.cell in covered_cells:
            raise SystemExit(f"more than one GeoTIFF maps to validation cell {rec.cell}")
        covered_cells.append(rec.cell)
        covered.append(box(x0, y0 - h * sy, x0 + w * sx, y0))
        for i in range(0, h, PATCH):
            for j in range(0, w, PATCH):
                vh, vw = min(PATCH, h - i), min(PATCH, w - j)
                mask, px0, py0 = mask_for(x0, y0, sx, sy, i, j, vh, vw)
                pk = int(mask.sum())
                raster_m2 += pk * sx * sy
                rows.append({"name": f"{rec.cell}_{i}_{j}.png", "cell": rec.cell,
                             "split": rec.split, "tif": os.path.basename(path),
                             "row_off": i, "col_off": j, "valid_h": vh, "valid_w": vw,
                             "parking_px": pk, "x0": round(px0, 2), "y0": round(py0, 2)})
        if n % 20 == 0 or n == len(tifs):
            log(f"  {n}/{len(tifs)} tiles, {len(rows)} patches")

    if not rows:
        raise SystemExit("no GeoTIFF matched any validation cell")
    if not args.limit and set(covered_cells) != set(split["cell"]):
        missing = sorted(set(split["cell"]) - set(covered_cells))
        raise SystemExit(f"full run did not cover every split cell; missing: {missing}")

    # Compare like with like before decoding or writing gigabytes of imagery.  The vector
    # reference is clipped to the tiles actually processed, so --limit remains valid.
    from shapely.ops import unary_union
    extent = unary_union(covered)
    expect_km2 = dissolved.intersection(extent).area / 1e6
    raster_km2 = raster_m2 / 1e6
    diff = (100 * (raster_km2 - expect_km2) / expect_km2
            if expect_km2 else (0.0 if raster_km2 == 0 else float("inf")))
    log("\nalignment check")
    log(f"  tiles processed         {len(covered)}  ({extent.area / 1e6:.0f} km²)")
    log(f"  vector reference here   {expect_km2:.4f} km²")
    log(f"  rasterised from patches {raster_km2:.4f} km²   ({diff:+.2f}%)")
    if abs(diff) >= 1.0:
        raise SystemExit("*** MISALIGNED — area tolerance exceeded; no patches were written ***")
    log("  OK — geotransform is consistent")

    idx = pd.DataFrame(rows)

    # negatives are thinned in training only; the test split keeps everything
    keep = np.ones(len(idx), bool)
    tr = idx["split"] == "train"
    pos, neg = tr & (idx["parking_px"] > 0), tr & (idx["parking_px"] == 0)
    n_keep = int(round(args.neg_ratio * pos.sum()))
    if neg.sum() > n_keep:
        drop = rng.choice(np.flatnonzero(neg), int(neg.sum()) - n_keep, replace=False)
        keep[drop] = False
    idx["kept"] = keep
    idx.to_csv(OUT_INDEX, index=False)
    log(f"wrote: {OUT_INDEX}")

    # Confirm that the same Pillow RGB decoder used at training time can read the
    # JPEG-compressed GeoTIFFs before committing to the full mask build.
    probe = np.array(Image.open(tifs[0]).convert("RGB"))
    if probe.ndim != 3 or probe.shape[2] != 3:
        raise SystemExit(f"Pillow did not decode an RGB tile: {probe.shape}")
    del probe
    log("JPEG-compressed TIFF read check: OK")

    # Pass 2 writes masks.  Image patches are normally cropped directly from the source
    # TIFF during training, avoiding many gigabytes of duplicate lossless PNGs.
    log("\npass 2: writing masks" + (" and image PNGs ..." if args.materialize_images else " ..."))
    kept = idx[idx["kept"]]
    for n, (tif_name, group) in enumerate(kept.groupby("tif"), 1):
        path = next(p for p in tifs if os.path.basename(p) == tif_name)
        x0, y0, sx, sy, h, w = patch_geometry(path)
        img = None
        if args.materialize_images:
            # The released pipeline decodes through Pillow and converts to RGB.
            img = np.array(Image.open(path).convert("RGB"))
            if img.shape != (h, w, 3):
                raise RuntimeError(f"unexpected decoded image shape {img.shape} for {path}")
        for r in group.itertuples():
            mask, _, _ = mask_for(x0, y0, sx, sy, r.row_off, r.col_off, r.valid_h, r.valid_w)
            Image.fromarray(mask).save(f"{PATCH_DIR}/{r.split}/Masks/{r.name}")
            if img is not None:
                tile = img[r.row_off:r.row_off + PATCH, r.col_off:r.col_off + PATCH, :]
                if tile.shape[0] < PATCH or tile.shape[1] < PATCH:
                    padded = np.zeros((PATCH, PATCH, tile.shape[2]), dtype=tile.dtype)
                    padded[:tile.shape[0], :tile.shape[1], :] = tile
                    tile = padded
                Image.fromarray(tile).save(f"{PATCH_DIR}/{r.split}/Images/{r.name}")
        del img
        if n % 20 == 0 or n == kept["tif"].nunique():
            log(f"  {n}/{kept['tif'].nunique()} tiles written")

    log("\npatches written")
    w = idx[idx["kept"]]
    log(w.groupby("split").agg(patches=("name", "size"),
                               with_parking=("parking_px", lambda s: int((s > 0).sum())),
                               parking_km2=("parking_px", lambda s: s.sum() * .0625 / 1e6)
                               ).round(4).to_string())
    log(f"\ntotal patches generated {len(idx)}, written {int(keep.sum())}, "
        f"empty training patches dropped {int((~keep).sum())}")


if __name__ == "__main__":
    main()
