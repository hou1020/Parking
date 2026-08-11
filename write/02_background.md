# 2. Background

> **草稿 v1**｜正文约 2,530 词
> 引用均已对照 `resource/` 下原文核过，唯 **Qiam et al. (2025) 无 PDF**，§2.4 与 §2.5 中标 ⚠️ 的具体说法需最后对论文原文复核一次
> 待办：引用格式统一；`[Table 2.1]` 已排

---

This chapter brings together four literatures that rarely meet. Section 2.1 sets out why the land occupied by surface parking is worth measuring, and why UK policy has recently made that question sharper. Section 2.2 reviews what is actually known about parking extent, and shows that the evidence base and the methods behind it are predominantly American. Sections 2.3 and 2.4 turn to the method that could close that gap — semantic segmentation of aerial imagery, and the specific model used here. Section 2.5 asks what could go wrong when such a model crosses a national boundary, and converts that question into a set of expectations the results chapter can test. Section 2.6 explains why the obvious alternative reference, OpenStreetMap, cannot serve as ground truth. Section 2.7 states the gap.

---

## 2.1 Parking as urban land

The case for treating parking as a land-use question rather than a transport one was made most forcefully by Shoup (2005). Minimum parking requirements, he argues, operate as a hidden subsidy: by obliging developers to supply parking regardless of demand, they raise development costs, encourage driving, and commit land to a use that generates little activity and no housing. The argument's force is spatial. A parking requirement is a rule about how much land a building must set aside, so its cumulative effect is a pattern of land use — and one that is rarely inventoried, because no agency is responsible for counting it.

That framing has become directly relevant to English planning policy. The National Planning Policy Framework instructs authorities to make "as much use as possible of previously-developed or 'brownfield' land" (MHCLG, 2024, para. 124) and to give substantial weight to brownfield development within settlements. More pointedly for this study, paragraph 125(d) asks authorities to

> promote and support the development of under-utilised land and buildings, especially if this would help to meet identified needs for housing where land supply is constrained and available sites could be used more effectively (for example converting space above shops, and building on or above service yards, **car parks**, lock-ups and railway infrastructure).

Car parks are thus named in national policy as an example of under-utilised land. The policy instruction presupposes a spatial answer to a question nobody has answered: where are they, and how much land do they hold?

The same gap appears in the densification literature. Centre for Cities research finds that Britain's largest cities — Manchester, Birmingham, Liverpool, Leeds and Glasgow — carry the largest density gaps relative to their European peers, and that the gap is driven substantially by post-war neighbourhoods "located just beyond the city centre", which can be up to 40 per cent less dense than similarly located pre-war neighbourhoods (Lange et al., 2026). Livingstone et al. (2021) examine how densification policy plays out in practice in London and at what cost, while Habermehl and McFarlane (2025) argue that density is better understood as a contested dialectic between "hard" and "gentle" forms than as a single quantity to be maximised. What none of this work can draw on is a consistent measurement of how much land inside British cities is currently held as surface parking. The policy asks for under-utilised land to be found; the evidence base cannot yet say how much of it is car park.

## 2.2 What is known about parking extent, and where that knowledge comes from

Systematic parking inventories exist, but almost exclusively for American cities, and they were built by methods that do not port straightforwardly to the UK.

Scharnhorst (2018) compiled comprehensive inventories for five US cities — New York, Philadelphia, Seattle, Des Moines and Jackson, Wyoming — combining satellite imagery with tax and cadastral records. The results are striking both for supply and for its use: reviewing occupancy studies across the five cities, he reports empty stalls making up 68 per cent of supply in Jackson's residential core and 61 per cent in its midtown area, and 92 per cent of spaces empty in a major public facility in Des Moines. Downtown Philadelphia carries more than 100 parking spaces per acre. Hoehne et al. (2019) take a different route for metropolitan Phoenix, cross-referencing cadastral and roadway data against minimum parking requirements to estimate 12.2 million parking spaces in 2017 — against 4.04 million inhabitants, 2.86 million registered personal vehicles and 1.84 million jobs — with 10.9 million of those spaces added since 1960.

Two things follow for the present study. The first is substantive: where parking has been counted, it has consistently been found in quantities far exceeding observed use, which is what makes its land take a live question rather than an accounting curiosity. The second is methodological, and is the more important here. Both studies depend on institutional data that either does not exist in comparable form in the UK or does not carry the same information: Hoehne et al.'s method requires codified minimum parking requirements attached to parcels, and Scharnhorst's requires cadastral records that identify parking as a use. Neither is available as a national UK dataset. An approach that reads parking directly from imagery, and therefore depends on no institutional record at all, is attractive precisely because it sidesteps this.

A related strand of work provides the spatial framing rather than the counts. Jiao (2015) shows that urban land density follows regular, describable functions of distance from the centre, which supplies a natural way to organise a within-city analysis: not "how much parking is there" alone, but how its share of land changes across the urban gradient.

## 2.3 Segmenting parking from aerial imagery

Deep learning is now the standard approach to semantic segmentation of remote-sensing imagery, and the field has consolidated around encoder–decoder architectures that trade accuracy against computational cost (Lv et al., 2023). Among these, SegFormer (Xie et al., 2021) pairs a hierarchical Transformer encoder — released as a family, MiT-B0 to MiT-B5, sharing an architecture but differing in size — with a deliberately lightweight all-MLP decoder. Its most relevant design choice for aerial work is the absence of positional encoding. Fixed positional codes must be interpolated when the test resolution differs from the training resolution, which costs accuracy; dispensing with them makes the model comparatively indifferent to the size of the tile it is given. Aerial imagery arrives as arbitrary tiles rather than at a canonical size, so this matters in practice.

The authors also report "excellent zero-shot robustness", demonstrated on Cityscapes-C, a benchmark that perturbs the imagery with noise, blur, weather and digital corruptions. **It is worth being precise about what that claim does and does not cover.** Cityscapes-C degrades the *pixels* while holding the scene constant: the same German streets, photographed badly. Geographic transfer is close to the inverse — the imaging conditions may be perfectly good, while the objects themselves, their size, their surfacing and their arrangement, are different. Robustness to a corrupted image of a familiar city is not evidence of robustness to a clean image of an unfamiliar one. The architectural robustness reported in the source paper therefore does not settle the question this dissertation asks, and it is one reason why the transfer needs to be measured rather than assumed.

Applying such a model to parking is attractive because parking is, visually, a comparatively well-defined target: a paved surface, usually with painted bays, usually with vehicles on it, usually adjacent to a building or road. It is also a target whose boundary is genuinely ambiguous — where a car park ends and its access road, service yard or forecourt begins is a matter of definition rather than of observation. That ambiguity is not incidental to what follows: it turns out to account for a substantial share of the apparent error measured in Chapter 4, and separating it from genuine misrecognition is one of the main analytical tasks of this study.

## 2.4 The model used here and its annotation definition

The model applied in this study is the parking-lot segmentation network released by Qiam et al. (2025), who introduce both a pipeline and an NIR-enhanced training dataset for the task. The released checkpoint is a SegFormer-B5 configuration whose backbone was initialised from Cityscapes weights and fine-tuned on their parking dataset. It is used here exactly as released, with no UK training data.

What matters as much as the architecture is the *definition* the model was trained on, because that definition determines what a correct output looks like. Qiam et al.'s target is off-street surface parking visible from above: marked bays and the aisles that connect them, including rooftop parking where the surface is visible, and excluding on-street parking and enclosed structures. ⚠️ They deliberately exclude longer access driveways from the labels so that the model does not learn to recognise roads. ⚠️ They also note that NIR information assists in separating parking surfaces from adjacent vegetation, and that OpenStreetMap parking polygons tend to follow parcel boundaries rather than the edge of the paving.

Two consequences run through this dissertation. First, any reference dataset used to assess the model must follow the same definition, or the resulting accuracy figures measure disagreement about categories rather than model performance; the annotation protocol in Chapter 3 is therefore derived from theirs. Second, the imagery available for this study is three-band RGB with no NIR channel, so one of the input signals the model's authors identify as useful is simply absent — a difference returned to below.

## 2.5 Domain shift: what could go wrong across a national boundary

A model trained in one geographical setting frequently performs worse in another, a problem framed in the remote-sensing literature as domain shift and surveyed comprehensively by Lyu et al. (2025). The sources are usually decomposed into sensor and resolution differences, atmospheric and illumination differences, and differences in the appearance and arrangement of the objects themselves.

Most of that literature is concerned with *correcting* domain shift through adaptation methods. That framing is not available to the user this study has in mind. Adaptation presupposes either labelled data in the target domain or a substantial engineering effort to exploit unlabelled data; a planner or analyst who wants to know how much land in their city is car park has neither, and their realistic option is to run the published checkpoint on the imagery they hold. The relevant question for them is not how the shift could be corrected but what the uncorrected output can still be trusted to do. That question is under-served: accuracy metrics reported in transfer studies describe how far performance has fallen, but not which downstream uses survive the fall.

Stating "the model was trained in the US and applied in the UK" is not, on its own, an analysis. The useful move is to name the specific differences that plausibly matter for this target, and to state them as expectations that the results can confirm or refute. Table 2.1 sets these out.

**Table 2.1** Expected sources of transfer error, and the observable failure each would produce.

| Difference between the training and application settings | Expected failure |
|---|---|
| British off-street car parks are typically smaller and more irregularly shaped than American ones | Failures concentrated in small lots and awkward site geometry |
| Unmarked parking is more common; the annotation rules accept vehicles plus layout as sufficient evidence | Missed lots lacking painted bay markings |
| Setts, block paving and gravel are common surfacing materials | Missed lots whose surface is not asphalt |
| Leeds lies at 53.8 °N, well north of the US cities in the training data (mostly 30–42 °N), so solar elevation is lower and shadows longer; street tree canopy is also denser | Missed or fragmented lots under shadow and canopy occlusion |
| Commercial vehicle and van share differs | Failures on lots occupied by vans and lorries rather than cars |
| The available imagery is RGB only, with no NIR band ⚠️ | Vegetated ground and grass margins confused with paved parking |

Each expectation implies a category in the error typology of Chapter 3 and is tested against sampled evidence in Chapter 4. Setting them out in advance also means the analysis can be wrong: one of these expectations is substantially corrected by the results, which is more informative than a set of predictions that all survive.

The framing also clarifies what "transferability" means operationally. It is not a single number. A model may transfer well enough to locate a phenomenon while transferring poorly for measuring it, and those two properties support entirely different downstream uses. Establishing which of them holds is the purpose of this dissertation.

## 2.6 Why OpenStreetMap cannot serve as ground truth

The obvious way to avoid manual labelling would be to validate the model against OpenStreetMap's `amenity=parking` features. The OSM quality literature makes clear why this does not work.

Haklay's (2010) comparison of OSM against Ordnance Survey data — the foundational UK study — found positional accuracy to be reasonable where coverage exists, but completeness to vary sharply between places, being far better in areas with more contributors. Later reviews confirm the pattern: OSM is more complete in urban than rural areas, and more complete for common feature types than for rarer ones (Sehra et al., 2013). Zhou et al. (2022) look specifically at land-cover and land-use tagging and find accuracy and completeness varying substantially by category, which matters directly here because parking is recorded as a land-use-like polygon rather than as part of the road network that attracts the most contributor attention.

There is also a definitional problem independent of completeness. As Qiam et al. observe, OSM parking polygons are frequently drawn to parcel boundaries rather than to the edge of the paved surface, so even a perfectly complete OSM layer would disagree with an imagery-derived one at the margins.

OSM is therefore treated in this study in two distinct roles, kept strictly separate. Its building and road layers are *inputs* to the post-processing stage of the pipeline. Its parking, land-use and related layers are used only to *attribute* errors after the fact, never to decide what the map should contain. Independently, the manual reference built here allows OSM's parking completeness to be assessed rather than assumed — a secondary result reported in Chapter 4.

## 2.7 Research gap

The four literatures leave a gap where they meet. Parking is argued to be under-used urban land, but the empirical evidence for how much land it occupies is almost entirely American and rests on institutional records the UK does not hold in comparable form. English planning policy now names car parks explicitly as under-utilised land to be brought forward, and the densification literature identifies exactly the kind of city — and the kind of inner ring — where that land would matter most, but neither can point to a measurement. Segmentation models can produce such a measurement at scale, and one trained specifically for parking is publicly available, but the remote-sensing literature that would tell us whether it transfers is largely concerned with correcting domain shift rather than characterising the residual reliability of an uncorrected transfer. And the reference dataset that would let a UK user check the output for themselves is incomplete in ways that vary from place to place.

The gap this dissertation addresses is therefore not that nobody has mapped parking in Leeds. It is that a scalable method exists whose transferred output has never been tested in a way that establishes *what it can be used for*. Reporting a precision and a recall does not answer that question. Establishing which errors are boundary effects, which are systematic confusions, which are disagreements about definition, and which are artefacts of the processing pipeline — and then testing whether the residual bias is stable enough to be corrected, and at what spatial grain — does. That is the contribution attempted here.
