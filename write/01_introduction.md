# 1. Introduction

> **草稿 v1**｜目标 1,000 词
> §1.4 伦理按 CASA 惯例置于引言（Slater 1.4、Ker、Campbell 均如此）；若你更想放进方法章，整节可平移
> 待办：引用格式统一

---

## 1.1 Context and motivation

Surface parking is one of the few urban land uses that almost every city has in quantity and almost no city has counted. It is usually treated as a transport question — how many spaces, priced how, used when — but its more consequential character is spatial. A minimum parking requirement is a rule about how much land a building must set aside, so the cumulative effect of decades of such rules is a pattern of land use, one that generates little activity and no housing, and that no agency has ever been responsible for inventorying (Shoup, 2005).

In England that omission has become awkward. The National Planning Policy Framework asks planning authorities to bring forward under-utilised land, and names car parks explicitly among its examples (MHCLG, 2024, para. 125(d)). The instruction presupposes an answer to a question nobody has answered: where are they, and how much land do they hold? The densification literature runs into the same wall. Britain's largest cities are found to carry substantial density gaps relative to their European peers, driven in part by the neighbourhoods lying just beyond the city centre (Lange, Kovacevic and Johnson, 2026), yet no consistent measurement exists of how much of that inner land is currently held as car park.

The gap is not for want of trying. It reflects how parking has been measured where it has been measured at all. American inventories are the fullest available, but they are built from cadastral records and codified parking requirements that the UK does not hold in comparable form (Scharnhorst, 2018; Hoehne et al., 2019). British measurement has been local and survey-based — most substantially a sample of on-the-ground inspections in London — and counts *spaces* rather than land area. The authors of the most substantial recent UK review conclude bluntly that little information is collected about how much parking exists at all (Bates and Leibling, 2012).

Segmentation of aerial imagery offers a way past both obstacles, because it depends on no institutional record and no fieldwork. A model trained specifically for parking has been published and can be run on any imagery a user holds (Qiam, Devunuri and Lehe, 2025). That is an attractive proposition for a planner in a British city, and it is the proposition this dissertation tests.

The risk is that models transfer badly. A network trained on one country's imagery and urban form may perform quite differently on another's, a problem sufficiently recognised that benchmarks exist to measure it (Maggiori et al., 2017; Lyu et al., 2025). Nor does the architecture's own robustness claim settle the matter: SegFormer's reported zero-shot robustness is demonstrated against corrupted images of familiar cities, which is close to the opposite of the situation here (Xie et al., 2021). Before a transferred map is used as evidence about land, someone has to establish what it can be used for.

That last phrase names an established question rather than a new one. Spatial data quality is conventionally divided into *internal* quality, meaning how far a dataset matches the ground, and *external* quality or **fitness for use**, meaning whether it is adequate for a particular purpose — a distinction that exists because the same dataset can be sufficient for one task and useless for another, so quality cannot be settled independently of the use (Devillers et al., 2007). This dissertation is a fitness-for-use assessment of a transferred model, and its contribution is to make that assessment quantitative: not whether the map is good, but which uses its measured error still permits.

## 1.2 Research questions

| | |
|---|---|
| **RQ1** | How accurate is a US-trained surface-parking segmentation model on UK aerial imagery, and does that accuracy vary systematically within the city? |
| **RQ2** | What systematic errors does it make, and how much of that error is removed — or created — by post-processing? |
| **RQ3** | Under the measured reliability, how much central-city land is surface parking, and where is it concentrated? |

The three are sequential rather than parallel. RQ1 establishes whether the transfer works at all. RQ2 explains why the accuracy figures look as they do, which determines what they mean. Only under the reliability those two establish does RQ3 become answerable.

## 1.3 Scope

The study covers 100 km² of Leeds, validated against 2,037 manually labelled car parks. That it examines one city in depth rather than several in outline is a design decision, not a shortfall. Comparing cities presupposes that the model's output is trustworthy, and that had never been established in the UK; spending the available effort on a labelled reference, a per-cell validation and a sampled error typology establishes what the map supports before anything is built on it. Multi-city extension then becomes future work with a defined precondition, which §5.5 specifies.

Three boundaries define the primary analysis. The target is off-street surface parking as the source model defines it, so on-street parking and enclosed structures are outside it by rule. The model is used exactly as released, with no UK training data, because what is being measured is what an off-the-shelf user would obtain; a bounded supplementary experiment departs from this second boundary alone and is reported separately in Appendix C. And the study identifies where parking is and how much land it occupies; it does not judge whether any site should be redeveloped, a question requiring ownership, access, demand and viability information that none of the data used here contains.

## 1.4 Ethical considerations

All data are secondary and either openly licensed or licensed to the institution, and no human participants are involved. Two points warrant reflection nonetheless. The labelling was carried out by a single annotator, so the reference embodies one person's judgement on a target whose boundaries are genuinely ambiguous; §4.3 quantifies the effect this has on measurable accuracy rather than leaving it as a caveat. Second, an output identifying low-intensity urban land could be read as a development prospectus. The scope statement above is a substantive commitment, not a formality: no site-level claim is made anywhere in what follows.

## 1.5 Structure of the dissertation

Chapter 2 brings together four literatures — parking as urban land, the evidence on its extent, segmentation of aerial imagery, and the limits of volunteered reference data — and states the gap where they meet. Chapter 3 sets out the annotation protocol, the pipeline, the accuracy measures, the two-track error typology, the ablation design and the checks on imagery consistency and on the calibration estimator. Chapter 4 reports the measured accuracy, decomposes the error, tests the post-processing stage, shows the apparent location effect to be confounded, and gives the extent and distribution of surface parking. Chapter 5 answers the three research questions, states what the transferred map does and does not support, and sets out the limitations. Chapter 6 concludes.
