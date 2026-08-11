"""Patch datasets that preserve the original TIFF -> RGB -> 512 px input contract."""
import glob
import os

import numpy as np
from PIL import Image
from torch.utils.data import Dataset

from modeling import PATCH_SIZE


class SourcePatchDataset(Dataset):
    """Read masks from the experiment folder and image windows from source GeoTIFFs.

    Materialised patch PNGs are used when present.  Otherwise a worker caches its current
    decoded TIFF and crops the requested 512 px window.  This is pixel-equivalent to the
    original split_images function without duplicating many gigabytes of aerial imagery.
    """

    def __init__(self, rows, patch_root, tif_root, processor, ignore_padding=False,
                 return_index=False):
        self.rows = rows
        self.patch_root = patch_root
        self.processor = processor
        self.ignore_padding = ignore_padding
        self.return_index = return_index
        paths = glob.glob(os.path.join(tif_root, "**", "*.tif"), recursive=True)
        by_name = {}
        for path in paths:
            name = os.path.basename(path)
            if name in by_name:
                raise RuntimeError(f"duplicate TIFF basename under {tif_root}: {name}")
            by_name[name] = path
        needed = {r["tif"] for r in rows}
        missing = sorted(needed - set(by_name))
        if missing:
            raise FileNotFoundError(f"source TIFFs not found under {tif_root}: {missing[:5]}")
        self.tifs = by_name
        self._cache_name = None
        self._cache_image = None

    def __len__(self):
        return len(self.rows)

    def __getstate__(self):
        state = self.__dict__.copy()
        state["_cache_name"] = None
        state["_cache_image"] = None
        return state

    def _source_patch(self, r):
        name = r["tif"]
        if name != self._cache_name:
            with Image.open(self.tifs[name]) as source:
                self._cache_image = np.array(source.convert("RGB"))
            self._cache_name = name
        i, j = r["row_off"], r["col_off"]
        tile = self._cache_image[i:i + PATCH_SIZE, j:j + PATCH_SIZE]
        if tile.shape[:2] != (PATCH_SIZE, PATCH_SIZE):
            padded = np.zeros((PATCH_SIZE, PATCH_SIZE, 3), dtype=tile.dtype)
            padded[:tile.shape[0], :tile.shape[1]] = tile
            tile = padded
        return Image.fromarray(tile)

    def __getitem__(self, i):
        r = self.rows[i]
        image_path = os.path.join(self.patch_root, "Images", r["name"])
        if os.path.exists(image_path):
            with Image.open(image_path) as source:
                image = source.convert("RGB")
        else:
            image = self._source_patch(r)
        with Image.open(os.path.join(self.patch_root, "Masks", r["name"])) as source:
            mask = source.copy()
        encoded = self.processor(image, mask, return_tensors="pt")
        encoded = {k: v.squeeze(0) for k, v in encoded.items()}
        labels = encoded["labels"]
        if labels.shape[-2:] != (PATCH_SIZE, PATCH_SIZE):
            raise RuntimeError(
                f"processor returned label size {tuple(labels.shape[-2:])}, expected 512²"
            )
        if self.ignore_padding:
            labels[r["valid_h"]:, :] = 255
            labels[:, r["valid_w"]:] = 255
        return (encoded, i) if self.return_index else encoded


class TileBatchSampler:
    """Shuffle tiles and patches while keeping each batch within one source TIFF."""

    def __init__(self, rows, batch_size, seed=42, drop_last=True):
        self.batch_size = batch_size
        self.seed = seed
        self.drop_last = drop_last
        self.epoch = 0
        self.groups = {}
        for i, row in enumerate(rows):
            self.groups.setdefault(row["tif"], []).append(i)

    def __iter__(self):
        rng = np.random.default_rng(self.seed + self.epoch)
        self.epoch += 1
        names = list(self.groups)
        rng.shuffle(names)
        for name in names:
            indices = np.array(self.groups[name], dtype=int)
            rng.shuffle(indices)
            for start in range(0, len(indices), self.batch_size):
                batch = indices[start:start + self.batch_size].tolist()
                if len(batch) == self.batch_size or not self.drop_last:
                    yield batch

    def __len__(self):
        if self.drop_last:
            return sum(len(x) // self.batch_size for x in self.groups.values())
        return sum((len(x) + self.batch_size - 1) // self.batch_size
                   for x in self.groups.values())
