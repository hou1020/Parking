# 2. Background

> **草稿 v3**｜引用 19 条
> v3：§2.3、§2.5 精简为与本研究直接相关的内容；借来的 IoU 数字移交 §5.1（比较在那里才真正发生）；§2.2 的借用数字减半
> 引用均已对照 `resource/` 下原文核过。Qiam, Devunuri and Lehe (2025) 原文已找到（`Parking/literature/A_Pipeline_and_NIR-Enhanced_Dataset_for_Parking_Lot_Segmentation.pdf`），§2.4 与 §2.5 原标 ⚠️ 的三处已逐条核实：车道规则改为原文的「逐例判断 + 只纳入极短车道」；NIR 与 OSM 地块边界两说法原文支持，措辞未动。§2.4 对 checkpoint 的著录口径改为「取自模型卡与仓库」，不引用任何已发表准确率数字。
> 待办：引用格式统一

---

This chapter brings together four literatures that rarely meet. Section 2.1 sets out why the land occupied by surface parking is worth measuring, and why UK policy has recently made that question sharper. Section 2.2 reviews what is actually known about parking extent, and shows that the evidence base and the methods behind it are predominantly American. Sections 2.3 and 2.4 turn to the method that could close that gap — semantic segmentation of aerial imagery, and the specific model used here. Section 2.5 asks what could go wrong when such a model crosses a national boundary, and converts that question into a set of expectations the results chapter can test. Section 2.6 explains why the obvious alternative reference, OpenStreetMap, cannot serve as ground truth. Section 2.7 states the gap.

---

## 2.1 Parking as urban land

The case for treating parking as a land-use question rather than a transport one was made most forcefully by Shoup (2005). Minimum parking requirements, he argues, operate as a hidden subsidy: by obliging developers to supply parking regardless of demand, they raise development costs, encourage driving, and commit land to a use that generates little activity and no housing. The argument's force is spatial. A parking requirement is a rule about how much land a building must set aside, so its cumulative effect is a pattern of land use — and one that is rarely inventoried, because no agency is responsible for counting it.

That framing has become directly relevant to English planning policy. The National Planning Policy Framework instructs authorities to make "as much use as possible of previously-developed or 'brownfield' land" (MHCLG, 2024, para. 124) and to give substantial weight to brownfield development within settlements. More pointedly for this study, paragraph 125(d) asks authorities to

> promote and support the development of under-utilised land and buildings, especially if this would help to meet identified needs for housing where land supply is constrained and available sites could be used more effectively (for example converting space above shops, and building on or above service yards, **car parks**, lock-ups and railway infrastructure).

Car parks are thus named in national policy as an example of under-utilised land. The policy instruction presupposes a spatial answer to a question nobody has answered: where are they, and how much land do they hold?

The same gap appears in the densification literature. Centre for Cities research finds that Britain's largest cities — Manchester, Birmingham, Liverpool, Leeds and Glasgow — carry the largest density gaps relative to their European peers, and that the gap is driven substantially by post-war neighbourhoods "located just beyond the city centre", which can be up to 40 per cent less dense than similarly located pre-war neighbourhoods (Lange, Kovacevic and Johnson, 2026). Livingstone, Fiorentino and Short (2021) examine how densification policy plays out in practice in London and at what cost, while Habermehl and McFarlane (2025) argue that density is better understood as a contested dialectic between "hard" and "gentle" forms than as a single quantity to be maximised. What none of this work can draw on is a consistent measurement of how much land inside British cities is currently held as surface parking. The policy asks for under-utilised land to be found; the evidence base cannot yet say how much of it is car park.

## 2.2 What is known about parking extent, and where that knowledge comes from

Systematic parking inventories exist, but they are overwhelmingly American, and they were built by methods that do not port straightforwardly to the UK. The British evidence that does exist measures something different, in one atypical city, by means too expensive to repeat.

Scharnhorst (2018) compiled comprehensive inventories for five US cities — New York, Philadelphia, Seattle, Des Moines and Jackson, Wyoming — combining satellite imagery with tax and cadastral records. The results are striking both for supply and for its use: reviewing occupancy studies across the five cities, he reports empty stalls making up 68 per cent of supply in Jackson's residential core. Hoehne et al. (2019) take a different route for metropolitan Phoenix, cross-referencing cadastral and roadway data against minimum parking requirements to estimate 12.2 million parking spaces in 2017, against 2.86 million registered vehicles.

The British evidence is thinner, and its own authors say so. The most substantial recent review of UK parking policy, Bates and Leibling's (2012) study for the RAC Foundation, concludes that a central obstacle to coherent policy is simply the absence of data: their study, they write, shows "how little information is collected about the quantity of parking space" that exists (p. 99), a problem they attribute to fragmented responsibility and to local authorities lacking the resources to audit their own parking supply. Where UK measurement has been attempted it has been local and survey-based. The fullest example remains a study commissioned for London, in which parking availability was estimated by inspecting a sample of three hundred 500 m squares on the ground, later partially resurveyed; it put the capital's supply at roughly 6.8 million spaces, counted as spaces (Bates and Leibling, 2012).

Three limitations of that evidence base define the opening this study works in. It counts **spaces rather than land area**, which cannot answer a question about how much ground a city gives over to parking. It is **concentrated on London**, which is atypical of British cities in density, land value and parking regulation alike. And it rests on **ground survey**, which is expensive enough that the exercise has not been repeated at scale or extended to other cities. No comparable measurement of off-street surface parking *area* appears to exist for a British city outside London.

Two further things follow for the present study. The first is substantive: where parking has been counted, it has consistently been found in quantities far exceeding observed use, which is what makes its land take a live question rather than an accounting curiosity. The second is methodological, and is the more important here. The American studies depend on institutional data that either does not exist in comparable form in the UK or does not carry the same information: Hoehne et al.'s method requires codified minimum parking requirements attached to parcels, and Scharnhorst's requires cadastral records that identify parking as a use. Neither is available as a national UK dataset, and the British alternative — sending surveyors out to look — is precisely what has proved too costly to repeat. An approach that reads parking directly from imagery, and therefore depends on no institutional record and no fieldwork, is attractive because it sidesteps both.

A related strand of work provides the spatial framing rather than the counts. Jiao (2015) shows that urban land density follows regular, describable functions of distance from the centre, which supplies a natural way to organise a within-city analysis: not "how much parking is there" alone, but how its share of land changes across the urban gradient.

## 2.3 Segmenting parking from aerial imagery

Semantic segmentation of remote-sensing imagery is now dominated by deep encoder–decoder architectures (Lv et al., 2023). The model used here is built on SegFormer (Xie et al., 2021), whose relevant property for aerial work is that it dispenses with positional encoding, leaving it comparatively indifferent to the tile size it is given — useful because aerial imagery is processed as arbitrary tiles rather than at a canonical size.

Its authors also report strong zero-shot robustness, demonstrated on Cityscapes-C, a benchmark that degrades image quality with noise, blur, weather and digital artefacts while leaving the scene unchanged. That is a different test from the one run here. A corrupted image of a familiar city and a clean image of an unfamiliar one stress different capacities, so the reported robustness does not by itself settle whether the model transfers geographically. Chapter 5 returns to the point once the error has been decomposed and it can be said which capacity the crossing taxed.

Parking is an attractive segmentation target because it is visually distinctive: a paved surface, usually with painted bays, usually with vehicles on it. It is also a target whose boundary is genuinely ambiguous — where a car park ends and its access road, service yard or forecourt begins is a matter of definition rather than observation. That ambiguity is not incidental here. It accounts for a substantial share of the apparent error measured in Chapter 4, and separating it from genuine misrecognition is one of this study's main analytical tasks.

Two studies take parking specifically as the segmentation target. Berry et al. (2019) address a direct consequence of that ambiguity — adjacent car parks merge into one another under ordinary semantic segmentation — by segmenting instances through associative embeddings rather than classifying pixels. Hurst-Tarrab et al. (2020) assemble APKLOT, a purpose-built dataset of parking-block polygons cut from satellite imagery, and report the accuracy their models reach on it — the closest published point of comparison for a parking segmentation result, obtained with training and test data drawn from the same source, and taken up in §5.1. Neither study asks what the resulting map is fit for; accuracy is the endpoint.

## 2.4 The model used here and its annotation definition

The model applied in this study is the parking-lot segmentation network released by Qiam, Devunuri and Lehe (2025), who introduce both a pipeline and an NIR-enhanced training dataset for the task. The released checkpoint is a SegFormer-B5 configuration whose backbone was initialised from Cityscapes weights and fine-tuned on their parking dataset, as documented in the released model card and repository. No published accuracy figure is carried over to describe it. It is used here exactly as released, with no UK training data.

What matters as much as the architecture is the *definition* the model was trained on, because that definition determines what a correct output looks like. Qiam, Devunuri and Lehe's target is off-street surface parking visible from above: marked bays and the aisles that connect them, including rooftop parking where the surface is visible — their dataset admits a parking structure only where the deck on top of it is visible — and excluding on-street parking and enclosed structures. Access driveways were not excluded by rule but left to case-by-case judgement, with annotators encouraged to take in only very short ones, expressly so that the model would not learn to recognise roads in general. Boundaries were drawn to the edge of the paving rather than to the parcel line, on the reasoning that only the paved edge offers a visual cue the model can learn; the authors note that OpenStreetMap parking polygons instead follow the parcel. They also note that NIR information assists in separating parking surfaces from adjacent vegetation.

Two consequences run through this dissertation. First, any reference dataset used to assess the model must follow the same definition, or the resulting accuracy figures measure disagreement about categories rather than model performance; the annotation protocol in Chapter 3 is therefore derived from theirs. Second, the imagery available for this study is three-band RGB with no NIR channel — a limitation returned to below.

## 2.5 Domain shift: what could go wrong across a national boundary

A model trained in one geographical setting frequently performs worse in another — domain shift, surveyed by Lyu et al. (2025) — with sources conventionally divided into sensor and resolution differences, illumination differences, and differences in the objects themselves. The problem is recognised enough that benchmarks exist to measure it. Maggiori et al. (2017) built the Inria Aerial Image Labeling benchmark so that testing is carried out over entirely different cities rather than over held-out parts of the training area, and judged the accuracy their network reached on those unseen cities to represent satisfactory generalisation. Hong et al. (2023) approach the same problem from the other side, arguing that models succeeding within a single city meet a bottleneck across cities and regions.

Two things about that work bear directly on this study. Maggiori et al. operate at 0.3 m with RGB bands and two classes, against 0.25 m RGB and two classes here, so their accuracy levels are a reasonable frame of reference for Chapter 4 rather than an arbitrary comparison. But those benchmarks test transfer between cities within a broadly shared building stock, whereas the transfer examined here also crosses a national boundary, an imagery programme and a different tradition of laying out car parks.

Most of that literature is concerned with *correcting* domain shift through adaptation. That option is not open to the user this study has in mind. Adaptation presupposes either labelled data in the target domain or substantial engineering to exploit unlabelled data, and a planner who wants to know how much land in their city is car park has neither; their realistic option is to run the published checkpoint on the imagery they hold. The uncorrected output is therefore the object of study here, and the question is what it can still be trusted to do.

Stating that a model was trained in the US and applied in the UK is not on its own an analysis. Table 2.1 names the specific differences that plausibly matter for this target, and states each as an expectation the results can confirm or refute.

**Table 2.1** Expected sources of transfer error, and the observable failure each would produce.

| Difference between the training and application settings | Expected failure |
|---|---|
| British off-street car parks are typically smaller and more irregularly shaped than American ones — a prior of this study, drawn from the labelling rather than from a source, and tested rather than assumed | Failures concentrated in small lots and awkward site geometry |
| Unmarked parking is more common; the annotation rules accept vehicles plus layout as sufficient evidence | Missed lots lacking painted bay markings |
| Setts, block paving and gravel are common surfacing materials | Missed lots whose surface is not asphalt |
| Leeds lies at 53.8 °N, well north of the US cities in the training data (mostly 30–42 °N), so solar elevation is lower and shadows longer; street tree canopy is also denser | Missed or fragmented lots under shadow and canopy occlusion |
| Commercial vehicle and van share differs | Failures on lots occupied by vans and lorries rather than cars |
| The imagery used here is RGB only, with no NIR band | Vegetated ground and grass margins confused with paved parking |

Each expectation implies a category in the error typology of Chapter 3 and is tested against sampled evidence in Chapter 4. Setting them out in advance also allows them to be wrong: one is substantially revised by the results, which is more informative than a set of predictions that all survive.

## 2.6 Why OpenStreetMap cannot serve as ground truth

The obvious way to avoid manual labelling would be to validate the model against OpenStreetMap's `amenity=parking` features. OSM is the best-known instance of what Goodchild (2007) named volunteered geographic information: geographic data contributed by non-specialists outside any formal quality-control regime. The quality literature that framing prompted makes clear why the shortcut does not work.

Haklay's (2010) comparison of OSM against Ordnance Survey data — the foundational UK study — found positional accuracy to be reasonable where coverage exists, but completeness to vary sharply between places, being far better in areas with more contributors. Later reviews confirm the pattern: OSM is more complete in urban than rural areas, and more complete for common feature types than for rarer ones (Sehra, Singh and Rai, 2013). Zhou, Wang and Liu (2022) look specifically at land-cover and land-use tagging and find accuracy and completeness varying substantially by category, which matters directly here because parking is recorded as a land-use-like polygon rather than as part of the road network that attracts the most contributor attention.

There is also a definitional problem independent of completeness. As Qiam, Devunuri and Lehe observe, OSM parking polygons are frequently drawn to parcel boundaries rather than to the edge of the paved surface, so even a perfectly complete OSM layer would disagree with an imagery-derived one at the margins.

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
