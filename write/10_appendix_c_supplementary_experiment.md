# Appendix C — Supplementary adaptation experiment

## C.1 Purpose and standing

The analysis in Chapters 4 and 5 measures the released checkpoint applied to Leeds without any UK training data. This appendix reports a bounded supplementary experiment that departs from that boundary alone, in order to ask a question the main study cannot: if a user does hold local pixel-level labels, what does the error typology of §4.2 buy them?

Three interventions are compared against the zero-shot model: generic fine-tuning on Leeds labels, targeted fine-tuning that weights the loss by the attributed false-positive categories, and probability-threshold adjustment of the generic model with no retraining.

Nothing here enters the main analysis. All figures are raw pixel output on a fixed held-out split, without the post-processing that Chapter 4 applies throughout, and they are valid only for comparison with each other. They are not comparable with the headline figures of Chapter 4 and are not used to qualify them.

## C.2 Data and split

The 100 cells of the study area are partitioned at cell level, so no patch from a training cell appears in evaluation:

| Role | Cells | Use |
|---|---:|---|
| Fit | 40 | gradient updates |
| Validation | 10 | epoch selection and threshold selection |
| Test | 50 | reported results only |

Patch sampling keeps every patch containing labelled parking and an equal number of empty patches, giving 2,256 retained training patches. The validation set is the 438 retained patches of the ten validation cells — the same sample used to select checkpoints during training, so that threshold selection and epoch selection see identical data. The test set is the complete 3,200 patches of the fifty held-out cells, with no retention filter, so evaluation covers whole cells rather than a parking-enriched sample.

The zero-shot arm reproduces precision 0.5190, recall 0.8819 and IoU 0.4853 on this split, which is the consistency check the other arms depend on: without it none of the comparisons below would be interpretable.

Tables C.1 to C.5 label the four arms A to D, following the result files listed in C.8. The text refers to them by description, so that arm letters are never confused with appendix letters.

## C.3 Generic and targeted fine-tuning

Both fine-tuning arms start from the released checkpoint and share batch size, learning rate, optimiser and seed; only the loss differs. The targeted arm assigns per-pixel weights from the model's own zero-shot errors on the fit cells, coded against the reference layers of §4.2: standalone false positives on precise layers (road buffer, curtilage, OSM parking, sports) are weighted most heavily, those on broad land-use layers less so, and false negatives receive a counterweight computed from the observed code composition rather than chosen by hand. False positives within the boundary band are deliberately left at unit weight, since upweighting them is precisely how a model is taught to draw everything smaller.

An earlier targeted configuration was run with a hand-set counterweight and is not reported here: its suppression and recovery terms were unbalanced, which confounds the comparison the arm was built to make. Only the rebalanced run is reported.

The two targeted checkpoints come from a single training trajectory, not from two independently trained models. Epoch 12 gave the best validation IoU (0.6105); among epochs within 0.02 of it, epoch 7 gave the highest validation recall (0.8385) at validation IoU 0.6093. The two differ by 0.0012 in validation IoU, which is within the run-to-run variation visible across epochs 7 to 12, so the pair should be read as two operating points on one trade-off curve rather than as a better and a worse model.

**Table C.1 — Overall accuracy, 50 held-out cells, raw pixels (micro)**

| Arm | Precision | Recall | IoU | Predicted ÷ reference |
|---|---:|---:|---:|---:|
| A zero-shot | 0.5190 | 0.8819 | 0.4853 | 1.699 |
| B generic fine-tuning | 0.7664 | 0.7548 | **0.6136** | 0.985 |
| C targeted, epoch 12 (best validation IoU) | 0.7393 | 0.7168 | 0.5722 | 0.970 |
| D targeted, epoch 7 (best validation recall) | 0.6668 | 0.7852 | 0.5640 | 1.178 |

**Table C.2 — The same arms under macro (per-cell mean) aggregation**

| Arm | Precision | Recall | IoU |
|---|---:|---:|---:|
| A zero-shot | 0.4773 | 0.8777 | 0.4473 |
| B generic fine-tuning | 0.7553 | 0.7205 | **0.5833** |
| C targeted, epoch 12 | 0.7116 | 0.6839 | 0.5374 |
| D targeted, epoch 7 | 0.6391 | 0.7595 | 0.5322 |

Generic fine-tuning raises IoU from 0.485 to 0.614, gaining 0.247 of precision at a cost of 0.127 of recall: standalone false-positive area falls by 74.5% while false-negative area doubles. Neither targeted checkpoint improves on it, under either aggregation.

The generic model's predicted area is within 1.5% of the reference total. This is arithmetic coincidence at this operating point, not a corrected bias: false-positive area (0.3736 km²) and false-negative area (0.3982 km²) happen to be close, and they cancel. The epoch-7 targeted checkpoint, from the same run, over-predicts by 17.8%. Nothing in this appendix supports a claim that fine-tuning corrects the area bias measured in Chapter 4, which concerns post-processed output over the whole study area.

**Table C.3 — Boundary decomposition at 5 m (km²)**

| Arm | FP dilation | FP standalone | FN erosion | FN standalone |
|---|---:|---:|---:|---:|
| A zero-shot | 0.3737 | 0.9537 | 0.0858 | 0.1059 |
| B generic fine-tuning | 0.1302 | 0.2434 | 0.1684 | 0.2298 |
| C targeted, epoch 12 | 0.1503 | 0.2602 | 0.1686 | 0.2913 |
| D targeted, epoch 7 | 0.2359 | 0.4013 | 0.1254 | 0.2233 |

Under every arm the added false negative is majority standalone rather than erosion — whole car parks missed, not edges trimmed. Bands at 2 m and 10 m are reported in `boundary_bands_arms.csv` and do not change this ordering.

## C.4 Selectivity

The targeted arm was designed to remove false positives from four categories specifically: road buffer, curtilage, OSM parking and sports. If positional weighting works as intended, the removal rate for those categories should exceed the removal rate for the others by more than it does under generic fine-tuning.

**Table C.4 — Standalone false-positive removal against zero-shot (%)**

| Arm | Targeted categories | Other categories | Gap (pts) |
|---|---:|---:|---:|
| B generic fine-tuning | 72.5 | 62.8 | **9.7** |
| C targeted, epoch 12 | 71.6 | 63.2 | 8.4 |
| D targeted, epoch 7 | 58.3 | 50.6 | 7.8 |

Neither targeted arm is more selective than generic fine-tuning. Per category, generic fine-tuning removes more standalone false positive than the epoch-12 targeted checkpoint on road buffer (81.4% against 78.0%), curtilage (75.8% against 70.6%) and OSM parking (42.7% against 40.1%); only sports favours the targeted arm (97.5% against 90.0%). Total standalone false-positive removal is also higher under generic fine-tuning (74.5% against 72.7% and 57.9%).

## C.5 Threshold adjustment: method

The targeted checkpoints differ from the generic model mainly in where they sit on a precision–recall trade-off. That raises a question the fine-tuning arms cannot settle on their own: whether those operating points require targeted training at all, or whether they are reachable by moving the decision threshold of the generic model.

The released pipeline takes the argmax of the two output logits, equivalent to thresholding the parking probability at 0.50. The sweep replaces that rule and nothing else. No weights are retrained, and the generic checkpoint is used unmodified.

1. Sweep the parking-class probability threshold from 0.05 to 0.95 in steps of 0.01 (91 values) on the 10 validation cells.
2. Select thresholds on validation only, under four rules: the default 0.50; the best validation IoU; the threshold matching the epoch-12 checkpoint's validation recall; and the threshold matching the epoch-7 checkpoint's validation recall.
3. Lock each selected threshold, then evaluate once on the 50 test cells.

Test labels play no part in selection. At threshold 0.50 the sweep reproduces the generic model's test figures exactly (0.7664 / 0.7548 / 0.6136), confirming that the sweep and the training evaluation share one pipeline.

## C.6 Threshold adjustment: results

**Table C.5 — Threshold-adjusted generic model against the targeted checkpoints, test cells**

| Model and rule | Threshold | Precision | Recall | IoU |
|---|---:|---:|---:|---:|
| B generic, default | 0.50 | 0.7664 | 0.7548 | 0.6136 |
| B generic, best validation IoU | 0.48 | 0.7590 | 0.7625 | **0.6139** |
| B generic, matched to C's validation recall | 0.60 | 0.8020 | 0.7113 | 0.6051 |
| C targeted, epoch 12 | — | 0.7393 | 0.7168 | 0.5722 |
| B generic, matched to D's validation recall | 0.39 | 0.7227 | 0.7948 | 0.6090 |
| D targeted, epoch 7 | — | 0.6668 | 0.7852 | 0.5640 |

At the threshold matched to the epoch-12 checkpoint, the generic model gives 0.063 more precision and 0.033 more IoU at recall within 0.006. At the threshold matched to the epoch-7 checkpoint, it is higher on all three measures: precision by 0.056, recall by 0.010, IoU by 0.045. The ordering holds under macro aggregation, where the matched generic thresholds give IoU 0.5707 against the epoch-12 checkpoint's 0.5374 and 0.5801 against the epoch-7 checkpoint's 0.5322.

Threshold selection itself gains almost nothing: the best validation threshold, 0.48, improves test IoU by 0.0003 over the default. The released argmax rule is already close to optimal for this model, which is why the comparison is informative — the targeted checkpoints are being measured against a generic model that has not been tuned in its own favour.

The conclusion this supports is that positional targeted weighting produced no overall performance gain that threshold adjustment of the generic model could not supply. It does not support the stronger claim that the targeted model learned no new features: these are aggregate accuracy measures, and they cannot observe what the network represents internally.

## C.7 Limitations

- **One seed, one weighting scheme.** Every arm was trained once. The epoch-to-epoch spread in validation IoU across epochs 7 to 12 is comparable to the gap between the two targeted checkpoints, so the experiment cannot separate a small real effect from run-to-run variation.
- **Positional proxies are not visual categories.** Standalone false positives were weighted by the layer they fall on. A false positive on industrial land may be a roof, a hardstanding, a road or a vehicle storage yard; these are one location but not one appearance, and weighting them together may present the network with no consistent feature to learn. This is the most likely explanation for the negative result and is untested.
- **Raw pixels only.** No arm passes through the post-processing of §3.4. Comparison with Chapter 4 is invalid in both directions.
- **Validation is a parking-enriched sample.** Epoch and threshold selection used the 438 retained patches of ten cells, not whole cells, so the selected operating points are tuned on a distribution denser in parking than the test cells.
- **One city, one annotator.** Fit, validation and test cells are all Leeds, labelled by the same annotator against the same protocol. Nothing here tests whether a fine-tuned model transfers to a second British city, which remains the precondition identified in §4.7.
- **The threshold result is about aggregate accuracy.** It shows no measurable overall advantage from targeted weighting; it does not establish that the two models are equivalent, nor that targeted training is unproductive in general.

## C.8 Files

Results are reproduced from `targeted-finetuning/Parking_targeted_run2/`: `evaluation_arms.csv` (Tables C.1–C.2), `boundary_bands_arms.csv` (C.3), `selectivity.csv` and `standalone_fp_by_category.csv` (C.4), `threshold_sweep/generic_threshold_selected.csv` (C.5), and `targeted_log.csv` for the epoch record. The notebooks are `run_targeted_colab.ipynb` and `threshold_sweep_colab.ipynb`.
