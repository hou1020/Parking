"""
Visual check that masks land on the pixels they should — Leeds fine-tuning experiment
Author: Hou

make_patches.py compares rasterised area against vector area, which catches a wrong pixel
size or a displaced tie point. It does not catch a flipped or transposed mask: mirroring an
image preserves its area exactly, so a mask drawn upside down passes the numeric check and
then quietly trains the model against nonsense.

This renders the patches holding the most parking with their mask outlined on top. If the
outlines sit on the car parks, the geotransform is right in every respect that matters. If
they sit on roofs or fields, stop.

Reads read-only. Writes only into this folder.
Output:
  - alignment_check.png
"""
import os, glob
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
import warnings; warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
INDEX = f"{HERE}/patch_index.csv"
PATCH_DIR = f"{HERE}/patches"
TIF_ROOT = f"{os.path.dirname(HERE)}/parking-lot-mapping-tool/files/tif"
OUT = f"{HERE}/alignment_check.png"
N = 6


def log(m):
    print(m, flush=True)


idx = pd.read_csv(INDEX)
avail = []
for r in idx[idx["kept"] & (idx["parking_px"] > 0)].itertuples():
    p = f"{PATCH_DIR}/{r.split}/Masks/{r.name}"
    if os.path.exists(p):
        avail.append(r)
if not avail:
    raise SystemExit("no written patches with parking found — run make_patches.py first")

avail.sort(key=lambda r: -r.parking_px)
pick, used_cells = [], set()
for r in avail:
    if r.cell not in used_cells:
        pick.append(r); used_cells.add(r.cell)
    if len(pick) == N:
        break
log(f"showing high-parking patches from {len(pick)} distinct cells")

tif_paths = glob.glob(f"{TIF_ROOT}/**/*.tif", recursive=True)
tif_by_name = {os.path.basename(p): p for p in tif_paths}
cache_name = cache_image = None

cols = 3
rows = int(np.ceil(len(pick) / cols))
fig, axes = plt.subplots(rows, cols, figsize=(4.1 * cols, 4.3 * rows))
for ax, r in zip(np.atleast_1d(axes).ravel(), pick):
    image_path = f"{PATCH_DIR}/{r.split}/Images/{r.name}"
    if os.path.exists(image_path):
        img = np.array(Image.open(image_path).convert("RGB"))
    else:
        if r.tif not in tif_by_name:
            raise FileNotFoundError(f"source TIFF not found: {r.tif}")
        if cache_name != r.tif:
            cache_image = np.array(Image.open(tif_by_name[r.tif]).convert("RGB"))
            cache_name = r.tif
        img = cache_image[r.row_off:r.row_off + 512, r.col_off:r.col_off + 512]
        if img.shape[:2] != (512, 512):
            padded = np.zeros((512, 512, 3), dtype=img.dtype)
            padded[:img.shape[0], :img.shape[1]] = img
            img = padded
    msk = np.array(Image.open(f"{PATCH_DIR}/{r.split}/Masks/{r.name}"))
    ax.imshow(img)
    ax.contour(msk, levels=[0.5], colors="#ffd400", linewidths=1.4)
    if r.valid_h < msk.shape[0]:
        ax.axhline(r.valid_h, color="#4878a8", lw=1, ls="--")
    if r.valid_w < msk.shape[1]:
        ax.axvline(r.valid_w, color="#4878a8", lw=1, ls="--")
    share = 100 * r.parking_px / (r.valid_h * r.valid_w)
    ax.set_title(f"{r.cell}  offset ({r.row_off}, {r.col_off})\n"
                 f"{share:.1f}% of valid area labelled", fontsize=8.5)
    ax.set_xticks([]); ax.set_yticks([])
for ax in np.atleast_1d(axes).ravel()[len(pick):]:
    ax.axis("off")

fig.suptitle("Mask outlines over imagery — outlines must sit on the car parks",
             fontsize=11)
fig.tight_layout()
fig.savefig(OUT, dpi=150, bbox_inches="tight", facecolor="white")
log(f"wrote: {OUT}")
