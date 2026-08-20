# 5. Discussion

## 5.1 Answering the research questions

**RQ1 — How accurate is the model on UK aerial imagery, and does accuracy vary systematically within the city?**

The transfer works, but unevenly. Recall of 0.854 (Table 4.1) means that most labelled parking is found; precision of 0.571 means that a little under half of the returned area is not labelled parking, and predicted area is 1.50 times labelled area. Figure 4.1 shows the asymmetry across the city: recall is generally high and less spatially variable, while precision varies by more than a factor of two between neighbouring cells.

The IoU of 0.520 is better read against transfer studies than against an implicit standard of perfection. Maggiori et al. (2017) regarded roughly 65% IoU on unseen-city building footprints as satisfactory generalisation, while Hurst-Tarrab et al. (2020) report parking-block models above 50%. The present result lies in that range despite using no target-domain training in the primary analysis; the comparison studies drew training and test data from the same source. Scalar performance therefore survived the crossing better than might be expected, but it does not reveal where the cost fell.

Nor does the apparent spatial pattern survive closer examination. Once parking share is controlled for, distance from the centre no longer predicts precision, whereas parking share remains strongly associated with it (Table 4.7, Figure 4.5). Accuracy tracks parking abundance rather than location, consistent with macro scores falling below micro scores and sparse cells performing poorly. Lot size shows a separate association (Table 4.4); neither relationship establishes causation. The raw distance correlation alone would therefore give a plausible but misleading account of central-city performance.

**RQ2 — What systematic errors does the model make, and how much error does post-processing remove or create?**

Complete-lot non-detection is not the dominant explanation. Automated attribution leaves 0.0699 km² unresolved, **2.1% of labelled area** and under 3% of all error area; sampled adjudication also finds reference–imagery disagreement within this population. Boundary placement is the largest single component: 28.8% of false-positive area and 54.1% of false-negative area lie within 5 m of a matched feature, together about a third of all error area. Consistently, 44.4% of missed area belongs to lots detected to better than 70% (Tables 4.2, 4.3). The remainder mixes look-alike surfaces, definitional disagreement and pipeline artefacts rather than one dominant cause.

This qualifies the zero-shot robustness reported for SegFormer by Xie et al. (2021). Their benchmark degrades familiar scenes through noise, blur, weather and digital artefacts; geographic transfer changes the scene itself. Here, complete-lot detection appears comparatively robust, while boundary placement is the larger constraint. No comparable source-domain decomposition exists, so the study cannot say that delineation became worse after transfer. It can say that the architecture's corruption robustness and the error pattern observed here are not in tension.

The sampled typology also revises the expectation in §2.5 that absent markings would be the principal difficulty. Irregular layout was identified in 11 of 42 chips and accounted for an estimated 23.3% of the unresolved whole-lot population, against one chip and 3.7% for absent markings. The latter estimate is imprecise, so the evidence supports an ordering rather than a precise ratio: irregular arrangement was the most frequently identified mechanism and unmarked surfacing among the least. Shadow, unusual surfacing and commercial vehicles appeared at more modest magnitudes.

Building and road subtraction is a genuine trade: it raises precision by 0.043 and costs 0.040 of recall (Table 4.5). It also creates a specific blind spot. The pre-subtraction output detects rooftop parking at 0.916 recall, but building subtraction removes four fifths of it; 31.9% of whole-lot misses were detected before being deleted by the pipeline (Table 4.6). That component is about half the size of the unresolved whole-lot remainder. Domain-adaptation research usually treats the model as the object transferred (Lyu et al., 2025), but deployment transfers a model and its corrections. The rooftop result therefore argues for re-evaluating both.

The ablation rejects another tempting inference. Although industrial and commercial land coincides with 52.8% of false-positive area, using it as a filter reduces recall from 0.854 to 0.279 and IoU from 0.520 to 0.214 because real retail parking occupies the same land. All four additional filters lower IoU, even where the loss is small. **Reference layers can explain where error falls without being able to remove it.**

**RQ3 — How much central-city land is surface parking, and where is it concentrated?**

The complete-coverage reference records surface parking over 3.26% of the 100 km² study area, rising to 3.30% after the sampled reference corrections (Table 4.8). Parking peaks at 7.11% in the 1–2 km band and declines to 1.39% beyond 4 km; the <1 km band contains only two cells, so the apparent central dip is uncertain. Distribution is strongly right-skewed: a median cell holds 1.71%, while six exceed 10%.

Jiao (2015) shows urban land density generally declining with distance from the centre. Parking does not show a clear decline within the inner 2 km, only beyond it. This is not a contradiction—the quantities differ—but it raises a question the data cannot answer: whether surface parking is displaced from the highest-value centre while remaining close to it. Testing that would require land-value data and more central cells.

## 5.2 What the transferred map is good for

The practical question is not whether 0.571 is a good precision but what a map of that precision supports—the fitness-for-use question raised in §1.1, for which quality depends on both the data and the task (Devillers et al., 2007).

It supports **screening for candidate parking locations**. Generally high recall means that most labelled parking is detected, but low precision means that returned locations require checking before site-level use.

It supports **area estimation after local validation**, at a stated grain. Across 200 random half splits, the central 90% of held-out errors runs from −6.6% to +7.8%; at 1 km², only 63% fall within ±25%. The evidence therefore supports totals over comparable sub-areas within the city, not individual grid-cell values. Evidence between those scales is thinner: five held-out distance bands show errors from −20% to +13%.

For area calibration, *p/r* reduces to labelled area divided by predicted area. Testing the approach in a second city would therefore require labelled total area over sampled cells, not a full object-level error analysis—although transfer between cities remains untested. The map does **not** support uncorrected area measurement or site-level judgement: its raw area is 1.50 times the labelled total, and part of the apparent excess reflects the annotation definition rather than model error.

## 5.3 What the error decomposition adds

Three methodological observations follow, each from a single case.

First, equal IoU need not imply equal fitness for use. Cross-city benchmarks conventionally report per-city IoU (Maggiori et al., 2017), but that scalar conceals whether error comes from complete omission or imperfect boundaries. Here, complete-lot detection was comparatively robust and boundary placement contributed more error; the opposite profile at the same IoU would support different tasks. The distinction can be recovered from the spatial reference already required for segmentation validation.

Second, one accuracy figure can combine problems needing different remedies. Domain differences are candidates for adaptation (Lyu et al., 2025; Hong et al., 2023), whereas the 34.9% of unexplained over-prediction assigned to on-street parking and private driveways reflects the annotation scope. Reporting measured and effective precision separately prevents that definitional disagreement from being mistaken for model incapacity.

Third, area correction also has a spatial grain. Olofsson et al. (2014) show how reference data can adjust mapped area and quantify sampling uncertainty; the hold-out design here asks how far a locally fitted factor carries. It transferred across comparable sub-areas within Leeds but became unstable at 1 km². The result is case-specific, but the test is reusable.

## 5.4 Implications for UK parking evidence and densification

Bates and Leibling (2012) identify the absence of basic parking information as an obstacle to coherent British policy. Existing inventory routes do not transfer easily: American studies depend on cadastral records and codified parking requirements unavailable nationally in comparable UK form (Scharnhorst, 2018; Hoehne et al., 2019), while the British ground-survey approach has not been repeated at scale since the 1999 London exercise. Imagery offers a third route. It also measures area directly, unlike space counts that require assumptions about layout and aisle provision before they can answer a land-use question.

Where that area lies matters. The highest parking shares occur within 2 km of the centre, overlapping the inner band that Centre for Cities identifies as important to Britain's density gap (Lange, Kovacevic and Johnson, 2026). This is a spatial coincidence, not evidence that parking causes the deficit. The narrower conclusion is that the band where the density deficit is concentrated is not short of surface parking.

Concentration also qualifies Shoup's (2005) aggregate opportunity-cost argument. A citywide share of 3.26% does not reveal whether parking is diffuse or concentrated; here the median cell holds 1.71%, while six exceed 10%. For policy seeking under-utilised land (MHCLG, 2024, para. 125(d)), identifying concentrations at supported aggregate scales is more useful than the headline share alone.

The OpenStreetMap comparison adds a smaller result to the VGI quality literature. OSM completeness is known to vary by place and feature type (Haklay, 2010; Sehra, Singh and Rai, 2013; Zhou, Wang and Liu, 2022); here, 63.5% of labelled parking is absent. Similar median polygon areas suggest that incompleteness is not explained simply by object size, but cannot establish the shape of the full size distribution. Separately, the sampled OSM polygons showing no parking in the model-input imagery were recently edited. Subject to the fact that timestamps record any edit rather than construction, this disagreement sample is not dominated by untouched legacy records.

## 5.5 Limitations and future work

**One city.** Hold-outs test transfer within Leeds, not between cities. Because the calibration factor is an area ratio, a multi-city test needs labelled totals over sampled cells rather than a repeat of the full object-level analysis, but that test has not yet been made.

**A single annotator.** Detection is lower for low-confidence than high-confidence labels (0.713 against 0.856, Table 4.4), indicating where visual or definitional ambiguity is concentrated. It cannot quantify annotation error or an accuracy ceiling without independent labels. Multiple annotators and an agreement measure are required (Foody, 2002).

**Two imagery sources.** Labels were drawn over a satellite basemap, while predictions used Digimap tiles. The unresolved whole-lot residual is 2.1% of labelled area and sampled adjudication gives a 1.0% reference-side correction (§3.8). The spatial diagnostic finds no large common displacement, but none of these checks eliminates source disagreement; labelling on the model-input imagery would.

**Conventions shape the figures.** The 5 m boundary band is not a natural break, so 2 m and 10 m are also reported. The sampling frame excludes fragments below 100 m² and covers 0.3883 km² of a 0.4396 km² residual. Reference-layer attribution is positional: a false positive on industrial land has not necessarily been verified as a storage yard.

**The target definition matters.** On-street parking and private driveways form 34.9% of unexplained over-prediction. They are real parking excluded by rule, so another defensible protocol would produce a different precision from the same map. Appendix A therefore reports the scope in full.

The typology suggests one training-data hypothesis: include more irregularly arranged car parks rather than simply more unmarked ones. With only eleven supporting chips, this is a direction to test, not a settled prescription.

Appendix C tests whether positional error categories can also guide training. Generic Leeds fine-tuning raises raw-pixel IoU from 0.485 to 0.614, trading recall for precision; targeted loss weighting adds no advantage that validation-selected thresholding of the generic model cannot match or exceed. The categories are therefore useful explanations but not, in this experiment, useful supervision. This single-split, one-seed result does not test visually targeted irregular layouts or transfer to another city. Its raw-pixel figures on 50 held-out cells are also not comparable with the post-processed results of Chapter 4.
