# 2. Background

> **草稿 v2**｜正文 3,095 词（含表 3,258）｜引用 18 条
> v2 补入五条新文献：Bates & Leibling (2012)、Maggiori et al. (2017)、Hong et al. (2023)、Berry et al. (2019)、Hurst-Tarrab et al. (2020)
> 引用均已对照 `resource/` 下原文核过，唯 **Qiam et al. (2025) 无 PDF**，§2.4 与 §2.5 中标 ⚠️ 的具体说法需最后对论文原文复核一次
> ⚠️ **超预算 595 词**（目标 2,500）。可裁处见文末批注
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

Systematic parking inventories exist, but they are overwhelmingly American, and they were built by methods that do not port straightforwardly to the UK. The British evidence that does exist measures something different, in one atypical city, by means too expensive to repeat.

Scharnhorst (2018) compiled comprehensive inventories for five US cities — New York, Philadelphia, Seattle, Des Moines and Jackson, Wyoming — combining satellite imagery with tax and cadastral records. The results are striking both for supply and for its use: reviewing occupancy studies across the five cities, he reports empty stalls making up 68 per cent of supply in Jackson's residential core and 61 per cent in its midtown area, and 92 per cent of spaces empty in a major public facility in Des Moines. Downtown Philadelphia carries more than 100 parking spaces per acre. Hoehne et al. (2019) take a different route for metropolitan Phoenix, cross-referencing cadastral and roadway data against minimum parking requirements to estimate 12.2 million parking spaces in 2017 — against 4.04 million inhabitants, 2.86 million registered personal vehicles and 1.84 million jobs — with 10.9 million of those spaces added since 1960.

The British evidence is thinner, and its own authors say so. The most substantial recent review of UK parking policy, Bates and Leibling's (2012) study for the RAC Foundation, concludes that a central obstacle to coherent policy is simply the absence of data: their study, they write, shows "how little information is collected about the quantity of parking space" that exists (p. 99), a problem they attribute to fragmented responsibility and to local authorities lacking the resources to audit their own parking supply. Where UK measurement has been attempted it has been local and survey-based. The fullest example remains a study commissioned for London, in which parking availability was estimated by inspecting a sample of three hundred 500 m squares on the ground, later partially resurveyed; it put the capital's supply at roughly 6.8 million spaces, of which some 1.8 million were private driveways and garages and 2.4 million were unrestricted on-street (Bates and Leibling, 2012).

Three limitations of that evidence base define the opening this study works in. It counts **spaces rather than land area**, which cannot answer a question about how much ground a city gives over to parking. It is **concentrated on London**, which is atypical of British cities in density, land value and parking regulation alike. And it rests on **ground survey**, which is expensive enough that the exercise has not been repeated at scale or extended to other cities. No comparable measurement of off-street surface parking *area* appears to exist for a British city outside London.

Two further things follow for the present study. The first is substantive: where parking has been counted, it has consistently been found in quantities far exceeding observed use, which is what makes its land take a live question rather than an accounting curiosity. The second is methodological, and is the more important here. The American studies depend on institutional data that either does not exist in comparable form in the UK or does not carry the same information: Hoehne et al.'s method requires codified minimum parking requirements attached to parcels, and Scharnhorst's requires cadastral records that identify parking as a use. Neither is available as a national UK dataset, and the British alternative — sending surveyors out to look — is precisely what has proved too costly to repeat. An approach that reads parking directly from imagery, and therefore depends on no institutional record and no fieldwork, is attractive because it sidesteps both.

A related strand of work provides the spatial framing rather than the counts. Jiao (2015) shows that urban land density follows regular, describable functions of distance from the centre, which supplies a natural way to organise a within-city analysis: not "how much parking is there" alone, but how its share of land changes across the urban gradient.

## 2.3 Segmenting parking from aerial imagery

Deep learning is now the standard approach to semantic segmentation of remote-sensing imagery, and the field has consolidated around encoder–decoder architectures that trade accuracy against computational cost (Lv et al., 2023). Among these, SegFormer (Xie et al., 2021) pairs a hierarchical Transformer encoder — released as a family, MiT-B0 to MiT-B5, sharing an architecture but differing in size — with a deliberately lightweight all-MLP decoder. Its most relevant design choice for aerial work is the absence of positional encoding. Fixed positional codes must be interpolated when the test resolution differs from the training resolution, which costs accuracy; dispensing with them makes the model comparatively indifferent to the size of the tile it is given. Aerial imagery arrives as arbitrary tiles rather than at a canonical size, so this matters in practice.

The authors also report "excellent zero-shot robustness", demonstrated on Cityscapes-C, a benchmark that perturbs the imagery with noise, blur, weather and digital corruptions. **It is worth being precise about what that claim does and does not cover.** Cityscapes-C degrades the *pixels* while holding the scene constant: the same German streets, photographed badly. Geographic transfer is close to the inverse — the imaging conditions may be perfectly good, while the objects themselves, their size, their surfacing and their arrangement, are different. Robustness to a corrupted image of a familiar city is not evidence of robustness to a clean image of an unfamiliar one. The architectural robustness reported in the source paper therefore does not settle the question this dissertation asks, and it is one reason why the transfer needs to be measured rather than assumed.

Applying such a model to parking is attractive because parking is, visually, a comparatively well-defined target: a paved surface, usually with painted bays, usually with vehicles on it, usually adjacent to a building or road. It is also a target whose boundary is genuinely ambiguous — where a car park ends and its access road, service yard or forecourt begins is a matter of definition rather than of observation. That ambiguity is not incidental to what follows: it turns out to account for a substantial share of the apparent error measured in Chapter 4, and separating it from genuine misrecognition is one of the main analytical tasks of this study.

A small body of work has taken parking specifically as the segmentation target, and it is worth noting both what it has achieved and how it has been evaluated. Berry et al. (2019) address a problem that follows directly from the boundary ambiguity above: adjacent car parks merge into one another under ordinary semantic segmentation, so they segment *instances* using associative embeddings, deliberately choosing a method independent of object classification and tolerant of missing labels. Hurst-Tarrab et al. (2020) assemble APKLOT, a set of roughly 7,000 parking-block polygons across 500 labelled satellite images, and report that all their models exceed 50% IoU on the satellite view. That figure is a useful marker: it indicates the order of accuracy this task supports even when training and test data are drawn from the same source, and it is one of the few published points of comparison for a parking segmentation result. What this literature does not do is ask what a resulting map is fit for. Accuracy is reported as an endpoint rather than as a property that determines which downstream uses survive.

## 2.4 The model used here and its annotation definition

The model applied in this study is the parking-lot segmentation network released by Qiam et al. (2025), who introduce both a pipeline and an NIR-enhanced training dataset for the task. The released checkpoint is a SegFormer-B5 configuration whose backbone was initialised from Cityscapes weights and fine-tuned on their parking dataset. It is used here exactly as released, with no UK training data.

What matters as much as the architecture is the *definition* the model was trained on, because that definition determines what a correct output looks like. Qiam et al.'s target is off-street surface parking visible from above: marked bays and the aisles that connect them, including rooftop parking where the surface is visible, and excluding on-street parking and enclosed structures. ⚠️ They deliberately exclude longer access driveways from the labels so that the model does not learn to recognise roads. ⚠️ They also note that NIR information assists in separating parking surfaces from adjacent vegetation, and that OpenStreetMap parking polygons tend to follow parcel boundaries rather than the edge of the paving.

Two consequences run through this dissertation. First, any reference dataset used to assess the model must follow the same definition, or the resulting accuracy figures measure disagreement about categories rather than model performance; the annotation protocol in Chapter 3 is therefore derived from theirs. Second, the imagery available for this study is three-band RGB with no NIR channel, so one of the input signals the model's authors identify as useful is simply absent — a difference returned to below.

## 2.5 Domain shift: what could go wrong across a national boundary

A model trained in one geographical setting frequently performs worse in another, a problem framed in the remote-sensing literature as domain shift and surveyed comprehensively by Lyu et al. (2025). The sources are usually decomposed into sensor and resolution differences, atmospheric and illumination differences, and differences in the appearance and arrangement of the objects themselves. It is a sufficiently recognised problem that benchmarks have been built specifically to measure it. Maggiori et al. (2017) constructed the Inria Aerial Image Labeling benchmark from 810 km² of 0.3 m RGB imagery over ten cities in North America and Europe, splitting it so that testing is performed, in their words, over entirely different cities rather than over held-out parts of the training area. Their reported figure is worth carrying forward: a network reaching about 60% IoU for building footprints across unseen cities was judged to generalise satisfactorily. Hong et al. (2023) make the same point from the other direction, arguing that models succeeding within a single city meet a performance bottleneck across cities and regions, and building the C2Seg benchmark across Berlin–Augsburg and Beijing–Wuhan to study it.

Two features of this literature matter for what follows. The benchmarks are closely comparable to the present setting — Maggiori et al. work at 0.3 m with RGB bands and two classes, against 0.25 m RGB and two classes here — which means their accuracy levels provide a reasonable frame of reference for the figures reported in Chapter 4. But they also test transfer between cities within a broadly shared building stock, whereas the transfer examined here crosses a national boundary, an imagery programme, and a different tradition of laying out car parks.

Most of that literature is concerned with *correcting* domain shift through adaptation methods. That framing is not available to the user this study has in mind. Adaptation presupposes either labelled data in the target domain or a substantial engineering effort to exploit unlabelled data; a planner or analyst who wants to know how much land in their city is car park has neither, and their realistic option is to run the published checkpoint on the imagery they hold. The relevant question for them is not how the shift could be corrected but what the uncorrected output can still be trusted to do. That question is under-served: accuracy metrics reported in transfer studies describe how far performance has fallen, but not which downstream uses survive the fall.

Stating "the model was trained in the US and applied in the UK" is not, on its own, an analysis. The useful move is to name the specific differences that plausibly matter for this target, and to state them as expectations that the results can confirm or refute. Table 2.1 sets these out.

**Table 2.1** Expected sources of transfer error, and the observable failure each would produce.

| Difference between the training and application settings | Expected failure |
|---|---|
| British off-street car parks are typically smaller and more irregularly shaped than American ones — a prior of this study, drawn from the labelling rather than from a source, and tested rather than assumed | Failures concentrated in small lots and awkward site geometry |
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

The four literatures leave a gap where they meet. Parking is argued to be under-used urban land, but the empirical evidence for how much land it occupies is overwhelmingly American and rests on institutional records the UK does not hold in comparable form; the British evidence counts spaces rather than area, covers London rather than the country, and its own authors identify the absence of data as the central problem. English planning policy now names car parks explicitly as under-utilised land to be brought forward, and the densification literature identifies exactly the kind of city — and the kind of inner ring — where that land would matter most, but neither can point to a measurement. Segmentation models can produce such a measurement at scale, and one trained specifically for parking is publicly available, but the parking segmentation literature reports accuracy as an endpoint, and the transfer literature is largely concerned with correcting domain shift rather than characterising the residual reliability of an uncorrected transfer. And the reference dataset that would let a UK user check the output for themselves is incomplete in ways that vary from place to place.

The gap this dissertation addresses is therefore not that nobody has mapped parking in Leeds. It is that a scalable method exists whose transferred output has never been tested in a way that establishes *what it can be used for*. Reporting a precision and a recall does not answer that question. Establishing which errors are boundary effects, which are systematic confusions, which are disagreements about definition, and which are artefacts of the processing pipeline — and then testing whether the residual bias is stable enough to be corrected, and at what spatial grain — does. That is the contribution attempted here.

---

> ## 批注：字数与可裁处
>
> 本章 3,095 词，超预算 595。方法章 2,964，超 464。两章合计超 1,059 词，若其余各章按计划，全篇约 12,059 —— **超出 CASA 上限 12,000**。需要在两章之间收回约 1,000 词。
>
> 本章建议裁的三处，按"裁掉损失最小"排序：
>
> | 处 | 约可裁 | 代价 |
> |---|---|---|
> | §2.2 伦敦 6.8 million 车位的分项明细 | 60 词 | 只留总数与"数车位不数面积"这一点，论证不受影响 |
> | §2.3 SegFormer 架构描述（MiT-B0–B5、位置编码） | 120 词 | 压成两句。zero-shot robustness 那段**不能动**，它是本章的关键转折 |
> | §2.5 第二段"两个特征"中的第一点 | 80 词 | 分辨率可比性可以并进前一句 |
> | §2.1 Livingstone 与 Habermehl 各一句 | 90 词 | 密度化文献是背景而非论证主干 |
>
> 合计约 350 词，其余从方法章收回。**§2.2 的英国证据段和 §2.5 的 Maggiori 基准段不建议裁**——前者是 gap 陈述的支柱，后者是第 4 章数字唯一的外部参照系。
