# Local fine-tuning experiment: design, implementation, results and interpretation

## 1. Role of the experiment

The dissertation's main empirical object remains **zero-shot geographic transfer**: the
performance a UK user would obtain by applying the released US-trained parking model without
UK supervision. The local fine-tuning exercise is a bounded supplementary experiment. It
does not replace the zero-shot evaluation and its results must not be mixed with the headline
precision and recall reported for the full 100 km² post-processed map.

The experiment asks a narrower question raised by the error decomposition:

> Does a small amount of local supervision change the *composition* of transferred-model
> error, and in particular does it reduce locally inappropriate detections without resolving
> the geometric boundary problem?

Three expectations followed from the main analysis:

1. **Definitional disagreement should be learnable.** The zero-shot model detects some
   on-street parking, private residential forecourts and related paved areas excluded by the
   Leeds annotation rules. Local labels should teach a narrower target and reduce standalone
   false positives.
2. **Boundary imprecision may be less responsive.** Boundary error is partly constrained by
   0.25 m imagery, ambiguous pavement edges and annotation precision. Local labels might
   change the size of predictions without making their edges intrinsically more accurate.
3. **Small and irregular car parks might improve, but only partly.** Local examples expose
   forms that differ from the US training data, although the experiment does not include a
   separate object-level test capable of isolating this mechanism.

The relevant outcome is therefore not simply whether IoU rises. Precision, recall,
standalone error and boundary-associated error must be read together.

## 2. Experimental separation from the main analysis

The main analysis evaluates the released model over all 100 cells after mask cleaning,
polygonisation, removal of components below 1,000 px², and subtraction of OSM buildings and
roads. The fine-tuning comparison instead uses **raw pixel predictions** from both models on
the same held-out cells under identical preprocessing. It deliberately omits polygonisation,
minimum-area filtering and OSM subtraction.

Consequently:

- the fine-tuning zero-shot baseline is not expected to reproduce the dissertation's
  full-area headline metrics;
- only the zero-shot and fine-tuned rows within this experiment are directly comparable;
- improvement here describes the network output, not the complete operational mapping
  pipeline; and
- the main dissertation can still state that its primary model was used without UK
  fine-tuning, provided this experiment is explicitly presented as a supplementary analysis.

## 3. Spatial split and leakage control

The imagery consists of 100 GeoTIFFs, each exactly 4,000 × 4,000 pixels at 0.25 m resolution.
Each GeoTIFF covers one OS 1 km grid square and matches one validation cell. Each tile is cut
into an 8 × 8 grid of 512 px patches; the last patch in each direction contains 416 real
pixels and 96 pixels of right or bottom padding.

A random patch split would be invalid because neighbouring patches can contain different
parts of the same car park and are strongly spatially correlated. The split was therefore
made at the 1 km cell/tile level:

| Split | Cells | Vector-labelled area | Mean distance from centre |
|---|---:|---:|---:|
| Training half | 50 | 1.6500 km² | 4.020 km |
| Held-out test half | 50 | 1.6097 km² | 4.030 km |

Cells were stratified by distance band and assigned using constrained greedy balancing on
labelled area. Each half received approximately half the cells in every distance band, while
the labelled-area difference was held to 2.5%. This matters because both distance from the
centre and parking abundance are associated with measured accuracy. An unbalanced split
could otherwise make apparent fine-tuning gains a property of the test geography.

The 50-cell training half was divided again, by cell rather than by patch, into 40 fitting
cells and 10 validation cells. The final held-out 50 cells were never used for gradient
updates or epoch selection. The design guarantees disjoint image pixels and no overlapping
patches between the partitions. As with any split into adjacent spatial cells, it does not
eliminate all wider neighbourhood autocorrelation or the possibility that a feature crosses
a cell boundary; the claim is therefore spatial separation, not complete statistical
independence.

## 4. Mask construction and alignment

The 2,037 manually labelled parking polygons were repaired, dissolved and rasterised directly
onto the grid defined by each GeoTIFF's tie point and pixel scale. Masks are single-channel
512 × 512 PNGs with the exact categorical encoding:

- `0`: background;
- `1`: parking; and
- `255`: introduced only inside the training loader to mark synthetic padding as ignored.

The patch loop reproduces the original inference function:

```python
for row in range(0, height, 512):
    for col in range(0, width, 512):
        patch = image[row:row + 512, col:col + 512]
```

Short edge patches are padded with zeros to 512 × 512. Their real extents are recorded as
`valid_h` and `valid_w`. Padding is set to label 255 during training, so it contributes
neither loss nor validation metrics; it is cropped out of held-out evaluation.

Alignment was checked in two complementary ways:

1. **Area check.** Across the full 100-cell extent, the vector reference clipped to the
   imagery covers 3.2597 km², while the raster masks contain 3.2884 km² of parking pixels, a
   difference of +0.88%. The small positive difference is consistent with polygon filling
   including boundary pixels. A tolerance of 1% was imposed before masks could be written.
2. **Visual check.** Mask contours were rendered over high-parking patches from six distinct
   cells. The outlines follow the visible parking surfaces, ruling out mirror, transpose and
   axis-direction errors that an area-only check could not detect.

All 5,456 written masks were subsequently checked to be 512 × 512 with values restricted to
`{0, 1}`, and all padded regions were confirmed to be zero before the loader applies the
ignore label.

## 5. Patch sampling and storage

Every one of the 3,200 held-out test patches was retained, including empty patches. Removing
empty test patches would artificially raise precision by excluding exactly those locations
where a model can generate unsupported parking detections.

Parking occupies a minority of the training imagery, so empty fitting patches were sampled
at a 1:1 ratio with positive patches. Across the 50-cell training half this produced 2,256
patches: 1,128 containing parking and 1,128 empty. After the cell-level validation split,
1,818 patches were used for fitting and 438 for validation.

Lossless copies of all image patches were not stored. The local machine lacked sufficient
free space, and the images already existed in the GeoTIFFs. Instead, the dataset decodes the
source TIFF through Pillow, converts it to RGB and crops the required 512 px window at load
time. Training batches are grouped by source tile so each worker can reuse a decoded 4,000 ×
4,000 image. This changes storage and I/O only; the pixel window and padding contract remain
the same as the original pipeline.

## 6. Model and preprocessing contract

Both models use the released SegFormer-B5 architecture based on
`nvidia/segformer-b5-finetuned-cityscapes-1024-1024`, with two output classes: background and
parking. Preprocessing reproduces the source notebook:

- input size 512 × 512;
- RGB input;
- `do_reduce_labels = False`; and
- the same Hugging Face image normalization inherited from the Cityscapes processor.

The released parking checkpoint is a PyTorch Lightning file whose network parameters appear
under `model.*`. Loading removes only that wrapper prefix and then requires every tensor name
and shape to match the SegFormer model exactly. Git LFS pointer files, undersized files,
missing tensors, unexpected tensors and shape mismatches cause an immediate failure rather
than leaving part of the Cityscapes model randomly initialised.

The runtime is pinned to `transformers==4.57.1`. Later Transformers versions renamed many
SegFormer modules (for example, `decode_head.linear_c` to
`decode_head.linear_projections`). The original Lightning checkpoint uses the earlier names,
so an unpinned current version produced 1,164 missing and 1,164 unexpected keys. Pinning the
compatible implementation preserves the released checkpoint's architecture instead of
manually guessing a large key-conversion map.

## 7. Fine-tuning procedure

All SegFormer parameters were fine-tuned on a Colab CUDA GPU using one fixed configuration:

| Setting | Value |
|---|---:|
| Optimiser | Adam |
| Learning rate | 2 × 10⁻⁵ |
| Batch size | 2 |
| Epochs attempted | 6 |
| Mixed precision | Enabled |
| Random seed | 42 |
| Model selection | Highest parking-class IoU on 10 validation cells |

The optimiser and learning rate match the released project's `SegformerFinetuner`. No
hyperparameter search or repeated seeds were performed. The test cells played no part in
choosing the checkpoint.

Training history was:

| Epoch | Training loss | Validation parking IoU |
|---:|---:|---:|
| 0 (zero-shot) | — | 0.5349 |
| 1 | 0.0627 | 0.6178 |
| 2 | 0.0428 | 0.6172 |
| **3** | **0.0344** | **0.6543** |
| 4 | 0.0286 | 0.6412 |
| 5 | 0.0230 | 0.6227 |
| 6 | 0.0197 | 0.6053 |

Epoch 3 was selected. Its validation IoU exceeds the zero-shot validation result by 0.1194.
The continued fall in training loss alongside declining validation IoU after epoch 3 is
clear overfitting, which confirms the need for cell-level validation and best-epoch
selection. The evaluated checkpoint is epoch 3, not the final epoch.

## 8. Held-out evaluation

Zero-shot and fine-tuned checkpoints were evaluated on the same 3,200 patches from the 50
held-out cells. Logits were bilinearly upsampled to 512 × 512 and reduced by argmax. Metrics
were accumulated in two forms:

- **micro:** all valid held-out pixels pooled, so cells contribute in proportion to their
  pixel-level confusion counts;
- **macro:** precision, recall and IoU computed per cell and then averaged, so sparse and
  parking-rich cells receive equal weight.

For the error decomposition, patch predictions were first rebuilt into complete 4,000 ×
4,000 cell rasters. This avoids treating patch seams as object boundaries. At 2, 5 and 10 m:

- FP dilation is false-positive area within distance *d* of the reference; and
- FN erosion is false-negative reference area within distance *d* of a prediction.

The second definition is important. FN erosion must be measured against the prediction, not
against the edge of the reference itself; otherwise the perimeter of a completely missed car
park would be misclassified as a boundary error.

## 9. Results

### 9.1 Overall held-out performance

| Aggregation | Model | Precision | Recall | IoU |
|---|---|---:|---:|---:|
| Micro | Zero-shot | 0.5190 | 0.8819 | 0.4853 |
| Micro | Fine-tuned | **0.7664** | 0.7548 | **0.6136** |
| Macro | Zero-shot | 0.4773 | 0.8777 | 0.4473 |
| Macro | Fine-tuned | **0.7553** | 0.7205 | **0.5834** |

Fine-tuning raises micro IoU by 0.1283 and macro IoU by 0.1361. However, the gain is not a
uniform improvement. Micro precision rises by 0.2474 while recall falls by 0.1271. The local
model is substantially more conservative.

### 9.2 Error areas and predicted extent

| Model | TP | FP | FN | Predicted area | Reference area |
|---|---:|---:|---:|---:|---:|
| Zero-shot | 1.4322 km² | 1.3274 km² | 0.1917 km² | 2.7596 km² | 1.6239 km² |
| Fine-tuned | 1.2257 km² | 0.3736 km² | 0.3982 km² | 1.5993 km² | 1.6239 km² |

Relative to zero-shot, fine-tuning:

- reduces FP by 0.9538 km², or 71.9%;
- increases FN by 0.2065 km², or 107.7%;
- reduces correctly detected area by 0.2065 km², or 14.4%; and
- changes total predicted area from 69.9% above the reference total to 1.5% below it.

The near match in total area after fine-tuning must not be mistaken for near-perfect spatial
mapping. The model still misallocates substantial area: 0.3736 km² is falsely added and
0.3982 km² is missed. Aggregate area balance can coexist with spatial disagreement.

### 9.3 Boundary sensitivity

| Model | Distance | FP dilation | FP dilation share | Standalone FP | FN erosion | FN erosion share | Standalone FN |
|---|---:|---:|---:|---:|---:|---:|---:|
| Zero-shot | 2 m | 0.2123 | 16.0% | 1.1151 | 0.0524 | 27.3% | 0.1393 |
| Zero-shot | 5 m | 0.3737 | 28.2% | 0.9537 | 0.0858 | 44.8% | 0.1059 |
| Zero-shot | 10 m | 0.4720 | 35.6% | 0.8554 | 0.1140 | 59.5% | 0.0777 |
| Fine-tuned | 2 m | 0.0845 | 22.6% | 0.2891 | 0.1055 | 26.5% | 0.2927 |
| Fine-tuned | 5 m | 0.1302 | 34.9% | 0.2434 | 0.1685 | 42.3% | 0.2297 |
| Fine-tuned | 10 m | 0.1613 | 43.2% | 0.2123 | 0.2173 | 54.6% | 0.1809 |

At the working 5 m threshold, standalone FP falls from 0.9537 to 0.2434 km², a reduction of
74.5%. FP dilation also falls in absolute terms, from 0.3737 to 0.1302 km², a reduction of
65.2%. Conversely, FN erosion rises from 0.0858 to 0.1685 km² and standalone FN rises from
0.1059 to 0.2297 km².

The percentage columns cannot be interpreted without the absolute areas. FP dilation rises
from 28.2% to 34.9% *as a share of FP* even though its area falls sharply, because standalone
FP falls faster. Similarly, a roughly stable FN erosion share does not mean stable boundary
FN when total FN more than doubles.

## 10. Interpretation

The experiment provides strong evidence that a small amount of local supervision can adapt
the transferred model's operating behaviour. The dominant effect is a large contraction of
predicted parking: unsupported detections are removed, precision rises sharply and predicted
total area becomes almost unbiased. This behaviour is consistent with the expectation that
local labels teach the model the narrower Leeds annotation scope.

The standalone FP reduction is **consistent with**, but does not by itself prove, correction
of definitional disagreement. The standalone category also contains genuine visual
confusions and other errors more than 5 m from labelled parking. Demonstrating that the
removed predictions are specifically on-street parking or private driveways would require a
paired typological sample of zero-shot and fine-tuned outputs.

The boundary hypothesis is not supported in the simple form “boundary error does not move”.
Absolute FP near reference boundaries decreases substantially. Yet this occurs alongside a
large rise in FN, including both erosion-associated and standalone FN. The most defensible
interpretation is therefore not that fine-tuning learned uniformly better geometry, but that
it shifted the decision boundary toward under-prediction. The model draws less parking
overall; this removes exterior overreach but also retracts from genuine parking surfaces and
misses more lots.

The current evaluation cannot determine whether small or irregular car parks improved.
Recall declines overall, which gives no affirmative support to that expectation and may mean
that subtle targets were sacrificed as the model became conservative. A separate object-level
analysis by lot size and layout would be needed before making a claim.

## 11. What the experiment establishes

The defensible findings are:

1. Local fine-tuning improves held-out pixel IoU under a spatially separated comparison.
2. The improvement generalises beyond the validation cells and appears under both micro and
   macro aggregation.
3. It is achieved mainly through a large reduction in false positives, accompanied by a
   substantial loss of recall.
4. Standalone FP is especially responsive to local supervision, consistent with learnable
   geographic or definitional mismatch.
5. Boundary-associated error does not behave as a fixed resolution floor: exterior FP falls,
   but interior and standalone FN increase as predictions contract.
6. Matching aggregate predicted and labelled area does not imply accurate spatial allocation.

Claims that are **not** supported are:

- that local fine-tuning improves every error class;
- that the new model is unambiguously better for every use case;
- that the standalone FP reduction consists entirely of corrected definition disagreements;
- that fine-tuning improves small or irregular car parks; or
- that these results identify an optimal training configuration.

## 12. Limitations

This is one bounded run with one random seed, one 40/10/50 cell partition and one fixed
hyperparameter setting. Epoch selection used only ten cells, and no uncertainty interval is
available across seeds or alternative spatial splits. The source labels come from one
annotator, and adjacent cells retain some spatial dependence even though their pixels do not
overlap.

Metrics are pixel-wise and omit the original pipeline's polygon cleaning and OSM subtraction.
Operational performance after post-processing could change differently. In particular, some
raw false positives removed by fine-tuning might already have been removed by the downstream
pipeline, while new false negatives cannot be recovered by post-processing.

The experiment also changes the model's precision–recall operating point through learning,
but it does not compare this with a simpler probability-threshold calibration. Because the
released workflow uses argmax rather than a tuned threshold, a future analysis should test
whether part of the same precision gain could be obtained without updating model weights.

## 13. Reporting rules for the dissertation

The experiment should be described as a **supplementary local-adaptation test**, not as the
main model. The methodology must state the cell-level split, validation-based epoch selection,
single run, lack of tuning and pixel-wise evaluation. The results should present precision,
recall and IoU together, followed by absolute FP/FN areas and the 5 m decomposition. Reporting
only IoU would conceal the central trade-off.

Suggested concise result statement:

> On the 50 held-out cells, local fine-tuning increased pixel IoU from 0.485 to 0.614 and
> precision from 0.519 to 0.766, but reduced recall from 0.882 to 0.755. False-positive area
> fell by 71.9%, including a 74.5% reduction in standalone FP beyond 5 m of a label, while
> false-negative area more than doubled. Local supervision therefore corrected much of the
> model's tendency to over-predict UK parking, but did so by shifting it toward a conservative
> operating point rather than by improving every component of segmentation.

Suggested discussion statement:

> The supplementary experiment shows that geographic mismatch is partly learnable: a small
> set of Leeds labels sharply reduced unsupported detections and removed the aggregate area
> surplus. Yet the cost was lower recall and greater missed area. This qualifies a simple
> recommendation to fine-tune locally. The intervention is attractive where false positives
> are costly, but less so where inventory completeness matters, and the near-unbiased citywide
> total conceals substantial compensating FP and FN. The error decomposition is therefore
> necessary not only to diagnose zero-shot transfer but also to determine what local
> adaptation actually changes.

The principal zero-shot chapters must retain their original wording that no UK data adjusted
the model used in the main analysis. Any future-work sentence claiming that local fine-tuning
has not been tested should be revised if this supplementary experiment is included.

## 14. Reproducibility record

All experiment code is contained in `fine-tuning/`:

| File | Purpose |
|---|---|
| `make_split.py` | Balanced cell-level train/test allocation |
| `make_patches.py` | Raster masks, patch index, sampling and alignment guard |
| `check_alignment.py` | Visual mask-over-image inspection |
| `modeling.py` | Processor/model construction and strict checkpoint loading |
| `patch_data.py` | TIFF-backed patch dataset and tile-aware batch sampling |
| `finetune.py` | Cell-level validation, training and best-epoch checkpointing |
| `evaluate.py` | Held-out micro/macro metrics and 2/5/10 m error bands |
| `run_finetuning_colab.ipynb` | End-to-end Drive, Git LFS, training and evaluation workflow |

The durable run outputs are `finetuned.ckpt`, `finetune_log.csv`, `fit_val_split.csv`,
`checkpoint_metadata.csv`, `evaluation.csv`, `boundary_bands.csv`, and the console logs. The
released `best_model.ckpt` must be the 1.017 GB model file, not its 135-byte Git LFS pointer.
