# 4. Results

> **草稿 v1**｜目标 3,000 词
> 图：全部在 `figures/`，七张现在统一由 `analysis/make_results_figures.py` 一次生成（含 `parking_extent` 与 `calibration_transfer` 的本章重绘版，不再从 `analysis/` 复制）。图 3.1、3.2 由 `make_methods_figures.py` 生成。重跑分析后只需重跑这两个脚本
> 完整数值表进附录 C；正文只保留头条数字
> 待办：引用格式统一；附录表编号

---

This chapter reports the measured transfer. Section 4.1 gives the headline accuracy and how it varies across the city, answering the first half of RQ1. Sections 4.2 to 4.4 decompose the error and test the post-processing stage, answering RQ2. Section 4.5 returns to spatial variation and shows the apparent location effect to be confounded. Section 4.6 reports the sampled corrections and what the reference data itself is worth. Section 4.7 answers RQ3 within the reliability the preceding sections establish.

---

## 4.1 Overall accuracy and its spatial variation

Against 3.2597 km² of labelled surface parking, the model predicts 4.8785 km² — **1.50 times the labelled area**.

**Table 4.1** Accuracy of the post-processed output over the 100 km² study area.

| Aggregation | Precision | Recall | IoU |
|---|---:|---:|---:|
| **Micro, all confidence levels** | **0.5708** | **0.8543** | **0.5202** |
| Micro, confidence 2–3 only | 0.5287 | 0.8658 | 0.4886 |
| Macro (mean of 100 cells) | 0.5136 | 0.8468 | 0.4697 |

The pattern is asymmetric. Recall of 0.854 means the model finds most labelled parking; precision of 0.571 means that a little under half of what it returns is not labelled parking. Decomposed by area, TP is 2.7848 km², FP 2.0937 km² and FN 0.4749 km², the last being 14.6% of labelled area.

![Per-cell accuracy](figures/fig_accuracy_maps.png)

**Figure 4.1** Precision, recall and IoU for each 1 km² cell, on a common colour scale. Recall is high and spatially even; precision is neither. One cell contains no labelled parking and is hatched.

Figure 4.1 shows that the asymmetry is not an artefact of aggregation: recall is uniformly high across the study area, while precision varies from below 0.3 to above 0.8 between neighbouring cells. The macro figures fall below the micro figures on all three measures — precision 0.514 against 0.571 — indicating that cells contributing little parking area perform worse than the area-weighted total suggests.

Restricting the reference to the more confident labels does not improve precision; it lowers it, from 0.571 to 0.529. Since removing labels can only convert true positives into false positives, this establishes that the confidence-1 labels are not a substantial source of the measured over-prediction.

## 4.2 False positives

False-positive area is 2.0937 km². Figure 4.2 shows what it is made of.

![Error composition](figures/fig_error_composition.png)

**Figure 4.2** Composition of false-positive area (upper) and false-negative area (lower). In each case the lower bar expands the residual segment of the bar above it. Exclusive shares are of all FP or FN and sum to 100%.

**Boundary effects account for a substantial minority.** False-positive area lying within a fixed distance of a labelled car park — the model finding the right lot and drawing it too large — is 17.3% at 2 m, **28.8% at 5 m** and 36.3% at 10 m. The three thresholds are reported because 5 m is a working convention; the value chosen shifts this component by nearly twenty percentage points.

**Attribution of the standalone remainder.** Table 4.2 gives the exclusive partition alongside the unordered diagnostic.

**Table 4.2** Where false-positive area falls. The two columns have different denominators and are not differences of one another: exclusive shares are assigned once each and sum to 100%, while unordered overlaps are measured against all FP independently and may overlap one another.

| Layer | Exclusive (% of all FP) | Unordered overlap (% of all FP) |
|---|---:|---:|
| Boundary dilation (≤ 5 m) | 28.8 | — |
| Industrial / commercial land | 29.6 | **52.8** |
| Road-adjacent (+6 m) | 11.6 | 16.9 |
| OSM parking | 4.7 | 9.1 |
| Sports courts | 2.5 | 3.1 |
| Brownfield | 1.7 | 2.3 |
| Buildings | 0.0 | 0.0 |
| **Unexplained** | **21.0** | — |

Industrial and commercial land coincides with over half of all false-positive area. Buildings account for none, because OSM building footprints have already been subtracted at the post-processing stage; false positives on buildings the OSM data does not record fall into the unexplained residual. Moving industrial land from an early position in the peeling order to last changes its exclusive share from 30.0% to 29.6%, so the attribution is not an artefact of the ordering.

**The unexplained residual divides into three unlike things.** Stratified sampling of 70 chips (Figure 4.3) estimates that 44.5% of the residual is genuine misdetection — grey hardstanding, goods yards, sports courts, unpaved ground and unmapped houses — while **34.9% is real parking that the annotation rules deliberately exclude**, principally private driveways (20.2%) and on-street parking (14.7%). A further 17.2% is parking the labelling itself missed. Percentages are of the sampling frame, which excludes fragments below 100 m² and so covers 0.3883 km² of the 0.4396 km² residual.

## 4.3 False negatives

Missed area is 0.4749 km², 14.6% of labelled parking. Measured against the prediction, 33.4% of it lies within 2 m of something the model did find, **54.1% within 5 m** and 69.4% within 10 m.

**Most missed area is the edge of a car park the model found.** Classifying missed area by how much of its parent lot the model covered gives a more useful split than any distance threshold:

**Table 4.3** Missed area by the state of the car park it belongs to.

| Class | Coverage of the lot | Lots | Missed area (km²) | Share of FN |
|---|---|---:|---:|---:|
| Fringe of a well-detected lot | > 70% | 1,638 | 0.2108 | 44.4% |
| Partly detected | 10–70% | 278 | 0.1510 | 31.8% |
| **Whole lot missed** | ≤ 10% | **121** | **0.1131** | **23.8%** |

Nearly half of all missed area belongs to lots the model detected to better than 70%. Only the third row is a detection failure in any useful sense, and it is not what it appears: **31.9% of it was found by the model and then deleted by post-processing**, with a further 2.9% labelled as rooftop and 3.4% falling inside OSM building footprints. The genuine blind spot is 0.0699 km², **2.1% of labelled area at most** — and §4.6 shows part of even that is not parking in the imagery the model was given.

**Detection tracks size and annotator confidence.**

**Table 4.4** Detection rate by lot size and by labelling confidence.

| Lot size | Lots | Mean detection rate | Missed entirely |
|---|---:|---:|---:|
| < 200 m² | 47 | 0.658 | **19.1%** |
| 200–500 m² | 563 | 0.763 | 8.2% |
| 500–1,000 m² | 573 | 0.805 | 5.4% |
| 1,000–2,500 m² | 559 | 0.852 | 3.0% |
| 2,500–5,000 m² | 182 | 0.850 | 4.9% |
| > 5,000 m² | 113 | 0.864 | **1.8%** |

| Confidence | Lots | Mean detection rate | Missed entirely |
|---|---:|---:|---:|
| 1 (uncertain) | 435 | 0.713 | 10.6% |
| 2 | 1,137 | 0.829 | 3.8% |
| 3 (clear) | 465 | 0.856 | 5.4% |

Lots below 200 m² are missed outright more than ten times as often as lots above 5,000 m². Detection is also lowest where the annotator was least certain, which indicates that part of the measured error reflects genuine ambiguity in the target rather than model deficiency.

**What the genuine misses look like.** Sampling of 42 chips estimates the composition of the residual as: not parking in the Digimap imagery 41.8%, **irregular layout 23.3%**, obscured by shadow or canopy 9.8%, unusual surface 9.2%, no cars present 6.3%, vans and lorries rather than cars 5.2%, and **no markings 3.7%**.

![Worked examples](figures/fig_error_chips.png)

**Figure 4.3** One worked example of each failure category, on the Digimap imagery the model was given. Red outlines the sampled polygon, blue the model's prediction, yellow other labelled parking nearby.

Irregular layout was assigned to 11 of the 42 chips and absent markings to one, so the latter estimate rests on a single observation and its 3.7% should not be read as a precise share. The two are nonetheless separated cleanly by their intervals — 23.3% [16.9, 31.1] against 3.7% [0.6, 9.8] — so the ordering does not depend on that one chip. What the sample supports is that irregular arrangement was the most frequently identified mechanism and unmarked surfacing among the least — which revises the expectation set out in §2.5, where unmarked surfaces were anticipated as the difficulty.

## 4.4 Post-processing and the reference layers as filters

![Ablation](figures/fig_ablation.png)

**Figure 4.4** The eight variants on the precision–recall plane, with IoU iso-lines. Circles are the post-processing factorial; squares are reference layers applied as filters.

**Table 4.5** Ablation. Variants A–D vary the two post-processing subtractions; E–H apply further layers as filters to the finished map.

| Variant | Precision | Recall | IoU |
|---|---:|---:|---:|
| A raw model | 0.5278 | 0.8939 | 0.4967 |
| B − buildings | 0.5467 | 0.8691 | 0.5051 |
| C − roads | 0.5498 | 0.8789 | 0.5111 |
| **D − buildings − roads** | **0.5708** | **0.8543** | **0.5202** |
| E − sports pitches | 0.5701 | 0.8373 | 0.5132 |
| **F − industrial land** | 0.4794 | **0.2789** | **0.2140** |
| G − wider roads | **0.5962** | 0.7884 | 0.5140 |
| H − all three | 0.5195 | 0.2419 | 0.1976 |

Reconstructing D from the raw output in a single operation reproduces the pipeline's own tile-by-tile result to within 0.0% on all three measures, so the ablation isolates what it claims to.

The two subtractions together raise precision by 0.043 and lower recall by 0.040, for a net IoU gain of 0.024. Each contributes roughly half. Applied as filters, the further layers behave quite differently. Subtracting industrial and commercial land — the layer that coincided with 52.8% of false-positive area — **collapses recall from 0.854 to 0.279 and IoU from 0.520 to 0.214**, because supermarket and retail-park car parks sit on exactly that land. Widening the road buffers is the only variant to raise precision (to 0.596), and it still lowers IoU.

**The pipeline creates a blind spot of its own.** Sixteen labelled lots, 0.0395 km² or 1.21% of the reference, are rooftop parking.

**Table 4.6** Rooftop parking, before and after post-processing.

| Measure | Value |
|---|---:|
| Recall on rooftop lots, raw model | **0.916** |
| Recall on rooftop lots, after subtraction | **0.115** |
| Recall on non-rooftop lots, raw model | 0.894 |
| Rooftop area falling inside OSM buildings | 85.6% |
| Rooftop area detected then removed | **80.1%** |

The raw model detects rooftop parking slightly *better* than ground-level parking. Subtracting building footprints removes four fifths of it.

## 4.5 Accuracy and location

**Table 4.7** Correlations with per-cell precision, recall and IoU (Pearson r, p in brackets). Recall statistics use the 99 cells with labelled parking.

| Metric | Distance | Parking share | Distance \| parking share | Parking share \| distance |
|---|---:|---:|---:|---:|
| **Precision** | −0.172 (0.087) | **+0.536 (<0.0001)** | +0.186 (0.065) | **+0.540 (<0.0001)** |
| Recall | +0.181 (0.073) | +0.103 (0.313) | +0.289 (0.004) | +0.250 (0.013) |
| IoU | −0.127 (0.208) | **+0.515 (<0.0001)** | +0.229 (0.022) | **+0.540 (<0.0001)** |

Distance from the city centre does not predict precision. The share of a cell given over to parking does, strongly, and continues to do so after controlling for distance. The reverse does not hold: controlling for parking share, the distance effect is not significant. Distance and parking share are themselves correlated at −0.562.

All three metrics are reported to avoid selective presentation, but only precision is interpreted here. The partial correlations for recall and IoU reach significance while their raw correlations do not, and their signs reverse between the two; with n = 100 and two strongly correlated predictors this pattern is not a stable basis for a claim.

Read across distance bands, precision falls from 0.584 within 1 km to 0.485 beyond 4 km while recall stays between 0.70 and 0.86 (see Figure 4.5 and Appendix B). The band means move with parking share, not with distance.

![Accuracy and location](figures/fig_accuracy_vs_location.png)

**Figure 4.5** Per-cell precision against distance and against parking share, and parking share against distance. Solid red fits are significant at p < 0.05; the dashed grey fit is not. Diamonds are distance-band means.

## 4.6 Sampled corrections, and what the reference is worth

Applying the sampled estimates as corrections gives four cumulative variants:

**Table 4.8** Accuracy under cumulative correction.

| Variant | Reference (km²) | Prediction (km²) | Precision | Recall | IoU |
|---|---:|---:|---:|---:|---:|
| **1 As measured** | 3.2597 | 4.8785 | **0.5708** | **0.8543** | **0.5202** |
| 2 + reference-side (−0.0313, not parking in the imagery) | 3.2284 | 4.8785 | 0.5708 | 0.8626 | 0.5233 |
| 3 + prediction-side (+0.0667, parking the labelling missed) | 3.2951 | 4.8785 | 0.5845 | 0.8654 | 0.5358 |
| **4 Effective (−0.1358, definitional exclusions removed)** | 3.2951 | 4.7427 | **0.6012** | 0.8654 | **0.5498** |

The corrected figures carry sampling uncertainty, and the bootstrap of §3.6 puts 95% intervals on them: precision 0.5845 [0.5783, 0.5917] at variant 3 and 0.6012 [0.5941, 0.6090] at variant 4, recall 0.8654 [0.8635, 0.8675], IoU 0.5498 [0.5434, 0.5569]. The variant-4 interval does not reach the measured 0.5708, so the gain is not an artefact of which polygons happened to be sampled. The intervals are narrow because the corrections are small relative to the quantities they adjust: a near-threefold range in the estimated prediction-side correction, 0.0366 to 0.1018 km², moves precision by under a point and a half.

Precision rises from 0.571 to 0.601 across the four steps, and roughly half of that gain comes from the final step — removing on-street parking and private driveways from the prediction, which are real parking excluded by rule rather than model error. Recall moves only between 0.854 and 0.865. **The headline pattern does not change under any correction**; variant 1 is reported throughout as the primary figure.

**OpenStreetMap, assessed against the same reference.** OSM records 1.7641 km² of parking in the study area, 54.1% of the labelled total, across 985 polygons against 2,037 labelled. Their median polygon areas are almost identical (763 m² against 799 m²), so OSM is not simply recording the large car parks and omitting small ones. It overlaps 1.1882 km² of labelled parking — 36.5% of it — leaving **63.5% of labelled parking absent from OSM entirely**. In the other direction, sampling of the area where OSM claims parking and the reference does not estimates that 63.2% shows no parking on the ground.

Last-edit timestamps were retrieved for all 985 OSM parking features. The median across the study area is 2024. Among the sampled polygons judged not to be parking, the median is **2025**, and 8 of 11 were edited in 2024 or later — later than any other sampled category. The disagreement is therefore not attributable to OSM being out of date.

## 4.7 The extent and distribution of surface parking

**Table 4.9** Surface parking as a share of land, by distance band.

| Band | Cells | Labelled | Model | Calibrated (km²) |
|---|---:|---:|---:|---:|
| < 1 km | 2 | 5.33% | 6.42% | 0.086 |
| **1–2 km** | 11 | **7.11%** | 10.35% | 0.761 |
| 2–3 km | 14 | 4.80% | 7.19% | 0.673 |
| 3–4 km | 22 | 4.50% | 6.53% | 0.959 |
| > 4 km | 51 | 1.39% | 2.29% | 0.781 |
| **Whole area** | 100 | **3.26%** | 4.88% | 3.2595 |

The calibrated column applies the whole-area factor of §3.9. In the final row that is an identity and carries no information: the factor was fitted on exactly these cells, so it returns their labelled area by construction. In the band rows it is not, because a factor fitted over the whole area is being applied to a sub-area it was not fitted to; the difference between the calibrated and labelled columns there is the factor's transfer error within the city, ranging from −19.6% in the two-cell innermost band to +10.0% beyond 4 km.

Surface parking covers 3.2597 km², **3.26% of the 100 km² study area**. This is a figure from the labelled reference rather than from the model: every car park in the study area was labelled, so it is a census and not an estimate. Its uncertainty is that of the labelling, which the corrections of §4.6 bound directly — removing the labelled area that is not parking in the Digimap imagery and adding the parking the labelling missed moves the reference to 3.2951 km², or **3.30%**. The two corrections together shift the share by less than a tenth of a percentage point of the study area.

The share is highest in the inner 2 km — 5.33% within 1 km and 7.11% between 1 and 2 km — and falls monotonically beyond that, to 4.80%, 4.50% and 1.39% in the successive bands. The decline outward is well supported, resting on bands of 14, 22 and 51 cells. Whether the profile also turns down at the very centre is not established: the innermost band holds only two cells, so the apparent dip from 7.11% to 5.33% cannot be distinguished from the variation between individual cells.

The distribution across cells is strongly right-skewed: mean 3.26%, **median 1.71%**, maximum 18.81%, with six cells above 10%. Parking land is concentrated rather than spread evenly.

![Parking extent](figures/parking_extent.png)

**Figure 4.6** Parking share by cell, against distance, and its distribution across the 100 cells.

**Calibration and the grain at which it holds.** For a map of precision *p* and recall *r*, true area is estimated as predicted area × *p*/*r*, here 4.8785 × 0.6681 = 3.2595 km². On the cells the factor was fitted to this is an identity. Tested by holding cells out (Table 4.10), it is not.

**Table 4.10** Error of the calibrated estimate on cells excluded from fitting the factor.

| Scheme | Held out | Tests | Mean error | 5–95% | Within ±25% |
|---|---|---:|---:|---:|---:|
| **Random half split** | 50 cells | 200 | +0.3% | **−6.6% to +7.8%** | 100% |
| Leave one distance band out | 1 band | 5 | −2.9% | −16.9% to +10.6% | — |
| **Leave one cell out** | 1 cell | 99 | +16.5% | −22.0% to +80.5% | **63%** |

A factor fitted on half the city predicts the other half to within about **±7%** at 90% confidence. This figure describes what the method would deliver where no labelling exists — it is not an error bar on the 3.26% above, which was measured directly and is the quantity the calibration is attempting to recover. Applied to a single 1 km² cell the estimator fails: only 63% of cells fall within ±25%, and the leave-one-out mean sits well above its median because relative error is unstable where a cell holds little parking — the median absolute error is 0.0035 km² against a mean labelled area of 0.0329 km² per cell.

![Calibration transfer](figures/calibration_transfer.png)

**Figure 4.7** Distribution of calibrated-estimate error under the three hold-out schemes. The red line marks the median of each distribution; Table 4.10 reports the mean, which for the leave-one-out scheme is the higher of the two.
