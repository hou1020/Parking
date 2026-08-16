# Targeted fine-tuning — closing the loop between the typology and the intervention

**Status:** designed and ready to run; not yet run.
**Relationship to `fine-tuning/`:** strictly additive. Nothing in that folder is modified.
`modeling.py` and `patch_data.py` are imported from it read-only so the preprocessing contract
cannot drift between the two experiments.

---

## 1. Why this exists

The first experiment fed the model every Leeds label and let it work things out. It raised
held-out IoU from 0.485 to 0.614, but bought 0.247 of precision with 0.127 of recall, and
false-negative area more than doubled. Standalone false positives fell 74.5%, which *looked*
like the model learning the narrower Leeds definition — on-street parking and private
driveways that the annotation rules exclude.

That reading is confounded. **The model contracted everywhere.** A map that simply predicts
less will show a fall in standalone FP for a trivial reason, so the 74.5% cannot on its own be
attributed to any particular confusion class.

There is one piece of evidence against pure contraction, and it is worth stating because it
motivates the design here: true positives fell only 14.4% while false positives fell 71.9%.
Uniform shrinkage would not produce that asymmetry, so the fine-tuned model's probability field
*is* better ordered. But better ordered *with respect to what* remains unknown.

This experiment answers that by making the supervision category-aware and then measuring
whether the removal is selective.

## 2. Design

### Three arms, one held-out set

| Arm | Model | Source |
|---|---|---|
| A | zero-shot | released `best_model.ckpt` |
| B | generic fine-tune | the first experiment's epoch-3 checkpoint (optional) |
| C | **targeted fine-tune** | this notebook |

All three are scored on the same 50 held-out cells, same preprocessing, raw pixel output.
Arm B runs only if the first experiment's `finetuned.ckpt` is in Drive; the notebook says so
and continues with A and C otherwise.

### What makes arm C "targeted"

The supervision is built from the zero-shot model's **own errors on the training half**,
attributed to the same reference layers used in §4.2 of the dissertation:

1. Run the released model over the 50 training cells.
2. `FP = pred ∧ ¬ref`, `FN = ¬pred ∧ ref`; split FP at 5 m into dilation and standalone.
3. Attribute the standalone FP by peeling order — building, OSM parking, sports, road buffer,
   curtilage, brownfield, industrial — most specific evidence first, exactly as
   `analysis/fp_analysis.py` does.
4. Emit a per-pixel code raster, and train with weighted cross-entropy.

| Code | Meaning | Weight |
|---|---|---:|
| 0 | ordinary pixel, **including boundary/dilation FP** | 1.0 |
| 1 | standalone FP no layer explains | 1.0 |
| 2 | false negative (missed parking) | 3.0 |
| 3 | standalone FP on a precise layer — road, curtilage, OSM parking, sports | 5.0 |
| 4 | standalone FP on a broad land-use layer — brownfield, industrial | 2.0 |

Three of those choices carry the design:

**Boundary FP is deliberately left at weight 1.** Upweighting false positives that lie within
5 m of a real car park is precisely how a model is taught to draw everything smaller — the
failure mode of the generic run. Only *standalone* FP becomes a hard negative.

**False negatives are upweighted.** The generic run lost 0.127 of recall. Weighting missed
parking pushes the other way, so recall loss and FP removal can be separated rather than
observed as one lump.

**Broad land-use layers get a lower weight than precise ones.** §4.4 showed that subtracting
industrial land outright collapses recall from 0.854 to 0.279, because supermarket and
retail-park car parks sit on exactly that land. The risk is much smaller here — weight is
applied only where the reference says background, so a real retail car park is a true positive
and never touched — but the tiering mirrors `fp_analysis.py`'s own specificity ordering rather
than pretending a land-use blanket is as good evidence as a road buffer.

### Controls

* Optimiser (Adam), LR (2e-5), batch size (2), epochs (6), seed (42), mixed precision, the
  cell-level 40/10 fit/validation split and the best-epoch-on-validation-IoU rule are **all
  identical to the generic run**. The loss weighting is the only difference.
* The loss is normalised by the **sum of weights**, not the pixel count. Dividing by count
  would make the weighted loss numerically larger and effectively raise the learning rate,
  confounding the comparison with the thing being tested.
* Weight maps are derived from **training-half cells only**. The held-out 50 are never read
  until evaluation.
* Epoch selection still uses parking-class IoU, even though IoU selection is part of what
  pulled the generic run conservative. Changing it would break comparability; the notebook
  logs per-epoch precision and recall as well, so the effect of the criterion stays visible.

### The measurement

For each arm: micro/macro precision, recall, IoU; FP split into dilation and standalone at
2/5/10 m; FN split against the *prediction*; and standalone FP attributed to the seven
categories. From those, the derived quantity that answers the question:

> **removal rate by category** = (FP_zero-shot − FP_arm) / FP_zero-shot

If removal is uniform, every category shows the same rate. If targeting worked, the four
precise categories show a higher rate than the rest, and recall holds up better than arm B's.

### Built-in sanity check

Arm A must reproduce the first experiment's held-out zero-shot row — micro P 0.5190,
R 0.8819, IoU 0.4853. The notebook checks this and prints a loud warning if it does not. If
arm A has drifted, nothing downstream is comparable and the run should be discarded.

## 3. New layer: `curtilage`

The sampled typology attributed 20.2% of the unexplained FP residual to private driveways,
but that came from manual chip inspection — no layer in the pipeline represents it. Here it is
approximated as OSM building footprints buffered outward 8 m with the footprints removed.

This is a **proxy**, and §4.2's standing caveat applies to it more than to any other layer:
attribution is by location, not by inspection. FP falling in the curtilage band is "FP
immediately adjacent to a building", which is not the same as a confirmed residential
forecourt. Report it as such.

## 4. Running it

Upload `run_targeted_colab.ipynb` to Colab, choose a GPU runtime, run all cells. The notebook
is self-contained: it clones the repository for data, so nothing needs to be pushed first.

Roughly 1.5–2.5 h end to end on a T4, faster on an A100:

| Stage | Approx. |
|---|---|
| clone + LFS pull of 100 TIFFs | 10–20 min |
| category rasters (100 cells, cached to Drive after the first run) | 5–10 min |
| zero-shot inference on 2,256 training patches + code rasters | 10–15 min |
| training, 6 epochs × 909 steps | 40–70 min |
| evaluation, 3 arms × 3,200 patches with distance transforms | 20–40 min |

Resumable: category rasters, weight codes and the checkpoint are each cached, with a
`FORCE_*` flag to redo any stage.

### Outputs, all to `MyDrive/Parking_targeted_run/`

| File | Contents |
|---|---|
| `weight_codes.csv` | composition of the five weight codes over the training half |
| `targeted_log.csv` | per-epoch loss, validation precision, recall, IoU |
| `targeted.ckpt` | best-epoch weights |
| `evaluation_3arm.csv` | micro and macro metrics for every arm |
| `boundary_bands_3arm.csv` | dilation/standalone FP and erosion/standalone FN at 2, 5, 10 m |
| `standalone_fp_by_category.csv` | the attribution, per arm |
| `table1_overall.csv`, `table2_category_removal.csv` | the two tables for the write-up |

## 5. How to read the result — decided in advance

Stating the readings before the run is what stops the outcome being narrated after the fact.

**(1) Selectivity gap large and positive, recall held.** Targeting reached the categories the
typology named. §4.8 can then say local supervision corrects definitional disagreement
*specifically*, and that the decomposition is what made the better intervention possible. This
is the strongest outcome and the one that puts the typology at the centre of the future-work
argument.

**(2) Gap near zero in both arms.** Both models simply contracted; the definitional reading of
the generic run's 74.5% is unsupported. This is a **negative result that is still worth
reporting** — it converts the write-up's current hedge ("consistent with, but does not prove")
into a measurement, which is stronger than a caveat.

**(3) Gap positive but recall still falls.** Targeting reaches the right pixels and the model
still shrinks. That points at the decision rule rather than the training signal, and makes the
argmax-versus-tuned-threshold comparison the obvious next step.

None of the three requires any headline figure in Chapters 4–6 to change. Arm A is the same
released model on the same held-out cells.

## 6. Limitations, in advance

* One run, one seed, one weight setting. Same as the first experiment — this does not fix
  that, it adds a second point.
* The weight tiers (5.0 / 3.0 / 2.0) are a judgement, not a search. A different tiering would
  give a different operating point.
* `curtilage` and `industrial` are positional proxies, not confirmed object classes.
* Evaluation is pixel-wise on raw output, with no polygonisation, no 1,000 px² minimum and no
  OSM subtraction — so these numbers are comparable to the first experiment's and to nothing
  else in the dissertation.
* Epoch selection on IoU is retained for comparability, which means the conservative bias that
  criterion introduces is present in arm C too.
