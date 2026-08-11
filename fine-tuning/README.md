# Fine-tuning experiment — bounded side study

Does local supervision fix the error classes the zero-shot evaluation identified?

**This is not an attempt to deliver a better model.** The dissertation's object of study is
zero-shot transfer. This experiment exists to answer one question that the main analysis
raises but cannot settle on its own, and to answer it cheaply enough that a null result is
still worth reporting.

---

## The question

The zero-shot error decomposes into three things (Chapter 4):

| Error class | Share | Would local supervision fix it? |
|---|---|---|
| Boundary imprecision | FP 28.8% dilation, FN 54.1% erosion | **Predicted no** — limited by imagery resolution and annotation precision, not by what the model knows |
| Definitional disagreement | 34.9% of unexplained FP (on-street, private driveways) | **Predicted yes** — the model would learn the local annotation rules |
| Small and irregular lots | <200 m² missed 19.1% of the time; `irregular_layout` 23.3% of sampled misses | **Predicted partly** — more local examples of the failing form |

So the experiment is not "does IoU go up" (it will, somewhat, and that is uninteresting).
It is **which of these three moves**. A negative result on boundary imprecision is a
positive finding: it would confirm that this component is a resolution limit rather than a
learnable bias, which is exactly what the dissertation claims.

---

## Two design rules that make or break this

**1. Split spatially, never by patch.** Adjacent 512 px patches share the same car parks.
A random patch-level split leaks the test set into training and produces a fake improvement.

Fortunately the geometry is clean: each Digimap GeoTIFF is exactly one OS 1 km square and
exactly one validation cell (verified — 100 tiles, 100 cells, identical extents). Patches
never cross a tile boundary, so **splitting by cell is sufficient and airtight**.

**2. Compare on the same held-out half.** The comparison is

> zero-shot model on the 50 held-out cells **vs** fine-tuned model on the same 50 cells

It is *not* a comparison against the 0.571 / 0.854 headline figures, which were computed on
all 100 cells with the full polygonisation and post-processing pipeline. Comparing a
fine-tuned half against a whole-area baseline is the standard way this experiment goes
wrong.

For the same reason, metrics here are computed **pixel-wise on the held-out patches**, with
both models run through identical preprocessing. That deliberately skips polygonisation,
the 1,000 px² minimum and the OSM subtraction — all of which are separate factors already
ablated in the main analysis. The numbers are therefore internally comparable to each other
but **not** directly comparable to the headline figures in Chapter 4, and must be reported
as such.

---

## Abort rule

**Stop at 12:00 on 13 August regardless of where this has got to.**

If there is no comparable pair of numbers by then, write it up as future work in one
paragraph and go back to the results chapter. Six thousand words and four figures are still
outstanding, and those carry the marks. A half-finished experiment contributes nothing and
the two days it costs come directly out of the chapters that do.

---

## Run order

| Step | Script | Where | Time |
|---|---|---|---|
| 1 | `make_split.py` | local | seconds |
| 2 | `make_patches.py` | local | ~10 min |
| 3 | `finetune.py` | Colab GPU | 1–2 h |
| 4 | `evaluate.py` | Colab GPU | ~10 min |

Steps 1–2 need only what is already in the `casa` environment (geopandas, tifffile, Pillow).
Steps 3–4 need `torch` and `transformers`, which are not installed locally — the machine has
no usable GPU, so they run on Colab exactly as the original inference did
(`main.ipynb` already mounts Drive and uses CUDA).

**The released checkpoint is not in the repository.** `Parking/model/best_model.ckpt` is a
1 GB Git LFS pointer, not the weights. Download the real checkpoint directly into this
folder on Colab; the loader rejects LFS pointers and partial/incompatible state dicts rather
than silently evaluating a partly initialised Cityscapes model.

Both models use the original notebook's exact preprocessing contract:
`SegformerFeatureExtractor.from_pretrained("nvidia/segformer-b5-finetuned-cityscapes-1024-1024")`,
`do_reduce_labels = False`, and `size = 512`. The released Lightning `model.*` keys are
stripped once and then required to match every Hugging Face model tensor exactly.

---

## Inputs (all read-only)

| Path | Use |
|---|---|
| `manual/leeds_grid.gpkg` | the 100 validation cells |
| `manual/leeds_manual.gpkg` | 2,037 labelled polygons → training masks |
| `Parking/parking-lot-mapping-tool/files/tif/**/*.tif` | 100 aerial tiles, 4000 × 4000 px, 0.25 m, EPSG:27700 |
| `Parking/model/best_model.ckpt` | released zero-shot weights (LFS — fetch first) |

Nothing outside this folder is written to.

---

## Outputs

```
split.csv              cell -> train / test, with distance band and labelled area
split.png              map of the split, for the methods chapter if the experiment is kept
patch_index.csv        every patch: cell, offsets, valid extent, parking pixel count, split
patches/train/Masks/*.png
patches/test/Masks/*.png
finetuned.ckpt         written by step 3
fit_val_split.csv      the cell-level fit / validation allocation used for epoch selection
finetune_log.csv       zero-shot validation and every fine-tuned epoch
evaluation.csv         written by step 4 — the comparison table
boundary_bands.csv     FP/FN distance decomposition at 2, 5 and 10 m
```

Image patches are not materialised by default. Lossless PNG copies of all 6,400 patches
would consume many gigabytes while duplicating imagery already present in the GeoTIFFs.
Training and evaluation instead decode each source TIFF through Pillow, crop the same 512 px
windows and apply the same right/bottom zero padding as `functions.split_images`. Training
batches are grouped by source tile so each data-loader worker reuses its decoded image.
Pass `make_patches.py --materialize-images` only when storage is plentiful; downstream
results are identical because existing image PNGs are preferred automatically.

## Exact commands

Local data preparation (from `Parking/`):

```bash
/opt/anaconda3/envs/casa/bin/python fine-tuning/make_split.py
/opt/anaconda3/envs/casa/bin/python fine-tuning/make_patches.py
/opt/anaconda3/envs/casa/bin/python fine-tuning/check_alignment.py
```

On Colab, mount or copy the complete `Parking/` project so the source TIFF tree remains at
`parking-lot-mapping-tool/files/tif`. Also transfer the generated `patch_index.csv` and
`patches/*/Masks` directories: they are deliberately git-ignored because they are derived
data. Then:

```bash
cd /content/drive/MyDrive/Parking/fine-tuning
pip install -r requirements-colab.txt
python -c "from huggingface_hub import hf_hub_download; hf_hub_download(repo_id='UTEL-UIUC/SegFormer-large-parking', filename='best_model.ckpt', local_dir='.')"
python finetune.py --ckpt best_model.ckpt
python evaluate.py --zero-shot best_model.ckpt --finetuned finetuned.ckpt
```

`finetune.py` enables CUDA mixed precision by default and refuses CPU training. It selects
the best genuinely fine-tuned epoch on a cell-level validation subset. Even if every trained
epoch is worse than zero-shot, the least-bad one is saved so the held-out comparison can
still report the negative result rather than ending without a comparable pair.

Padding is excluded from training loss, validation IoU and held-out metrics. Boundary terms
are computed only after all 64 patches have been rebuilt into their complete 4,000 × 4,000
cell: FP dilation is FP within *d* of the reference, while FN erosion is FN within *d* of a
prediction. This matches Chapter 3 and avoids both patch-seam artefacts and the earlier
factual error of defining FN erosion against the reference itself.

---

## Reporting, whatever the outcome

One short subsection in Chapter 4 and one paragraph in the discussion. The framing is the
same either way:

- **If the definitional error falls and the boundary error does not** — the predicted
  outcome. It confirms the decomposition and sharpens the future-work claim: a UK user
  should expect local labelling to buy back the scope disagreement, not the geometry.
- **If nothing moves** — worth reporting. It would mean 50 cells of single-annotator labels
  are not enough to shift a model of this size, which is itself useful for anyone
  considering the same route.
- **If everything improves** — the decomposition needs revisiting, and that is a finding
  too.

State the sample size, the single hyperparameter setting, and the absence of any tuning.
This is one run, not a study of fine-tuning.
