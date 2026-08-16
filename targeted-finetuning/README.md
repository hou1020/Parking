# Targeted fine-tuning — closing the loop between the typology and the intervention

**Relationship to `fine-tuning/`:** strictly additive. Nothing in that folder is modified.
`modeling.py` and `patch_data.py` are imported from it read-only so the preprocessing contract
cannot drift between experiments.

| | |
|---|---|
| **Run 1** | complete. Results in `Parking_targeted_run/`, copied locally under `Parking_targeted_run/`. Mistuned — see §3. |
| **Run 2** | ready to run. Rebalanced and resumable. Writes to `Parking_targeted_run2/`; run 1's folder is never written to. |

---

## 1. Why this exists

The first fine-tuning experiment fed the model every Leeds label and let it work things out. It
raised held-out IoU from 0.485 to 0.614, but bought 0.247 of precision with 0.127 of recall.
Standalone false positives fell 74.5%, which *looked* like the model learning the narrower
Leeds definition — on-street parking and private driveways that the annotation rules exclude.

That reading is confounded: **the model contracted everywhere**, and a map that predicts less
shows a fall in standalone FP for a trivial reason. This experiment makes the supervision
category-aware and then measures whether the removal is selective.

## 2. Design

### Arms, all on the same 50 held-out cells

| Arm | Model |
|---|---|
| A | zero-shot — released `best_model.ckpt` |
| B | generic fine-tune — the first experiment's checkpoint (skipped if absent) |
| C | targeted, **best validation IoU** — same selection rule as the generic run, so C vs B isolates the loss weighting |
| D | targeted, **best validation recall** within `IOU_TOL` of the best IoU — measures what the selection rule costs, model held fixed |

### What makes C and D "targeted"

Supervision is built from the zero-shot model's **own errors on the training half**, attributed
to the same reference layers used in §4.2 of the dissertation:

1. Run the released model over the 50 training cells.
2. `FP = pred ∧ ¬ref`, `FN = ¬pred ∧ ref`; split FP at 5 m into dilation and standalone.
3. Attribute the standalone FP by peeling order — building, OSM parking, sports, road buffer,
   curtilage, brownfield, industrial — most specific evidence first, as `fp_analysis.py` does.
4. Emit a per-pixel code raster, and train with weighted cross-entropy.

| Code | Meaning | Weight |
|---|---|---|
| 0 | ordinary pixel, **including boundary/dilation FP** | 1.0 |
| 1 | standalone FP no layer explains | 1.0 |
| 2 | false negative (missed parking) | **computed — see §3** |
| 3 | standalone FP on a precise layer — road, curtilage, OSM parking, sports | 5.0 |
| 4 | standalone FP on a broad land-use layer — brownfield, industrial | 2.0 |

**Boundary FP is deliberately left at weight 1.** Upweighting false positives within 5 m of a
real car park is precisely how a model is taught to draw everything smaller. Run 1 confirmed the
guard works: boundary FP and FN erosion were both unchanged between the generic and targeted
models, at every threshold.

**Broad land-use layers get a lower weight than precise ones.** §4.4 showed that subtracting
industrial land outright collapses recall from 0.854 to 0.279, because supermarket and
retail-park car parks sit on exactly that land. Weight is applied only where the reference says
background, so a real retail car park is a true positive and never touched — but the tiering
mirrors `fp_analysis.py`'s own specificity ordering rather than pretending a land-use blanket is
as good evidence as a road buffer.

### Controls

* Optimiser (Adam), LR (2e-5), batch size (2), seed (42), mixed precision, the cell-level 40/10
  fit/validation split and the epoch-selection rule for arm C are **identical to the generic
  run**. The loss weighting is the only difference between B and C.
* The loss is normalised by the **sum of weights**, not the pixel count. Dividing by count would
  make the weighted loss numerically larger and effectively raise the learning rate,
  confounding the comparison with the thing being tested. With all weights at 1.0 the function
  reduces exactly to the generic run's loss.
* Weight maps are derived from **training-half cells only**. The held-out 50 are never read
  until evaluation.

### Sanity check

Arm A must reproduce the first experiment's held-out zero-shot row — micro P 0.5190, R 0.8819,
IoU 0.4853. The notebook checks this and prints a loud warning if it does not. Run 1 reproduced
it exactly.

## 3. What run 1 found, and what run 2 changes

Run 1 established two things that hold:

* **The targeting reaches its categories.** Selectivity gap +9.7 (generic) → +16.1 (targeted),
  with the increment concentrated in the targeted layers (+7.7 points on average) rather than
  the others (+1.3).
* **The boundary guard works.** FP dilation 0.1302 → 0.1259 km²; FN erosion at 2 m actually
  *improved*, 0.1055 → 0.0926. The extra suppression did not come from shrinking edges.

But its headline was worse than the generic model's (IoU 0.5795 vs 0.6136, recall 0.6935 vs
0.7548), and the log showed this was **configuration, not a property of the task**:

**Fault 1 — the counterweight was ~4× too weak.** Hard-negative pixels carried 4.04% of the
gradient mass; the false-negative counterweight only 0.93%. A 4.33 : 1 tilt toward predicting
less, which guarantees a contracting model. `W_FN` was guessed at 3.0.

*Fix:* `W_FN` is now **computed** so that false-negative gradient mass equals the total
upweighted false-positive mass. It is also computed over the **fit patches** rather than whole
cells — sampling kept every positive patch but only an equal number of empty ones, so parking,
and therefore FN, is much denser in what the loss actually sees. Run 1 balanced against the
wrong denominator as well as with the wrong target.

**Fault 2 — wrong epoch budget, and IoU picked the wrong checkpoint.** Validation recall was
still climbing at epoch 6 (0.532 → 0.710 → 0.731 → 0.758 → 0.794), and epoch 5 held 0.063 more
recall than the selected epoch 3 for 0.0018 less IoU. Only the best-IoU checkpoint was saved, so
epoch 5's weights were lost.

*Fix:* 12 epochs; every candidate checkpoint kept; both the best-IoU and the best-recall-within-
tolerance epochs evaluated as separate arms.

One signal that is **not** explained by either fault: run 1's best validation IoU (0.6300) never
reached the generic run's best (0.6543). The weighting did not improve overall segmentation
quality at any epoch. IoU is the metric most hostile to a precision/recall rebalance, so this is
weak evidence — but it should not be forgotten if run 2 repeats it.

## 4. New layer: `curtilage`

The sampled typology attributed 20.2% of the unexplained FP residual to private driveways, but
that came from manual chip inspection — no layer in the pipeline represents it. Here it is
approximated as OSM building footprints buffered outward 8 m with the footprints removed.

This is a **proxy**, and §4.2's standing caveat applies to it more than to any other layer:
attribution is by location, not by inspection. FP falling in the curtilage band is "FP
immediately adjacent to a building", which is not the same as a confirmed residential forecourt.
Report it as such.

## 5. Running it

Upload `run_targeted_colab.ipynb` to Colab, choose a GPU runtime, run all cells. The notebook is
self-contained: it clones the repository for data, so nothing needs to be pushed first.

### Caching — what a disconnect costs

| Stage | Cached to | Cost if the runtime is recycled |
|---|---|---|
| clone + 100 LFS TIFFs | not cacheable | 10–20 min |
| prepared patches | `RUN/prepared_data/` | ~1 min copy |
| category rasters | `RUN/cache/category_layers.npz` | seconds |
| weight codes | `RUN/weight_codes.zip` | ~30 s unzip |
| training | `last.ckpt` + `epochs/` + `targeted_log.csv`, **written every epoch** | resumes at the next epoch |
| each evaluation arm | `eval_cache/*.json` | only the unfinished arm |

After a drop the only unavoidable cost is the LFS pull. Everything else resumes, and reusable
caches are searched across `Parking_targeted_run2`, `Parking_targeted_run` and
`Parking_finetuning_run`, so run 1's work is reused without being overwritten.

Resumed training restores the optimiser, the gradient scaler **and the batch sampler's epoch
counter**, so the data ordering matches what an uninterrupted run would have had. Candidate
checkpoints outside `IOU_TOL` of the running best are pruned as they fall out of contention,
keeping Drive usage near 2 GB rather than 4.

The category-raster build now streams one cell at a time straight into the compressed archive
(peak memory ~16 MB instead of 1.6 GB), and both it and the codes archive are written to a
`.partial` file and renamed on completion, so an interrupted write never leaves a corrupt cache.

Roughly 2–3 h end to end on a T4 for a cold run, faster on an A100; far less when caches hit.

### Outputs, all to `MyDrive/Parking_targeted_run2/`

| File | Contents |
|---|---|
| `weight_codes.csv` | composition of the five weight codes |
| `targeted_log.csv` | per-epoch loss, validation precision, recall, IoU |
| `epochs/epoch_NN.ckpt` | candidate checkpoints |
| `targeted.ckpt` | best-IoU weights |
| `evaluation_arms.csv` | micro and macro metrics for every arm |
| `boundary_bands_arms.csv` | dilation/standalone FP and erosion/standalone FN at 2, 5, 10 m |
| `standalone_fp_by_category.csv` | the attribution, per arm |
| `selectivity.csv` | targeted vs other removal rates and the gap |
| `table1_overall.csv`, `table2_category_removal.csv` | the two tables for the write-up |

### If an import fails with a numpy or scipy `AttributeError`

`module 'numpy._core._multiarray_umath' has no attribute '_blas_supports_fpe'` means pip
replaced numpy's files on disk after the process had already loaded the old C extension — the
new `.py` files and the old `.so` disagree. **Restart the runtime and run all cells again.** If a
plain session restart does not clear it, the on-disk install is genuinely inconsistent: run
`pip install -q --force-reinstall --no-cache-dir numpy scipy`, restart, and run all again.

Section 2 avoids causing it: nothing is installed with `--upgrade`, only missing or wrongly
pinned packages are touched, `import torch` is held back until after the install, and the cell
restarts the runtime itself if a dependency forced numpy or scipy to change.

## 6. How to read the result — decided in advance

1. **Arm A must reproduce 0.5190 / 0.8819 / 0.4853.** If not, stop; nothing else is comparable.
2. **Check the gradient-mass print in section 8.** Suppression and recovery mass should now be
   near 1 : 1, against run 1's 4.33 : 1. If they are not, the rest is uninterpretable in the
   same way run 1 was.
3. **Recall, arm C vs arm B.** Run 1 gave 0.6935 against 0.7548. If the rebalance worked, C
   should reach or beat B while keeping the higher precision.
4. **Selectivity gap.** Run 1: B +9.7, C +16.1. The real question is whether the gap survives
   once the model is no longer contracting — a gap that appears *only* under contraction is not
   evidence about categories.
5. **Arm D versus arm C.** How much recall the IoU selection rule costs with the model fixed.
   This is a direct, cheap answer to a question the write-up currently raises and cannot settle.
6. **Whole-lot share of FN.** Run 1's targeted arm put 68% of false-negative area in whole-lot
   misses against the generic model's 58%. If the rebalance works this should fall back.

### Three outcomes, three sentences for §4.8

* **Gap survives, recall restored.** The typology did more than describe the error — it improved
  the intervention. Local supervision corrects definitional disagreement *specifically*, and the
  decomposition is what made that possible.
* **Gap collapses once contraction stops.** The selectivity in run 1 was an artefact of a
  shrinking map. That is a negative result worth reporting: it converts the write-up's hedge
  ("consistent with, but does not prove") into a measurement.
* **Gap survives but recall still falls.** Targeting reaches the right pixels and the model still
  shrinks even when the counterweight is balanced. That is evidence the categories are not
  separable from legitimate parking by anything in the imagery — which would make the
  definitional component a scope-definition problem rather than a model problem.

## 7. Limitations, in advance

* Still one seed and one weight tiering per run. Run 2 adds a second configuration, not a search.
* The tiers (5.0 / 2.0 / 1.0, with `W_FN` solved) are a judgement about *relative* evidence
  strength, not a tuned optimum.
* `curtilage` and `industrial` are positional proxies, not confirmed object classes.
* Evaluation is pixel-wise on raw output, with no polygonisation, no 1,000 px² minimum and no
  OSM subtraction — comparable to the fine-tuning experiments and to nothing else in the
  dissertation.
* The human-adjudicated sample (31 `fp_other` chips in the held-out half, of which 11 are the
  definitional classes) is **not** used anywhere here. Adding it to the evaluation would give
  inspection-based rather than positional evidence, and is the obvious next step.
