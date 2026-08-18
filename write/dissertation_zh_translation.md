# 论文全文英中对照译稿与逐段证据审读

> 本文件翻译自 `00_abstract.md` 至 `12_appendix_e_research_log.md` 的当前英文全文，供理解、校对论证与数据审计使用。英文原稿未作改动；引文作者、年份、表号、图号、数字、公式、路径与代码名均按原文保留。每个正文单元均按“英文原稿—中文翻译—段落审读”的顺序排列；审读分别标明逻辑用途、核对结论、引用文献中的对应原句、原始数据／文本依据和可加强之处。这里插入的英文论文正文用于英中对照，但引用论断的证据仍以文献原文核对索引为准。

> **段落审读**
> - **逻辑用途：** 说明译文范围与批注阅读方式
> - **核对状态：** ✅ 已核对：章节范围已与编号 00–12 的当前文件清单核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 译稿范围说明；无外部数据。
> - **可加强：** 英文正文再修改后，应同步标注译稿对应的提交版本或日期。

---

## 文献原文核对索引

下表只收录各文献中直接支撑正文论断的短原句；段落标注用证据编号回指本表。页码能由出版版确认时列页码，否则列摘要、章节或表格位置。英文论文正文仅用于定位译文，不作为引文证据。`🟨` 表示原文只能部分支持当前概括，`⚠️` 表示本地缺少可核原件。

| 证据 | 文献原句（短摘录） | 定位与核对说明 | 本地原文 |
|---|---|---|---|
| <a id="l01"></a>**L01** Bates and Leibling (2012) | “This study has shown how little information is collected about the quantity of parking space that is available” | p. 99；直接支持英国停车供给数据不足。 | [PDF](</Users/hou/Desktop/dissertation/resource/spaced_out-bates_leibling-jul12.pdf>) |
| <a id="l02"></a>**L02** Berry et al. (2019) | “differentiate adjacent parking areas from each other” | 论文方法说明；支持用实例分割拆分相邻停车区。 | [PDF](</Users/hou/Desktop/dissertation/resource/3347146.3359364.pdf>) |
| <a id="l03"></a>**L03** Cheng et al. (2021) | “Boundary IoU is significantly more sensitive than the standard Mask IoU measure to boundary errors for large objects” | 摘要；直接支持大目标边界敏感性。 | [PDF](</Users/hou/Desktop/dissertation/resource/Cheng_Boundary_IoU_Improving_Object-Centric_Image_Segmentation_Evaluation_CVPR_2021_paper.pdf>) |
| <a id="l04"></a>**L04** Cochran (1977) | “based on a separate ratio in each stratum” | 分层比率估计章节；支持各层分别构造比率。 | [PDF](</Users/hou/Desktop/dissertation/resource/Cochran_1977_Sampling Techniques.pdf>) |
| <a id="l05"></a>**L05** Csurka, Larlus and Perronnin (2013) | “the Trimap … focuses on the boundary regions” | 方法说明；支持边界带评价思路，但正文中的误差归因是本研究自己的扩展。 | [PDF](</Users/hou/Desktop/dissertation/resource/paper0032.pdf>) |
| <a id="l06"></a>**L06** Devillers et al. (2007) | “how data fit the user’s needs (i.e. external quality)” | 摘要／概念框架；直接支持 fitness for use。 | [PDF](</Users/hou/Desktop/dissertation/resource/Towards spatial data quality information analysis tools for experts assessing the fitness for use of spatial data.pdf>) |
| <a id="l07"></a>**L07** Foody (2002) | “A meaningful accuracy assessment clearly requires that the ground data are accurate.” | p. 192；直接支持参考数据质量限制可测准确率。 | [PDF](</Users/hou/Desktop/dissertation/resource/1-s2.0-S0034425701002954-main.pdf>) |
| <a id="l08"></a>**L08** Foody (2005) | “a useful accompaniment to the global estimate of accuracy” | 方法讨论；直接支持局部准确率应补充而非替代全局指标。 | [PDF](</Users/hou/Desktop/dissertation/resource/Local characterization of thematic classification accuracy through spatially constrained confusion matrices.pdf>) |
| <a id="l09"></a>**L09** Goodchild (2007) | “I term this volunteered geographic information (VGI)” | 正文概念提出处；直接支持 VGI 术语来源。 | [PDF](</Users/hou/Desktop/dissertation/resource/s10708-007-9111-y.pdf>) |
| <a id="l10"></a>**L10** Habermehl and McFarlane (2025) | “we identify the tensions and contradictions of current densification approaches” | 摘要；支持把密度提升理解为有争议的过程。 | [PDF](</Users/hou/Desktop/dissertation/resource/Int J Urban Regional Res - 2025 - Habermehl - THE DENSITY DIALECTIC  Between Hard and Gentle Densification in London.pdf>) |
| <a id="l11"></a>**L11** Haklay (2010) | “OSM information can be fairly accurate: on average within about 6 m” | 摘要；仅直接支持已有覆盖处的位置精度，完整度差异需结合正文结果。 | [PDF](</Users/hou/Desktop/dissertation/resource/haklay-2010-how-good-is-volunteered-geographical-information-a-comparative-study-of-openstreetmap-and-ordnance-survey.pdf>) |
| <a id="l12"></a>**L12** Hoehne et al. (2019) | “there were 12.2 million parking spaces … 2.86 million registered personal vehicles” | 摘要；数字对应 Phoenix 2017。 | [PDF](</Users/hou/Desktop/dissertation/resource/1-s2.0-S0264275118311636-main.pdf>) |
| <a id="l13"></a>**L13** Hong et al. (2023) | “models tend to meet the performance bottleneck in the case studies across cities or regions” | 摘要；直接支持跨城市泛化瓶颈。 | [PDF](</Users/hou/Desktop/dissertation/resource/2309.16499v2.pdf>) |
| <a id="l14"></a>**L14** Hurst-Tarrab et al. (2020) | “achieves more than 50% intersection over union (IoU) in all the testing sets” | 摘要；直接支持停车分割 IoU 比较值。 | [PDF](</Users/hou/Desktop/dissertation/resource/applsci-10-05364-v2.pdf>) |
| <a id="l15"></a>**L15** Jiao (2015) | “urban land density decreases slowly in the main urban core area” | 结果讨论；支持用距中心距离组织城市土地密度剖面。 | [PDF](</Users/hou/Desktop/dissertation/resource/1-s2.0-S0169204615000481-main.pdf>) |
| <a id="l16"></a>**L16** Lange, Kovacevic and Johnson (2026) | “Post-war neighbourhoods are up to 40 per cent less dense than similarly located pre-war neighbourhoods” | p. 12，Figure 3a；直接支持 40% 密度差。 | [PDF](</Users/hou/Desktop/dissertation/resource/Course-correction-April-2026.pdf>) |
| <a id="l17"></a>**L17** Livingstone, Fiorentino and Short (2021) | “the agency and influence of planning processes and densification policies on urban landscapes in London” | 摘要；支持伦敦密度政策实践研究。 | [PDF](</Users/hou/Desktop/dissertation/resource/88-1-3041-1-10-20210217.pdf>) |
| <a id="l18"></a>**L18** Lv et al. (2023) | “Semantic segmentation is a fundamental but challenging problem of pixel-level remote sensing (RS) data analysis.” | 摘要；支持遥感语义分割的研究背景。 | [PDF](</Users/hou/Desktop/dissertation/resource/fevo-11-1201125.pdf>) |
| <a id="l19"></a>**L19** Lyu et al. (2025) | “variations in ground sampling distance, imaging modes from various sensors, geographical landscapes, and environmental conditions” | 摘要；直接列出遥感领域偏移来源。 | [PDF](</Users/hou/Desktop/dissertation/resource/2510.15615v1.pdf>) |
| <a id="l20"></a>**L20** Maggiori et al. (2017) | “the testing is not performed over excluded areas … but over entirely different cities instead” | 结论；Table 2 的 MLP overall IoU 为 64.67。 | [PDF](</Users/hou/Desktop/dissertation/resource/AerialImageLabelingDataset.pdf>) |
| <a id="l21"></a>**L21** MHCLG (2024) | “building on or above service yards, car parks, lock-ups and railway infrastructure” | NPPF para. 125(d)；para. 124 另要求尽量利用 brownfield land。 | [PDF](</Users/hou/Desktop/dissertation/resource/NPPF_December_2024.pdf>) |
| <a id="l22"></a>**L22** Olofsson et al. (2014) | “the three major components: sampling design, response design and analysis” | 摘要；直接支持准确率评估三部分框架及基于参考样本的面积估计。 | [PDF](</Users/hou/Desktop/dissertation/resource/articolo_oloffson.pdf>) |
| <a id="l23"></a>**L23** Openshaw (1984) | “different aggregations yield different results” | MAUP 论述处；直接支持分区方式会改变统计结果。 | [PDF](</Users/hou/Desktop/dissertation/resource/38-maup-openshaw.pdf>) |
| <a id="l24"></a>**L24** Qiam, Devunuri and Lehe (2025) | “Parking lot annotations must be drawn along the edge of the pavement”; “Vegetation reflects more NIR” | pp. 1229–1230；直接支持铺装边界与 NIR 动机；极短车道规则见同页。 | [PDF](</Users/hou/Desktop/dissertation/Parking/literature/A_Pipeline_and_NIR-Enhanced_Dataset_for_Parking_Lot_Segmentation.pdf>) |
| <a id="l25"></a>**L25** Roberts et al. (2017) | “randomly drawn folds lead to artificially low error estimates” | 模拟结果；直接支持空间依赖数据采用分块验证。 | [PDF](</Users/hou/Desktop/dissertation/resource/Ecography - 2016 - Roberts - Cross‐validation strategies for data with temporal  spatial  hierarchical  or phylogenetic.pdf>) |
| <a id="l26"></a>**L26** Scharnhorst (2018) | “empty parking stalls made up 68 percent of the supply in the residential core” | Jackson 结果；直接支持 68% 空置比例。 | [PDF](</Users/hou/Desktop/dissertation/resource/18806-research-riha-parking-report.pdf>) |
| <a id="l27"></a>**L27** Sehra, Singh and Rai (2013) | “the discrepancies between the rural and urban areas in the USA showed an opposite tendency … the rural data was, in parts, even more complete” | 综述 p. 18 的美国案例；正文已改写为“方向不一致”，与本句直接对应。 | [PDF](</Users/hou/Desktop/dissertation/resource/Assessment_of_OpenStreetMap_Data_-_A_Review.pdf>) |
| <a id="l28"></a>**L28** Shoup (2005) | “parking requirements reduce density because each building has its own, unshared parking” | 土地利用／密度讨论；支持停车配建的空间机会成本。 | [PDF](</Users/hou/Desktop/dissertation/resource/High Cost of Free Parking_26_07_09_01_26_53.pdf>) |
| <a id="l29"></a>**L29** Stehman and Foody (2019) | “the three major components of accuracy assessment, the sampling design, response design, and analysis” | 接受稿摘要；支持严谨准确率评估的设计框架。 | [PDF](</Users/hou/Desktop/dissertation/resource/AccuracyReview_Final_Submitted.pdf>) |
| <a id="l30"></a>**L30** Stehman and Wickham (2011) | “A universally best spatial assessment unit does not exist” | 接受稿摘要；直接支持评估单元是设计选择。 | [PDF](</Users/hou/Desktop/dissertation/resource/WICKSHAM 11-004 FINAL JOURNAL ARTICLE PIXELPPR_FINAL.PDF>) |
| <a id="l31"></a>**L31** Xie et al. (2021) | “It does not need positional encoding”; “excellent zero-shot robustness on Cityscapes-C” | 摘要及稳健性实验；Cityscapes-C 是图像退化测试，不等同地理迁移。 | [PDF](</Users/hou/Desktop/dissertation/resource/2105.15203v3.pdf>) |
| <a id="l33"></a>**L33** Yin et al. (2022) | “the focus of this paper is to detect the location and the polygon of the parking lot”；“it can be modeled as a binary semantic segmentation problem”；Table 1 将 APKLOT 的目标列为 `Parking Block`、Grab-Pklot 列为 `Parking Lot` | p. 1372 及 Table 1；支持「整个停车场多边形」这一目标形态，及其与 APKLOT 标注单元的差别。该文无 APKLOT §3.1–3.2 那样逐项的纳入／排除清单，其 §4.2.2 为候选生成＋人工修正流程（共 2,883 个停车场多边形、1,344 组影像—掩膜），故未用以支撑「规则清单」。 | [PDF](</Users/hou/Desktop/dissertation/resource/Yin_A_Context-Enriched_Satellite_Imagery_Dataset_and_an_Approach_for_Parking_WACV_2022_paper.pdf>) |
| <a id="l32"></a>**L32** Zhou, Wang and Liu (2022) | “most countries are characterized by a low completeness, [but] relatively high accuracy” | 摘要；支持 OSM 土地利用／覆盖数据的完整度与准确度并不等同。 | [PDF](</Users/hou/Desktop/dissertation/resource/1-s2.0-S0143622822001138-main.pdf>) |

---

# 摘要

**英文原稿**

The United Kingdom holds no consistent spatial record of off-street surface parking, so the land it occupies is missing from densification debates — even as national planning policy names car parks explicitly among the under-utilised land authorities should bring forward. Segmentation of aerial imagery offers a route needing neither institutional records nor fieldwork, and a model trained for the task has been published, but whether it transfers to British cities has not been tested.

**中文翻译**

英国目前没有统一的路外露天停车场空间记录。因此，停车场占用的土地一直缺席于城市密度提升的讨论，尽管国家规划政策已经明确将停车场列为地方政府应推动利用的低效用地之一。利用航空影像进行图像分割提供了一条不依赖政府记录、也不需要实地调查的路径；目前已经有专门为该任务训练并公开发布的模型，但它能否迁移到英国城市，尚未得到检验。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/fp_analysis_summary.csv`；`analysis/fn_analysis_summary.csv`；`analysis/calibration_transfer_errors.csv`；译文对应位置：`00_abstract.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

This dissertation applies that US-trained model, exactly as released and with no UK training data in the primary analysis, to 100 km² of Leeds, evaluating it against 2,037 manually labelled car parks drawn to the source model's own target definition. Rather than reporting accuracy alone, it decomposes the error: attributed against independent reference layers, characterised by stratified sampling of 142 image chips adjudicated on the imagery the model actually consumed, and tested by ablating the post-processing stage.

**中文翻译**

本论文将这一美国训练的模型完全按照公开版本、在主分析中不使用任何英国训练数据，应用于利兹 100 km² 的区域，并用 2,037 个按照源模型目标定义人工标注的停车场进行评估。本研究不只报告准确率，还进一步分解误差：利用独立参考图层归因错误；通过对 142 个影像样本进行分层抽样，并依据模型实际使用的影像进行人工判读；同时通过消融实验检验后处理阶段的影响。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/fp_analysis_summary.csv`；`analysis/fn_analysis_summary.csv`；`analysis/calibration_transfer_errors.csv`；本段核对值：100, 2,037, 142；译文对应位置：`00_abstract.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

Transfer proves asymmetric. Recall is **0.854** and spatially even; precision is **0.571**, and predicted area is **1.50 times** the labelled area. Error is concentrated in boundary placement rather than misrecognition — the genuine blind spot is at most 2.1% of labelled area — and the post-processing pipeline creates a blind spot of its own, deleting four fifths of the rooftop parking that the raw model detects more reliably than parking at ground level.

**中文翻译**

结果表明，模型迁移具有明显的不对称性。召回率为 **0.854**，且空间分布较为均匀；精确率为 **0.571**，预测面积是标注面积的 **1.50 倍**。误差主要来自边界划分，而不是无法识别停车场——真正的识别盲区最多只占标注面积的 2.1%。与此同时，后处理流程又制造了自己的盲区：原始模型识别屋顶停车场的能力甚至优于地面停车场，但后处理删除了其中五分之四。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/fp_analysis_summary.csv`；`analysis/fn_analysis_summary.csv`；`analysis/calibration_transfer_errors.csv`；本段核对值：0.854, 0.571, 1.50, 2.1；译文对应位置：`00_abstract.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

Measured against that reliability, the labelled reference puts surface parking at **3.26%** of the study area, concentrated in the inner 2 km and declining sharply beyond it. The over-prediction is systematic and correctable to within about ±7% at half-city scale, though not at the scale of a single square kilometre. A bounded fine-tuning supplement is reported separately. A transferred map cannot measure how much land a city gives to parking on its own; paired with one local validation, it can — a materially different claim from either accepting or dismissing it.

**中文翻译**

在这一可靠性水平下，人工参考数据表明，露天停车场占研究区面积的 **3.26%**，主要集中在内侧 2 km 范围内，此后迅速下降。模型的高估具有系统性；在半个城市的尺度上，经校正后的误差可以控制在约 ±7%，但在单个 1 km² 网格尺度上不能做到这一点。另有一项范围受限的微调补充实验，单独报告。一个迁移而来的地图无法单独测量一座城市有多少土地用于停车；但如果配合一次本地验证，它可以做到——这一结论与简单地接受或否定这张地图有本质区别。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/fp_analysis_summary.csv`；`analysis/fn_analysis_summary.csv`；`analysis/calibration_transfer_errors.csv`；本段核对值：3.26, 2, ±7, 1；译文对应位置：`00_abstract.md`（仅作定位，不作为引文证据）
> - **可加强：** 继续明确 3.26% 来自人工参考而非模型估计，并避免把 3.30% 当作独立观测。

---

# 1. 引言

## 1.1 背景与研究动机

**英文原稿**

Surface parking is one of the few urban land uses that almost every city has in quantity and almost no city has counted. It is usually treated as a transport question — how many spaces, priced how, used when — but its more consequential character is spatial. A minimum parking requirement is a rule about how much land a building must set aside, so the cumulative effect of decades of such rules is a pattern of land use, one that generates little activity and no housing, and that no agency has ever been responsible for inventorying (Shoup, 2005).

**中文翻译**

露天停车场是少数几种几乎每座城市都大量拥有、却几乎没有城市真正统计过的土地用途之一。停车通常被视为一个交通问题——有多少车位、如何定价、何时使用——但它更重要的属性其实是空间性的。最低停车位配建要求，本质上是一条规定建筑必须留出多少土地用于停车的规则。因此，几十年累积下来，这些规定形成了一种土地利用格局：这些土地几乎不产生城市活动，也不提供住房，却从来没有任何机构负责系统地清点它们（Shoup, 2005）。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L28](#l28) Shoup (2005)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`01_introduction.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

In England that omission has become awkward. The National Planning Policy Framework asks planning authorities to bring forward under-utilised land, and names car parks explicitly among its examples (MHCLG, 2024, para. 125(d)). The instruction presupposes an answer to a question nobody has answered: where are they, and how much land do they hold? The densification literature runs into the same wall. Britain's largest cities are found to carry substantial density gaps relative to their European peers, driven in part by the neighbourhoods lying just beyond the city centre (Lange, Kovacevic and Johnson, 2026), yet no consistent measurement exists of how much of that inner land is currently held as car park.

**中文翻译**

在英格兰，这一缺失如今变得越来越难以忽视。《国家规划政策框架》要求地方规划部门推动利用低效土地，并明确将停车场列为例子之一（MHCLG, 2024, para. 125(d)）。但这项要求预设了一个尚无人回答的问题：这些停车场在哪里，又占用了多少土地？城市密度提升研究也遇到了同样的障碍。研究发现，与欧洲同类城市相比，英国最大的城市存在显著的密度缺口，其中一部分由紧邻市中心之外的社区造成（Lange, Kovacevic and Johnson, 2026）；然而，目前并没有统一测量能够说明这些内城区土地中有多少正在被停车场占用。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L16](#l16) Lange, Kovacevic and Johnson (2026)、[L21](#l21) MHCLG (2024)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：125；译文对应位置：`01_introduction.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

The gap is not for want of trying. It reflects how parking has been measured where it has been measured at all. American inventories are the fullest available, but they are built from cadastral records and codified parking requirements that the UK does not hold in comparable form (Scharnhorst, 2018; Hoehne et al., 2019). British measurement has been local and survey-based — most substantially a sample of on-the-ground inspections in London — and counts *spaces* rather than land area. The authors of the most substantial recent UK review conclude bluntly that little information is collected about how much parking exists at all (Bates and Leibling, 2012).

**中文翻译**

这一空白并不是因为从未有人尝试，而是由既有停车测量方法造成的。美国拥有目前最完整的停车清单，但这些清单依赖地籍记录和编码明确的停车配建要求，而英国并没有可比形式的数据（Scharnhorst, 2018; Hoehne et al., 2019）。英国的测量则主要是地方性的实地调查——其中规模最大的是伦敦的地面抽样调查——而且统计的是*车位数量*，不是土地面积。英国近年来最重要的一份停车研究直言，关于停车设施究竟有多少，现实中几乎没有收集相关信息（Bates and Leibling, 2012）。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L01](#l01) Bates and Leibling (2012)、[L12](#l12) Hoehne et al. (2019)、[L26](#l26) Scharnhorst (2018)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`01_introduction.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

Segmentation of aerial imagery offers a way past both obstacles, because it depends on no institutional record and no fieldwork. A model trained specifically for parking has been published and can be run on any imagery a user holds (Qiam, Devunuri and Lehe, 2025). That is an attractive proposition for a planner in a British city, and it is the proposition this dissertation tests.

**中文翻译**

航空影像分割提供了一条绕开这两种障碍的路径，因为它既不依赖机构记录，也不需要实地调查。目前已经有一个专门识别停车场的模型公开发布，只要使用者拥有影像，就可以运行该模型（Qiam, Devunuri and Lehe, 2025）。对于英国城市的规划人员而言，这很有吸引力，而本论文检验的正是这一设想。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L24](#l24) Qiam, Devunuri and Lehe (2025)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`01_introduction.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

The risk is that models transfer badly. A network trained on one country's imagery and urban form may perform quite differently on another's, a problem sufficiently recognised that benchmarks exist to measure it (Maggiori et al., 2017; Lyu et al., 2025). Nor does the architecture's own robustness claim settle the matter: SegFormer's reported zero-shot robustness is demonstrated against corrupted images of familiar cities, which is close to the opposite of the situation here (Xie et al., 2021). Before a transferred map is used as evidence about land, someone has to establish what it can be used for.

**中文翻译**

风险在于，模型可能无法良好迁移。在一个国家的影像和城市形态上训练的网络，应用到另一个国家时，表现可能完全不同。这个问题已经受到足够重视，以至于研究者专门建立了衡量这种差异的基准数据集（Maggiori et al., 2017; Lyu et al., 2025）。模型架构本身关于稳健性的声明也不能解决问题：SegFormer 所报告的零样本稳健性，是在熟悉城市的影像受到噪声、模糊等破坏时得到的，这几乎与本研究的情形相反（Xie et al., 2021）。在把迁移得到的地图用作土地证据之前，必须先确定它究竟可以用于什么。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L19](#l19) Lyu et al. (2025)、[L20](#l20) Maggiori et al. (2017)、[L31](#l31) Xie et al. (2021)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`01_introduction.md`（仅作定位，不作为引文证据）
> - **可加强：** 把文献的一般机制与利兹案例的可检验预期逐项对应。

**英文原稿**

That last phrase names an established question rather than a new one. Spatial data quality is conventionally divided into *internal* quality, meaning how far a dataset matches the ground, and *external* quality or **fitness for use**, meaning whether it is adequate for a particular purpose — a distinction that exists because the same dataset can be sufficient for one task and useless for another, so quality cannot be settled independently of the use (Devillers et al., 2007). This dissertation is a fitness-for-use assessment of a transferred model, and its contribution is to make that assessment quantitative: not whether the map is good, but which uses its measured error still permits.

**中文翻译**

最后这句话并不是提出了一个全新的问题，而是对应了一个已有的数据质量概念。空间数据质量通常被分为*内部质量*与*外部质量*：内部质量指数据与现实地表的吻合程度；外部质量或**用途适合性（fitness for use）**，则指数据是否足以支持某项具体用途。之所以需要这种区分，是因为同一数据集可能适合一种任务，却完全不适合另一种任务，因此数据质量不能脱离用途单独判断（Devillers et al., 2007）。本论文所做的是对迁移模型进行用途适合性评估，并把这种评估量化：问题不是这张地图笼统而言“好不好”，而是它已经测得的误差仍允许哪些用途。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L06](#l06) Devillers et al. (2007)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`01_introduction.md`（仅作定位，不作为引文证据）
> - **可加强：** 把文献的一般机制与利兹案例的可检验预期逐项对应。

## 1.2 研究问题

**英文原稿**

| | |
|---|---|
| **RQ1** | How accurate is a US-trained surface-parking segmentation model on UK aerial imagery, and does that accuracy vary systematically within the city? |
| **RQ2** | What systematic errors does it make, and how much of that error is removed — or created — by post-processing? |
| **RQ3** | Under the measured reliability, how much central-city land is surface parking, and where is it concentrated? |

**中文翻译**

| | |
|---|---|
| **RQ1** | 一个在美国训练的露天停车场分割模型，在英国航空影像上的准确度如何？这种准确度是否在城市内部呈现系统性的空间差异？ |
| **RQ2** | 模型会产生哪些系统性错误？后处理消除了多少错误，又制造了多少错误？ |
| **RQ3** | 在已经测得的可靠性条件下，中心城区有多少土地属于露天停车场，它们集中在哪里？ |

> **段落审读**
> - **逻辑用途：** 把本段论证的关键量化关系集中展示
> - **核对状态：** ✅ 已核对：表内核心数字已与项目结果 CSV 及正文恒等式复核。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；译文对应位置：`01_introduction.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿可补样本量、单位或不确定区间。

**英文原稿**

The three are sequential rather than parallel. RQ1 establishes whether the transfer works at all. RQ2 explains why the accuracy figures look as they do, which determines what they mean. Only under the reliability those two establish does RQ3 become answerable.

**中文翻译**

这三个问题是依次推进的，而不是相互平行的。RQ1 首先确定模型迁移是否有效。RQ2 解释准确率数字为何呈现当前形态，并由此决定这些数字意味着什么。只有在前两个问题建立的可靠性条件下，RQ3 才能得到回答。

> **段落审读**
> - **逻辑用途：** 组织章节、概括贡献或承接后文
> - **核对状态：** 🟨 结构性判断：已检查与全文结构一致；不存在独立原数据。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；译文对应位置：`01_introduction.md`（仅作定位，不作为引文证据）
> - **可加强：** 确保每项预告或贡献都能回指具体章节和证据。

## 1.3 研究范围

**英文原稿**

The study covers 100 km² of Leeds, validated against 2,037 manually labelled car parks. That it examines one city in depth rather than several in outline is a design decision, not a shortfall. Comparing cities presupposes that the model's output is trustworthy, and that had never been established in the UK; spending the available effort on a labelled reference, a per-cell validation and a sampled error typology establishes what the map supports before anything is built on it. Multi-city extension then becomes future work with a defined precondition, which §5.5 specifies.

**中文翻译**

本研究覆盖利兹 100 km² 的区域，并以 2,037 个手工标注的停车场进行验证。深入研究一座城市，而不是粗略比较多座城市，是一项主动的研究设计选择，不是研究缺陷。城市间比较预设模型输出值得信任，但这种可信度此前从未在英国得到验证。因此，本研究将有限的工作量用于建立人工参考、逐网格验证和抽样错误分类，在基于地图开展其他分析之前，先确定地图能够支持哪些用途。这样，多城市扩展就成为具有明确前提条件的未来研究；§4.7 对这一条件作了具体说明。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；本段核对值：100, 2,037, 4.7；译文对应位置：`01_introduction.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

Three boundaries define the primary analysis. The target is off-street surface parking as the source model defines it, so on-street parking and enclosed structures are outside it by rule. The model is used exactly as released, with no UK training data, because what is being measured is what an off-the-shelf user would obtain; a bounded supplementary experiment departs from this second boundary alone and is reported separately in Appendix C. And the study identifies where parking is and how much land it occupies; it does not judge whether any site should be redeveloped, a question requiring ownership, access, demand and viability information that none of the data used here contains.

**中文翻译**

全文始终遵循三条边界。第一，研究目标是源模型所定义的路外露天停车场，因此路边停车和封闭式停车建筑按规则排除。第二，模型完全按照公开版本使用，不采用任何英国训练数据，因为本研究衡量的是普通使用者直接采用现成模型时会得到的结果。第三，本研究识别停车场的位置及其占地面积，但不判断任何具体地点是否应该重建。后者需要所有权、出入条件、停车需求和开发可行性等信息，而本研究使用的数据均不包含这些内容。

> **段落审读**
> - **逻辑用途：** 限制结论适用范围，防止从城市尺度证据跳到地块判断
> - **核对状态：** 🟨 需人工复核：限制来自研究设计与已报告验证结果。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；译文对应位置：`01_introduction.md`（仅作定位，不作为引文证据）
> - **可加强：** 区分可在本研究内量化的限制和只能在未来研究中检验的限制。

## 1.4 伦理考虑

**英文原稿**

All data are secondary and either openly licensed or licensed to the institution, and no human participants are involved. Two points warrant reflection nonetheless. The labelling was carried out by a single annotator, so the reference embodies one person's judgement on a target whose boundaries are genuinely ambiguous; §4.3 quantifies the effect this has on measurable accuracy rather than leaving it as a caveat. Second, an output identifying low-intensity urban land could be read as a development prospectus. The scope statement above is a substantive commitment, not a formality: no site-level claim is made anywhere in what follows.

**中文翻译**

本研究使用的全部数据都是二手数据，或者采用开放许可，或者由学校获得授权；研究不涉及任何人类参与者。尽管如此，仍有三个问题需要反思。首先，标注由一名标注者完成，因此人工参考包含个人对一个边界本身就存在模糊性的目标所作的判断。§4.3 对这项因素如何影响可测准确率进行了量化，而不是仅仅把它作为一般性限制。其次，人工参考是在卫星底图上绘制的，而模型使用的是另一套影像；这一差异在标注完成后才被发现，并在 §3.8 中作为一个范围有限、经过测量的影响明确报告，而不是被隐瞒。最后，一张识别低强度城市用地的地图可能被理解为开发机会清单。前述范围声明是一项实质性的承诺，而不是形式要求：下文不会作出任何具体地块层面的判断。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；本段核对值：4.3, 3.8；译文对应位置：`01_introduction.md`（仅作定位，不作为引文证据）
> - **可加强：** 增加第二标注者与标注者间一致性，而不只依赖重标一致性。

## 1.5 论文结构

**英文原稿**

Chapter 2 brings together four literatures — parking as urban land, the evidence on its extent, segmentation of aerial imagery, and the limits of volunteered reference data — and states the gap where they meet. Chapter 3 sets out the annotation protocol, the pipeline, the accuracy measures, the two-track error typology, the ablation design and the checks on imagery consistency and on the calibration estimator. Chapter 4 reports the measured accuracy, decomposes the error, tests the post-processing stage, shows the apparent location effect to be confounded, and gives the extent and distribution of surface parking. Chapter 5 answers the three research questions, states what the transferred map does and does not support, and sets out the limitations. Chapter 6 concludes.

**中文翻译**

第 2 章汇集四组通常彼此分离的文献：停车作为城市土地、停车规模的既有证据、航空影像分割，以及自愿地理信息作为参考数据的局限，并指出它们交汇处的研究空白。第 3 章介绍标注规则、处理流程、准确率指标、两条错误分类路径、消融实验设计，以及影像一致性和校准估计量的检验。第 4 章报告实测准确率、分解误差、检验后处理阶段、说明表面的区位效应受到混杂，并给出露天停车场的规模与分布。第 5 章回答三个研究问题，说明迁移地图能够和不能够支持什么，并讨论研究局限。第 6 章总结全文。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；本段核对值：2, 3, 4, 5, 6；译文对应位置：`01_introduction.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

---

# 2. 背景

**英文原稿**

This chapter brings together four literatures that rarely meet. Section 2.1 sets out why the land occupied by surface parking is worth measuring, and why UK policy has recently made that question sharper. Section 2.2 reviews what is actually known about parking extent, and shows that the evidence base and the methods behind it are predominantly American. Sections 2.3 and 2.4 turn to the method that could close that gap — semantic segmentation of aerial imagery, and the specific model used here. Section 2.5 asks what could go wrong when such a model crosses a national boundary, and converts that question into a set of expectations the results chapter can test. Section 2.6 explains why the obvious alternative reference, OpenStreetMap, cannot serve as ground truth. Section 2.7 states the gap.

**中文翻译**

本章汇集四组很少被放在一起讨论的文献。§2.1 说明为什么值得测量露天停车场占用的土地，以及英国近期政策为何使这个问题更加紧迫。§2.2 回顾我们实际上知道多少停车规模信息，并说明既有证据及其背后的方法主要来自美国。§2.3 和 §2.4 转向可能填补这一空白的方法——航空影像语义分割，以及本研究使用的具体模型。§2.5 讨论模型跨越国界时可能出现什么问题，并把这些问题转化为结果章可以检验的一组预期。§2.6 解释为什么看似显然的替代参考 OpenStreetMap 不能充当地面真值。§2.7 最后明确研究空白。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；本段核对值：2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

## 2.1 停车作为城市土地

**英文原稿**

The case for treating parking as a land-use question rather than a transport one was made most forcefully by Shoup (2005). Minimum parking requirements, he argues, operate as a hidden subsidy: by obliging developers to supply parking regardless of demand, they raise development costs, encourage driving, and commit land to a use that generates little activity and no housing. The argument's force is spatial. A parking requirement is a rule about how much land a building must set aside, so its cumulative effect is a pattern of land use — and one that is rarely inventoried, because no agency is responsible for counting it.

**中文翻译**

Shoup（2005）最有力地主张，应把停车视为土地利用问题，而不仅仅是交通问题。他认为，最低停车位配建要求是一种隐性补贴：无论实际需求如何，它都迫使开发者提供停车位，从而增加开发成本、鼓励驾车，并把土地长期固定在一种几乎不产生活动、也不提供住房的用途上。这个论点的力量来自空间层面。停车配建规定决定建筑必须留出多少土地，因此其累积结果是一种土地利用格局；但这种格局很少被系统统计，因为没有任何机构负责清点它。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L28](#l28) Shoup (2005)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

That framing has become directly relevant to English planning policy. The National Planning Policy Framework instructs authorities to make "as much use as possible of previously-developed or 'brownfield' land" (MHCLG, 2024, paras 124–125) and to give substantial weight to brownfield development within settlements. More pointedly for this study, paragraph 125(d) asks authorities to

**中文翻译**

这一视角如今与英格兰规划政策直接相关。《国家规划政策框架》要求地方政府“尽可能充分利用已经开发过的土地或‘棕地’”（MHCLG, 2024, para. 124），并在城镇内部对棕地开发给予高度重视。与本研究更直接相关的是第 125(d) 段，它要求地方政府：

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L21](#l21) MHCLG (2024)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：124, 125；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

> promote and support the development of under-utilised land and buildings, especially if this would help to meet identified needs for housing where land supply is constrained and available sites could be used more effectively (for example converting space above shops, and building on or above service yards, **car parks**, lock-ups and railway infrastructure).

**中文翻译**

> 促进并支持低效土地和建筑的开发，尤其是在土地供应受限、而现有地点能够得到更有效利用的情况下，如果这有助于满足已经确定的住房需求。例如，可以改造商店上方空间，或者在服务场地、**停车场**、车库和铁路基础设施之上或其所在地进行建设。

> **段落审读**
> - **逻辑用途：** 用政策原文直接确立停车场属于低效用地的政策依据
> - **核对状态：** ✅ 已核对：引文已与 NPPF 2024 第 125(d) 段逐字核实。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 保留英文原句或页码／段号，便于考官复查译义。

**英文原稿**

Car parks are thus named in national policy as an example of under-utilised land. The policy instruction presupposes a spatial answer to a question nobody has answered: where are they, and how much land do they hold?

**中文翻译**

因此，国家政策明确把停车场列为低效土地的例子。可是，这项政策要求预设了一个尚无人回答的空间问题：停车场在哪里，又占用了多少土地？

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

The same gap appears in the densification literature. Centre for Cities research finds that Britain's largest cities — Manchester, Birmingham, Liverpool, Leeds and Glasgow — carry the largest density gaps relative to their European peers, and that the gap is driven substantially by post-war neighbourhoods "located just beyond the city centre", which can be up to 40 per cent less dense than similarly located pre-war neighbourhoods (Lange, Kovacevic and Johnson, 2026). Livingstone, Fiorentino and Short (2021) examine how densification policy plays out in practice in London and at what cost, while Habermehl and McFarlane (2025) argue that density is better understood as a contested dialectic between "hard" and "gentle" forms than as a single quantity to be maximised. What none of this work can draw on is a consistent measurement of how much land inside British cities is currently held as surface parking. The policy asks for under-utilised land to be found; the evidence base cannot yet say how much of it is car park.

**中文翻译**

城市密度提升文献中也存在同样的空白。Centre for Cities 的研究发现，与欧洲同类城市相比，曼彻斯特、伯明翰、利物浦、利兹和格拉斯哥等英国最大城市具有最大的密度缺口。这个缺口很大程度上由“紧邻市中心之外”的战后社区造成；与位置相似的战前社区相比，这些地区的密度最多可以低 40%（Lange, Kovacevic and Johnson, 2026）。Livingstone、Fiorentino 和 Short（2021）研究伦敦的密度提升政策如何在现实中实施及其代价；Habermehl 和 McFarlane（2025）则认为，密度不应被理解为一个需要单纯最大化的数值，而应理解为“强硬”与“温和”密度提升方式之间充满争议的辩证关系。这些研究都无法使用一项统一测量，说明英国城市内部有多少土地目前被露天停车场占用。政策要求找到低效土地，但证据基础甚至还不能说明其中有多少是停车场。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 见 [L10](#l10) Habermehl and McFarlane (2025)、[L16](#l16) Lange, Kovacevic and Johnson (2026)、[L17](#l17) Livingstone, Fiorentino and Short (2021)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：40%；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

## 2.2 关于停车规模已有何种知识，这些知识来自哪里

**英文原稿**

Systematic parking inventories exist, but they are overwhelmingly American, and they were built by methods that do not port straightforwardly to the UK. The British evidence that does exist measures something different, in one atypical city, by means too expensive to repeat.

**中文翻译**

系统性的停车清单确实存在，但绝大多数来自美国，而且建立这些清单的方法无法直接移植到英国。英国现有的证据测量的是不同事物，集中在一座不具代表性的城市，并且采用了成本高昂、难以重复的方法。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

Scharnhorst (2018) compiled comprehensive inventories for five US cities — New York, Philadelphia, Seattle, Des Moines and Jackson, Wyoming — combining satellite imagery with tax and cadastral records. The results are striking both for supply and for its use: reviewing occupancy studies across the five cities, he reports empty stalls making up 68 per cent of supply in Jackson's residential core. Hoehne et al. (2019) take a different route for metropolitan Phoenix, cross-referencing cadastral and roadway data against minimum parking requirements to estimate 12.2 million parking spaces in 2017, against 2.86 million registered vehicles.

**中文翻译**

Scharnhorst（2018）结合卫星影像、税务和地籍记录，为纽约、费城、西雅图、得梅因和怀俄明州杰克逊五座美国城市建立综合停车清单。无论供应量还是使用情况，结果都很突出：在回顾五城占用率研究后，他报告杰克逊住宅核心区的空置车位占供应量 68%。Hoehne et al.（2019）采用另一种方法研究凤凰城都会区，把地籍和道路数据与最低停车位配建要求交叉对照，估计 2017 年共有 1,220 万个停车位，而登记车辆为 286 万辆。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 见 [L12](#l12) Hoehne et al. (2019)、[L26](#l26) Scharnhorst (2018)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：68%、1,220 万、286 万；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

The British evidence is thinner, and its own authors say so. The most substantial recent review of UK parking policy, Bates and Leibling's (2012) study for the RAC Foundation, concludes that a central obstacle to coherent policy is simply the absence of data: their study, they write, shows "how little information is collected about the quantity of parking space" that exists (p. 99), a problem they attribute to fragmented responsibility and to local authorities lacking the resources to audit their own parking supply. Where UK measurement has been attempted it has been local and survey-based. The fullest example remains a study commissioned for London, in which parking availability was estimated by inspecting a sample of three hundred 500 m squares on the ground, later partially resurveyed; it put the capital's supply at roughly 6.8 million spaces, counted as spaces (Bates and Leibling, 2012).

**中文翻译**

英国证据薄弱得多，而且研究者本人也承认这一点。Bates 和 Leibling（2012）为 RAC Foundation 完成的研究，是近年来英国停车政策最重要的综述。他们认为， coherent parking policy 面临的核心障碍就是数据缺失；研究表明，现实中关于停车空间数量的信息“少得惊人”（p. 99）。他们把问题归因于管理责任分散，以及地方政府缺乏审计停车供应的资源。英国已有的测量主要是地方性实地调查。规模最大的例子仍然是一项受托开展的伦敦研究：研究人员实地检查了 300 个 500 m 方格的样本，此后又对其中一部分进行复查，并估算伦敦约有 680 万个停车位。该研究统计的是车位数量（Bates and Leibling, 2012）。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L01](#l01) Bates and Leibling (2012)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：99, 300, 500, 680；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

Three limitations of that evidence base define the opening this study works in. It counts **spaces rather than land area**, which cannot answer a question about how much ground a city gives over to parking. It is **concentrated on London**, which is atypical of British cities in density, land value and parking regulation alike. And it rests on **ground survey**, which is expensive enough that the exercise has not been repeated at scale or extended to other cities. No comparable measurement of off-street surface parking *area* appears to exist for a British city outside London.

**中文翻译**

这些证据的三个局限构成了本研究的切入点。第一，它统计的是**车位而不是土地面积**，因此无法回答一座城市究竟把多少地面用于停车。第二，它**集中在伦敦**，而伦敦在密度、土地价值和停车监管方面都不能代表其他英国城市。第三，它依赖**地面调查**，成本高到无法大规模重复，也没有扩展到其他城市。目前似乎不存在针对伦敦以外英国城市的、具有可比性的路外露天停车场*面积*测量。

> **段落审读**
> - **逻辑用途：** 限制结论适用范围，防止从城市尺度证据跳到地块判断
> - **核对状态：** 🟨 需人工复核：限制来自研究设计与已报告验证结果。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 区分可在本研究内量化的限制和只能在未来研究中检验的限制。

**英文原稿**

Two further things follow for the present study. The first is substantive: where parking has been counted, it has consistently been found in quantities far exceeding observed use, which is what makes its land take a live question rather than an accounting curiosity. The second is methodological, and is the more important here. The American studies depend on institutional data that either does not exist in comparable form in the UK or does not carry the same information: Hoehne et al.'s method requires codified minimum parking requirements attached to parcels, and Scharnhorst's requires cadastral records that identify parking as a use. Neither is available as a national UK dataset, and the British alternative — sending surveyors out to look — is precisely what has proved too costly to repeat. An approach that reads parking directly from imagery, and therefore depends on no institutional record and no fieldwork, is attractive because it sidesteps both.

**中文翻译**

这又带来两点结论。第一点是实质性的：凡是进行过统计的地方，停车供应都持续表现为明显超过实际使用量，因此停车占地是一个现实的土地问题，而不只是一个统计上的好奇现象。第二点是方法性的，也是本研究更重要的关注点。美国研究依赖的机构数据，在英国要么不存在可比形式，要么不包含同样的信息：Hoehne et al. 的方法需要与地块相连的法定最低停车要求；Scharnhorst 的方法需要能把停车识别为土地用途的地籍记录。英国没有任何可在全国范围内使用的同类数据。英国的替代方法是派调查员实地检查，但它恰恰因为成本过高而未能重复。直接从影像读取停车场、因而不依赖机构记录和实地调查的方法之所以有吸引力，是因为它绕开了这两类障碍。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 见 [L12](#l12) Hoehne et al. (2019)、[L26](#l26) Scharnhorst (2018)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

A related strand of work provides the spatial framing rather than the counts. Jiao (2015) shows that urban land density follows regular, describable functions of distance from the centre, which supplies a natural way to organise a within-city analysis: not "how much parking is there" alone, but how its share of land changes across the urban gradient.

**中文翻译**

另一组相关研究提供了空间分析框架，而不是停车数量。Jiao（2015）表明，城市土地密度会随着距中心距离的变化呈现规则且可描述的函数。这为城市内部分析提供了一种自然组织方式：问题不只是“有多少停车场”，还包括停车场占地比例如何沿城市梯度变化。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L15](#l15) Jiao (2015)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

## 2.3 从航空影像中分割停车场

**英文原稿**

Semantic segmentation of remote-sensing imagery is now dominated by deep encoder–decoder architectures (Lv et al., 2023). The model used here is built on SegFormer (Xie et al., 2021), whose relevant property for aerial work is that it dispenses with positional encoding, leaving it comparatively indifferent to the tile size it is given — useful because aerial imagery is processed as arbitrary tiles rather than at a canonical size.

**中文翻译**

深度学习已经成为遥感影像语义分割的标准方法，这一领域主要使用在准确率和计算成本之间作出不同权衡的编码器—解码器架构（Lv et al., 2023）。其中，SegFormer（Xie et al., 2021）将分层 Transformer 编码器与刻意设计得十分轻量的全 MLP 解码器结合起来。对航空影像而言，其最相关的设计是取消位置编码：当测试影像分辨率不同于训练分辨率时，固定位置编码必须经过插值，这会损失准确率；取消位置编码后，模型对输入图块大小相对不敏感。航空影像通常以任意大小的图块出现，而不是固定标准尺寸，因此这一点具有实际意义。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L18](#l18) Lv et al. (2023)、[L31](#l31) Xie et al. (2021)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 把文献的一般机制与利兹案例的可检验预期逐项对应。

**英文原稿**

Its authors also report strong zero-shot robustness, demonstrated on Cityscapes-C, a benchmark that degrades image quality with noise, blur, weather and digital artefacts while leaving the scene unchanged. That is a different test from the one run here. A corrupted image of a familiar city and a clean image of an unfamiliar one stress different capacities, so the reported robustness does not by itself settle whether the model transfers geographically. Chapter 5 returns to the point once the error has been decomposed and it can be said which capacity the crossing taxed.

**中文翻译**

作者还报告了“出色的零样本稳健性”，证据来自 Cityscapes-C 基准。该基准通过噪声、模糊、天气和数字伪影破坏影像。**必须准确区分这一声明覆盖和没有覆盖的内容。** Cityscapes-C 在保持场景不变的同时降低*像素*质量：它仍然是相同的德国街道，只是拍摄质量变差。地理迁移几乎相反：影像条件可能完全良好，但物体本身、大小、铺装材料和排列方式发生了变化。在熟悉城市的受损影像上保持稳健，并不能证明模型在陌生城市的清晰影像上也稳健。因此，源论文报告的架构稳健性不能回答本论文的问题，这正是迁移表现必须经过测量、而不能被假定的原因之一。

> **段落审读**
> - **逻辑用途：** 限制结论适用范围，防止从城市尺度证据跳到地块判断
> - **核对状态：** 🟨 需人工复核：限制来自研究设计与已报告验证结果。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 区分可在本研究内量化的限制和只能在未来研究中检验的限制。

**英文原稿**

Parking is an attractive segmentation target because it is visually distinctive: a paved surface, usually with painted bays, usually with vehicles on it. It is also a target whose boundary is genuinely ambiguous — where a car park ends and its access road, service yard or forecourt begins is a matter of definition rather than observation. That ambiguity is not incidental here. It accounts for a substantial share of the apparent error measured in Chapter 4, and separating it from genuine misrecognition is one of this study's main analytical tasks.

**中文翻译**

把这类模型应用于停车场具有吸引力，因为从视觉上看，停车场是一个相对明确的目标：通常是铺装表面，常有画线车位和车辆，并且通常邻近建筑或道路。但它的边界也确实存在模糊性——停车场在哪里结束，出入道路、服务场地或前院从哪里开始，往往是定义问题而不是观察问题。这种模糊性并不是下文中的次要因素：第 4 章表明，它解释了相当一部分表面误差；把它与真正的识别错误分开，是本研究的主要分析任务之一。

> **段落审读**
> - **逻辑用途：** 限制结论适用范围，防止从城市尺度证据跳到地块判断
> - **核对状态：** 🟨 需人工复核：限制来自研究设计与已报告验证结果。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；本段核对值：4；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 区分可在本研究内量化的限制和只能在未来研究中检验的限制。

**英文原稿**

Two studies take parking specifically as the segmentation target. Berry et al. (2019) address a direct consequence of that ambiguity — adjacent car parks merge into one another under ordinary semantic segmentation — by segmenting instances through associative embeddings rather than classifying pixels. Hurst-Tarrab et al. (2020) assemble APKLOT, a purpose-built dataset of parking-block polygons cut from satellite imagery, and report the accuracy their models reach on it — the closest published point of comparison for a parking segmentation result, obtained with training and test data drawn from the same source, and taken up in §5.1. Neither study asks what the resulting map is fit for; accuracy is the endpoint.

**中文翻译**

有两项研究把停车本身作为分割目标。Berry et al.（2019）处理上述模糊性的一项直接后果——普通语义分割会把相邻停车场合并——因而使用关联嵌入划分实例，而非只给像素分类。Hurst-Tarrab et al.（2020）建立专门由卫星影像停车区块多边形组成的 APKLOT 数据集，并报告模型在其中达到的准确率；这是已发表停车分割结果中最接近的比较点，且其训练与测试数据来自同一来源，第 5.1 节将再次使用。两项研究都没有追问生成地图适合何种用途；准确率本身就是终点。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 见 [L02](#l02) Berry et al. (2019)、[L14](#l14) Hurst-Tarrab et al. (2020)、[L33](#l33) Yin et al. (2022)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：5.1；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

## 2.4 本研究使用的模型及其标注定义

**英文原稿**

The model applied in this study is the parking-lot segmentation network released by Qiam, Devunuri and Lehe (2025), who introduce both a pipeline and an NIR-enhanced training dataset for the task. The released checkpoint is a SegFormer-B5 configuration whose backbone was initialised from Cityscapes weights and fine-tuned on their parking dataset, as documented in the released model card and repository. No published accuracy figure is carried over to describe it. It is used here exactly as released, with no UK training data in the primary analysis.

**中文翻译**

本研究使用 Qiam、Devunuri 和 Lehe（2025）公开的停车场分割网络；他们同时提出处理流程和加入近红外信息的训练数据集。模型卡与发布仓库显示，公开检查点采用 SegFormer-B5 配置，骨干网络由 Cityscapes 权重初始化，再用其停车数据集微调。本文不把论文中的任何已发表准确率数字移用来描述该检查点，而是完全按发布版本、在主分析中不加入英国训练数据的条件下使用。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L24](#l24) Qiam, Devunuri and Lehe (2025)、[L31](#l31) Xie et al. (2021)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

What matters as much as the architecture is the *definition* the model was trained on, because that definition determines what a correct output looks like. Qiam, Devunuri and Lehe's target is off-street surface parking visible from above: marked bays and the aisles that connect them, including rooftop parking where the surface is visible — their dataset admits a parking structure only where the deck on top of it is visible — and excluding on-street parking and enclosed structures. Access driveways were not excluded by rule but left to case-by-case judgement, with annotators encouraged to take in only very short ones, expressly so that the model would not learn to recognise roads in general. Boundaries were drawn to the edge of the paving rather than to the parcel line, on the reasoning that only the paved edge offers a visual cue the model can learn; the authors note that OpenStreetMap parking polygons instead follow the parcel. They also note that NIR information assists in separating parking surfaces from adjacent vegetation.

**中文翻译**

与架构同样重要的是模型训练时所采用的*定义*，因为定义决定何种输出才算正确。Qiam、Devunuri 和 Lehe 的目标是从上方可见的路外地面停车：包括划线车位及连接通道，也包括从上方能够看见停车面的屋顶停车——其数据集只有在停车建筑顶层平台可见时才予纳入——而路边停车和封闭建筑则排除。引道并非一律排除，而是逐案判断；标注者被鼓励只纳入很短的引道，明确目的是避免模型学习一般道路。边界沿铺装边缘而非地块边界绘制，因为前者才提供模型可学习的视觉线索；作者指出 OSM 停车多边形反而常沿地块边界。他们还指出，NIR 有助于区分停车面与相邻植被。

> **段落审读**
> - **逻辑用途：** 限制结论适用范围，防止从城市尺度证据跳到地块判断
> - **核对状态：** 🟨 需人工复核：限制来自研究设计与已报告验证结果。
> - **文献原句：** 见 [L24](#l24) Qiam, Devunuri and Lehe (2025)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 区分可在本研究内量化的限制和只能在未来研究中检验的限制。

**英文原稿**

Two consequences run through this dissertation. First, any reference dataset used to assess the model must follow the same definition, or the resulting accuracy figures measure disagreement about categories rather than model performance; the annotation protocol in Chapter 3 is therefore derived from theirs. Second, the imagery available for this study is three-band RGB with no NIR channel — a limitation returned to below.

**中文翻译**

这带来两个贯穿全文的后果。第一，用来评估模型的参考数据必须采用相同定义，否则准确率衡量的是类别定义之间的分歧，而不是模型表现。因此，第 3 章的标注规则以源研究为基础。第二，本研究可用的影像只有三波段 RGB，没有 NIR 通道，因此模型作者认为有用的一项输入信号在这里完全缺失；下文会再次讨论这一差异。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；本段核对值：3；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

## 2.5 领域偏移：模型跨越国界时可能出现什么问题

**英文原稿**

A model trained in one geographical setting frequently performs worse in another — domain shift, surveyed by Lyu et al. (2025) — with sources conventionally divided into sensor and resolution differences, illumination differences, and differences in the objects themselves. The problem is recognised enough that benchmarks exist to measure it. Maggiori et al. (2017) built the Inria Aerial Image Labeling benchmark so that testing is carried out over entirely different cities rather than over held-out parts of the training area, and judged the accuracy their network reached on those unseen cities to represent satisfactory generalisation. Hong et al. (2023) approach the same problem from the other side, arguing that models succeeding within a single city meet a bottleneck across cities and regions.

**中文翻译**

在一个地理环境中训练的模型，应用到另一个环境时经常表现下降；遥感文献把这一问题称为领域偏移，Lyu et al.（2025）对此作了系统综述。偏移来源通常分为传感器与分辨率差异、光照差异，以及物体本身的差异。这个问题已受到足够重视，研究者甚至建立了专门衡量它的基准。Maggiori et al.（2017）设计 Inria Aerial Image Labeling benchmark，使测试完全在不同城市进行，而不是在训练区内留出局部，并认为其网络在这些未见城市达到的准确率代表令人满意的泛化。Hong et al.（2023）从另一方向处理同一问题，指出模型在单一城市内取得成功后，跨城市和地区时会遇到性能瓶颈。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 见 [L13](#l13) Hong et al. (2023)、[L19](#l19) Lyu et al. (2025)、[L20](#l20) Maggiori et al. (2017)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

Two things about that work bear directly on this study. Maggiori et al. operate at 0.3 m with RGB bands and two classes, against 0.25 m RGB and two classes here, so their accuracy levels are a reasonable frame of reference for Chapter 4 rather than an arbitrary comparison. But those benchmarks test transfer between cities within a broadly shared building stock, whereas the transfer examined here also crosses a national boundary, an imagery programme and a different tradition of laying out car parks.

**中文翻译**

这些研究有两个方面与下文直接相关。首先，相关基准与本研究条件较接近：Maggiori et al. 使用 0.3 m RGB、两个类别；本研究使用 0.25 m RGB、两个类别，因此其准确率可以为第 4 章结果提供合理背景。但这些研究测试的是共享大致相似建筑类型的不同城市；本研究则跨越国界、影像项目，以及不同的停车场布局传统。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 见 [L20](#l20) Maggiori et al. (2017)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；本段核对值：0.3, 0.25, 4；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

Most of that literature is concerned with *correcting* domain shift through adaptation. That option is not open to the user this study has in mind. Adaptation presupposes either labelled data in the target domain or substantial engineering to exploit unlabelled data, and a planner who wants to know how much land in their city is car park has neither; their realistic option is to run the published checkpoint on the imagery they hold. The uncorrected output is therefore the object of study here, and the question is what it can still be trusted to do.

**中文翻译**

多数领域偏移研究关注如何通过适应方法*纠正*偏移。但本研究设想的使用者无法采用这种框架。领域适应需要目标地区的标注数据，或者需要大量工程工作利用无标签数据；希望知道自己城市有多少停车土地的规划人员通常两者都不具备。他们现实可行的选择，是把公开检查点直接运行在手中的影像上。因此，未经纠正的输出才是本研究对象，问题是它仍能在哪些方面受到信任。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

Stating that a model was trained in the US and applied in the UK is not on its own an analysis. Table 2.1 names the specific differences that plausibly matter for this target, and states each as an expectation the results can confirm or refute.

**中文翻译**

仅仅说“模型在美国训练、在英国应用”本身并不是分析。更有用的做法，是明确指出哪些具体差异可能影响当前目标，并把它们写成可以被结果支持或反驳的预期。表 2.1 列出了这些预期。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；本段核对值：2.1；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

**Table 2.1** Expected sources of transfer error, and the observable failure each would produce.

**中文翻译**

**表 2.1** 预期的迁移误差来源，以及每一种差异可能产生的可观察失败。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；本段核对值：2.1；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

| Difference between the training and application settings | Expected failure |
|---|---|
| British off-street car parks are typically smaller and more irregularly shaped than American ones — a prior of this study, drawn from the labelling rather than from a source, and tested rather than assumed | Failures concentrated in small lots and awkward site geometry |
| Unmarked parking is more common; the annotation rules accept vehicles plus layout as sufficient evidence | Missed lots lacking painted bay markings |
| Setts, block paving and gravel are common surfacing materials | Missed lots whose surface is not asphalt |
| Leeds lies at 53.8 °N, well north of the US cities in the training data (mostly 30–42 °N), so solar elevation is lower and shadows longer; street tree canopy is also denser | Missed or fragmented lots under shadow and canopy occlusion |
| Commercial vehicle and van share differs | Failures on lots occupied by vans and lorries rather than cars |
| The imagery used here is RGB only, with no NIR band | Vegetated ground and grass margins confused with paved parking |

**中文翻译**

| 训练环境与应用环境的差异 | 预期失败 |
|---|---|
| 英国路外停车场通常比美国停车场更小、形状更不规则——这是本研究从标注过程形成、需要检验而非直接假定的先验判断 | 错误集中在小型停车场和几何形状不规则的地点 |
| 无标线停车场更常见；标注规则允许在车辆和布局共同提供充分证据时纳入 | 漏检没有画线车位的停车场 |
| 石块、块状铺装和碎石等表面材料较常见 | 漏检表面不是沥青的停车场 |
| 利兹位于北纬 53.8°，明显高于训练数据中的美国城市（主要在北纬 30–42°）；因此太阳高度角较低、阴影较长，行道树树冠也更密集 | 阴影和树冠遮挡下的停车场被漏检或分割破碎 |
| 商用车辆和面包车比例不同 | 主要停放面包车和卡车、而不是小汽车的停车场识别失败 |
| 可用影像只有 RGB，没有 NIR 波段 | 把植被覆盖地面和草地边缘误认为铺装停车场 |

> **段落审读**
> - **逻辑用途：** 把本段论证的关键量化关系集中展示
> - **核对状态：** ✅ 已核对：表内核心数字已与项目结果 CSV 及正文恒等式复核。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；本段核对值：53.8, 30, 42；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿可补样本量、单位或不确定区间。

**英文原稿**

Each expectation implies a category in the error typology of Chapter 3 and is tested against sampled evidence in Chapter 4. Setting them out in advance also allows them to be wrong: one is substantially revised by the results, which is more informative than a set of predictions that all survive.

**中文翻译**

这些预期分别对应第 3 章错误分类中的一个类别，并通过第 4 章的抽样证据进行检验。提前列出预期也意味着分析允许自己出错：结果对其中一项预期进行了明显修正，而这比所有预期都被确认更有信息价值。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；本段核对值：3, 4；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

## 2.6 为什么 OpenStreetMap 不能作为地面真值

**英文原稿**

The obvious way to avoid manual labelling would be to validate the model against OpenStreetMap's `amenity=parking` features. OSM is the best-known instance of what Goodchild (2007) named volunteered geographic information: geographic data contributed by non-specialists outside any formal quality-control regime. The quality literature that framing prompted makes clear why the shortcut does not work.

**中文翻译**

避免人工标注的一个明显方法，是直接利用 OpenStreetMap 中的 `amenity=parking` 要素验证模型。OSM 是 Goodchild（2007）所称“自愿地理信息”最著名的例子：由非专业人员在没有正式质量控制体系的情况下贡献的地理数据。由这一概念引发的数据质量研究清楚说明了为什么这种捷径行不通。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L09](#l09) Goodchild (2007)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 把一般 VGI 结论与本研究的停车类别实测结果明确分开。

**英文原稿**

Haklay's (2010) comparison of OSM against Ordnance Survey data — the foundational UK study — found positional accuracy to be reasonable where coverage exists, but completeness to vary sharply between places, being far better in areas with more contributors. Later reviews confirm that completeness varies both between places and between feature types, though not always in the same direction: Sehra, Singh and Rai (2013) note that the urban–rural gap found in Germany and England ran the opposite way in parts of the United States, where rural coverage was in places more complete than the proprietary datasets it was compared against. Zhou, Wang and Liu (2022) look specifically at land-cover and land-use tagging and find accuracy and completeness varying substantially by category, which matters directly here because parking is recorded as a land-use-like polygon rather than as part of the road network that attracts the most contributor attention.

**中文翻译**

Haklay（2010）把 OSM 与 Ordnance Survey 数据进行比较，这也是英国相关研究的奠基性工作。研究发现，在已有覆盖的地方，OSM 位置准确度尚可，但完整性在不同地点之间差异明显；贡献者越多的地区，覆盖通常越好。之后的综述确认，完整性既随地点变化，也随要素类型变化，但方向并不一致：Sehra、Singh 和 Rai（2013）指出，德国和英国观察到的城乡差距，在美国部分地区方向相反——那里的乡村覆盖在某些方面甚至比作为比较对象的商业数据集更完整。Zhou、Wang 和 Liu（2022）专门研究土地覆盖和土地利用标签，发现不同类别的准确性和完整性差异明显。这与本研究直接相关，因为停车在 OSM 中更像一种土地利用多边形，而不是最容易吸引贡献者注意的道路网络组成部分。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：正文表述已与 Sehra et al.（2013）原文一致——该综述记录城乡完整度差异在不同国家方向不同（德、英与美国相反），正文不再断言“普遍城市高于乡村”。
> - **文献原句：** 见 [L11](#l11) Haklay (2010)、[L27](#l27) Sehra, Singh and Rai (2013)、[L32](#l32) Zhou, Wang and Liu (2022)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 缩窄该概括，或补一项直接比较英国城乡 OSM 完整度的原始研究。

**英文原稿**

There is also a definitional problem independent of completeness. As Qiam, Devunuri and Lehe observe, OSM parking polygons are frequently drawn to parcel boundaries rather than to the edge of the paved surface, so even a perfectly complete OSM layer would disagree with an imagery-derived one at the margins.

**中文翻译**

除了完整性，还有一个独立的定义问题。Qiam、Devunuri 和 Lehe 指出，OSM 停车多边形经常沿地块边界绘制，而不是沿铺装表面边缘绘制。因此，即使 OSM 停车图层完全没有遗漏，它仍然会在边缘处与影像标注发生分歧。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 见 [L24](#l24) Qiam, Devunuri and Lehe (2025)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

OSM is therefore treated in this study in two distinct roles, kept strictly separate. Its building and road layers are *inputs* to the post-processing stage of the pipeline. Its parking, land-use and related layers are used only to *attribute* errors after the fact, never to decide what the map should contain. Independently, the manual reference built here allows OSM's parking completeness to be assessed rather than assumed — a secondary result reported in Chapter 4.

**中文翻译**

因此，本研究把 OSM 用于两个严格分离的角色。建筑轮廓和道路图层是后处理流程的*输入*。停车、土地利用及其他相关图层则只在事后用于*解释误差*，从不用于决定地图应当包含什么。与此同时，本研究建立的人工参考使 OSM 停车完整性本身可以被测量，而不是被假定；这一附带结果在第 4 章报告。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；本段核对值：4；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

## 2.7 研究空白

**英文原稿**

The four literatures leave a gap where they meet. Parking is argued to be under-used urban land, but the empirical evidence for how much land it occupies is overwhelmingly American and rests on institutional records the UK does not hold in comparable form; the British evidence counts spaces rather than area, covers London rather than the country, and its own authors identify the absence of data as the central problem. English planning policy now names car parks explicitly as under-utilised land to be brought forward, and the densification literature identifies exactly the kind of city — and the kind of inner ring — where that land would matter most, but neither can point to a measurement. Segmentation models can produce such a measurement at scale, and one trained specifically for parking is publicly available, but the parking segmentation literature reports accuracy as an endpoint, and the transfer literature is largely concerned with correcting domain shift rather than characterising the residual reliability of an uncorrected transfer. And the reference dataset that would let a UK user check the output for themselves is incomplete in ways that vary from place to place.

**中文翻译**

上述四组文献在交汇处留下了一个空白。停车被认为是一种利用不足的城市土地，但关于它究竟占用多少土地的实证证据主要来自美国，并依赖英国没有同类形式的机构记录。英国证据统计车位而不是面积，集中于伦敦而不是全国，而且研究者自己把数据缺失视为核心问题。英格兰规划政策现在明确把停车场列为应推动利用的低效土地；城市密度提升研究也指出了这种土地可能最重要的城市类型和内侧环带，但两者都无法引用一项实际测量。分割模型可以大规模生成这种测量，而且已经有专门识别停车场的公开模型；但停车分割研究把准确率当作终点，迁移研究则主要关心如何纠正领域偏移，而不是描述未经纠正的迁移结果仍具有何种可靠性。与此同时，能够让英国使用者自行检查结果的现成参考数据，又以随地点变化的方式存在缺失。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

The gap this dissertation addresses is therefore not that nobody has mapped parking in Leeds. It is that a scalable method exists whose transferred output has never been tested in a way that establishes *what it can be used for*. Reporting a precision and a recall does not answer that question. Establishing which errors are boundary effects, which are systematic confusions, which are disagreements about definition, and which are artefacts of the processing pipeline — and then testing whether the residual bias is stable enough to be corrected, and at what spatial grain — does. That is the contribution attempted here.

**中文翻译**

因此，本论文要解决的空白并不是“从来没有人绘制过利兹停车场”。真正的空白是：一种可扩展的方法已经存在，但其迁移输出从未经过一种能够确定*它究竟可以用于什么*的检验。只报告精确率和召回率无法回答这一问题。必须进一步确定：哪些错误是边界效应，哪些是系统性混淆，哪些来自定义分歧，哪些是处理流程的人为产物；然后检验剩余偏差是否稳定到足以校正，以及这种校正在什么空间尺度上成立。本研究尝试作出的贡献正在于此。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 作者论证／章节结构，无独立数据；译文对应位置：`02_background.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

# 3. 研究方法

**英文原稿**

This chapter sets out how the transfer was tested. It describes the study area and the imagery the model consumed (3.1), the annotation protocol used to build an independent reference (3.2), the segmentation pipeline itself (3.3), and the accuracy measures (3.4). It then sets out the two complementary procedures used to characterise error — automated attribution against reference layers (3.5) and stratified sampling with visual adjudication (3.6) — followed by the ablation design used to isolate the contribution of post-processing (3.7). Two checks close the chapter: one on the imagery underlying the reference and the predictions (3.8), and one on the estimator used to correct the model's systematic bias (3.9).

**中文翻译**

本章说明如何检验模型迁移。第 3.1 节介绍研究区和模型使用的影像；第 3.2 节说明如何建立独立人工参考；第 3.3 节介绍分割流程；第 3.4 节定义准确率指标。随后，第 3.5 节用外部参考图层自动归因误差，第 3.6 节用分层抽样和人工判读补充分析，第 3.7 节用消融实验分离后处理的作用。最后，第 3.8 节检查两套影像是否一致，第 3.9 节检验用于校正系统偏差的估算方法。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 当前英文稿及项目内证据链；本段核对值：3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

## 3.1 研究区与数据

**英文原稿**

The study area is a 100 km² square centred on Leeds, divided into one hundred 1 km² cells on the British National Grid (Figure 3.1). The city centre is taken as City Square (E 429832, N 433449); cell centroids lie between 0.34 km and 7.64 km from it. Leeds was chosen as a large English city outside London with substantial surface parking in and around its core, and with complete aerial coverage at the resolution the model requires. A square grid rather than an administrative boundary was used so that every cell is an equal-area unit and per-cell statistics are directly comparable. The choice of areal unit is not neutral — figures computed over zones depend on how the zones are drawn, the modifiable areal unit problem (Openshaw, 1984) — so the unit is held constant throughout and whole-area figures are reported alongside per-cell ones.

**中文翻译**

研究区是一个以利兹为中心、面积 100 km² 的正方形，按英国国家格网划分为 100 个 1 km² 单元（图 3.1）。市中心定义为 City Square（E 429832，N 433449），各单元中心距它 0.34–7.64 km。选择利兹，是因为它是伦敦以外的大型英格兰城市，市中心及周边有大量地面停车场，而且具备模型所需分辨率的完整航空影像。采用规则方格而不是行政边界，是为了让每个单元面积相同、统计结果可直接比较。不过，分区方式会影响统计结果，即“可变空间单元问题”（Openshaw, 1984）。因此，全文始终使用同一套单元，并同时报告全区和单元级结果。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 见 [L23](#l23) Openshaw (1984)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** `fine-tuning/leeds_grid.gpkg`；`manual/leeds_manual.gpkg`；Digimap 图块元数据；本段核对值：100, 1, 3.1, 429832, 433449, 0.34, 7.64；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

![研究区](figures/fig_study_area.png)

**英文原稿**

**Figure 3.1** The study area: one hundred 1 km² validation cells on the British National Grid, the 2,037 manually labelled surface parking polygons, and distance rings from City Square. Labelled parking is visibly concentrated in a band around, rather than at, the centre — a pattern quantified in 4.7.

**中文翻译**

**图 3.1** 研究区：英国国家格网上的 100 个 1 km² 验证单元、2,037 个人工标注的地面停车场多边形，以及以 City Square 为中心的距离环带。图上可见，停车场主要集中在市中心外围的一圈，而不是最中心；第 4.7 节会量化这一现象。

> **段落审读**
> - **逻辑用途：** 说明图件承载的证据
> - **核对状态：** 🟨 需人工复核：图由项目分析脚本及对应 CSV 生成。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `fine-tuning/leeds_grid.gpkg`；`manual/leeds_manual.gpkg`；Digimap 图块元数据；本段核对值：3.1, 100, 1, 2,037, 4.7；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿检查图例、单位、色盲可读性和印刷尺寸。

**英文原稿**

The imagery is Getmapping aerial photography supplied through Digimap: 109 tiles at 0.25 m ground sample distance, three visible bands (RGB), projected in EPSG:27700. The tiles carry three version suffixes — `_03` (79 tiles), `_04` (20) and `_05` (10) — reflecting different processing runs. All spatial operations are carried out in EPSG:27700, whose units are metres, so polygon areas are read directly in m² without further projection.

**中文翻译**

模型使用 Getmapping 航空影像，由 Digimap 提供：共 109 个图块，地面采样距离 0.25 m，三个可见光波段（RGB），投影为 EPSG:27700。文件有三个版本后缀：\`_03\` 79 个、\`_04\` 20 个、\`_05\` 10 个，表示不同的拍摄或处理批次；下载资料没有公布拍摄日期，这一限制在第 3.8 节讨论。所有空间运算都在以米为单位的 EPSG:27700 中完成，因此多边形面积可直接以 m² 读取。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `fine-tuning/leeds_grid.gpkg`；`manual/leeds_manual.gpkg`；Digimap 图块元数据；本段核对值：109, 0.25, 27700, 03, 79, 04, 20；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

Three reference datasets are used, none of them as ground truth. OpenStreetMap building footprints and road centrelines (retrieved 25 June 2026) are inputs to the post-processing stage. OpenStreetMap land use, brownfield, pitch and `amenity=parking` polygons are used only to attribute errors after the fact. Ordnance Survey Open Greenspace supplies sports facilities. The distinction matters: reference layers are used here to explain where errors fall, and — with the deliberate exception tested in 3.7 — never to decide what the map should contain.

**中文翻译**

研究使用三组参考数据，但都不直接当作“真实答案”。OpenStreetMap（OSM）建筑轮廓和道路中心线（2026 年 6 月 25 日获取）用于后处理；OSM 土地利用、棕地、运动场和 \`amenity=parking\` 多边形只用于事后解释误差；Ordnance Survey Open Greenspace 提供体育设施数据。关键区别是：除了第 3.7 节专门测试的情况外，参考图层只解释错误出现在哪里，不决定最终地图应该包含什么。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `fine-tuning/leeds_grid.gpkg`；`manual/leeds_manual.gpkg`；Digimap 图块元数据；本段核对值：6, 25, 3.7；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把一般 VGI 结论与本研究的停车类别实测结果明确分开。

**英文原稿**

Appendix D lists the code repository, the licensing position of each dataset and the file behind every table reported here. The aerial imagery is licensed to the institution and cannot be redistributed; everything else, including the manual reference labels, is available.

**中文翻译**

附录 D 列出代码仓库、各数据集的许可状态，以及论文每张表所对应的源文件。航空影像由学校持有许可，不能再分发；其余材料（包括人工参考标签）均可获得。

> **段落审读**
> - **逻辑用途：** 交代复现材料与许可边界
> - **核对状态：** ✅ 已核对：已与附录 D、仓库目录和影像许可说明核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `fine-tuning/leeds_grid.gpkg`；`manual/leeds_manual.gpkg`；Digimap 图块元数据；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 公开提交后补充仓库版本号或 DOI，避免后续文件变化影响复现。

## 3.2 标注规则

**英文原稿**

Accuracy figures are only meaningful against a reference that follows the definition the model was trained on. The annotation rules therefore follow those of Qiam, Devunuri and Lehe (2025), whose dataset the model was trained on, and are reproduced in full in Appendix A. The target is off-street surface parking: open-air parking surfaces visible from above, outside the public road. Labels are binary. No minimum size threshold is applied. Marked bays and the aisles connecting them are included, as is rooftop parking where the parking surface is visible from above; on-street parking and enclosed multi-storey structures are excluded. Where markings are absent, an area is labelled only where parked vehicles and a bay-and-aisle layout together make the use unambiguous. Boundaries are drawn at the edge of the paving rather than the parcel line.

**中文翻译**

准确率只有在参考数据与模型训练时采用同一定义时才有意义。因此，标注规则遵循 Qiam、Devunuri 和 Lehe（2025）的训练数据规则，完整版本见附录 A。目标是公共道路以外、从上方可见的露天停车面。标签为二元标签，不设最小面积。包括停车位及连接车位的通道，也包括从上方可以看见停车面的屋顶停车场；不包括路边停车和封闭式多层停车楼。若没有标线，只有当停放车辆和“车位—通道”布局同时清楚表明停车用途时才标注。边界沿铺装面边缘绘制，而不是沿地块边界。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L24](#l24) Qiam, Devunuri and Lehe (2025)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** `manual/leeds_manual.gpkg`；`Rules.md`；附录 A；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

One boundary inside residential parking is worth stating explicitly, because it is the commonest ambiguous case in a British city. Parking courts shared between several dwellings are labelled; driveways and forecourts serving a single household are not. A communal court resembles a small car park in layout and in what it does, while a single driveway does not. The distinction is not introduced here: UK parking measurement already separates private residential parking into driveway and communal categories, and the two were surveyed and reported separately in the London study described in §2.2 (Bates and Leibling, 2012).

**中文翻译**

住宅停车内部有一条边界值得明确，因为它是英国城市中最常见的模糊情况。服务多户的共享停车院予以标注，单户住宅的私家车道和前院则不标注。公共停车院的布局和功能类似小型停车场，而单户车道并非如此。这一区分不是本研究凭空引入：§2.2 所述伦敦研究已经把私人住宅停车分为车道和公共停车两类，并分别调查、报告（Bates and Leibling, 2012）。

> **段落审读**
> - **逻辑用途：** 明确最常见的类别边界，并为后续“定义差异”误差提供依据
> - **核对状态：** ✅ 已核对：已与当前英文稿、附录 A 和 Bates and Leibling（2012）的分类口径核对。
> - **文献原句：** 见 [L01](#l01) Bates and Leibling (2012)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** `manual/leeds_manual.gpkg`；`Rules.md`；附录 A；本段核对值：2.2；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充典型单户车道与公共停车院的配对图例。

**英文原稿**

Labelling was carried out in QGIS by a single annotator over a satellite basemap, producing 2,037 polygons with a confidence attribute (3 = clear, 2 = fairly clear, 1 = uncertain) and a free-text note used to flag rooftop cases. Summed individually the polygons cover 3.2677 km². Dissolving them leaves both the area and the part count unchanged, so no two labelled polygons overlap; the reference is nonetheless dissolved before every comparison, since the accuracy measures of 3.4 are only well defined on non-overlapping geometry and the property should be enforced rather than assumed. Clipping to the study grid removes 0.0081 km² where polygons cross the outer boundary, giving the **3.2597 km²** used throughout. One cell (c0r9) contains no labelled parking, so recall is undefined there and per-cell statistics involving recall use $n = 99$.

**中文翻译**

一名标注者在 QGIS 中依据卫星底图完成标注，共得到 2,037 个多边形。每个多边形附有置信度（3＝明确，2＝较明确，1＝不确定）和自由文本备注，用来标记屋顶停车等情况。逐个求和的面积为 3.2677 km²；融合后面积和部件数不变，说明标注多边形彼此不重叠。尽管如此，每次比较前仍会先融合，因为第 3.4 节的指标要求几何不重叠。裁剪到研究区边界后，去掉跨出外边界的 0.0081 km²，最终得到全文使用的 **3.2597 km²**。一个单元（c0r9）没有标注停车，因此该单元的召回率无定义，涉及召回率的逐单元统计使用 \(n=99\)。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `manual/leeds_manual.gpkg`；`Rules.md`；附录 A；本段核对值：2,037, 3, 2, 1, 3.2677, 3.4, 0.0081；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 继续明确 3.26% 来自人工参考而非模型估计，并避免把 3.30% 当作独立观测。

**英文原稿**

Single-annotator labelling is a limitation with a measurable consequence rather than a generic caveat. Detection rates fall systematically with annotator confidence (4.3), so the reference itself places a ceiling on measurable accuracy; this is quantified in the results and returned to in the discussion.

**中文翻译**

单人标注不是一句笼统的局限，而会产生可测量的后果：标注置信度越低，模型检出率也系统性下降（第 4.3 节）。这说明参考数据本身给可测准确率设定了上限，结果章和讨论章会进一步分析。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `manual/leeds_manual.gpkg`；`Rules.md`；附录 A；本段核对值：4.3；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

## 3.3 模型与处理流程

**英文原稿**

The model is the SegFormer (Xie et al., 2021) parking-lot segmentation network released by Qiam, Devunuri and Lehe (2025). The released checkpoint is a B5 configuration whose backbone was initialised from Cityscapes weights and fine-tuned by those authors on their parking dataset, as documented in the released model card and repository. The published checkpoint is used exactly as released. **No UK imagery was used to adjust the weights**, so what is measured here is zero-shot transfer: the accuracy a UK user would obtain by taking the model off the shelf. The primary analysis retains that checkpoint throughout. A separate supplementary experiment, reported in Appendix C, compares generic fine-tuning, positional targeted loss weighting and validation-selected thresholding on raw pixel output from a fixed 40/10/50 cell split; none of its figures enters the analysis that follows.

**中文翻译**

本研究使用 Qiam、Devunuri 和 Lehe（2025）发布的 SegFormer（Xie et al., 2021）停车场分割网络。发布的检查点采用 B5 配置，骨干网络由 Cityscapes 权重初始化，再由原作者用停车场数据微调，出处为发布的模型卡与仓库。本研究直接使用公开检查点，**没有用英国影像调整任何权重**。因此测量的是“零样本迁移”：英国用户直接拿来使用时会得到怎样的准确率。主分析始终保留这一检查点；附录 C 另行比较普通微调、位置定向损失加权和验证集阈值选择，使用固定 40/10/50 单元划分的原始像素输出，其任何数字都不进入下文主分析。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L24](#l24) Qiam, Devunuri and Lehe (2025)、[L31](#l31) Xie et al. (2021)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** `parking-lot-mapping-tool/inference.py`；`post_processing_uk.py`；`analysis/ablation_summary.csv`；本段核对值：40, 10, 50；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把文献的一般机制与利兹案例的可检验预期逐项对应。

![处理流程](figures/fig_pipeline.png)

**英文原稿**

**Figure 3.2** The processing chain. Prediction runs from Digimap tile to two outputs — before and after post-processing — which the ablation of 3.7 compares against each other. The manual reference and the model outputs meet at the accuracy measures of 3.4; the reference layers enter only at the error-attribution stage of 3.5–3.6.

**中文翻译**

**图 3.2** 处理链。Digimap 图块经过预测后产生后处理前、后两套结果，第 3.7 节的消融实验比较两者。人工参考和模型输出只在第 3.4 节的准确率计算处相遇；参考图层只进入第 3.5–3.6 节的误差归因阶段。

> **段落审读**
> - **逻辑用途：** 说明图件承载的证据
> - **核对状态：** 🟨 需人工复核：图由项目分析脚本及对应 CSV 生成。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `parking-lot-mapping-tool/inference.py`；`post_processing_uk.py`；`analysis/ablation_summary.csv`；本段核对值：3.2, 3.7, 3.4, 3.5, 3.6；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿检查图例、单位、色盲可读性和印刷尺寸。

**英文原稿**

The pipeline proceeds in five stages. Digimap tiles and their world files are converted to georeferenced GeoTIFFs. Each tile is cut into 512 × 512 pixel patches, zero-padded at the edges. Patches are passed through the network and the upsampled logits reduced to a binary mask by argmax. Masks are cleaned with a mode filter and vectorised by contour extraction, with components below 1,000 px² (about 62 m² at 0.25 m) discarded and enclosed holes subtracted; polygons are then transformed from pixel to grid coordinates and merged across tiles.

**中文翻译**

流程分五步。首先把 Digimap 图块及其世界文件转换成带地理坐标的 GeoTIFF；然后切成 512 × 512 像素的小块，边缘用零填充；接着输入网络，将上采样后的 logits 通过 argmax 变成二元掩膜；再用众数滤波清理掩膜并提取轮廓，删除小于 1,000 px² 的部分（在 0.25 m 分辨率下约 62 m²），同时扣除内部孔洞；最后把多边形从像素坐标转换到格网坐标，并跨图块合并。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `parking-lot-mapping-tool/inference.py`；`post_processing_uk.py`；`analysis/ablation_summary.csv`；本段核对值：512, 1,000, 0.25, 62；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

Two post-processing subtractions follow, both UK-specific. OpenStreetMap building footprints are subtracted, on the reasoning that a roof cannot be surface parking. Road centrelines are buffered by carriageway class (Table 3.1), dissolved, and subtracted.

**中文翻译**

随后进行两项针对英国数据的扣除。第一，扣除 OSM 建筑轮廓，因为屋顶不应被当成地面停车。第二，按道路等级为 OSM 道路中心线设置缓冲距离（表 3.1），融合后从预测中扣除。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `parking-lot-mapping-tool/inference.py`；`post_processing_uk.py`；`analysis/ablation_summary.csv`；本段核对值：3.1；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

**Table 3.1** Road buffer half-widths by OSM `highway` class. Where a `lanes` tag is present, the width is the greater of the tabulated value and 3 m per lane.

**中文翻译**

**表 3.1** 各 OSM \`highway\` 类别的道路缓冲半宽。如果有 \`lanes\` 标签，则取表中宽度和“每车道 3 m”两者中的较大值。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `parking-lot-mapping-tool/inference.py`；`post_processing_uk.py`；`analysis/ablation_summary.csv`；本段核对值：3.1, 3；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

| Class | Width (m) | | Class | Width (m) |
|---|---:|---|---|---:|
| motorway | 14 | | tertiary | 7 |
| trunk | 12 | | tertiary_link | 5 |
| primary | 10 | | unclassified | 5 |
| secondary | 8 | | residential | 5 |
| motorway_link | 9 | | living_street | 4 |
| trunk_link | 8 | | *default* | *5* |
| primary_link | 7 | | | |
| secondary_link | 6 | | | |

**中文翻译**

| 类别 | 宽度（m） | | 类别 | 宽度（m） |
|---|---:|---|---|---:|
| motorway | 14 | | tertiary | 7 |
| trunk | 12 | | tertiary_link | 5 |
| primary | 10 | | unclassified | 5 |
| secondary | 8 | | residential | 5 |
| motorway_link | 9 | | living_street | 4 |
| trunk_link | 8 | | *默认值* | *5* |
| primary_link | 7 | | | |
| secondary_link | 6 | | | |

> **段落审读**
> - **逻辑用途：** 把本段论证的关键量化关系集中展示
> - **核对状态：** ✅ 已核对：表内核心数字已与项目结果 CSV 及正文恒等式复核。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `parking-lot-mapping-tool/inference.py`；`post_processing_uk.py`；`analysis/ablation_summary.csv`；本段核对值：14, 7, 12, 5, 10, 8, 9；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿可补样本量、单位或不确定区间。

**英文原稿**

The half-widths are approximations by class rather than measured carriageway dimensions: each value is a plausible half-width for the road type the OSM class denotes, with 5 m applied to any class not listed. Footways, cycleways, bridleways, tracks, steps, pedestrian ways and **service roads** are excluded from the road layer, service roads in particular because they commonly run *through* car parks; buffering them would remove the aisles the protocol explicitly includes. Both subtractions are evaluated rather than assumed in 3.7.

**中文翻译**

这些半宽按道路类别近似，而非实测车行道尺寸：每个值都是相应 OSM 类别的合理半宽，未列类别统一取 5 m。道路图层排除步道、自行车道、马道、土路、台阶、步行道路和**服务道路**。尤其排除服务道路，是因为它们经常穿过停车场；若缓冲并扣除，会删掉标注规则明确要求保留的停车通道。第 3.7 节会实际检验这两项扣除是否有用，而不是预先假定它们有用。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `parking-lot-mapping-tool/inference.py`；`post_processing_uk.py`；`analysis/ablation_summary.csv`；本段核对值：5, 3.7；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

The output before subtraction (6,814 polygons) and after (8,180 polygons) are both retained. The increase in count reflects single lots being split by the subtracted geometry, which is why polygon counts are never interpreted as numbers of car parks.

**中文翻译**

后处理前保留 6,814 个多边形，后处理后为 8,180 个。数量上升是因为扣除的几何把一个停车场切成多个部分，所以全文不把多边形数量解释成停车场数量。

> **段落审读**
> - **逻辑用途：** 组织章节、概括贡献或承接后文
> - **核对状态：** 🟨 结构性判断：已检查与全文结构一致；不存在独立原数据。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `parking-lot-mapping-tool/inference.py`；`post_processing_uk.py`；`analysis/ablation_summary.csv`；本段核对值：6,814, 8,180；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 确保每项预告或贡献都能回指具体章节和证据。

## 3.4 验证设计

**英文原稿**

Accuracy is measured by area rather than by object, following the general practice in land-cover accuracy assessment of comparing a map against an independent reference over a defined spatial support (Foody, 2002; Olofsson et al., 2014). Let $M$ and $R$ denote the dissolved model and reference geometry, and $|\cdot|$ denote area in m². Dissolving before comparison ensures overlapping geometry is not double-counted. The three quantities are then set operations:

**中文翻译**

参考土地覆盖准确率评估的通行做法，本研究按面积而不是按对象计算准确率，即在确定的空间范围内把地图与独立参考比较（Foody, 2002; Olofsson et al., 2014）。设 \(M\) 为融合后的模型几何，\(R\) 为融合后的参考几何，\(|\cdot|\) 表示面积（m²）。先融合可避免重叠几何被重复计算。三个基本量为：

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L07](#l07) Foody (2002)、[L22](#l22) Olofsson et al. (2014)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

$$
\mathrm{TP} = M \cap R, \qquad \mathrm{FP} = M \setminus R, \qquad \mathrm{FN} = R \setminus M
$$

**中文翻译**

\[
\mathrm{TP}=M\cap R,\qquad
\mathrm{FP}=M\setminus R,\qquad
\mathrm{FN}=R\setminus M
\]

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

from which

**中文翻译**

由此得到：

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

$$
\text{precision} = \frac{|\mathrm{TP}|}{|\mathrm{TP}| + |\mathrm{FP}|}, \qquad
\text{recall} = \frac{|\mathrm{TP}|}{|\mathrm{TP}| + |\mathrm{FN}|}, \qquad
\text{IoU} = \frac{|\mathrm{TP}|}{|\mathrm{TP}| + |\mathrm{FP}| + |\mathrm{FN}|}
$$

**中文翻译**

\[
\text{精确率}=\frac{|\mathrm{TP}|}{|\mathrm{TP}|+|\mathrm{FP}|},\qquad
\text{召回率}=\frac{|\mathrm{TP}|}{|\mathrm{TP}|+|\mathrm{FN}|},\qquad
\text{IoU}=\frac{|\mathrm{TP}|}{|\mathrm{TP}|+|\mathrm{FP}|+|\mathrm{FN}|}
\]

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

Area-based measures were chosen over object-based matching because the question is how much land the map assigns to parking, and because object matching would require an arbitrary rule for when a split or merged polygon counts as the same lot — a rule the post-processing stage makes particularly unstable. The unit on which accuracy is assessed is itself a design decision rather than a given, and one that governs what the resulting figures mean: no assessment unit is universally correct, so what matters is recognising what the choice does to the numbers (Stehman and Wickham, 2011; Stehman and Foody, 2019). As an internal check, $|M| = |\mathrm{TP}| + |\mathrm{FP}|$ and $|R| = |\mathrm{TP}| + |\mathrm{FN}|$; both hold to four decimal places.

**中文翻译**

选择面积指标，是因为本研究关心地图把多少土地判为停车场。若按对象匹配，就必须人为规定：一个停车场被拆分或多个停车场被合并时，何时算同一个对象；后处理又会让这种规则尤其不稳定。准确率所采用的评估单元本身就是设计选择，而不是天然给定；这个选择会决定结果的含义。不存在普遍正确的评估单元，关键是认识所选单元会怎样改变数字（Stehman and Wickham, 2011; Stehman and Foody, 2019）。作为内部核对，\(|M|=|\mathrm{TP}|+|\mathrm{FP}|\) 以及 \(|R|=|\mathrm{TP}|+|\mathrm{FN}|\)，两式都在小数点后四位成立。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L29](#l29) Stehman and Foody (2019)、[L30](#l30) Stehman and Wickham (2011)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

Two aggregations over the $n$ cells are reported. Writing $\mathrm{TP}_c$ for the true positive area within cell $c$, the **micro** (area-weighted) and **macro** (cell-averaged) forms of precision are

**中文翻译**

本文报告两种单元汇总方式。若 \(\mathrm{TP}_c\) 表示单元 \(c\) 中的真阳性面积，则精确率的 **micro（按面积加权）** 和 **macro（单元平均）** 形式为：

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

$$
p_{\text{micro}} = \frac{\sum_c |\mathrm{TP}_c|}{\sum_c\left(|\mathrm{TP}_c| + |\mathrm{FP}_c|\right)},
\qquad
p_{\text{macro}} = \frac{1}{n}\sum_c \frac{|\mathrm{TP}_c|}{|\mathrm{TP}_c| + |\mathrm{FP}_c|}
$$

**中文翻译**

\[
p_{\text{micro}}=
\frac{\sum_c|\mathrm{TP}_c|}
{\sum_c(|\mathrm{TP}_c|+|\mathrm{FP}_c|)},\qquad
p_{\text{macro}}=
\frac{1}{n}\sum_c
\frac{|\mathrm{TP}_c|}
{|\mathrm{TP}_c|+|\mathrm{FP}_c|}
\]

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；本段核对值：1；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

and recall and IoU follow the same pattern. The terms are borrowed from classification evaluation, where the same two averages are taken over classes; here they are taken over spatial units. The micro figure treats the whole study area as one unit, so large car parks carry proportionate weight; it answers whether the *total area* is right, and because summing over cells returns the whole-area quantity, it does not depend on how the cells were drawn. The macro figure weights every cell equally regardless of how much parking it contains, and does depend on it. The two are reported side by side because a global figure summarises the map as a whole while masking how accuracy varies across it, and local accuracy is better reported as an accompaniment to the global figure than in place of it (Foody, 2005; Stehman and Foody, 2019). Doing so needs a reference dense enough to support a figure in every sub-region, ordinarily the obstacle to it; here the reference is wall-to-wall rather than sampled, so every cell carries its own. Macro is used as a diagnostic of uniformity rather than as an estimator of any population quantity, and the difference between the two is itself the result: where macro falls below micro, the model is performing worse in cells with little parking than the area-weighted figure suggests.

**中文翻译**

召回率和 IoU 以同样方式计算。这两个术语借自分类评估：分类评估是在类别间取两种平均，这里则是在空间单元间取平均。Micro 把整个研究区视为一个单元，让大停车场按其面积获得相应权重；它回答的是“总面积是否正确”。由于跨单元求和会还原全区总量，micro 不依赖网格边界怎样划定。Macro 则不论停车面积多少都赋予每个单元相同权重，因此会受网格划分影响。两者并列报告，是因为全局数字虽能概括整张地图，却会掩盖准确率的空间差异；局部准确率更适合作为全局准确率的补充，而不是替代（Foody, 2005; Stehman and Foody, 2019）。通常，要在每个子区域报告指标，需要足够密集的参考数据；本研究使用全覆盖而不是抽样参考，因此每个单元都有自己的指标。Macro 在这里仅用于诊断表现是否均匀，而不用于估计任何总体量。两种汇总之间的差异本身就是结果：macro 低于 micro 时，说明停车较少的单元表现更差，而面积加权数字会掩盖这一点。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 见 [L08](#l08) Foody (2005)、[L29](#l29) Stehman and Foody (2019)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 可再明确 macro 是空间均匀性诊断量，不是总体停车面积的估计量。

## 3.5 误差类型 I：自动归因

**英文原稿**

The first characterisation of error asks where FP and FN area falls relative to independent layers. It is applied exhaustively to all of it.

**中文翻译**

第一种误差分析检查全部 FP 和 FN 分别落在独立参考图层的什么位置。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

**Boundary effects are separated first.** An area-based measure treats segmentation as pixel-level classification and returns a single figure in which a car park drawn slightly too wide and a car park invented in the wrong place are indistinguishable (Csurka, Larlus and Perronnin, 2013). The segmentation literature's response has been to evaluate within a band of fixed distance from the contour: Boundary IoU computes overlap only over pixels lying within a specified distance of the boundary, recovering a sensitivity to boundary error that mask IoU loses — particularly for large objects, whose interiors dominate the score (Cheng et al., 2021). The construction used here is of that family but serves a different purpose. Rather than producing a boundary-aware score, it partitions the error, so that the boundary component and the remainder can be reported separately and attributed to different causes.

**中文翻译**

**首先分离边界效应。** 面积型指标把分割视为像素分类，因此无法区分“把同一停车场画得稍宽”和“在错误地点凭空画出停车场”（Csurka, Larlus and Perronnin, 2013）。分割研究常在轮廓周围的固定距离带内评估；Boundary IoU 只计算距边界指定距离内像素的重叠，从而恢复普通 mask IoU 对边界误差失去的敏感性，尤其适用于内部像素主导分数的大对象（Cheng et al., 2021）。本文采用同一家族的构造，但目的不是生成一个边界感知分数，而是把误差划分为边界成分与剩余成分，以便分别报告并归因于不同原因。

> **段落审读**
> - **逻辑用途：** 说明为何必须把边界误差与独立识别错误拆开
> - **核对状态：** ✅ 已核对：Csurka et al.（2013）与 Cheng et al.（2021）的论断已在 `citation_audit.md` 中对照原文。
> - **文献原句：** 见 [L03](#l03) Cheng et al. (2021)、[L05](#l05) Csurka et al. (2013)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 明确本文方法与正式 Boundary IoU 指标的差别，避免被误读为直接采用该分数。

**英文原稿**

FP area within a fixed distance $d$ of a labelled lot is boundary *dilation* — the model drawing the same car park slightly too large — as distinct from a standalone false detection elsewhere. Symmetrically, FN area within $d$ of a predicted area is *erosion*: reference area the model did not cover, but lying immediately alongside something it did find.

**中文翻译**

距离标注停车场 \(d\) 米以内的 FP 被称为边界“外扩”：模型找到了同一个停车场，但边界画得稍大。对称地，距离预测区域 \(d\) 米以内的 FN 被称为“内缩”：模型发现了停车场，却没有覆盖紧邻预测的部分参考面积。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

$$
\mathrm{FP}_{\text{dilation}}(d) = \mathrm{FP} \cap \big(R \oplus d\big), \qquad
\mathrm{FN}_{\text{erosion}}(d) = \mathrm{FN} \cap \big(M \oplus d\big)
$$

**中文翻译**

\[
\mathrm{FP}_{\text{dilation}}(d)=\mathrm{FP}\cap(R\oplus d),\qquad
\mathrm{FN}_{\text{erosion}}(d)=\mathrm{FN}\cap(M\oplus d)
\]

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

where $\oplus$ denotes dilation by a buffer of $d$ metres. Erosion is defined against the *prediction* rather than against the reference boundary, so that it captures only reference area adjacent to a detection; defining it against the reference boundary would also count the outer edge of lots the model missed entirely, which is a detection failure rather than a boundary effect. Because no threshold separates the two cleanly, results are reported at $d = 2$, 5 and 10 m, with 5 m used as the working value. Sensitivity to the width chosen is a known property of band-based measures rather than a peculiarity of this application (Cheng et al., 2021), which is why three are given. That 5 m is a convention rather than a natural break is also visible in the sampled evidence: the sampled FP fragments that no category explained sit at a median distance of exactly 5.0 m from the nearest labelled lot, against 42–169 m for every substantive category (4.6).

**中文翻译**

其中 \(\oplus\) 表示向外缓冲 \(d\) 米。这里的 FN 内缩是相对“预测”定义的，因此只捕捉紧邻已检出区域的参考面积。若按参考边界来定义，也会把完全漏掉的停车场外围算进来，但那应是检出失败，不是边界误差。由于不存在天然阈值，本文同时报告 \(d=2\)、5 和 10 m 的结果，并把 5 m 作为主要工作值。第 4.6 节还会用数据证明这只是一个约定：无法解释的 FP 样本到最近标注停车场的中位距离恰好是 5.0 m，而各实质类别的中位距离为 42–169 m。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；本段核对值：2, 5, 10, 4.6, 5.0, 42, 169；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

**Standalone FP is then attributed in two ways, reported side by side.**

**中文翻译**

**之后用两种方式归因独立 FP，并把结果并列报告。**

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

- An **exclusive partition**: reference layers $L_1,\dots,L_k$ are peeled off in sequence, each claiming only the area not already claimed, so shares sum to 100%. Layers are ordered by how precisely they locate the phenomenon — building footprints and sports pitches, which are exact polygons, before road proximity buffers, before broad land-use classes — with industrial and commercial land last because it is the least specific evidence.
- An **unordered overlap**: each layer is intersected with all FP independently, $\mathrm{FP} \cap L_j$, so categories may overlap one another and need not sum to 100%.

**中文翻译**

- **互斥划分：** 按顺序从 FP 中扣除参考图层 \(L_1,\ldots,L_k\)，每个图层只能认领尚未被前面图层认领的面积，所以各项合计为 100%。顺序按定位精确程度安排：建筑轮廓和运动场等精确多边形在前，道路邻近缓冲区其次，范围较宽泛的工业和商业用地最后。
- **非互斥重叠：** 每个图层都单独与全部 FP 相交，即 \(\mathrm{FP}\cap L_j\)。不同类别可以重叠，因此总和不必等于 100%。

> **段落审读**
> - **逻辑用途：** 把并列规则或步骤拆成可执行清单
> - **核对状态：** 🟨 需人工复核：与相应代码、协议或实验日志一致。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；本段核对值：1, 100%；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 必要时为每项补充通过／失败判据。

**英文原稿**

Presenting both means the substantive conclusions do not depend on an ordering decision I made; as a robustness check, moving industrial land from an early position to last changes its exclusive share from 30.0% to 29.6%. **The two have different denominators and are not differences of one another** — a point carried into the results tables, where the exclusive column includes the dilation band as its first row so that it sums to 100%.

**中文翻译**

两种结果同时给出，可以避免结论依赖作者选择的顺序。稳健性检查显示，把工业用地从前面移到最后，其互斥占比只从 30.0% 变为 29.6%。需要注意，两列的分母和含义不同，不能彼此相减。结果表中，互斥列把边界外扩作为第一项，因此总和为 100%。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；本段核对值：30.0, 29.6, 100%；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

**FN is defined at the level of the car park, not the fragment.** An earlier version defined missed parking as reference area more than 5 m from any prediction, which conflated genuinely undetected car parks with the ragged edges of ones the model had largely found. Two diagnostics showed this: of 297 such fragments, 221 lay at a distance of exactly 5.0 m — the threshold itself — and 19.2% of the area belonged to lots the model had detected to better than 70%. FN is therefore partitioned by the *coverage* of the lot it belongs to, $\gamma = |R_i \cap M| / |R_i|$:

**中文翻译**

**FN 按整个停车场，而不是按碎片分类。** 早期方法把“距任何预测超过 5 m 的参考面积”定义为漏检，但这会把完全没找到的停车场与已找到停车场的毛糙边缘混在一起。297 个这类碎片中，有 221 个距预测恰好 5.0 m，19.2% 的面积甚至属于覆盖率超过 70% 的停车场。因此，FN 改为按所属停车场的覆盖率 \(\gamma=|R_i\cap M|/|R_i|\) 分类：

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；本段核对值：5, 297, 221, 5.0, 19.2, 70%；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

| Class | Coverage | Treatment |
|---|---|---|
| whole lot missed | $\gamma \le 0.10$ | a detection failure |
| partly detected | $0.10 < \gamma \le 0.70$ | partial failure |
| fringe of detected lot | $\gamma > 0.70$ | boundary imprecision |

**中文翻译**

| 类别 | 覆盖率 | 处理方式 |
|---|---|---|
| 整个停车场漏检 | \(\gamma\le0.10\) | 检出失败 |
| 部分检出 | \(0.10<\gamma\le0.70\) | 部分失败 |
| 已检出停车场的边缘 | \(\gamma>0.70\) | 边界不精确 |

> **段落审读**
> - **逻辑用途：** 把本段论证的关键量化关系集中展示
> - **核对状态：** ✅ 已核对：表内核心数字已与项目结果 CSV 及正文恒等式复核。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；本段核对值：10, 0.10, 70, 0.70；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿可补样本量、单位或不确定区间。

**英文原稿**

Both cut points are conventions, as the 5 m band is, and both were varied. The lower one is not load-bearing: from $\gamma \le 0.05$ to $\gamma \le 0.20$ the whole-lot-missed share moves between 22.3% and 29.9% of FN, and the residual left as genuine non-detection between 2.0% and 2.9% of labelled area, so what is concluded from it does not turn on where it sits. The upper one is more consequential — at 0.60, 0.70 and 0.80 the fringe class takes 51.0%, 44.4% and 31.9% of FN — so that share is quoted with its threshold attached.

**中文翻译**

两个切点都和 5 m 带宽一样是分析约定，因此均作了敏感性检验。下切点并不承载主结论：把“整块漏检”从 \(\gamma\le0.05\) 调到 \(\gamma\le0.20\)，其占 FN 的比例在 22.3%–29.9% 之间变化，剩余真正未识别部分占标注面积 2.0%–2.9%，结论不依赖具体切点。上切点影响更大：在 0.60、0.70 和 0.80 时，边缘类别分别占 FN 的 51.0%、44.4% 和 31.9%；因此正文每次引用该比例时都同时注明阈值。

> **段落审读**
> - **逻辑用途：** 检验误差分类是否受人为阈值驱动
> - **核对状态：** ✅ 已核对：比例已与 FN 分类输出和当前英文稿核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；本段核对值：5, 05, 20, 22.3, 29.9, 2.0, 2.9；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把完整敏感性结果放入附录表或图，而不只报告三个代表点。

**英文原稿**

Only the first is treated as a detection failure, and is further attributed to post-processing removal, rooftop labelling, containment within OSM buildings, or genuine non-detection.

**中文翻译**

只有第一类被视为检出失败，并进一步判断是否由后处理删除、屋顶停车标注、位于 OSM 建筑内部，或真正未被模型识别造成。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

Throughout, attribution is positional and is worded as such. A false positive lying on OSM industrial land is reported as *located on* industrial land; it is not a claim that each such polygon was individually confirmed to be a storage yard.

**中文翻译**

全文对自动归因都只作位置描述。例如，FP 位于 OSM 工业用地上，只能说它“落在工业用地”，不能据此声称每个多边形都经人工确认是堆场。

> **段落审读**
> - **逻辑用途：** 限制结论适用范围，防止从城市尺度证据跳到地块判断
> - **核对状态：** 🟨 需人工复核：限制来自研究设计与已报告验证结果。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 区分可在本研究内量化的限制和只能在未来研究中检验的限制。

## 3.6 误差类型 II：分层抽样

**英文原稿**

Automated attribution leaves a residual in each direction that no reference layer explains. These residuals are characterised by stratified random sampling with visual adjudication (Table 3.2). The design follows the three-part structure recommended for accuracy assessment — a sampling design, a response design specifying how each sampled unit is judged, and an analysis that scales the sample back to the population (Olofsson et al., 2014; Stehman and Foody, 2019).

**中文翻译**

自动归因后，FP 和 FN 都还有参考图层无法解释的剩余部分。本文用分层随机抽样和人工影像判读来分析这些部分（表 3.2）。设计遵循准确率评估建议的三部分结构：如何抽样、如何判断每个样本，以及如何把样本结果推回总体（Olofsson et al., 2014; Stehman and Foody, 2019）。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L22](#l22) Olofsson et al. (2014)、[L29](#l29) Stehman and Foody (2019)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** `analysis/sampling_worksheet.csv`；`analysis/sampling_results.csv`；`analysis/sampling_corrections.csv`；本段核对值：3.2；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

**Table 3.2** Sampling design. Large polygons are deliberately oversampled; the ratio estimator corrects for this.

**中文翻译**

**表 3.2** 抽样设计。大多边形被有意过度抽样；比率估计量会校正这一点。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/sampling_worksheet.csv`；`analysis/sampling_results.csv`；`analysis/sampling_corrections.csv`；本段核对值：3.2；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

| Population | Stratum (m²) | Polygons | Area (km²) | Sampled |
|---|---|---:|---:|---:|
| Unexplained FP | 100–300 | 604 | 0.1055 | 20 |
| | 300–1,000 | 327 | 0.1656 | 25 |
| | > 1,000 | 61 | 0.1172 | 25 |
| Whole lots missed | 100–300 | 34 | 0.0079 | 10 |
| | 300–1,000 | 51 | 0.0292 | 15 |
| | > 1,000 | 17 | 0.0377 | 17 |
| OSM-only parking | 100–300 | 97 | 0.0192 | 5 |
| | 300–1,000 | 117 | 0.0625 | 10 |
| | > 1,000 | 59 | 0.1793 | 15 |
| **Total** | | | | **142** |

**中文翻译**

| 总体 | 面积分层（m²） | 多边形数 | 面积（km²） | 抽样数 |
|---|---|---:|---:|---:|
| 无法解释的 FP | 100–300 | 604 | 0.1055 | 20 |
| | 300–1,000 | 327 | 0.1656 | 25 |
| | >1,000 | 61 | 0.1172 | 25 |
| 整体漏检停车场 | 100–300 | 34 | 0.0079 | 10 |
| | 300–1,000 | 51 | 0.0292 | 15 |
| | >1,000 | 17 | 0.0377 | 17 |
| 仅 OSM 记录的停车场 | 100–300 | 97 | 0.0192 | 5 |
| | 300–1,000 | 117 | 0.0625 | 10 |
| | >1,000 | 59 | 0.1793 | 15 |
| **总计** | | | | **142** |

> **段落审读**
> - **逻辑用途：** 把本段论证的关键量化关系集中展示
> - **核对状态：** ✅ 已核对：表内核心数字已与项目结果 CSV 及正文恒等式复核。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/sampling_worksheet.csv`；`analysis/sampling_results.csv`；`analysis/sampling_corrections.csv`；本段核对值：100, 300, 604, 0.1055, 20, 1,000, 327；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿可补样本量、单位或不确定区间。

**英文原稿**

Estimates use a stratified ratio estimator (Cochran, 1977). For stratum $h$ of known total area $A_h$, with sample $s_h$ and polygon areas $a_i$, the estimated area of category $c$ is

**中文翻译**

估算采用 Cochran（1977）的分层比率估计量。对已知总面积为 \(A_h\) 的第 \(h\) 层，样本为 \(s_h\)，多边形面积为 \(a_i\)，类别 \(c\) 的估计面积是：

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L04](#l04) Cochran (1977)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** `analysis/sampling_worksheet.csv`；`analysis/sampling_results.csv`；`analysis/sampling_corrections.csv`；本段核对值：1977；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

$$
\hat{A}_c = \sum_h A_h \cdot \frac{\sum_{i \in s_h,\, i \in c} a_i}{\sum_{i \in s_h} a_i}
$$

**中文翻译**

\[
\hat A_c=\sum_h A_h\cdot
\frac{\sum_{i\in s_h,\,i\in c}a_i}
{\sum_{i\in s_h}a_i}
\]

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/sampling_worksheet.csv`；`analysis/sampling_results.csv`；`analysis/sampling_corrections.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

so that oversampling of large polygons does not distort the totals. Intervals on these estimates come from a stratified bootstrap: the inspected polygons are resampled with replacement within each stratum and the estimator recomputed 5,000 times, with each replicate's deviation scaled by $\sqrt{1 - n_h/N_h}$ so that heavily sampled strata contribute proportionately less spread — the largest missed-lot stratum, inspected in full at 17 of 17, contributes none. The intervals cover sampling variance only: not adjudication error, and not the frame exclusion described next.

**中文翻译**

因此，大多边形被过度抽样不会扭曲总体估计。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/sampling_worksheet.csv`；`analysis/sampling_results.csv`；`analysis/sampling_corrections.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

The sampling frame excludes polygons below 100 m². For unexplained FP this removes 0.0513 km², or **11.7%** of that population (0.4396 km² in total, 0.3883 km² in frame). Percentages reported for this population are therefore shares of the frame, and the corrections derived from them (4.6) implicitly assume the excluded slivers have the same composition as the sampled material. The assumption is conservative in the direction that matters: were the slivers composed like the sampled polygons, the upward correction to precision would be *larger* than the one reported. Slivers below 100 m² are in any case more plausibly boundary artefacts than real parking, so they are not extrapolated to.

**中文翻译**

抽样框排除小于 100 m² 的多边形。对无法解释的 FP，这排除了 0.0513 km²，即总体 0.4396 km² 的 **11.7%**；进入抽样框的是 0.3883 km²。因此，后文百分比是抽样框内部的占比，而第 4.6 节的校正默认未抽到的小碎片组成与样本相同。这个假设在关键方向上是保守的：若小碎片确实与样本相似，对精确率的向上校正会比本文报告的更大。考虑到小于 100 m² 的碎片更可能是边界残差，本文没有把样本结果外推给它们。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/sampling_worksheet.csv`；`analysis/sampling_results.csv`；`analysis/sampling_corrections.csv`；本段核对值：100, 0.0513, 0.4396, 11.7, 0.3883, 4.6；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

Each sample was inspected as an image chip cut from the Digimap tiles and assigned one category from a fixed list, with an optional note. **Adjudication was carried out against the Digimap imagery**, since a model's failure can only be assessed against the imagery it was given. Categories are organised by failure *mechanism* rather than surface appearance — what visual cue was absent — so that the typology maps onto plausible causes rather than onto descriptions.

**中文翻译**

每个样本都以 Digimap 影像切片人工检查，并从固定列表中选择一个类别，可另加备注。**判断依据是模型实际使用的 Digimap 影像，而不是标注时使用的底图**，因为模型只能根据输入给它的影像作出判断。类别按失败机制——缺少了什么视觉线索——组织，而不是只描述表面外观，这样才便于把错误对应到可能原因。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/sampling_worksheet.csv`；`analysis/sampling_results.csv`；`analysis/sampling_corrections.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

## 3.7 消融实验设计

**英文原稿**

The contribution of each post-processing subtraction is measured by a $2 \times 2$ factorial design: the raw prediction, buildings removed only, roads removed only, and both. Because set difference is commutative in the relevant sense,

**中文翻译**

两项后处理扣除的贡献用 \(2\times2\) 因子设计测量：原始预测、只扣建筑、只扣道路，以及两者都扣。因为在这里：

> **段落审读**
> - **逻辑用途：** 组织章节、概括贡献或承接后文
> - **核对状态：** 🟨 结构性判断：已检查与全文结构一致；不存在独立原数据。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/ablation_summary.csv`；本段核对值：2；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 确保每项预告或贡献都能回指具体章节和证据。

**英文原稿**

$$
(X \setminus A) \setminus B = X \setminus (A \cup B)
$$

**中文翻译**

\[
(X\setminus A)\setminus B=X\setminus(A\cup B)
\]

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/ablation_summary.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

order does not affect this design; order matters only for the exclusive partition of 3.5. As a check that the reconstruction is faithful, applying both subtractions in one operation is compared against the pipeline's own tile-by-tile output; the two agree to within 0.0% on all three measures, so the ablation can be trusted to isolate what it claims to.

**中文翻译**

所以扣除顺序不影响消融结果；顺序只会影响第 3.5 节的互斥归因。为检查重建是否可靠，本文还把一次性扣除两者的结果与流程本身逐图块产生的输出比较，三个指标的差异均为 0.0%，说明消融确实分离了所声称的作用。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/ablation_summary.csv`；本段核对值：3.5, 0.0；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

A second set of variants tests the reference layers as **filters** rather than as explanations. Sports pitches, industrial and commercial land, and road buffers widened by a further 6 m are each subtracted from the finished map, singly and together. This is a deliberate test of a tempting inference: a layer that explains where errors fall might be assumed to improve the map if used to remove them. Reporting recall alongside precision for these variants is what makes the test informative.

**中文翻译**

第二组变体把参考图层当作**过滤器**而不是解释工具。运动场、工业和商业用地，以及额外扩宽 6 m 的道路缓冲区，分别或同时从最终地图中扣除。这是在检验一个很诱人的推断：既然某图层能解释错误出现在哪里，用它删掉预测或许就能改善地图。只有同时报告精确率和召回率，才能看出这个推断是否成立。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/ablation_summary.csv`；本段核对值：6；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

Rooftop parking is examined separately as a case where the pipeline and the model can be shown to disagree. The sixteen labelled rooftop lots are compared against both the pre-subtraction and post-subtraction outputs.

**中文翻译**

屋顶停车单独分析，因为这里可以直接展示模型与处理流程之间的冲突。16 个有标注的屋顶停车场分别与扣除建筑前、后的结果比较。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/ablation_summary.csv`；本段核对值：16；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

## 3.8 两套影像的一致性

**英文原稿**

Labelling was carried out over a satellite basemap, whereas the model operated on Digimap aerial tiles. Because these are different sources, any difference between them could in principle contribute to the measured error rather than the model. Three independent checks bound and quantify that contribution.

**中文翻译**

人工标注使用卫星底图，而模型使用 Digimap 航空影像，两者并非同一套影像。这个问题在标注完成后才发现，因此本文用三项独立检查来测量和限制它可能造成的影响。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/coregistration_summary.csv`；`analysis/sampling_results.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

**(i) Spatial alignment.** For the 1,478 labelled lots the model detected to better than 70% and larger than 300 m², let $\mathbf{d}_i$ be the vector from the centroid of the labelled polygon to the centroid of the intersecting prediction. A registration offset displaces every lot in the same direction, so the mean *vector* is large; imprecise boundaries displace lots in varying directions, so the mean vector stays small while individual displacements do not. The two are separated by

**中文翻译**

**（i）空间配准。** 对面积大于 300 m²、且模型覆盖超过 70% 的 1,478 个标注停车场，令 \(\mathbf d_i\) 为标注多边形中心指向相交预测中心的向量。若存在统一配准偏移，所有停车场都会朝同一方向移动，平均向量就会较大；若只是边界不精确，各停车场方向不同，平均向量会很小。两者用下式分开：

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/coregistration_summary.csv`；`analysis/sampling_results.csv`；本段核对值：300, 70%, 1,478；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

$$
\rho = \frac{\left\lVert \bar{\mathbf{d}} \right\rVert}{\frac{1}{n}\sum_i \lVert \mathbf{d}_i \rVert},
\qquad \bar{\mathbf{d}} = \frac{1}{n}\sum_i \mathbf{d}_i
$$

**中文翻译**

\[
\rho=
\frac{\|\bar{\mathbf d}\|}
{\frac1n\sum_i\|\mathbf d_i\|},
\qquad
\bar{\mathbf d}=\frac1n\sum_i\mathbf d_i
\]

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/coregistration_summary.csv`；`analysis/sampling_results.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

with $\rho \to 0$ where the shared component is negligible relative to the scatter, and $\rho \to 1$ under a uniform shift. Here $\lVert\bar{\mathbf{d}}\rVert = 0.208$ m — **0.83 of one 0.25 m pixel** — against a mean absolute displacement of 1.247 m (4.99 px), giving $\rho = 0.167$. A shared component is statistically detectable (both axes significant at $p < 0.001$; sector directions non-uniform, $\chi^2 = 169.2$, $p < 0.001$), but with 1,478 lots a sub-pixel bias is detectable without being practically meaningful: the significance here is a function of sample size, not of magnitude. The two sources are co-registered to well within a pixel, and the boundary error reported in the results is attributable to the model.

**中文翻译**

共同偏移相对离散很小时，\(\rho\) 接近 0；统一平移时接近 1。本研究中，\(\|\bar{\mathbf d}\|=0.208\) m，只相当于 **0.25 m 像素的 0.83 个像素**；平均绝对位移为 1.247 m（4.99 像素），所以 \(\rho=0.167\)。共同偏移在统计上可检出（两个方向均 \(p<0.001\)；方向扇区并非均匀，\(\chi^2=169.2,p<0.001\)），但 1,478 个样本会让亚像素差异也显著。这里的显著性主要来自样本量，不代表实际偏移很大。两套影像的配准误差远小于一个像素，因此结果中的边界误差主要可归于模型。

> **段落审读**
> - **逻辑用途：** 限制结论适用范围，防止从城市尺度证据跳到地块判断
> - **核对状态：** 🟨 需人工复核：限制来自研究设计与已报告验证结果。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/coregistration_summary.csv`；`analysis/sampling_results.csv`；本段核对值：0, 1, 0.208, 0.25, 0.83, 1.247, 4.99；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 区分可在本研究内量化的限制和只能在未来研究中检验的限制。

**英文原稿**

**(ii) A logical upper bound on temporal mismatch.** A model cannot partially detect a car park absent from its input imagery. Every lot detected even in part therefore demonstrably exists in the Digimap imagery, as does every lot the pre-subtraction output detected. Of the reference area the model misses, all but 0.0699 km² — **2.1% of labelled area** — belongs to such lots. Even were that entire residual imagery mismatch, recall would rise only from 0.854 to 0.873.

**中文翻译**

**（ii）时间不一致的逻辑上限。** 一个在输入影像中不存在的停车场，不可能被模型部分检出。因此，凡是被模型检出一点的停车场，都能证明它在 Digimap 影像中存在；后处理前被检出的停车场同理。在全部漏检参考面积中，除 0.0699 km² 外都属于这类停车场。该剩余面积仅占标注总面积的 **2.1%**。即使全部都是影像时间差造成的，召回率也只会从 0.854 提高到 0.873。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/coregistration_summary.csv`；`analysis/sampling_results.csv`；本段核对值：0.0699, 2.1, 0.854, 0.873；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

**(iii) A sampled estimate.** Within that residual, adjudication against the Digimap imagery estimates 0.0313 km², or **1.0% of labelled area**, as not parking in the imagery the model was given. Removing it raises recall from 0.854 to 0.863 and leaves precision unchanged.

**中文翻译**

**（iii）抽样估计。** 对上述剩余部分按 Digimap 影像人工判断，估计其中 0.0313 km²、即标注总面积的 **1.0%** 在模型所见影像中并非停车场。扣除它后，召回率从 0.854 提高到 0.863，精确率不变。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/coregistration_summary.csv`；`analysis/sampling_results.csv`；本段核对值：0.0313, 1.0, 0.854, 0.863；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

A related check addresses whether OpenStreetMap disagreement can be attributed to that source being out of date. Last-edit timestamps were retrieved for all 985 OSM parking features in the study area. Since the polygons judged to show no parking on the ground are the *most* recently edited of any sampled category, the convenient explanation is not supported by the data. Because Digimap capture dates are not available, no claim about currency is made in either direction, and disagreements are described neutrally as areas where no parking is visible in the imagery used here. The timestamp records any edit, including tag-only changes, and is not a construction date.

**中文翻译**

另一个检查针对 OSM 与影像不一致是否因为 OSM 过时。本文获取了研究区内全部 985 个 OSM 停车要素的最后编辑时间。样本中被判定为“地面看不见停车”的多边形，反而是最近编辑的一组，因此数据不支持“OSM 只是太旧”这一方便的解释。由于 Digimap 没有拍摄日期，本文不判断哪一方更新，只中性地描述为“在本研究所用影像中看不到停车”。OSM 时间戳可能只表示标签修改，不等于建设日期。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/coregistration_summary.csv`；`analysis/sampling_results.csv`；本段核对值：985；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

## 3.9 校正估计量及其空间尺度

**英文原稿**

Adjusting a mapped area using reference data is established practice: the area a map reports is biased by its own commission and omission error, and a reference sample provides the terms with which to correct it (Olofsson et al., 2014). The estimator used here is a simplified form of that idea, expressed through the two measures already reported. Where a map has precision $p$ and recall $r$, predicted area $|M|$ relates to true area $|R|$ by

**中文翻译**

用参考数据校正地图面积是成熟做法：地图报告的面积会受到误报和漏报影响，参考样本可提供校正项（Olofsson et al., 2014）。本文使用其简化形式。若地图精确率为 \(p\)、召回率为 \(r\)、预测面积为 \(|M|\)，则：

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 见 [L22](#l22) Olofsson et al. (2014)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** `analysis/calibration_transfer_errors.csv`；`analysis/accuracy_vs_distance.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

$$
|M| \cdot p = |\mathrm{TP}| = |R| \cdot r
\qquad\Longrightarrow\qquad
|R| = |M| \cdot \frac{p}{r}
$$

**中文翻译**

\[
|M|\cdot p=|\mathrm{TP}|=|R|\cdot r
\quad\Longrightarrow\quad
|R|=|M|\cdot\frac pr
\]

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/calibration_transfer_errors.csv`；`analysis/accuracy_vs_distance.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

Applied to the cells on which $p$ and $r$ were measured this is an identity and carries no information. It is also worth stating plainly that the factor reduces to an area ratio:

**中文翻译**

如果把这个公式应用回计算 \(p\) 和 \(r\) 的同一批单元，它只是一个恒等式，不提供新信息。事实上，校正因子可以直接化成面积比：

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/calibration_transfer_errors.csv`；`analysis/accuracy_vs_distance.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

$$
\frac{p}{r} = \frac{|\mathrm{TP}|/|M|}{|\mathrm{TP}|/|R|} = \frac{|R|}{|M|}
$$

**中文翻译**

\[
\frac pr=
\frac{|\mathrm{TP}|/|M|}{|\mathrm{TP}|/|R|}
=\frac{|R|}{|M|}
\]

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/calibration_transfer_errors.csv`；`analysis/accuracy_vs_distance.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

that is, the labelled area of the training cells divided by their predicted area. The estimator therefore requires only a labelled *total area* on a sample of cells, not a full object-level error analysis — which is what would make calibrating it in a second city affordable. Precision and recall are not redundant: they establish that the bias is systematic rather than noise, while what follows establishes the grain at which it holds.

**中文翻译**

也就是训练单元的标注总面积除以预测总面积。因此，在第二个城市校准时，只需对抽样单元标出停车总面积，不必完成整套对象级误差分析，这使应用成本可控。精确率和召回率仍非多余：它们证明偏差是系统性的，而非随机噪声；接下来的检验则确定这种偏差在多大空间尺度上稳定。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/calibration_transfer_errors.csv`；`analysis/accuracy_vs_distance.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

The question that matters for use is whether a factor fitted on one part of the city predicts another part, and how finely it can be applied. Three hold-out schemes are used (Table 3.3), each fitting $p/r$ on a training set of cells $\mathcal{T}$ and applying it to held-out cells $\mathcal{H}$ the fit never saw. Whole cells are the unit held out rather than individual polygons: parking is spatially dependent at short range, and splitting dependent units at random is known to understate predictive error, so blocks are withheld instead (Roberts et al., 2017). Error is reported relative to the labelled area of the held-out set:

**中文翻译**

真正与实际应用有关的问题是：在城市某一部分拟合的因子，能否预测另一部分，以及它最细能用到什么尺度。本文采用三种留出检验（表 3.3）。每次用训练单元集合 \(\mathcal T\) 拟合 \(p/r\)，再用于从未参与拟合的留出集合 \(\mathcal H\)。留出的是完整空间单元，而不是随机停车多边形，因为停车在短距离内存在空间相关；随机拆分相关样本会低估预测误差，因此应留出空间块（Roberts et al., 2017）。相对留出参考面积的误差为：

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L25](#l25) Roberts et al. (2017)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** `analysis/calibration_transfer_errors.csv`；`analysis/accuracy_vs_distance.csv`；本段核对值：3.3；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

$$
e = \frac{\left(\sum_{c \in \mathcal{H}} |M_c|\right)\left(p/r\right)_{\mathcal{T}} - \sum_{c \in \mathcal{H}} |R_c|}{\sum_{c \in \mathcal{H}} |R_c|}
$$

**中文翻译**

\[
e=
\frac{
\left(\sum_{c\in\mathcal H}|M_c|\right)(p/r)_{\mathcal T}
-\sum_{c\in\mathcal H}|R_c|
}{
\sum_{c\in\mathcal H}|R_c|
}
\]

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/calibration_transfer_errors.csv`；`analysis/accuracy_vs_distance.csv`；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

**Table 3.3** Hold-out schemes for the calibration factor.

**中文翻译**

**表 3.3** 校正因子的留出检验。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/calibration_transfer_errors.csv`；`analysis/accuracy_vs_distance.csv`；本段核对值：3.3；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

| Scheme | Held out | Tests | What it tests |
|---|---|---:|---|
| Random half split | 50 cells | 200 | transfer to a comparable area of the same city |
| Leave one distance band out | 1 band | 5 | transfer across the urban gradient |
| Leave one cell out | 1 cell | 99 | the finest grain the estimator could be used at |

**中文翻译**

| 方案 | 留出内容 | 检验次数 | 检验含义 |
|---|---|---:|---|
| 随机一半划分 | 50 个单元 | 200 | 能否迁移到同一城市中相似面积的区域 |
| 每次留出一个距离环带 | 1 个环带 | 5 | 能否跨城市梯度迁移 |
| 每次留出一个单元 | 1 个单元 | 99 | 估计量可以使用的最细尺度 |

> **段落审读**
> - **逻辑用途：** 把本段论证的关键量化关系集中展示
> - **核对状态：** ✅ 已核对：表内核心数字已与项目结果 CSV 及正文恒等式复核。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/calibration_transfer_errors.csv`；`analysis/accuracy_vs_distance.csv`；本段核对值：50, 200, 1, 5, 99；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿可补样本量、单位或不确定区间。

**英文原稿**

Two implementation points. Per-cell true positives are recovered as $|\mathrm{TP}_c| = p_c \cdot |M_c|$, and $p$ and $r$ are then aggregated micro — as in 3.4 — since averaging per-cell precision directly would give the macro figure (0.5136 rather than 0.5708) and a mismatched factor. The cell with no labelled parking has no defined relative error and is excluded from the leave-one-out scheme, leaving 99. Relative error is unstable where a cell holds little parking, which inflates the leave-one-out mean above its median; a median absolute error in km² is therefore reported alongside.

**中文翻译**

实现上有两点。第一，逐单元真阳性面积由 \(|\mathrm{TP}_c|=p_c|M_c|\) 恢复，然后像第 3.4 节一样按 micro 汇总 \(p\) 和 \(r\)。若直接平均逐单元精确率，会得到 macro 值 0.5136 而不是 0.5708，导致校正因子不匹配。第二，无标注停车的单元没有可定义的相对误差，因此从逐单元留一法中排除，留下 99 个单元。当单元停车很少时，相对误差会很不稳定，使逐单元留一法的均值高于中位数。因此，结果还会报告以 km² 表示的绝对误差中位数。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/calibration_transfer_errors.csv`；`analysis/accuracy_vs_distance.csv`；本段核对值：3.4, 0.5136, 0.5708, 99；译文对应位置：`03_methodology.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

# 4. 结果

**英文原稿**

This chapter reports the measured transfer. Section 4.1 gives the headline accuracy and how it varies across the city, answering the first half of RQ1. Sections 4.2 to 4.4 decompose the error and test the post-processing stage, answering RQ2. Section 4.5 returns to spatial variation and shows the apparent location effect to be confounded. Section 4.6 reports the sampled corrections and what the reference data itself is worth. Section 4.7 answers RQ3 within the reliability the preceding sections establish.

**中文翻译**

本章报告模型迁移的实测结果。第 4.1 节给出总体准确率及其城市内部差异，回答 RQ1 的前半部分。第 4.2–4.4 节拆解误差并检验后处理，回答 RQ2。第 4.5 节进一步表明，表面上的位置效应其实受到其他因素混杂。第 4.6 节报告抽样校正，以及参考数据本身的价值。最后，第 4.7 节在前文确定的可靠性范围内回答 RQ3。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 当前英文稿及项目内证据链；本段核对值：4.1, 4.2, 4.4, 4.5, 4.6, 4.7；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

## 4.1 总体准确率及其空间差异

**英文原稿**

Against 3.2597 km² of labelled surface parking, the model predicts 4.8785 km² — **1.50 times the labelled area**.

**中文翻译**

人工标注的地面停车面积为 3.2597 km²，而模型预测为 4.8785 km²，是标注面积的 **1.50 倍**。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；本段核对值：3.2597, 4.8785, 1.50；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

**Table 4.1** Accuracy of the post-processed output over the 100 km² study area.

**中文翻译**

**表 4.1** 后处理结果在 100 km² 研究区内的准确率。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；本段核对值：4.1, 100；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

| Aggregation | Precision | Recall | IoU |
|---|---:|---:|---:|
| **Micro, all confidence levels** | **0.5708** | **0.8543** | **0.5202** |
| Micro, confidence 2–3 only | 0.5287 | 0.8658 | 0.4886 |
| Macro (mean of 100 cells) | 0.5136 | 0.8468 | 0.4697 |

**中文翻译**

| 汇总方式 | 精确率 | 召回率 | IoU |
|---|---:|---:|---:|
| **Micro，所有置信度** | **0.5708** | **0.8543** | **0.5202** |
| Micro，仅置信度 2–3 | 0.5287 | 0.8658 | 0.4886 |
| Macro（100 个单元的平均） | 0.5136 | 0.8468 | 0.4697 |

> **段落审读**
> - **逻辑用途：** 把本段论证的关键量化关系集中展示
> - **核对状态：** ✅ 已核对：表内核心数字已与项目结果 CSV 及正文恒等式复核。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；本段核对值：0.5708, 0.8543, 0.5202, 2, 3, 0.5287, 0.8658；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿可补样本量、单位或不确定区间。

**英文原稿**

The pattern is asymmetric. Recall of 0.854 means the model finds most labelled parking; precision of 0.571 means that a little under half of what it returns is not labelled parking. Decomposed by area, TP is 2.7848 km², FP 2.0937 km² and FN 0.4749 km², the last being 14.6% of labelled area.

**中文翻译**

结果明显不对称。召回率 0.854 表示模型找到了绝大部分标注停车场；精确率 0.571 则表示模型返回的面积中，略少于一半没有被标注为停车。按面积分解，TP 为 2.7848 km²，FP 为 2.0937 km²，FN 为 0.4749 km²；FN 占标注面积的 14.6%。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；本段核对值：0.854, 0.571, 2.7848, 2.0937, 0.4749, 14.6；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

![逐单元准确率](figures/fig_accuracy_maps.png)

**英文原稿**

**Figure 4.1** Precision, recall and IoU for each 1 km² cell, on a common colour scale. Recall is high and spatially even; precision is neither. One cell contains no labelled parking and is hatched.

**中文翻译**

**图 4.1** 每个 1 km² 单元的精确率、召回率和 IoU，使用相同色标。召回率高而且空间上较均匀，精确率则不然。斜线单元没有标注停车。

> **段落审读**
> - **逻辑用途：** 说明图件承载的证据
> - **核对状态：** 🟨 需人工复核：图由项目分析脚本及对应 CSV 生成。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；本段核对值：4.1, 1；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿检查图例、单位、色盲可读性和印刷尺寸。

**英文原稿**

Figure 4.1 shows that the asymmetry is not an artefact of aggregation: recall is uniformly high across the study area, while precision varies from below 0.3 to above 0.8 between neighbouring cells. The macro figures fall below the micro figures on all three measures — precision 0.514 against 0.571 — indicating that cells contributing little parking area perform worse than the area-weighted total suggests.

**中文翻译**

图 4.1 表明，这种不对称不是汇总方法造成的：整个研究区的召回率都较高，而相邻单元的精确率可能从低于 0.3 变化到高于 0.8。三个 macro 指标都低于 micro，尤其精确率是 0.514 对 0.571。这说明停车面积较少的单元表现更差，而按面积加权的总体数字会显得更乐观。

> **段落审读**
> - **逻辑用途：** 说明图件承载的证据
> - **核对状态：** 🟨 需人工复核：图由项目分析脚本及对应 CSV 生成。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；本段核对值：4.1, 0.3, 0.8, 0.514, 0.571；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿检查图例、单位、色盲可读性和印刷尺寸。

**英文原稿**

Restricting the reference to the more confident labels does not improve precision; it lowers it, from 0.571 to 0.529. Since removing labels can only convert true positives into false positives, this establishes that the confidence-1 labels are not a substantial source of the measured over-prediction.

**中文翻译**

只保留置信度较高的标注并没有提高精确率，反而使它从 0.571 降到 0.529。因为删除参考标签只会把原来的真阳性变成假阳性，所以这证明低置信度标注并不是测得过度预测的主要来源。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；本段核对值：0.571, 0.529；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

## 4.2 假阳性

**英文原稿**

False-positive area is 2.0937 km². Figure 4.2 shows what it is made of.

**中文翻译**

假阳性面积为 2.0937 km²，其组成见图 4.2。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/sampling_results.csv`；本段核对值：2.0937, 4.2；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

![误差组成](figures/fig_error_composition.png)

**英文原稿**

**Figure 4.2** Composition of false-positive area (upper) and false-negative area (lower). In each case the lower bar expands the residual segment of the bar above it. Exclusive shares are of all FP or FN and sum to 100%.

**中文翻译**

**图 4.2** 假阳性面积（上）和假阴性面积（下）的组成。每组下面的条形图进一步展开上方条形图中的剩余部分。互斥占比以全部 FP 或 FN 为分母，合计为 100%。

> **段落审读**
> - **逻辑用途：** 说明图件承载的证据
> - **核对状态：** 🟨 需人工复核：图由项目分析脚本及对应 CSV 生成。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/sampling_results.csv`；本段核对值：4.2, 100%；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿检查图例、单位、色盲可读性和印刷尺寸。

**英文原稿**

**Boundary effects account for a substantial minority.** False-positive area lying within a fixed distance of a labelled car park — the model finding the right lot and drawing it too large — is 17.3% at 2 m, **28.8% at 5 m** and 36.3% at 10 m. The three thresholds are reported because 5 m is a working convention; the value chosen shifts this component by nearly twenty percentage points.

**中文翻译**

**边界效应占了相当一部分。** 在标注停车场一定距离内的 FP，代表模型找对了停车场但画得太大。距离阈值为 2 m 时占 17.3%，5 m 时占 **28.8%**，10 m 时占 36.3%。之所以三个阈值都报告，是因为 5 m 只是工作约定；阈值不同，会让该项相差接近 20 个百分点。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/sampling_results.csv`；本段核对值：2, 17.3, 5, 28.8, 10, 36.3, 20；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

**Attribution of the standalone remainder.** Table 4.2 gives the exclusive partition alongside the unordered diagnostic.

**中文翻译**

**独立剩余部分的归因。** 表 4.2 同时给出互斥划分和非互斥诊断。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/sampling_results.csv`；本段核对值：4.2；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

**Table 4.2** Where false-positive area falls. The two columns have different denominators and are not differences of one another: exclusive shares are assigned once each and sum to 100%, while unordered overlaps are measured against all FP independently and may overlap one another.

**中文翻译**

**表 4.2** 假阳性面积所在位置。两列分母不同，不能彼此相减：互斥占比每块面积只归一次、合计为 100%；非互斥重叠则每个图层都相对全部 FP 独立计算，类别之间可以重叠。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/sampling_results.csv`；本段核对值：4.2, 100%；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

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

**中文翻译**

| 图层 | 互斥占比（全部 FP 的 %） | 非互斥重叠（全部 FP 的 %） |
|---|---:|---:|
| 边界外扩（≤5 m） | 28.8 | — |
| 工业／商业用地 | 29.6 | **52.8** |
| 道路邻近区（额外 6 m） | 11.6 | 16.9 |
| OSM 停车场 | 4.7 | 9.1 |
| 运动场 | 2.5 | 3.1 |
| 棕地 | 1.7 | 2.3 |
| 建筑 | 0.0 | 0.0 |
| **无法解释** | **21.0** | — |

> **段落审读**
> - **逻辑用途：** 把本段论证的关键量化关系集中展示
> - **核对状态：** ✅ 已核对：表内核心数字已与项目结果 CSV 及正文恒等式复核。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/sampling_results.csv`；本段核对值：5, 28.8, 29.6, 52.8, 6, 11.6, 16.9；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿可补样本量、单位或不确定区间。

**英文原稿**

Industrial and commercial land coincides with over half of all false-positive area. Buildings account for none, because OSM building footprints have already been subtracted at the post-processing stage; false positives on buildings the OSM data does not record fall into the unexplained residual. Moving industrial land from an early position in the peeling order to last changes its exclusive share from 30.0% to 29.6%, so the attribution is not an artefact of the ordering.

**中文翻译**

工业和商业用地与超过一半的 FP 面积重合。建筑占 0，是因为后处理已扣除 OSM 建筑轮廓；OSM 没有记录的建筑所产生的 FP 会进入“无法解释”部分。把工业用地从较前位置移到归因顺序最后，其互斥占比只从 30.0% 变到 29.6%，说明结果不是排序造成的假象。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/sampling_results.csv`；本段核对值：0, 30.0, 29.6；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 注明 OSM 获取日期、要素标签范围和完整性口径。

**英文原稿**

**The unexplained residual divides into three unlike things.** Stratified sampling of 70 chips (Figure 4.3) estimates that 44.5% of the residual is genuine misdetection — grey hardstanding, goods yards, sports courts, unpaved ground and unmapped houses — while **34.9% is real parking that the annotation rules deliberately exclude**, principally private driveways (20.2%) and on-street parking (14.7%). A further 17.2% is parking the labelling itself missed. Percentages are of the sampling frame, which excludes fragments below 100 m² and so covers 0.3883 km² of the 0.4396 km² residual.

**中文翻译**

**无法解释的剩余部分其实混合了三类完全不同的情况。** 对 70 个影像切片分层抽样（图 4.3）后估计：44.5% 是真正的误检，包括灰色硬化地面、货场、运动场、未铺装空地和地图未记录的房屋；**34.9% 是标注规则刻意排除的真实停车区域**，主要是私人车道（20.2%）和路边停车（14.7%）；另有 17.2% 是标注本身漏掉的停车场。这些百分比以抽样框为分母；抽样框排除了小于 100 m² 的碎片，覆盖 0.4396 km² 剩余面积中的 0.3883 km²。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fp_analysis_summary.csv`；`analysis/sampling_results.csv`；本段核对值：70, 4.3, 44.5, 34.9, 20.2, 14.7, 17.2；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

## 4.3 假阴性

**英文原稿**

Missed area is 0.4749 km², 14.6% of labelled parking. Measured against the prediction, 33.4% of it lies within 2 m of something the model did find, **54.1% within 5 m** and 69.4% within 10 m.

**中文翻译**

漏检面积为 0.4749 km²，占标注停车面积的 14.6%。以预测区域为参照，其中 33.4% 距已检出区域不超过 2 m，**54.1% 不超过 5 m**，69.4% 不超过 10 m。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；`analysis/rooftop_summary.csv`；本段核对值：0.4749, 14.6, 33.4, 2, 54.1, 5, 69.4；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

**Most missed area is the edge of a car park the model found.** Classifying missed area by how much of its parent lot the model covered gives a more useful split than any distance threshold:

**中文翻译**

**大部分漏检只是模型已经找到的停车场边缘。** 按所属停车场的整体覆盖情况分类，比使用任意距离阈值更有意义：

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；`analysis/rooftop_summary.csv`；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

**Table 4.3** Missed area by the state of the car park it belongs to.

**中文翻译**

**表 4.3** 按所属停车场状态划分的漏检面积。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；`analysis/rooftop_summary.csv`；本段核对值：4.3；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

| Class | Coverage of the lot | Lots | Missed area (km²) | Share of FN |
|---|---|---:|---:|---:|
| Fringe of a well-detected lot | > 70% | 1,638 | 0.2108 | 44.4% |
| Partly detected | 10–70% | 278 | 0.1510 | 31.8% |
| **Whole lot missed** | ≤ 10% | **121** | **0.1131** | **23.8%** |

**中文翻译**

| 类别 | 停车场覆盖率 | 停车场数 | 漏检面积（km²） | FN 占比 |
|---|---|---:|---:|---:|
| 检出良好停车场的边缘 | >70% | 1,638 | 0.2108 | 44.4% |
| 部分检出 | 10–70% | 278 | 0.1510 | 31.8% |
| **整个停车场漏检** | ≤10% | **121** | **0.1131** | **23.8%** |

> **段落审读**
> - **逻辑用途：** 把本段论证的关键量化关系集中展示
> - **核对状态：** ✅ 已核对：表内核心数字已与项目结果 CSV 及正文恒等式复核。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；`analysis/rooftop_summary.csv`；本段核对值：70%, 1,638, 0.2108, 44.4, 10, 278, 0.1510；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿可补样本量、单位或不确定区间。

**英文原稿**

Nearly half of all missed area belongs to lots the model detected to better than 70%. Only the third row is a detection failure in any useful sense, and it is not what it appears: **31.9% of it was found by the model and then deleted by post-processing**, with a further 2.9% labelled as rooftop and 3.4% falling inside OSM building footprints. The genuine blind spot is 0.0699 km², **2.1% of labelled area at most** — and §4.6 shows part of even that is not parking in the imagery the model was given.

**中文翻译**

接近一半的漏检面积属于覆盖率已经超过 70% 的停车场。只有第三行在实际意义上属于检出失败，而且它也不完全像表面看起来那样：其中 **31.9% 原本已被模型找到，却被后处理删除**；另有 2.9% 是屋顶停车，3.4% 位于 OSM 建筑轮廓内。真正的模型盲区最多只有 0.0699 km²，即标注面积的 **2.1%**；第 4.6 节还会说明，其中一部分在模型所见影像中其实并非停车场。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；`analysis/rooftop_summary.csv`；本段核对值：70%, 31.9, 2.9, 3.4, 0.0699, 2.1, 4.6；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 注明 OSM 获取日期、要素标签范围和完整性口径。

**英文原稿**

**Detection tracks size and annotator confidence.**

**中文翻译**

**检出效果与停车场大小和标注置信度有关。**

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；`analysis/rooftop_summary.csv`；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

**Table 4.4** Detection rate by lot size and by labelling confidence.

**中文翻译**

**表 4.4** 按停车场大小和标注置信度划分的检出率。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；`analysis/rooftop_summary.csv`；本段核对值：4.4；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

| Lot size | Lots | Mean detection rate | Missed entirely |
|---|---:|---:|---:|
| < 200 m² | 47 | 0.658 | **19.1%** |
| 200–500 m² | 563 | 0.763 | 8.2% |
| 500–1,000 m² | 573 | 0.805 | 5.4% |
| 1,000–2,500 m² | 559 | 0.852 | 3.0% |
| 2,500–5,000 m² | 182 | 0.850 | 4.9% |
| > 5,000 m² | 113 | 0.864 | **1.8%** |

**中文翻译**

| 停车场面积 | 数量 | 平均检出率 | 完全漏检 |
|---|---:|---:|---:|
| <200 m² | 47 | 0.658 | **19.1%** |
| 200–500 m² | 563 | 0.763 | 8.2% |
| 500–1,000 m² | 573 | 0.805 | 5.4% |
| 1,000–2,500 m² | 559 | 0.852 | 3.0% |
| 2,500–5,000 m² | 182 | 0.850 | 4.9% |
| >5,000 m² | 113 | 0.864 | **1.8%** |

> **段落审读**
> - **逻辑用途：** 把本段论证的关键量化关系集中展示
> - **核对状态：** ✅ 已核对：表内核心数字已与项目结果 CSV 及正文恒等式复核。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；`analysis/rooftop_summary.csv`；本段核对值：200, 47, 0.658, 19.1, 500, 563, 0.763；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿可补样本量、单位或不确定区间。

**英文原稿**

| Confidence | Lots | Mean detection rate | Missed entirely |
|---|---:|---:|---:|
| 1 (uncertain) | 435 | 0.713 | 10.6% |
| 2 | 1,137 | 0.829 | 3.8% |
| 3 (clear) | 465 | 0.856 | 5.4% |

**中文翻译**

| 置信度 | 数量 | 平均检出率 | 完全漏检 |
|---|---:|---:|---:|
| 1（不确定） | 435 | 0.713 | 10.6% |
| 2 | 1,137 | 0.829 | 3.8% |
| 3（明确） | 465 | 0.856 | 5.4% |

> **段落审读**
> - **逻辑用途：** 把本段论证的关键量化关系集中展示
> - **核对状态：** ✅ 已核对：表内核心数字已与项目结果 CSV 及正文恒等式复核。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；`analysis/rooftop_summary.csv`；本段核对值：1, 435, 0.713, 10.6, 2, 1,137, 0.829；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿可补样本量、单位或不确定区间。

**英文原稿**

Lots below 200 m² are missed outright more than ten times as often as lots above 5,000 m². Detection is also lowest where the annotator was least certain, which indicates that part of the measured error reflects genuine ambiguity in the target rather than model deficiency.

**中文翻译**

小于 200 m² 的停车场被完全漏掉的概率，是大于 5,000 m² 停车场的十倍以上。标注者越不确定，检出率也越低。这说明一部分测得误差来自目标本身的真实模糊性，而不只是模型能力不足。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；`analysis/rooftop_summary.csv`；本段核对值：200, 5,000；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

**What the genuine misses look like.** Sampling of 42 chips estimates the composition of the residual as: not parking in the Digimap imagery 41.8%, **irregular layout 23.3%**, obscured by shadow or canopy 9.8%, unusual surface 9.2%, no cars present 6.3%, vans and lorries rather than cars 5.2%, and **no markings 3.7%**.

**中文翻译**

**真正漏检的停车场是什么样。** 对 42 个影像切片抽样后，估计剩余部分由以下情况组成：Digimap 影像中不是停车场 41.8%；**布局不规则 23.3%**；被阴影或树冠遮挡 9.8%；表面材料异常 9.2%；没有车辆 6.3%；停的是货车而非小汽车 5.2%；**没有标线 3.7%**。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；`analysis/rooftop_summary.csv`；本段核对值：42, 41.8, 23.3, 9.8, 9.2, 6.3, 5.2；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

![误差案例](figures/fig_error_chips.png)

**英文原稿**

**Figure 4.3** One worked example of each failure category, on the Digimap imagery the model was given. Red outlines the sampled polygon, blue the model's prediction, yellow other labelled parking nearby.

**中文翻译**

**图 4.3** 各类失败的实例，底图为模型实际使用的 Digimap 影像。红线是抽样多边形，蓝色是模型预测，黄色是附近其他标注停车区域。

> **段落审读**
> - **逻辑用途：** 说明图件承载的证据
> - **核对状态：** 🟨 需人工复核：图由项目分析脚本及对应 CSV 生成。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；`analysis/rooftop_summary.csv`；本段核对值：4.3；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿检查图例、单位、色盲可读性和印刷尺寸。

**英文原稿**

Irregular layout was assigned to 11 of the 42 chips and absent markings to one, so the latter estimate rests on a single observation and its 3.7% should not be read as a precise share. The two are nonetheless separated cleanly by their intervals — 23.3% [16.9, 31.1] against 3.7% [0.6, 9.8] — so the ordering does not depend on that one chip. What the sample supports is that irregular arrangement was the most frequently identified mechanism and unmarked surfacing among the least — which revises the expectation set out in §2.5, where unmarked surfaces were anticipated as the difficulty.

**中文翻译**

不规则布局造成的漏检约为“没有标线”的六倍。这与第 2.5 节提出的一项预期相反：失败案例主要并非没有标线，而是空间布局偏离典型的“停车位—通道”模式。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/fn_analysis_summary.csv`；`analysis/fn_detection_by_class.csv`；`analysis/rooftop_summary.csv`；本段核对值：2.5；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

## 4.4 后处理，以及把参考图层当作过滤器

![消融实验](figures/fig_ablation.png)

**英文原稿**

**Figure 4.4** The eight variants on the precision–recall plane, with IoU iso-lines. Circles are the post-processing factorial; squares are reference layers applied as filters.

**中文翻译**

**图 4.4** 八种变体在精确率—召回率平面上的位置，并标出 IoU 等值线。圆形是后处理因子组合，方形是把参考图层当作过滤器的结果。

> **段落审读**
> - **逻辑用途：** 说明图件承载的证据
> - **核对状态：** 🟨 需人工复核：图由项目分析脚本及对应 CSV 生成。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/ablation_summary.csv`；`analysis/rooftop_summary.csv`；本段核对值：4.4；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿检查图例、单位、色盲可读性和印刷尺寸。

**英文原稿**

**Table 4.5** Ablation. Variants A–D vary the two post-processing subtractions; E–H apply further layers as filters to the finished map.

**中文翻译**

**表 4.5** 消融实验。A–D 改变两项后处理扣除；E–H 在最终地图上继续应用其他图层过滤。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/ablation_summary.csv`；`analysis/rooftop_summary.csv`；本段核对值：4.5；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

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

**中文翻译**

| 变体 | 精确率 | 召回率 | IoU |
|---|---:|---:|---:|
| A 原始模型 | 0.5278 | 0.8939 | 0.4967 |
| B − 建筑 | 0.5467 | 0.8691 | 0.5051 |
| C − 道路 | 0.5498 | 0.8789 | 0.5111 |
| **D − 建筑 − 道路** | **0.5708** | **0.8543** | **0.5202** |
| E − 运动场 | 0.5701 | 0.8373 | 0.5132 |
| **F − 工业用地** | 0.4794 | **0.2789** | **0.2140** |
| G − 更宽道路 | **0.5962** | 0.7884 | 0.5140 |
| H − 以上三项全部扣除 | 0.5195 | 0.2419 | 0.1976 |

> **段落审读**
> - **逻辑用途：** 把本段论证的关键量化关系集中展示
> - **核对状态：** ✅ 已核对：表内核心数字已与项目结果 CSV 及正文恒等式复核。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/ablation_summary.csv`；`analysis/rooftop_summary.csv`；本段核对值：0.5278, 0.8939, 0.4967, 0.5467, 0.8691, 0.5051, 0.5498；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿可补样本量、单位或不确定区间。

**英文原稿**

Reconstructing D from the raw output in a single operation reproduces the pipeline's own tile-by-tile result to within 0.0% on all three measures, so the ablation isolates what it claims to.

**中文翻译**

把原始输出一次性扣除建筑和道路，三个指标与流程逐图块产生的 D 结果相差均为 0.0%，说明消融实验确实分离了相应作用。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/ablation_summary.csv`；`analysis/rooftop_summary.csv`；本段核对值：0.0；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

The two subtractions together raise precision by 0.043 and lower recall by 0.040, for a net IoU gain of 0.024. Each contributes roughly half. Applied as filters, the further layers behave quite differently. Subtracting industrial and commercial land — the layer that coincided with 52.8% of false-positive area — **collapses recall from 0.854 to 0.279 and IoU from 0.520 to 0.214**, because supermarket and retail-park car parks sit on exactly that land. Widening the road buffers is the only variant to raise precision (to 0.596), and it still lowers IoU.

**中文翻译**

两项扣除合起来使精确率提高 0.043、召回率下降 0.040，IoU 净提高 0.024；两项贡献大致各占一半。进一步参考图层作为过滤器时，结果完全不同。工业和商业用地与 52.8% 的 FP 重合，但将其扣除会使**召回率从 0.854 暴跌到 0.279，IoU 从 0.520 降到 0.214**，因为超市和零售园区停车场恰好就在这类土地上。扩大道路缓冲区是唯一继续提高精确率的变体（提高到 0.596），但 IoU 仍然下降。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/ablation_summary.csv`；`analysis/rooftop_summary.csv`；本段核对值：0.043, 0.040, 0.024, 52.8, 0.854, 0.279, 0.520；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

**The pipeline creates a blind spot of its own.** Sixteen labelled lots, 0.0395 km² or 1.21% of the reference, are rooftop parking.

**中文翻译**

**处理流程自己制造了一个盲区。** 16 个标注停车场属于屋顶停车，总面积 0.0395 km²，占参考面积 1.21%。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/ablation_summary.csv`；`analysis/rooftop_summary.csv`；本段核对值：16, 0.0395, 1.21；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

**Table 4.6** Rooftop parking, before and after post-processing.

**中文翻译**

**表 4.6** 后处理前后的屋顶停车检出情况。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/ablation_summary.csv`；`analysis/rooftop_summary.csv`；本段核对值：4.6；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

| Measure | Value |
|---|---:|
| Recall on rooftop lots, raw model | **0.916** |
| Recall on rooftop lots, after subtraction | **0.115** |
| Recall on non-rooftop lots, raw model | 0.894 |
| Rooftop area falling inside OSM buildings | 85.6% |
| Rooftop area detected then removed | **80.1%** |

**中文翻译**

| 指标 | 数值 |
|---|---:|
| 原始模型对屋顶停车的召回率 | **0.916** |
| 扣除建筑后的屋顶停车召回率 | **0.115** |
| 原始模型对非屋顶停车的召回率 | 0.894 |
| 落在 OSM 建筑内部的屋顶停车面积 | 85.6% |
| 被模型找到后又被删除的屋顶停车面积 | **80.1%** |

> **段落审读**
> - **逻辑用途：** 把本段论证的关键量化关系集中展示
> - **核对状态：** ✅ 已核对：表内核心数字已与项目结果 CSV 及正文恒等式复核。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/ablation_summary.csv`；`analysis/rooftop_summary.csv`；本段核对值：0.916, 0.115, 0.894, 85.6, 80.1；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿可补样本量、单位或不确定区间。

**英文原稿**

The raw model detects rooftop parking slightly *better* than ground-level parking. Subtracting building footprints removes four fifths of it.

**中文翻译**

原始模型识别屋顶停车甚至略好于地面停车；扣除建筑轮廓却删除了其中五分之四。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/ablation_summary.csv`；`analysis/rooftop_summary.csv`；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

## 4.5 准确率与位置

**英文原稿**

**Table 4.7** Correlations with per-cell precision, recall and IoU (Pearson r, p in brackets). Recall statistics use the 99 cells with labelled parking.

**中文翻译**

**表 4.7** 逐单元精确率、召回率和 IoU 与位置变量的相关性（Pearson \(r\)，括号内为 \(p\) 值）。召回率使用有标注停车的 99 个单元。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/accuracy_vs_distance.csv`；`analysis/accuracy_vs_distance_summary.csv`；本段核对值：4.7, 99；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

| Metric | Distance | Parking share | Distance \| parking share | Parking share \| distance |
|---|---:|---:|---:|---:|
| **Precision** | −0.172 (0.087) | **+0.536 (<0.0001)** | +0.186 (0.065) | **+0.540 (<0.0001)** |
| Recall | +0.181 (0.073) | +0.103 (0.313) | +0.289 (0.004) | +0.250 (0.013) |
| IoU | −0.127 (0.208) | **+0.515 (<0.0001)** | +0.229 (0.022) | **+0.540 (<0.0001)** |

**中文翻译**

| 指标 | 距市中心距离 | 停车占地比例 | 距离 \| 控制停车比例 | 停车比例 \| 控制距离 |
|---|---:|---:|---:|---:|
| **精确率** | −0.172 (0.087) | **+0.536 (<0.0001)** | +0.186 (0.065) | **+0.540 (<0.0001)** |
| 召回率 | +0.181 (0.073) | +0.103 (0.313) | +0.289 (0.004) | +0.250 (0.013) |
| IoU | −0.127 (0.208) | **+0.515 (<0.0001)** | +0.229 (0.022) | **+0.540 (<0.0001)** |

> **段落审读**
> - **逻辑用途：** 把本段论证的关键量化关系集中展示
> - **核对状态：** ✅ 已核对：表内核心数字已与项目结果 CSV 及正文恒等式复核。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/accuracy_vs_distance.csv`；`analysis/accuracy_vs_distance_summary.csv`；本段核对值：0.172, 0.087, 0.536, 0.0001, 0.186, 0.065, 0.540；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿可补样本量、单位或不确定区间。

**英文原稿**

Distance from the city centre does not predict precision. The share of a cell given over to parking does, strongly, and continues to do so after controlling for distance. The reverse does not hold: controlling for parking share, the distance effect is not significant. Distance and parking share are themselves correlated at −0.562.

**中文翻译**

距市中心的距离不能预测精确率；一个单元中停车占地比例却能强烈预测精确率，而且控制距离后仍然成立。反过来则不成立：控制停车比例后，距离效应不显著。距离与停车占地比例本身的相关系数为 −0.562。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/accuracy_vs_distance.csv`；`analysis/accuracy_vs_distance_summary.csv`；本段核对值：0.562；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

All three metrics are reported to avoid selective presentation, but only precision is interpreted here. The partial correlations for recall and IoU reach significance while their raw correlations do not, and their signs reverse between the two; with n = 100 and two strongly correlated predictors this pattern is not a stable basis for a claim.

**中文翻译**

为了避免选择性展示，表中列出三个指标，但这里只解释精确率。召回率和 IoU 的偏相关达到显著，而原始相关不显著，并且两者的符号变化方式不同。在 \(n=100\) 且两个预测变量高度相关的情况下，这种模式不足以支持稳定结论。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/accuracy_vs_distance.csv`；`analysis/accuracy_vs_distance_summary.csv`；本段核对值：100；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

Read across distance bands, precision falls from 0.584 within 1 km to 0.485 beyond 4 km while recall stays between 0.70 and 0.86 (see Figure 4.5 and Appendix B). The band means move with parking share, not with distance.

**中文翻译**

按距离环带看，精确率从 1 km 内的 0.584 降到 4 km 外的 0.485，而召回率保持在 0.70–0.86（见图 4.5 和附录 C）。这些环带均值跟随的是停车占地比例，而不是距离本身。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/accuracy_vs_distance.csv`；`analysis/accuracy_vs_distance_summary.csv`；本段核对值：1, 0.584, 4, 0.485, 0.70, 0.86, 4.5；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

![准确率与位置](figures/fig_accuracy_vs_location.png)

**英文原稿**

**Figure 4.5** Per-cell precision against distance and against parking share, and parking share against distance. Solid red fits are significant at p < 0.05; the dashed grey fit is not. Diamonds are distance-band means.

**中文翻译**

**图 4.5** 逐单元精确率分别与距离、停车占地比例的关系，以及停车占地比例与距离的关系。红色实线表示 \(p<0.05\) 的拟合；灰色虚线不显著；菱形表示距离环带均值。

> **段落审读**
> - **逻辑用途：** 说明图件承载的证据
> - **核对状态：** 🟨 需人工复核：图由项目分析脚本及对应 CSV 生成。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/accuracy_vs_distance.csv`；`analysis/accuracy_vs_distance_summary.csv`；本段核对值：4.5, 0.05；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿检查图例、单位、色盲可读性和印刷尺寸。

## 4.6 抽样校正，以及参考数据的价值

**英文原稿**

Applying the sampled estimates as corrections gives four cumulative variants:

**中文翻译**

依次应用抽样估计进行校正，得到四个累计变体：

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/sampling_corrections.csv`；`analysis/bootstrap_ci_results.csv`；`analysis/bootstrap_ci_corrections.csv`；`analysis/osm_timestamps_summary.csv`；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

**Table 4.8** Accuracy under cumulative correction.

**中文翻译**

**表 4.8** 累计校正后的准确率。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/sampling_corrections.csv`；`analysis/bootstrap_ci_results.csv`；`analysis/bootstrap_ci_corrections.csv`；`analysis/osm_timestamps_summary.csv`；本段核对值：4.8；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

| Variant | Reference (km²) | Prediction (km²) | Precision | Recall | IoU |
|---|---:|---:|---:|---:|---:|
| **1 As measured** | 3.2597 | 4.8785 | **0.5708** | **0.8543** | **0.5202** |
| 2 + reference-side (−0.0313, not parking in the imagery) | 3.2284 | 4.8785 | 0.5708 | 0.8626 | 0.5233 |
| 3 + prediction-side (+0.0667, parking the labelling missed) | 3.2951 | 4.8785 | 0.5845 | 0.8654 | 0.5358 |
| **4 Effective (−0.1358, definitional exclusions removed)** | 3.2951 | 4.7427 | **0.6012** | 0.8654 | **0.5498** |

**中文翻译**

| 变体 | 参考面积（km²） | 预测面积（km²） | 精确率 | 召回率 | IoU |
|---|---:|---:|---:|---:|---:|
| **1 原始测量** | 3.2597 | 4.8785 | **0.5708** | **0.8543** | **0.5202** |
| 2 + 参考侧校正（−0.0313，影像中不是停车） | 3.2284 | 4.8785 | 0.5708 | 0.8626 | 0.5233 |
| 3 + 预测侧校正（+0.0667，标注漏掉的停车） | 3.2951 | 4.8785 | 0.5845 | 0.8654 | 0.5358 |
| **4 有效结果（−0.1358，去除定义上排除的部分）** | 3.2951 | 4.7427 | **0.6012** | 0.8654 | **0.5498** |

> **段落审读**
> - **逻辑用途：** 把本段论证的关键量化关系集中展示
> - **核对状态：** ✅ 已核对：表内核心数字已与项目结果 CSV 及正文恒等式复核。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/sampling_corrections.csv`；`analysis/bootstrap_ci_results.csv`；`analysis/bootstrap_ci_corrections.csv`；`analysis/osm_timestamps_summary.csv`；本段核对值：1, 3.2597, 4.8785, 0.5708, 0.8543, 0.5202, 2；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿可补样本量、单位或不确定区间。

**英文原稿**

The corrected figures carry sampling uncertainty, and the bootstrap of §3.6 puts 95% intervals on them: precision 0.5845 [0.5783, 0.5917] at variant 3 and 0.6012 [0.5941, 0.6090] at variant 4, recall 0.8654 [0.8635, 0.8675], IoU 0.5498 [0.5434, 0.5569]. The variant-4 interval does not reach the measured 0.5708, so the gain is not an artefact of which polygons happened to be sampled. The intervals are narrow because the corrections are small relative to the quantities they adjust: a near-threefold range in the estimated prediction-side correction, 0.0366 to 0.1018 km², moves precision by under a point and a half.

**中文翻译**

校正结果带有抽样不确定性；§3.6 的 bootstrap 给出 95% 区间：变体 3 的精确率为 0.5845 [0.5783, 0.5917]，变体 4 为 0.6012 [0.5941, 0.6090]；召回率为 0.8654 [0.8635, 0.8675]；IoU 为 0.5498 [0.5434, 0.5569]。变体 4 的区间没有延伸到原始测量的 0.5708，因此提升不是恰好抽到某些多边形造成的假象。区间较窄，是因为校正量相对于被调整总量很小：预测侧校正估计即使从 0.0366 增至 0.1018 km²、接近三倍，精确率也只变化不到 1.5 个百分点。

> **段落审读**
> - **逻辑用途：** 量化抽样校正的不确定性，并检验“有效精确率提高”是否稳健
> - **核对状态：** ✅ 已核对：区间已与 `bootstrap_ci_results.csv` 和 `bootstrap_ci_corrections.csv` 核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/sampling_corrections.csv`；`analysis/bootstrap_ci_results.csv`；`analysis/bootstrap_ci_corrections.csv`；`analysis/osm_timestamps_summary.csv`；本段核对值：3.6, 95%, 3, 0.5845, 0.5783, 0.5917, 4；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 注明 bootstrap 次数、重采样单位和区间算法。

**英文原稿**

Precision rises from 0.571 to 0.601 across the four steps, and roughly half of that gain comes from the final step — removing on-street parking and private driveways from the prediction, which are real parking excluded by rule rather than model error. Recall moves only between 0.854 and 0.865. **The headline pattern does not change under any correction**; variant 1 is reported throughout as the primary figure.

**中文翻译**

四步下来，精确率从 0.571 提高到 0.601，其中约一半的提升来自最后一步：从预测中去掉路边停车和私人车道。这些地方确实在停车，只是按规则不属于目标，并非模型识别错误。召回率只在 0.854–0.865 之间变化。**任何校正都没有改变总体结论**，所以全文仍以变体 1 的原始测量作为主要结果。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/sampling_corrections.csv`；`analysis/bootstrap_ci_results.csv`；`analysis/bootstrap_ci_corrections.csv`；`analysis/osm_timestamps_summary.csv`；本段核对值：0.571, 0.601, 0.854, 0.865, 1；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

**OpenStreetMap, assessed against the same reference.** OSM records 1.7641 km² of parking in the study area, 54.1% of the labelled total, across 985 polygons against 2,037 labelled. Their median polygon areas are almost identical (763 m² against 799 m²), so OSM is not simply recording the large car parks and omitting small ones. It overlaps 1.1882 km² of labelled parking — 36.5% of it — leaving **63.5% of labelled parking absent from OSM entirely**. In the other direction, sampling of the area where OSM claims parking and the reference does not estimates that 63.2% shows no parking on the ground.

**中文翻译**

**使用同一参考评估 OpenStreetMap。** 研究区内 OSM 记录了 1.7641 km² 停车面积，是人工标注总量的 54.1%；OSM 有 985 个多边形，人工标注有 2,037 个。两者多边形面积中位数几乎相同（763 m² 对 799 m²），所以 OSM 并不是只记录大停车场而漏掉小停车场。OSM 与人工标注重叠 1.1882 km²，只占标注面积的 36.5%，即 **63.5% 的人工标注停车在 OSM 中完全缺失**。反方向看，在 OSM 说有停车、但人工参考没有的区域中，抽样估计有 63.2% 的地面影像看不到停车。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/sampling_corrections.csv`；`analysis/bootstrap_ci_results.csv`；`analysis/bootstrap_ci_corrections.csv`；`analysis/osm_timestamps_summary.csv`；本段核对值：1.7641, 54.1, 985, 2,037, 763, 799, 1.1882；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 注明 OSM 获取日期、要素标签范围和完整性口径。

**英文原稿**

Last-edit timestamps were retrieved for all 985 OSM parking features. The median across the study area is 2024. Among the sampled polygons judged not to be parking, the median is **2025**, and 8 of 11 were edited in 2024 or later — later than any other sampled category. The disagreement is therefore not attributable to OSM being out of date.

**中文翻译**

研究取得全部 985 个 OSM 停车要素的最后编辑时间。全区中位年份为 2024。样本中被判断为并非停车的多边形，中位年份反而是 **2025**，11 个中有 8 个在 2024 年或之后编辑，比其他任何抽样类别都新。因此，差异不能简单归因为 OSM 太旧。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/sampling_corrections.csv`；`analysis/bootstrap_ci_results.csv`；`analysis/bootstrap_ci_corrections.csv`；`analysis/osm_timestamps_summary.csv`；本段核对值：985, 11, 8；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

## 4.7 地面停车的面积与分布

**英文原稿**

**Table 4.9** Surface parking as a share of land, by distance band.

**中文翻译**

**表 4.9** 各距离环带中地面停车占土地的比例。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/accuracy_vs_distance.csv`；`analysis/calibration_transfer_errors.csv`；`analysis/parking_extent.py`；本段核对值：4.9；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

| Band | Cells | Labelled | Model | Calibrated (km²) |
|---|---:|---:|---:|---:|
| < 1 km | 2 | 5.33% | 6.42% | 0.086 |
| **1–2 km** | 11 | **7.11%** | 10.35% | 0.761 |
| 2–3 km | 14 | 4.80% | 7.19% | 0.673 |
| 3–4 km | 22 | 4.50% | 6.53% | 0.959 |
| > 4 km | 51 | 1.39% | 2.29% | 0.781 |
| **Whole area** | 100 | **3.26%** | 4.88% | 3.2595 |

**中文翻译**

| 环带 | 单元数 | 人工标注 | 模型 | 校准面积（km²） |
|---|---:|---:|---:|---:|
| <1 km | 2 | 5.33% | 6.42% | 0.086 |
| **1–2 km** | 11 | **7.11%** | 10.35% | 0.761 |
| 2–3 km | 14 | 4.80% | 7.19% | 0.673 |
| 3–4 km | 22 | 4.50% | 6.53% | 0.959 |
| >4 km | 51 | 1.39% | 2.29% | 0.781 |
| **全区** | 100 | **3.26%** | 4.88% | 3.2595 |

> **段落审读**
> - **逻辑用途：** 把本段论证的关键量化关系集中展示
> - **核对状态：** ✅ 已核对：表内核心数字已与项目结果 CSV 及正文恒等式复核。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/accuracy_vs_distance.csv`；`analysis/calibration_transfer_errors.csv`；`analysis/parking_extent.py`；本段核对值：1, 2, 5.33, 6.42, 0.086, 11, 7.11；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿可补样本量、单位或不确定区间。

**英文原稿**

The calibrated column applies the whole-area factor of §3.9. In the final row that is an identity and carries no information: the factor was fitted on exactly these cells, so it returns their labelled area by construction. In the band rows it is not, because a factor fitted over the whole area is being applied to a sub-area it was not fitted to; the difference between the calibrated and labelled columns there is the factor's transfer error within the city, ranging from −19.6% in the two-cell innermost band to +10.0% beyond 4 km.

**中文翻译**

“校准面积”列使用第 3.9 节的全区因子。最后一行只是恒等式，不包含新信息：因子正是用这 100 个单元拟合的，所以按定义会返回它们的标注总面积。各环带行则不是恒等式，因为全区因子被应用到了未单独拟合的子区域。校准值与标注值的差异就是因子在城市内部的迁移误差，从最内侧两个单元的 −19.6%，到 4 km 外的 +10.0%。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/accuracy_vs_distance.csv`；`analysis/calibration_transfer_errors.csv`；`analysis/parking_extent.py`；本段核对值：3.9, 100, 19.6, 4, 10.0；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

Surface parking covers 3.2597 km², **3.26% of the 100 km² study area**. This is a figure from the labelled reference rather than from the model: every car park in the study area was labelled, so it is a census and not an estimate. Its uncertainty is that of the labelling, which the corrections of §4.6 bound directly — removing the labelled area that is not parking in the Digimap imagery and adding the parking the labelling missed moves the reference to 3.2951 km², or **3.30%**. The two corrections together shift the share by less than a tenth of a percentage point of the study area.

**中文翻译**

地面停车覆盖 3.2597 km²，即 **100 km² 研究区的 3.26%**。这个数字来自人工标注参考，而不是模型估算：研究区内的停车场全部经过标注，所以它是一次普查，而非抽样估计。它的不确定性来自标注质量，第 4.6 节的校正直接限定了范围。删除在 Digimap 影像中并非停车的标注，再加入标注漏掉的停车，参考面积变成 3.2951 km²，即 **3.30%**。两项校正合起来使全区占比变化不到 0.1 个百分点。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/accuracy_vs_distance.csv`；`analysis/calibration_transfer_errors.csv`；`analysis/parking_extent.py`；本段核对值：3.2597, 100, 3.26, 4.6, 3.2951, 3.30, 0.1；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 继续明确 3.26% 来自人工参考而非模型估计，并避免把 3.30% 当作独立观测。

**英文原稿**

The share is highest in the inner 2 km — 5.33% within 1 km and 7.11% between 1 and 2 km — and falls monotonically beyond that, to 4.80%, 4.50% and 1.39% in the successive bands. The decline outward is well supported, resting on bands of 14, 22 and 51 cells. Whether the profile also turns down at the very centre is not established: the innermost band holds only two cells, so the apparent dip from 7.11% to 5.33% cannot be distinguished from the variation between individual cells.

**中文翻译**

停车占地比例在内侧 2 km 最高：1 km 内为 5.33%，1–2 km 为 7.11%；再向外依次单调下降到 4.80%、4.50% 和 1.39%。向外下降的趋势较可靠，因为三个外侧环带分别包含 14、22 和 51 个单元。但最中心是否也真的下降尚不能确定：最内环带只有两个单元，所以从 7.11% 到 5.33% 的表面下降，可能只是单元间差异。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/accuracy_vs_distance.csv`；`analysis/calibration_transfer_errors.csv`；`analysis/parking_extent.py`；本段核对值：2, 1, 5.33, 7.11, 4.80, 4.50, 1.39；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

The distribution across cells is strongly right-skewed: mean 3.26%, **median 1.71%**, maximum 18.81%, with six cells above 10%. Parking land is concentrated rather than spread evenly.

**中文翻译**

逐单元分布明显右偏：均值 3.26%，**中位数 1.71%**，最大值 18.81%，有 6 个单元超过 10%。也就是说，停车用地集中在少数区域，并非均匀铺开。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/accuracy_vs_distance.csv`；`analysis/calibration_transfer_errors.csv`；`analysis/parking_extent.py`；本段核对值：3.26, 1.71, 18.81, 6, 10%；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 继续明确 3.26% 来自人工参考而非模型估计，并避免把 3.30% 当作独立观测。

![停车占地](figures/parking_extent.png)

**英文原稿**

**Figure 4.6** Parking share by cell, against distance, and its distribution across the 100 cells.

**中文翻译**

**图 4.6** 各单元停车占地比例、它与距离的关系，以及 100 个单元中的分布。

> **段落审读**
> - **逻辑用途：** 说明图件承载的证据
> - **核对状态：** 🟨 需人工复核：图由项目分析脚本及对应 CSV 生成。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/accuracy_vs_distance.csv`；`analysis/calibration_transfer_errors.csv`；`analysis/parking_extent.py`；本段核对值：4.6, 100；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿检查图例、单位、色盲可读性和印刷尺寸。

**英文原稿**

**Calibration and the grain at which it holds.** For a map of precision *p* and recall *r*, true area is estimated as predicted area × *p*/*r*, here 4.8785 × 0.6681 = 3.2595 km². On the cells the factor was fitted to this is an identity. Tested by holding cells out (Table 4.10), it is not.

**中文翻译**

**校准在什么空间尺度上有效。** 若地图精确率为 \(p\)、召回率为 \(r\)，真实面积估为“预测面积 × \(p/r\)”；这里是 \(4.8785\times0.6681=3.2595\) km²。在拟合因子的同一批单元上，这只是恒等式；真正的检验是把单元留出（表 4.10）。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/accuracy_vs_distance.csv`；`analysis/calibration_transfer_errors.csv`；`analysis/parking_extent.py`；本段核对值：4.8785, 6681, 3.2595, 4.10；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

**Table 4.10** Error of the calibrated estimate on cells excluded from fitting the factor.

**中文翻译**

**表 4.10** 在未参与因子拟合的单元上，校准面积估计的误差。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/accuracy_vs_distance.csv`；`analysis/calibration_transfer_errors.csv`；`analysis/parking_extent.py`；本段核对值：4.10；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

| Scheme | Held out | Tests | Mean error | 5–95% | Within ±25% |
|---|---|---:|---:|---:|---:|
| **Random half split** | 50 cells | 200 | +0.3% | **−6.6% to +7.8%** | 100% |
| Leave one distance band out | 1 band | 5 | −2.9% | −16.9% to +10.6% | — |
| **Leave one cell out** | 1 cell | 99 | +16.5% | −22.0% to +80.5% | **63%** |

**中文翻译**

| 方案 | 留出内容 | 检验次数 | 平均误差 | 5–95% 范围 | 落在 ±25% 内 |
|---|---|---:|---:|---:|---:|
| **随机一半划分** | 50 个单元 | 200 | +0.3% | **−6.6% 至 +7.8%** | 100% |
| 每次留出一个距离环带 | 1 个环带 | 5 | −2.9% | −16.9% 至 +10.6% | — |
| **每次留出一个单元** | 1 个单元 | 99 | +16.5% | −22.0% 至 +80.5% | **63%** |

> **段落审读**
> - **逻辑用途：** 把本段论证的关键量化关系集中展示
> - **核对状态：** ✅ 已核对：表内核心数字已与项目结果 CSV 及正文恒等式复核。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/accuracy_vs_distance.csv`；`analysis/calibration_transfer_errors.csv`；`analysis/parking_extent.py`；本段核对值：5, 95%, ±25, 50, 200, 0.3, 6.6；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿可补样本量、单位或不确定区间。

**英文原稿**

A factor fitted on half the city predicts the other half to within about **±7%** at 90% confidence. This figure describes what the method would deliver where no labelling exists — it is not an error bar on the 3.26% above, which was measured directly and is the quantity the calibration is attempting to recover. Applied to a single 1 km² cell the estimator fails: only 63% of cells fall within ±25%, and the leave-one-out mean sits well above its median because relative error is unstable where a cell holds little parking — the median absolute error is 0.0035 km² against a mean labelled area of 0.0329 km² per cell.

**中文翻译**

用半个城市拟合的因子，在 90% 的检验中可把另半个城市预测到约 **±7%** 以内。这个数字表示在没有标注的区域中，该方法可能达到的表现；它不是上述 3.26% 的误差条，因为 3.26% 是直接测量值，也是校准想要恢复的目标。若把因子用于单个 1 km² 单元，估计会失效：只有 63% 的单元落在 ±25% 内。逐单元留一法的平均误差明显高于中位数，是因为停车面积很少时相对误差很不稳定；绝对误差中位数为 0.0035 km²，而每个单元的平均标注面积为 0.0329 km²。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/accuracy_vs_distance.csv`；`analysis/calibration_transfer_errors.csv`；`analysis/parking_extent.py`；本段核对值：90%, ±7, 3.26, 1, 63%, ±25, 0.0035；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 继续明确 3.26% 来自人工参考而非模型估计，并避免把 3.30% 当作独立观测。

![校准迁移](figures/calibration_transfer.png)

**英文原稿**

**Figure 4.7** Distribution of calibrated-estimate error under the three hold-out schemes. The red line marks the median of each distribution; Table 4.10 reports the mean, which for the leave-one-out scheme is the higher of the two.

**中文翻译**

**图 4.7** 三种留出方案下校准估计误差的分布。

> **段落审读**
> - **逻辑用途：** 说明图件承载的证据
> - **核对状态：** 🟨 需人工复核：图由项目分析脚本及对应 CSV 生成。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/accuracy_vs_distance.csv`；`analysis/calibration_transfer_errors.csv`；`analysis/parking_extent.py`；本段核对值：4.7；译文对应位置：`04_results.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿检查图例、单位、色盲可读性和印刷尺寸。

# 5. 讨论

## 5.1 回答研究问题

**英文原稿**

**RQ1 — How accurate is the model on UK aerial imagery, and does accuracy vary systematically within the city?**

**中文翻译**

**RQ1——模型迁移到英国航空影像后有多准确？准确率是否在城市内部呈现系统差异？**

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

The transfer works, but unevenly, and the unevenness has a definite shape. Recall of 0.854 (Table 4.1) means the model finds most of what is there; precision of 0.571 means a little under half of what it returns is not labelled parking, and the predicted area is 1.50 times the labelled area. Figure 4.1 shows this is not an artefact of aggregation: recall is high and spatially even, while precision varies by more than a factor of two between neighbouring cells.

**中文翻译**

迁移是有效的，但表现并不均匀，而且这种不均匀有清楚的结构。召回率 0.854（表 4.1）说明模型找到了大多数真实停车场；精确率 0.571 表示模型返回的面积中略少于一半没有被标注为停车，预测总面积是标注面积的 1.50 倍。图 4.1 说明这不是汇总方法造成的：召回率高且空间上均匀，精确率却能在相邻单元间相差一倍以上。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：0.854, 4.1, 0.571, 1.50；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

These figures are better read against the transfer literature than against an implicit standard of perfection. Maggiori et al. (2017) judged a network reaching roughly 65% IoU on building footprints in cities it had never seen to generalise satisfactorily, and Hurst-Tarrab et al. (2020) report parking-block models exceeding 50% IoU. The 0.520 measured here sits within that range. What makes the comparison worth drawing is not geography — Maggiori et al. test on unseen cities across two continents, and Hurst-Tarrab et al. report their figure as holding worldwide — but training. Both of those results were obtained with training data drawn from the same source as the test data; the figure here required no target-domain training at all. On a scalar measure, transferring appears to have cost less than that asymmetry might lead one to expect. What that measure does not show is where the cost fell, which the decomposition below sets out.

**中文翻译**

与其拿一个隐含的“完美标准”比较，不如把这些数字放进迁移研究中理解。Maggiori et al.（2017）的建筑轮廓模型在从未见过的城市达到约 65% IoU，便被认为泛化良好；Hurst-Tarrab et al.（2020）的停车区域模型也报告超过 50% IoU。本研究的 0.520 落在这个范围内。这里值得比较的并不是地理位置：前者跨两洲测试未见城市，后者称结果在全球成立；真正的区别在训练数据。它们的训练和测试数据来自同一来源，而本研究完全没有使用目标地区数据训练。单看一个总体指标，迁移造成的损失似乎没有预想中那么大；但这个指标没有说明损失具体发生在哪里，下面的误差拆解正是为了回答这一点。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 见 [L14](#l14) Hurst-Tarrab et al. (2020)、[L20](#l20) Maggiori et al. (2017)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：65%, 50%, 0.520；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

On spatial variation the intuitive reading does not hold up. Distance from the city centre does not predict precision once parking share is controlled for, while parking share continues to predict it strongly (Table 4.7, Figure 4.5). Distance appears to matter only because it tracks parking abundance. What tracks accuracy is how much parking a cell contains, not where in the city it sits — which is consistent with the macro figures falling below the micro figures, and with the sparse cells being the weak ones. Lot size shows a separate and equally clear gradient (Table 4.4), though the two analyses are distinct and the relationships are associations rather than demonstrated causes. Reporting the raw distance correlation alone would have supported a plausible but misleading claim about central-city performance.

**中文翻译**

关于空间差异，直觉上的解释站不住脚。控制停车占地比例后，距市中心距离不能预测精确率；相反，控制距离后，停车占地比例仍然具有很强的预测力（表 4.7、图 4.5）。距离看起来重要，只是因为它与停车多少相关。真正随准确率变化的是一个单元内有多少停车，而不是它位于城市什么位置。这也与 macro 低于 micro、停车稀少单元表现较弱的结果一致。停车场大小还呈现另一条明确梯度（表 4.4），不过这两项分析彼此独立，而且都只是相关关系，不能直接解释为因果。若只报告距离的原始相关性，就会得到一个听起来合理、实际上容易误导的“市中心表现差异”结论。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：4.7, 4.5, 4.4；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

**RQ2 — What systematic errors does the model make, and how much error does post-processing remove or create?**

**中文翻译**

**RQ2——模型会产生哪些系统性错误？后处理消除了多少错误，又制造了多少错误？**

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

What the error is *not* is a failure to recognise parking. After every attributable component is removed, the genuine blind spot — parking present in the imagery that the model simply did not see — is at most 2.1% of labelled area, or under 3% of all error area, and sampling suggests part of even that is not parking in the imagery at all.

**中文翻译**

首先，这些错误**并不是模型认不出停车场**。扣除所有能够归因的成分后，模型真正的盲区——影像中确实有停车，但模型完全没有看到——最多只占标注面积的 2.1%，不到全部误差面积的 3%；抽样还表明，其中一部分在模型所见影像里其实不是停车场。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：2.1, 3%；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

What it is instead is a mixture. Boundary placement accounts for the largest single component: 28.8% of false-positive area lies within 5 m of a real car park, 54.1% of missed area lies within 5 m of something the model did find, and 44.4% of missed area belongs to lots detected to better than 70% (Tables 4.2, 4.3) — together about a third of all error area. The remainder is made up of confusions with particular look-alike surfaces, disagreement about what counts as parking, and artefacts of the processing pipeline. No one of these dominates; what matters is that recognition is not among them.

**中文翻译**

真正的误差是一组混合问题。边界位置是最大的单项：28.8% 的 FP 距真实停车场不超过 5 m，54.1% 的 FN 距模型已找到的区域不超过 5 m，44.4% 的漏检面积来自模型覆盖率已经超过 70% 的停车场（表 4.2、4.3）。合起来，边界问题约占全部误差面积的三分之一。其余误差来自与特定相似地表的混淆、对“什么算停车场”的定义分歧，以及处理流程本身造成的人为错误。没有一项完全主导；关键是，停车场识别本身不是主要问题。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：28.8, 5, 54.1, 44.4, 70%, 4.2, 4.3；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

That decomposition helps place a claim made for the architecture itself. Xie et al. (2021) report SegFormer as showing strong zero-shot robustness, demonstrated on a benchmark that degrades image quality — noise, blur, weather, digital artefacts — while leaving the scene itself unchanged. Section 2.3 noted that this is not the same test as geographic transfer, and the results here let the distinction be put more concretely. What clearly did carry across is recognition: the model still identifies a car park when it sees one, and the residual blind spot is small. Where the error concentrates instead is in placing boundaries. Whether the model delineates *worse* here than in its source setting is not something this study can say, since no comparable source-domain measurement was available; what can be said is that after the crossing, boundary placement rather than recognition is the binding constraint. A corruption benchmark asks a model to find familiar objects in degraded images, which is closer to the first capacity than the second, so the robustness reported for the architecture and the pattern observed here are not in tension.

**中文翻译**

这一分解也帮助我们理解模型架构原本的主张。Xie et al.（2021）认为 SegFormer 具有很强的零样本稳健性，证据来自降低图像质量的基准测试，例如噪声、模糊、天气和数字伪影，但场景内容并未改变。第 2.3 节指出，这不等同于地理迁移；本研究让区别更具体。明显成功迁移的是“识别能力”：模型看到停车场时通常仍能认出来，真正完全看不到的部分很小。主要错误反而集中在边界绘制。本研究没有来源地区的可比测量，因此不能说模型在英国是否比原地区“画得更差”；能够确定的是，迁移之后的主要限制是边界，而不是识别。图像损坏基准主要测试在变差的影像里认出熟悉目标，更接近识别能力，所以原研究的稳健性结论与这里的发现并不矛盾。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L31](#l31) Xie et al. (2021)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：2.3；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 把文献的一般机制与利兹案例的可检验预期逐项对应。

**英文原稿**

The sampled typology also revises one of the expectations set out in §2.5. Shadow, unusual surfacing and commercial vehicles all appear, at the modest magnitudes anticipated. Absent markings, however, were rarer in the sample than expected: irregular layout was assigned to 11 of the 42 chips and accounts for an estimated 23.3% of the genuine misses, while absent markings was assigned to a single chip and 3.7%. The estimate for the latter therefore rests on one observation and should not be read as a precise share; what the sample supports is the weaker and still useful statement that irregular arrangement was the most frequently identified mechanism and unmarked surfacing among the least. The expectation stated in §2.5 was that unmarked surfaces would be the difficulty, which follows from the annotation protocol's own emphasis on markings; the sample points instead towards arrangement. Setting the expectation out in advance is what makes the revision visible.

**中文翻译**

抽样类型还修正了第 2.5 节的一项预期。阴影、特殊铺装和商用车辆都确实出现，程度也不大。没有标线却比预想少：42 个样本中，11 个被判为布局不规则，估计占真正漏检的 23.3%；只有 1 个被判为没有标线，占 3.7%。后一比例只来自一个样本，不能当作精确估计。样本真正支持的是一个更克制、但仍有用的结论：不规则布局是最常见的失败机制之一，而无标线地面是最少见的机制之一。第 2.5 节原先根据标注规则对标线的强调，预期无标线地面最困难；样本却指向空间布局。正因为预期事先写明，这个修正才清楚可见。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：2.5, 42, 11, 23.3, 1, 3.7；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

Two findings concern the pipeline rather than the model. First, post-processing is a genuine trade: subtracting buildings and roads raises precision by 0.043 and costs 0.040 of recall (Table 4.5). Second, and less comfortably, it creates a blind spot of its own. The raw model detects rooftop parking at recall 0.916, slightly *better* than ground-level parking, and building subtraction deletes four fifths of it (Table 4.6); across all whole-lot misses, 31.9% were found by the model and then removed by the pipeline. A correction step justified by a sound premise — that a roof cannot be surface parking — is wrong precisely where the protocol says rooftop parking counts.

**中文翻译**

另有两项发现针对处理流程，而不是模型。第一，后处理确实是一项取舍：扣除建筑和道路使精确率提高 0.043，但召回率损失 0.040（表 4.5）。第二，更值得警惕的是，它自己创造了盲区。原始模型识别屋顶停车的召回率为 0.916，甚至略高于地面停车；建筑扣除却删除了其中五分之四（表 4.6）。在所有整块停车场漏检中，31.9% 其实已经被模型找到，随后被流程删掉。一个看似合理的前提——屋顶不可能是地面停车——恰好与标注规则“屋顶停车也算”的定义冲突。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：0.043, 0.040, 4.5, 0.916, 4.6, 31.9；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

This has a bearing on how the transfer literature frames its object. Domain adaptation research treats the *model* as the thing that transfers, and asks how to close the gap between source and target feature distributions (Lyu et al., 2025). What is deployed in practice, however, is a pipeline: a model plus a set of ancillary corrections calibrated to the source setting. The rooftop result is a transfer failure located entirely in the corrections and invisible to any measure taken on the network alone; at 31.9% of whole-lot misses it is about half the size of the model's own blind spot, which is a large share for a component that no evaluation of the model would ever surface. Where a pipeline rather than a bare model is carried between settings, its correction stages seem worth re-examining alongside it.

**中文翻译**

这会影响迁移研究如何界定研究对象。领域适应研究通常把“模型”视为迁移对象，关心如何缩小来源域和目标域之间的特征差异（Lyu et al., 2025）。但实际部署的通常是整条流程：模型加上一组按来源地区情况设计的辅助修正规则。屋顶结果是一种完全发生在修正规则中的迁移失败，只评估神经网络本身根本看不到它。它占整块漏检的 31.9%，大约是模型自身盲区的一半；对于一个模型评估不会暴露的组件，这个比例很大。因此，在不同地区迁移的是整条流程时，修正阶段也应与模型一起重新检验。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 见 [L19](#l19) Lyu et al. (2025)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：31.9；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

The ablation settles a further tempting inference. Industrial and commercial land coincides with 52.8% of false-positive area, which invites using it as a filter. Doing so collapses recall from 0.854 to 0.279 and IoU from 0.520 to 0.214, because supermarket and retail-park car parks sit on exactly that land. **Reference layers can explain where error falls without being able to remove it.** Nor is the lesson simply that broad layers are unsafe and narrow ones safe: of the four additional filters tested, every one lowered IoU, the narrow ones slightly (sports pitches −0.007, widened road buffers −0.006) and the broad land-use class catastrophically (−0.306). The two subtractions retained in the pipeline earn their place; the further ones tested here all cost more than they bought.

**中文翻译**

消融实验还否定了另一个很诱人的推断。工业和商业用地与 52.8% 的 FP 重合，很容易让人想把这个图层当作过滤器。但这样做会把召回率从 0.854 压到 0.279，把 IoU 从 0.520 压到 0.214，因为超市和零售园停车场本来就位于这种土地上。**参考图层可以解释错误出现在哪里，却不一定能安全地删除错误。** 结论也不只是“宽泛图层危险、精细图层安全”：新增的四种过滤器全部降低 IoU，精细图层降得较少（运动场 −0.007，扩大道路缓冲区 −0.006），宽泛土地利用图层则造成灾难性下降（−0.306）。流程原有的两项扣除总体上值得保留，但这里测试的进一步过滤全都得不偿失。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：52.8, 0.854, 0.279, 0.520, 0.214, 0.007, 0.006；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

**RQ3 — How much central-city land is surface parking, and where is it concentrated?**

**中文翻译**

**RQ3——中心城区有多少土地用于地面停车？它集中在哪里？**

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

Surface parking covers 3.26% of the 100 km² study area, rising to 3.30% once the sampled corrections to the reference are applied (Table 4.8) — a figure measured by complete labelling rather than estimated from the model. The highest shares are in the inner 2 km, at 5.33% and 7.11% in the two innermost bands, with a monotonic decline beyond to 1.39% past 4 km. The two-cell innermost band is too small to establish whether the profile turns down at the very centre. The distribution across cells is strongly right-skewed: a median cell holds 1.71%, but six cells exceed 10%.

**中文翻译**

地面停车覆盖 100 km² 研究区的 3.26%；按抽样结果修正参考数据后为 3.30%（表 4.8）。这个数字来自完整人工标注，而不是模型估计。停车占地比例在内侧 2 km 最高，两个最内环带分别为 5.33% 和 7.11%，此后单调下降，4 km 外仅为 1.39%。最内环带只有两个单元，不足以证明停车比例在最中心真的回落。逐单元分布明显右偏：中位单元为 1.71%，但 6 个单元超过 10%。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：100, 3.26, 3.30, 4.8, 2, 5.33, 7.11；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 继续明确 3.26% 来自人工参考而非模型估计，并避免把 3.30% 当作独立观测。

**英文原稿**

The shape of that profile is worth setting against the way urban land is usually described radially. Jiao (2015) shows that urban land density follows regular functions that decline with distance from the centre. The parking profile measured here is not simply a scaled version of that form: rather than falling away from the centre throughout, it is roughly level across the inner 2 km and declines only beyond. The two are not the same quantity and no contradiction arises, but the difference invites a question the data cannot settle — whether surface parking is displaced outward from where land is most valuable while remaining dependent on proximity to it. Testing that would need land-value data and more cells near the centre than this study has.

**中文翻译**

这一径向形态可以和城市土地通常的描述作比较。Jiao（2015）发现，城市土地密度通常按规则函数随距市中心距离下降。本研究的停车曲线并不是这个形态的简单缩放：它没有从中心开始持续下降，而是在内侧 2 km 大致持平，之后才降低。两者测量的不是同一概念，所以并不矛盾；但差异提出了一个当前数据无法回答的问题：地面停车是否被挤出地价最高的最中心，同时又依赖与中心的接近性？要检验这一点，需要土地价值数据，也需要比本研究更多的中心附近单元。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L15](#l15) Jiao (2015)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：2；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

## 5.2 迁移后的地图适合做什么

**英文原稿**

The practical question is not whether 0.571 is a good precision but what a map of that precision supports — the question of fitness for use raised in §1.1, on which quality depends jointly on the data and on the task asked of it (Devillers et al., 2007). The three answers below differ not because the map differs but because the task does.

**中文翻译**

实际问题不是“0.571 的精确率算不算好”，而是这种精确率的地图能支持什么用途。这就是第 1.1 节提出的“是否适合用途”：质量由数据本身和使用者要它完成的任务共同决定（Devillers et al., 2007）。下面三个答案不同，不是因为地图发生了变化，而是因为任务不同。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 见 [L06](#l06) Devillers et al. (2007)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：0.571, 1.1；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

It supports **locating** parking. Recall is high, spatially even, and stable across every correction applied in §4.6, so a user asking where the surface parking is will be given an answer that is right about most of it.

**中文翻译**

它适合**寻找停车场位置**。召回率较高，在空间上也较均匀，而且经过第 4.6 节所有校正后都很稳定。因此，若用户问“地面停车大致在哪里”，地图能找出其中绝大部分。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：4.6；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

It supports **area estimation after one local validation**, at a stated grain. The over-prediction is systematic, not noise, and the estimator *T = A · p/r* corrects it. Tested by holding cells out, a factor fitted on half the city predicts the other half to within about ±7%, but predicts an individual 1 km² cell within ±25% only 63% of the time. The map can therefore give a total over an area of tens of square kilometres; it cannot give a grid-cell value. Between those two extremes the evidence is thinner: the distance bands, which range from 2 to 51 cells, show errors between −20% and +13%.

**中文翻译**

它适合在**进行一次本地验证后估算较大区域的面积**，但必须说明空间尺度。过度预测是系统偏差，不是随机噪声，因此可以用 \(T=A\cdot p/r\) 校正。留出检验显示，用半个城市拟合的因子可以把另半个城市预测到约 ±7% 内；但预测单个 1 km² 单元时，只有 63% 的结果落在 ±25% 内。因此，它可以估算几十平方公里区域的停车总面积，不能可靠地给出单个格网值。两者之间的尺度证据较弱：包含 2–51 个单元的距离环带，误差在 −20% 到 +13% 之间。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：±7, 1, 63%, ±25, 2, 51, 20%；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 增加跨城市外部验证后再把 ±7% 当作一般能力。

**英文原稿**

There is a practical corollary worth stating plainly. Because *p/r* reduces to the ratio of labelled to predicted area, calibrating the model in a second city requires only a labelled *total area* over a sample of cells — not a full object-level error analysis of the kind undertaken here. The expensive part of this study does not have to be repeated to reuse its output.

**中文翻译**

这里还有一个很实际的结论。因为 \(p/r\) 最终就是“标注面积／预测面积”，若要在第二个城市校准，只需在一批抽样单元中标出**停车总面积**，不必重复本研究完整的对象级误差分析。也就是说，重复使用模型时不需要再次承担本研究最昂贵的部分。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

It does **not** support uncorrected area measurement, per-cell values, or any site-level judgement. The 1.50× over-prediction is large enough that an uncorrected figure would be wrong by half, and a third of the unexplained over-prediction is not error at all but parking the annotation rules exclude by design.

**中文翻译**

它**不适合**直接使用未经校正的面积、逐单元数值或任何具体地点层面的判断。1.50 倍的过度预测意味着直接使用结果会高估一半；而无法解释的过度预测中，还有三分之一其实不算模型错误，而是标注规则有意排除的真实停车区域。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：1.50；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

## 5.3 误差分解带来的方法启示

**英文原稿**

Three observations follow that concern method rather than parking. Each comes from a single case and is offered as such.

**中文翻译**

下面三点讨论的是评估方法，而不是停车本身。它们都来自一个案例，因此应按案例证据理解。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

The first is that two maps with the same overall accuracy can differ in ways that matter for use. Cross-city benchmarks conventionally report a per-city IoU (Maggiori et al., 2017), and the figure obtained here would read as unremarkable against that convention. What it does not show is that recognition transferred largely intact while delineation did not; a map with the opposite profile and an identical IoU would be less useful for locating parking and more useful for measuring the lots it did find. Separating the two requires only the reference dataset that any validation exercise already needs.

**中文翻译**

第一，两张总体准确率相同的地图，在实际用途上可能完全不同。跨城市基准通常报告每个城市的 IoU（Maggiori et al., 2017），本研究的数字按这种惯例看并不特别。但 IoU 没有告诉我们：识别能力基本成功迁移，边界绘制却没有同样成功。另一张地图完全可能有相同 IoU，却恰好相反——它找到的停车场画得很准，但漏掉许多停车场；那种地图不适合找位置，却可能更适合测量已找到的地块。把两类能力分开，并不需要额外数据，只需使用任何验证本来就必须有的参考数据。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 见 [L20](#l20) Maggiori et al. (2017)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

The second is that a measured accuracy figure can combine differences of quite different kinds. Part of the shortfall here is a domain difference of the sort adaptation methods are designed to address (Lyu et al., 2025; Hong et al., 2023). Another part — 34.9% of the unexplained over-prediction — is on-street parking and private driveways, real parking that the annotation rules exclude by design. That component reflects where the scope line was drawn rather than what the model can see, and it would respond to a different remedy. Distinguishing them is what allows the effective precision of §4.6 to be reported alongside the measured one.

**中文翻译**

第二，一个准确率数字可能混合性质完全不同的差异。本研究一部分误差确实来自领域差异，是领域适应方法试图解决的问题（Lyu et al., 2025; Hong et al., 2023）。但无法解释的过度预测中还有 34.9% 是路边停车和私人车道：它们确实是停车区域，只是标注规则有意排除。这部分误差反映的是研究范围边界画在哪里，而不是模型能不能看见目标，因此需要完全不同的解决办法。正因为把两者分开，第 4.6 节才能同时报告“测得精确率”和“有效精确率”。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 见 [L13](#l13) Hong et al. (2023)、[L19](#l19) Lyu et al. (2025)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：34.9, 4.6；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

The third concerns the correction factor. Olofsson et al. (2014) set out how to adjust a mapped area using reference data, together with the uncertainty of the resulting estimate. What that framework does not speak to is a spatial question a user of a transferred map will meet: a factor estimated over one area, how far does it carry to another? The hold-out design of §3.9 is a small step towards it, and the answer here was at least specific — within about ±7% across half a city, and not at the scale of a single square kilometre.

**中文翻译**

第三点涉及校正因子。Olofsson et al.（2014）说明了如何用参考数据修正地图面积，以及如何计算估计的不确定性。但这个框架没有直接回答迁移地图使用者会遇到的空间问题：在一个区域估出的因子，能够带到多远的另一个区域？第 3.9 节的留出设计对此作了一个小规模尝试，并至少得到明确答案：在半个城市尺度上误差约为 ±7%，在单个 1 km² 单元尺度上则不成立。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 见 [L22](#l22) Olofsson et al. (2014)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：3.9, ±7, 1；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 增加跨城市外部验证后再把 ±7% 当作一般能力。

## 5.4 对英国停车证据和城市加密发展的意义

**英文原稿**

Bates and Leibling (2012) concluded that a central obstacle to coherent parking policy in Britain is simply that little information is collected about how much parking exists. This study supports that diagnosis and adds an account of why the gap persisted. The two routes by which parking has been quantified elsewhere are both closed in the UK: the American inventories depend on cadastral records and codified parking requirements the country does not hold in comparable form (Scharnhorst, 2018; Hoehne et al., 2019), and the British alternative of ground survey has not been repeated at that scale since the London exercise of 1999. What is demonstrated here is a third route, which needs neither. The result is also of a different kind from the American work: those studies count *spaces*, which cannot be converted to a land share without assumptions about layout and aisle provision, whereas the measure here is area directly.

**中文翻译**

Bates 和 Leibling（2012）认为，英国难以形成连贯停车政策，一个核心障碍就是几乎没有系统收集“到底有多少停车设施”的信息。本研究支持这一判断，并进一步解释了数据缺口为何长期存在。其他地方常用的两条量化路径在英国都走不通：美国清单依赖英国没有同类形式的地籍记录和法定停车要求（Scharnhorst, 2018; Hoehne et al., 2019）；英国的替代方案是地面调查，但自 1999 年的伦敦调查后，没有按相同规模重复。本研究展示了不依赖这两者的第三条路径。它与美国研究得到的结果类型也不同：美国研究统计**车位数**，若要换成土地占比，必须假设布局和通道面积；本研究直接测量面积。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L01](#l01) Bates and Leibling (2012)、[L12](#l12) Hoehne et al. (2019)、[L26](#l26) Scharnhorst (2018)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：1999；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

Two features of that result matter more than the headline share. The first is where it sits. The highest parking shares fall in the inner 2 km, which includes the band Centre for Cities research identifies as driving Britain's density gap, where post-war neighbourhoods just beyond the city centre are markedly less dense than comparable pre-war ones (Lange, Kovacevic and Johnson, 2026). That the two coincide in location is worth noting; this study does not establish that they are related, and the coincidence should not be read as a mechanism. What can be said is narrower and still useful: the band where the density deficit is largest is not a band where surface parking is scarce.

**中文翻译**

比总体占比更重要的是结果的两个特征。第一是它位于哪里。停车比例最高的区域在内侧 2 km，而 Centre for Cities 的研究认为，英国密度差距主要也来自这个地带：市中心外侧的战后社区，密度明显低于可比的战前社区（Lange, Kovacevic and Johnson, 2026）。二者位置重合值得注意，但本研究没有证明两者存在因果关系，不能把重合直接当成机制。能够谨慎说的是：密度不足最严重的地带，并不是一个地面停车稀少的地带。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L16](#l16) Lange, Kovacevic and Johnson (2026)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：2；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

The second is concentration, which bears on how Shoup's (2005) argument should be applied spatially. That argument is about an aggregate opportunity cost — land committed to parking is land not doing something else. The distribution found here is strongly uneven: a median cell gives over 1.71% of its area to parking while six cells exceed 10%. An aggregate share of 3.26% would suggest a diffuse phenomenon spread thinly across the city, in which case the opportunity cost would be real but hard to act on anywhere in particular. The distribution says otherwise. For policy directed at finding under-utilised land (MHCLG, 2024, para. 125(d)), the aggregate share understates how concentrated the opportunity is, and where that concentration falls is the kind of question this map can help with.

**中文翻译**

第二是停车用地高度集中，这会影响如何在空间上理解 Shoup（2005）的论点。Shoup 讨论的是总体机会成本：土地用于停车，就不能用于其他用途。本研究发现分布非常不均匀：中位单元只有 1.71% 用于停车，但 6 个单元超过 10%。若只看全区 3.26%，容易以为停车用地稀薄而均匀地散布在城市中，机会成本虽然存在，却很难在具体地点采取行动。实际分布并非如此。对于寻找低效用地的政策（MHCLG, 2024, para. 125(d)），总体占比反而低估了机会集中的程度；而指出这种集中发生在哪里，正是这张地图能够帮助回答的问题。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 见 [L21](#l21) MHCLG (2024)、[L28](#l28) Shoup (2005)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：1.71, 6, 10%, 3.26, 125；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 继续明确 3.26% 来自人工参考而非模型估计，并避免把 3.30% 当作独立观测。

**英文原稿**

Finally, the OpenStreetMap comparison contributes a small result to the VGI quality literature. Haklay (2010) established that OSM completeness varies substantially between places, and later reviews confirm the pattern by area and by feature type (Sehra, Singh and Rai, 2013; Zhou, Wang and Liu, 2022). The measurement here adds a characteristic of *how* it is incomplete for one feature class: 63.5% of labelled parking is absent from OSM, yet the median polygon areas of the two sources are almost identical, so the omission is not selective by object size. On that evidence a user of OSM parking data is not simply receiving the large car parks and missing the small ones — though a shared median is weak evidence about the rest of the size distribution, and a fuller comparison would test it properly. The records judged not to show parking are also the most recently edited of any sampled category, so the omission and the disagreement are not explained by OSM simply being old.

**中文翻译**

最后，与 OpenStreetMap 的比较也为志愿地理信息质量研究提供了一个小发现。Haklay（2010）证明 OSM 完整性在不同地点差异很大，后续综述也确认它会随地区和要素类型变化（Sehra, Singh and Rai, 2013; Zhou, Wang and Liu, 2022）。本研究进一步描述了一个要素类别具体“怎样不完整”：63.5% 的人工标注停车在 OSM 中缺失，但两套数据的多边形面积中位数几乎相同，所以遗漏并非明显只针对小停车场。换句话说，OSM 用户并不是简单地“得到大停车场、漏掉小停车场”。不过，中位数相同只能提供较弱证据，要确认完整面积分布还需更全面比较。时间戳检查也排除了最方便的解释，因为被判断为错误的记录反而是各抽样类别中最近编辑的。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：正文表述已与 Sehra et al.（2013）原文一致——该综述记录城乡完整度差异在不同国家方向不同（德、英与美国相反），正文不再断言“普遍城市高于乡村”。
> - **文献原句：** 见 [L11](#l11) Haklay (2010)、[L27](#l27) Sehra, Singh and Rai (2013)、[L32](#l32) Zhou, Wang and Liu (2022)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：63.5；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 缩窄该概括，或补一项直接比较英国城乡 OSM 完整度的原始研究。

## 5.5 局限与未来研究

**英文原稿**

**One city.** The calibration factor was tested by holding out cells within Leeds, not across cities, so its transferability between cities remains unestablished. The corollary in §5.2 makes this tractable: because the factor is an area ratio, testing it elsewhere needs only labelled total area on a sample of cells.

**中文翻译**

**仅研究一个城市。** 校正因子是在利兹内部留出单元测试，而不是跨城市测试，所以它能否在不同城市之间迁移仍未确定。第 5.2 节的结论使下一步测试可行：因子只是面积比，因此在其他城市只需对一批抽样单元标注总面积。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：5.2；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

**A single annotator.** Detection is markedly lower for lots the annotator marked uncertain (0.713 against 0.856, Table 4.4), which means the reference itself sets a ceiling on measurable accuracy. That reference data quality bounds what an accuracy assessment can report is long recognised (Foody, 2002); what this study can add is a measured indication of where the bound lies for this target. Multiple annotators and a reported agreement coefficient would establish it properly.

**中文翻译**

**只有一名标注者。** 标注者认为不确定的停车场，模型检出率明显较低（0.713 对 0.856，表 4.4）。这意味着参考数据本身给可测准确率设了上限。参考数据质量会限制准确率评估早已得到认识（Foody, 2002）；本研究能增加的，是针对这个目标测出上限大致出现在哪里。未来应使用多名标注者，并报告一致性系数。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L07](#l07) Foody (2002)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：0.713, 0.856, 4.4；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

**Two imagery sources.** The reference was labelled over a satellite basemap and the predictions were produced from Digimap tiles. The effect of the difference is bounded by construction at 2.1% of labelled area and measured by sampling at 1.0%, with precision unaffected (§3.8), and the two sources are co-registered to well within a pixel. Labelling on the model's own input imagery would remove the question rather than bound it.

**中文翻译**

**使用两套影像。** 人工标注绘制在卫星底图上，而模型使用 Digimap 图块。通过分析，这一影响的逻辑上限为标注面积的 2.1%，抽样估计为 1.0%（第 3.8 节），配准偏移也小于一个像素。但问题只是被限制和测量，并没有被消除。直接在模型输入影像上标注，才能彻底去掉这项问题。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：2.1, 1.0, 3.8；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

**Conventions that shape the numbers.** The 5 m boundary band is a convention, not a natural break, which is why 2 m and 10 m are reported alongside; the choice moves the dilation component by nearly twenty points. The sampling frame excludes fragments below 100 m², covering 0.3883 km² of a 0.4396 km² residual. And attribution against reference layers is positional: a false positive *located on* industrial land has not been individually confirmed to be a storage yard.

**中文翻译**

**会影响数字的分析约定。** 5 m 边界带是人为约定，不是自然断点，因此本文同时报告 2 m 和 10 m；阈值选择会使边界外扩占比变化接近 20 个百分点。抽样框排除了小于 100 m² 的碎片，只覆盖 0.4396 km² 剩余面积中的 0.3883 km²。此外，参考图层归因只是位置判断：“FP 位于工业用地”并不代表每一个都经人工确认是堆场。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：5, 2, 10, 20, 100, 0.4396, 0.3883；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

**A definitional boundary doing real work.** On-street parking and private driveways account for 34.9% of the unexplained over-prediction. These are real parking that the rules exclude, so the measured precision partly reflects where the scope line was drawn rather than what the model can see. A different but equally defensible protocol would produce a different headline figure from the same map — which is an argument for reporting the protocol in full, as Appendix A does, rather than only the number it produces.

**中文翻译**

**定义边界确实影响了结果。** 路边停车和私人车道占无法解释过度预测的 34.9%。这些地方确实有停车，只是规则将其排除，所以测得精确率一部分反映研究范围怎样划定，而不是模型能看见什么。同一张地图若使用另一套同样合理的协议，就会得到不同的主要数字。这正说明完整公开标注协议很重要，不能只报告最后一个准确率；附录 A 因此给出了完整规则。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：34.9；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

Beyond these, the most specific opportunity comes from the typology itself. If irregular arrangement is the mechanism most often identified among the genuine misses, then training data would be better extended with irregularly arranged car parks than simply with unmarked ones — though on eleven sampled chips that is a direction to test rather than a settled quantity.

**中文翻译**

除上述局限外，误差类型学给出的最具体机会来自布局机制。如果在真正漏检中最常被识别的是不规则布局，那么训练数据应优先增加布局不规则的停车场，而不只是增加无标线停车场；不过，这一判断只来自 11 个被如此分类的抽样图块，因此应被视为待检验方向，而不是已经稳定的数量结论。

> **段落审读**
> - **逻辑用途：** 从误差机制推出一个具体、可检验的训练数据改进方向
> - **核对状态：** ✅ 已核对：不规则布局类别来自分层抽样，但样本量仅 11，原文已把它限定为研究方向。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/sampling_results.csv`、`analysis/fn_analysis_summary.csv`；本段核对值：11 个 `irregular_layout` 样本；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 用更多样本、第二座城市和预注册类别检验该方向，再决定是否调整训练集构成。

**英文原稿**

A supplementary experiment tested the other half of that proposition — whether the typology can also direct how a model is trained — and found that it does not follow. Generic fine-tuning on Leeds labels raised raw-pixel IoU from 0.485 to 0.614, trading 0.127 of recall for 0.247 of precision. Weighting the loss by the positional categories of §4.2 did not improve on this: the two targeted checkpoints reached 0.572 and 0.564, and their selectivity gap between targeted and other categories, at 8.4 and 7.8 points, fell below the 9.7 of generic fine-tuning. Adjusting the decision threshold of the generic model alone, chosen on validation cells, then reached or bettered both targeted operating points, giving higher precision and higher IoU at comparable recall; the ordering is unchanged under macro aggregation. Positional error categories therefore explain where transfer fails without translating into a training gain that a threshold could not supply. This does not close off visually defined targeting, which would need hard negatives confirmed by inspection rather than positional proxies, tested across seeds, spatial splits and a second city. Nor does it bear on the irregular-layout direction above, which the experiment did not test. These are raw-pixel figures on 50 held-out cells, not comparable with those of Chapter 4; Appendix C reports the design and results in full.

**中文翻译**

一项补充实验检验了这一命题的另一半——误差类型学能否直接指导模型训练——结果表明二者并不自然相连。用利兹标签进行普通微调，把原始像素 IoU 从 0.485 提高到 0.614，以损失 0.127 召回率换取 0.247 精确率。按 §4.2 的位置类别加权损失并未超过这一结果：两个定向检查点的 IoU 为 0.572 和 0.564，定向类别相对其他类别的选择性差距为 8.4 和 7.8 个百分点，均低于普通微调的 9.7。随后，只在验证单元上选择普通模型的决策阈值，就达到或超过两个定向运行点：在召回率相近时，精确率和 IoU 都更高，macro 汇总下排序也不变。因此，位置型错误类别能够解释迁移在哪里失败，却没有转化为阈值调整无法提供的训练增益。这不排除按视觉特征进行定向训练；后者需要人工确认的困难负样本，并跨随机种子、空间划分和第二座城市检验。它也不检验上一段的不规则布局方向。以上结果来自 50 个留出单元的原始像素，不能与第 4 章数字比较；完整设计与结果见附录 C。

> **段落审读**
> - **逻辑用途：** 检验误差归因能否直接转化为定向训练收益，并限定阴性结果的含义
> - **核对状态：** ✅ 已核对：普通微调、两个定向检查点与阈值匹配结果均与附录 C 的五张结果表一致。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`、`selectivity.csv`、`threshold_sweep/generic_threshold_selected.csv`；核对值：IoU 0.485→0.614，定向 0.572/0.564，选择性差距 8.4/7.8/9.7；译文对应位置：`05_discussion.md`（仅作定位，不作为引文证据）
> - **可加强：** 增加多随机种子、视觉类别困难负样本和第二城市测试，才能判断定向训练一般是否无效。

# 6. 结论

**英文原稿**

This dissertation tested whether a US-trained surface-parking segmentation model can be used to measure off-street surface parking in a British city. The model was applied to 100 km² of Leeds exactly as released, with no UK training data in the primary analysis, and evaluated against 2,037 manually labelled car parks drawn to the source model's own target definition. The error was then decomposed rather than merely reported: attributed exhaustively against independent reference layers, characterised by stratified sampling of 142 image chips adjudicated on the imagery the model actually consumed, and tested by ablation of the post-processing stage.

**中文翻译**

本论文检验了一个在美国数据上训练的地面停车分割模型，能否用于测量英国城市的路外地面停车。模型完全按公开版本应用于利兹 100 km² 的研究区，主分析中没有使用任何英国训练数据；评估参考是按照原模型目标定义人工绘制的 2,037 个停车场。研究没有停留在报告一个准确率数字，而是进一步分解误差：用独立参考图层对全部误差作自动归因，对 142 个影像切片进行分层抽样并依据模型实际使用的影像人工判断，还通过消融实验检验后处理阶段。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：100, 2,037, 142；译文对应位置：`06_conclusion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

The transfer works asymmetrically. Recall of 0.854 is high and spatially even; precision of 0.571 is neither, and the model predicts 1.50 times the labelled parking area. Accuracy within the city tracks not distance from the centre but how much parking a cell contains — an apparent location effect that dissolves once parking abundance is controlled for.

**中文翻译**

迁移结果是不对称的。召回率 0.854，较高而且空间上均匀；精确率 0.571，较低且空间差异明显，模型预测面积是标注面积的 1.50 倍。城市内部的准确率并不由距市中心距离决定，而主要与目标有多少、面积有多大有关。控制停车数量后，表面上的位置效应就消失了。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：0.854, 0.571, 1.50；译文对应位置：`06_conclusion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

What the error is not is a failure to recognise parking: the genuine blind spot — parking present in the imagery that the model did not see — is at most 2.1% of labelled area, or under 3% of all error area. Boundary placement is the largest single component, at 28.8% of false-positive and 54.1% of false-negative area, with the remainder split between confusions with particular look-alike surfaces, disagreement over what counts as parking, and pipeline artefacts. Among the sampled whole-lot misses, irregular arrangement was the most frequently identified mechanism and absent markings among the least. Post-processing is a real trade, buying 0.043 of precision for 0.040 of recall, but it also creates a blind spot of its own: the raw model detects rooftop parking better than ground-level parking, and building subtraction deletes four fifths of it.

**中文翻译**

误差主要来自边界和布局，而不是模型无法识别停车场。边界效应占 FP 面积的 28.8% 和 FN 面积的 54.1%；影像中确实存在、但模型完全没有看到的真正盲区，最多只占标注面积的 2.1%。模型完全漏掉停车场时，不规则布局造成的影响约为没有标线的六倍。后处理是一项真实取舍：它用 0.040 的召回率换来 0.043 的精确率；但它也制造了自己的盲区——原始模型识别屋顶停车比地面停车还好，建筑扣除却删掉了其中五分之四。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：28.8, 54.1, 2.1, 0.040, 0.043；译文对应位置：`06_conclusion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

Under that measured reliability, surface parking covers 3.26% of the study area as labelled, or 3.30% after the sampled corrections. The highest shares fall in the inner 2 km, reaching 7.11% in the 1–2 km band, with a clear decline beyond; and it is strongly concentrated: a median cell gives over 1.71%, while six exceed 10%.

**中文翻译**

在上述已测可靠性下，人工标注显示地面停车覆盖研究区的 3.26%；应用抽样校正后为 3.30%。最高占比出现在内侧 2 km，其中 1–2 km 环带达到 7.11%，再往外明显下降。停车用地还高度集中：中位单元为 1.71%，但 6 个单元超过 10%。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：3.26, 3.30, 2, 1, 7.11, 1.71, 6；译文对应位置：`06_conclusion.md`（仅作定位，不作为引文证据）
> - **可加强：** 继续明确 3.26% 来自人工参考而非模型估计，并避免把 3.30% 当作独立观测。

**英文原稿**

**Contributions.** Four, in ascending order of transferability beyond this case. First, an empirical measurement of how a published US-trained parking segmentation model behaves in a British city, previously unavailable. Second, a reusable method for decomposing area-based segmentation error into boundary effects, attributable confusions, definitional disagreement and pipeline artefacts — a decomposition that turns a single accuracy figure into a statement about which uses survive. Third, evidence that a post-processing step justified by a sound premise can create a systematic blind spot, which is an argument for evaluating correction stages rather than assuming them. Fourth, a bias-correction estimator with its spatial grain established by hold-out rather than asserted: it holds to about ±7% at half-city scale and fails at the scale of a single square kilometre.

**中文翻译**

**研究贡献。** 按超出本案例的可迁移程度递增，共有四项。第一，首次实证测量一个公开的美国训练停车分割模型在英国城市中的表现。第二，提出一套可复用的方法，把面积分割误差分成边界效应、可归因混淆、定义分歧和处理流程人为错误，从而把单一准确率转化成“哪些用途仍然可靠”的判断。第三，证明即使后处理步骤的出发点合理，也可能制造系统性盲区，因此修正阶段也必须接受评估，不能默认其正确。第四，提出偏差校正方法，并用留出检验而不是口头假设确定其适用空间尺度：在半个城市尺度上约为 ±7%，在单个 1 km² 尺度上失效。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：±7, 1；译文对应位置：`06_conclusion.md`（仅作定位，不作为引文证据）
> - **可加强：** 增加跨城市外部验证后再把 ±7% 当作一般能力。

**英文原稿**

**Future work.** The calibration factor reduces to a ratio of labelled to predicted area, so testing whether it transfers between cities requires only labelled totals over a sample of cells rather than a repeat of the full error analysis undertaken here — which makes multi-city validation affordable and is the obvious next step. The typology points to a direction for training data: irregularly arranged car parks rather than simply unmarked ones, on the strength of eleven sampled chips. Imagery carrying a near-infrared band would test the one expected failure this study could not examine. A supplementary experiment (Appendix C) narrows what that validation should compare. Generic fine-tuning improved raw-pixel IoU while trading recall for precision; weighting the loss by positional error categories added neither overall nor selective gain, and its operating points were matched or bettered by adjusting the generic model's threshold alone. The open question is no longer whether local supervision helps, but which kind earns its labelling cost — a comparison of zero-shot use, area calibration, generic fine-tuning and visually targeted fine-tuning, judged on locating parking, estimating area, and the precision–recall trade-off each implies.

**中文翻译**

**未来工作。** 校正因子最终只是“标注面积／预测面积”的比率，因此，要检验它能否跨城市迁移，只需在若干抽样单元中取得标注总面积，不必重复本研究完整的误差分析。这使多城市验证的成本可接受，也自然成为下一步。误差类型还指出了明确的训练数据改进方向：增加布局不规则的停车场，而不只是增加无标线停车场。使用带近红外波段的影像，可以检验本研究未能考察的一项预期失败。最后，本地微调究竟能改善边界误差、定义差异，还是两者都不能改善，也可以继续用本文建立的分解方法回答。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`06_conclusion.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

A transferred model cannot yet be trusted to measure how much land a British city gives to parking. Paired with one local validation, it can — and that is a materially different claim from either accepting or dismissing the map.

**中文翻译**

一个未经验证的迁移模型，目前还不能直接被信任来测量英国城市把多少土地用于停车；但只要配合一次本地验证，它就可以做到。这与“直接接受地图”或“彻底否定地图”都是本质不同的结论。

> **段落审读**
> - **逻辑用途：** 限制结论适用范围，防止从城市尺度证据跳到地块判断
> - **核对状态：** 🟨 需人工复核：限制来自研究设计与已报告验证结果。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；译文对应位置：`06_conclusion.md`（仅作定位，不作为引文证据）
> - **可加强：** 区分可在本研究内量化的限制和只能在未来研究中检验的限制。

# 参考文献

**英文原稿**

> **草稿 v5**｜33 条，Harvard（Cite Them Right）
> **正文引用**：三位作者列全，四位及以上用 *et al.*
> **本表**：作者六位以内列全，超过六位用 *et al.*（Cite Them Right 允许四位以上简写）
> **核实状态**：33 条已全部对照原文核实，原文存于 `resource/`（Qiam et al. 存于 `Parking/literature/`）。三处例外须留意：Openshaw (1984) 原件（CATMOG 38）扉页未印年份，1984 取自标准目录记录，文内引及 1983 年资料可佐证下限；Stehman & Foody (2019) 与 Stehman & Wickham (2011) 本地均为接受稿（后者取自 US EPA Science Inventory 公开存档），非出版版，卷期页取自出版方著录，如需引页码须回出版版核对。Yin et al. (2022) 已用 Poppler 抽出全部十页正文，书目信息与正文论断均对照原文核实。

**中文翻译**

> **草稿 v5**｜33 条，Harvard（Cite Them Right）
> **正文引用**：三位作者列全，四位及以上用 *et al.*
> **本表**：作者六位以内列全，超过六位用 *et al.*（Cite Them Right 允许四位以上简写）
> **核实状态**：33 条已全部对照原文核实，原文存于 `resource/`（Qiam et al. 存于 `Parking/literature/`）。三处例外须留意：Openshaw (1984) 原件（CATMOG 38）扉页未印年份，1984 取自标准目录记录，文内引及 1983 年资料可佐证下限；Stehman & Foody (2019) 与 Stehman & Wickham (2011) 本地均为接受稿（后者取自 US EPA Science Inventory 公开存档），非出版版，卷期页取自出版方著录，如需引页码须回出版版核对。Yin et al. (2022) 已用 Poppler 抽出全部十页正文，书目信息与正文论断均对照原文核实。

> **段落审读**
> - **逻辑用途：** 声明参考文献格式与核验覆盖范围
> - **核对状态：** ✅ 已核对：附录原引 Yin et al.（2022）属 APKLOT 归属错误，已改为 Hurst-Tarrab et al.（2020）。Yin et al.（2022）原件其后取得并抽出全文，已作为独立文献新增入主参考文献表（第 33 条），与 APKLOT 并列引用、分别支撑不同论断。
> - **文献原句：** 见 [L23](#l23) Openshaw (1984)、[L24](#l24) Qiam, Devunuri and Lehe (2025)、[L29](#l29) Stehman and Foody (2019)、[L30](#l30) Stehman and Wickham (2011)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 引文逐条核对记录为 `citation_audit.md`；原始论文见上方证据索引；本段核对值：32, 1984, 38, 1983；译文对应位置：`07_references.md`（仅作定位，不作为引文证据）
> - **可加强：** 附录 A 的 A.8 Sources 仍是独立小列表，可考虑并入主参考文献表，使全文只保留一份书目。

---

Bates, J. and Leibling, D. (2012) *Spaced out: perspectives on parking policy*. London: RAC Foundation.

Berry, T., Dronen, N., Jackson, B. and Endres, I. (2019) 'Parking lot instance segmentation from satellite imagery through associative embeddings', in *Proceedings of the 27th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems*. New York: Association for Computing Machinery, pp. 528–531. doi:10.1145/3347146.3359364.

Cheng, B., Girshick, R., Dollár, P., Berg, A.C. and Kirillov, A. (2021) 'Boundary IoU: improving object-centric image segmentation evaluation', in *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*. Available at: https://openaccess.thecvf.com/content/CVPR2021/papers/Cheng_Boundary_IoU_Improving_Object-Centric_Image_Segmentation_Evaluation_CVPR_2021_paper.pdf (Accessed: 13 August 2026).

Cochran, W.G. (1977) *Sampling techniques*. 3rd edn. New York: John Wiley & Sons.

Csurka, G., Larlus, D. and Perronnin, F. (2013) 'What is a good evaluation measure for semantic segmentation?', in *Proceedings of the British Machine Vision Conference 2013*. Durham: BMVA Press. Available at: https://www.bmva-archive.org.uk/bmvc/2013/Papers/paper0032/paper0032.pdf (Accessed: 13 August 2026).

Devillers, R., Bédard, Y., Jeansoulin, R. and Moulin, B. (2007) 'Towards spatial data quality information analysis tools for experts assessing the fitness for use of spatial data', *International Journal of Geographical Information Science*, 21(3), pp. 261–282. doi:10.1080/13658810600911879.

Foody, G.M. (2002) 'Status of land cover classification accuracy assessment', *Remote Sensing of Environment*, 80(1), pp. 185–201. doi:10.1016/S0034-4257(01)00295-4.

Foody, G.M. (2005) 'Local characterization of thematic classification accuracy through spatially constrained confusion matrices', *International Journal of Remote Sensing*, 26(6), pp. 1217–1228. doi:10.1080/01431160512331326521.

Goodchild, M.F. (2007) 'Citizens as sensors: the world of volunteered geography', *GeoJournal*, 69(4), pp. 211–221. doi:10.1007/s10708-007-9111-y.

Habermehl, V. and McFarlane, C. (2025) 'The density dialectic: between hard and gentle densification in London', *International Journal of Urban and Regional Research*, 49(3), pp. 569–586. doi:10.1111/1468-2427.13319.

Haklay, M. (2010) 'How good is volunteered geographical information? A comparative study of OpenStreetMap and Ordnance Survey datasets', *Environment and Planning B: Planning and Design*, 37(4), pp. 682–703. doi:10.1068/b35097.

Hoehne, C.G., Chester, M.V., Fraser, A.M. and King, D.A. (2019) 'Valley of the sun-drenched parking space: the growth, extent, and implications of parking infrastructure in Phoenix', *Cities*, 89, pp. 186–198. doi:10.1016/j.cities.2019.02.007.

Hong, D. et al. (2023) 'Cross-city matters: a multimodal remote sensing benchmark dataset for cross-city semantic segmentation using high-resolution domain adaptation networks', *Remote Sensing of Environment*, 299, 113856. doi:10.1016/j.rse.2023.113856.

Hurst-Tarrab, N., Chang, L., Gonzalez-Mendoza, M. and Hernandez-Gress, N. (2020) 'Robust parking block segmentation from a surveillance camera perspective', *Applied Sciences*, 10(15), 5364. doi:10.3390/app10155364.

Jiao, L. (2015) 'Urban land density function: a new method to characterize urban expansion', *Landscape and Urban Planning*, 139, pp. 26–39. doi:10.1016/j.landurbplan.2015.02.017.

Lange, M., Kovacevic, L. and Johnson, Z. (2026) *Course correction: how to densify British cities*. London: Centre for Cities.

Livingstone, N., Fiorentino, S. and Short, M. (2021) 'Planning for residential "value"? London's densification policies and impacts', *Buildings and Cities*, 2(1), pp. 203–219. doi:10.5334/bc.88.

Lv, J., Shen, Q., Lv, M., Li, Y., Shi, L. and Zhang, P. (2023) 'Deep learning-based semantic segmentation of remote sensing images: a review', *Frontiers in Ecology and Evolution*, 11, 1201125. doi:10.3389/fevo.2023.1201125.

Lyu, S. et al. (2025) *Deep learning based domain adaptation methods in remote sensing: a comprehensive survey*. arXiv:2510.15615. Available at: https://arxiv.org/abs/2510.15615 (Accessed: 12 August 2026).

Maggiori, E., Tarabalka, Y., Charpiat, G. and Alliez, P. (2017) 'Can semantic labeling methods generalize to any city? The Inria aerial image labeling benchmark', in *2017 IEEE International Geoscience and Remote Sensing Symposium (IGARSS)*. Fort Worth, TX: IEEE, pp. 3226–3229. doi:10.1109/IGARSS.2017.8127684.

Ministry of Housing, Communities and Local Government (MHCLG) (2024) *National Planning Policy Framework*. London: MHCLG.

Olofsson, P., Foody, G.M., Herold, M., Stehman, S.V., Woodcock, C.E. and Wulder, M.A. (2014) 'Good practices for estimating area and assessing accuracy of land change', *Remote Sensing of Environment*, 148, pp. 42–57. doi:10.1016/j.rse.2014.02.015.

Openshaw, S. (1984) *The modifiable areal unit problem*. Concepts and Techniques in Modern Geography 38. Norwich: Geo Books.

Qiam, S., Devunuri, S. and Lehe, L.J. (2025) 'A pipeline and NIR-enhanced dataset for parking lot segmentation', in *2025 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)*. IEEE, pp. 1227–1236.

Roberts, D.R. et al. (2017) 'Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure', *Ecography*, 40(8), pp. 913–929. doi:10.1111/ecog.02881.

Scharnhorst, E. (2018) *Quantified parking: comprehensive parking inventories for five U.S. cities*. Washington, DC: Research Institute for Housing America.

Sehra, S.S., Singh, J. and Rai, H.S. (2013) 'Assessment of OpenStreetMap data — a review', *International Journal of Computer Applications*, 76(16), pp. 17–20.

Shoup, D.C. (2005) *The high cost of free parking*. Chicago: Planners Press, American Planning Association.

Stehman, S.V. and Foody, G.M. (2019) 'Key issues in rigorous accuracy assessment of land cover products', *Remote Sensing of Environment*, 231, 111199. doi:10.1016/j.rse.2019.05.018.

Stehman, S.V. and Wickham, J.D. (2011) 'Pixels, blocks of pixels, and polygons: choosing a spatial unit for thematic accuracy assessment', *Remote Sensing of Environment*, 115(12), pp. 3044–3055. doi:10.1016/j.rse.2011.06.007.

Xie, E., Wang, W., Yu, Z., Anandkumar, A., Alvarez, J.M. and Luo, P. (2021) 'SegFormer: simple and efficient design for semantic segmentation with transformers', *Advances in Neural Information Processing Systems*, 34, pp. 12077–12090.

Yin, Y., Hu, W., Tran, A., Kruppa, H., Zimmermann, R. and Ng, S.-K. (2022) 'A context-enriched satellite imagery dataset and an approach for parking lot detection', in *2022 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)*. IEEE, pp. 1371–1380. doi:10.1109/WACV51458.2022.00146.

Zhou, Q., Wang, S. and Liu, Y. (2022) 'Exploring the accuracy and completeness patterns of global land-cover/land-use data in OpenStreetMap', *Applied Geography*, 145, 102742. doi:10.1016/j.apgeog.2022.102742.

# 附录 A——人工标注规程

**英文原稿**

These are the rules under which the 2,037 reference car parks of §3.2 were labelled. They are reproduced in full because the measured precision depends on where the scope line was drawn as much as on what the model can see (§5.5), so the protocol has to be inspectable rather than summarised.

**中文翻译**

以下规则用于标注 §3.2 中的 2,037 个参考停车场。之所以完整重现，是因为测得的精确率既取决于研究范围边界画在哪里，也取决于模型能看见什么（§5.5）；因此规程必须可供检查，而不能只作摘要。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：附录用途、2,037 个参考多边形及相关章节号已与方法章和 `manual/leeds_manual.gpkg` 对照。
> - **文献原句：** 本段无外部引文；§3.2 与 §5.5 是论文内部交叉引用。
> - **原始数据／文本依据：** `Rules.md`；`manual/leeds_manual.gpkg`；本段核对值：2,037；译文对应位置：`08_appendix_a_annotation_protocol.md`（仅作定位，不作为引文证据）
> - **可加强：** 可在附录标题下补规则版本日期，便于与最终提交版对应。

## A.1 依据

**英文原稿**

The rules follow the annotation method of the US-trained model applied here (Qiam, Devunuri and Lehe, 2025). The same rules are used so that the accuracy figures are valid: ground-truth labels must follow the definition the model was trained on. Labelling was carried out in QGIS over the Google Satellite basemap.

**中文翻译**

本规则遵循本研究所应用的美国训练模型之标注方法（Qiam, Devunuri and Lehe, 2025）。采用相同规则是为了保证准确率数字有效：地面真值标签必须遵循模型训练时的定义。标注在 QGIS 中对照 Google Satellite 底图完成。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L24](#l24) Qiam, Devunuri and Lehe (2025)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** `Rules.md`；`manual/leeds_manual.gpkg`；Qiam et al.（2025）原文；译文对应位置：`08_appendix_a_annotation_protocol.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

## A.2 对象

**英文原稿**

Off-street surface parking: open-air parking surfaces visible from above, outside public roads. Labels are binary (parking / non-parking). The use served is not recorded, as it cannot be judged reliably from imagery. No minimum-size threshold is applied — all off-street surface parking is labelled regardless of size, to match the definition the model was trained on.

**中文翻译**

路外地面停车：位于公共道路之外、从上方可见的露天停车面。标签为二分类（停车／非停车）。不记录服务用途，因为无法仅凭影像可靠判断。不设最小面积阈值——无论大小，所有路外地面停车均予标注，以匹配模型训练时的定义。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `Rules.md`；`manual/leeds_manual.gpkg`；Qiam et al.（2025）原文；译文对应位置：`08_appendix_a_annotation_protocol.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

## A.3 停车区域的识别

**英文原稿**

An area is labelled as parking where it has marked parking bays, or — where markings are absent — parked cars and a layout of bays and aisles that clearly show parking use. Areas whose use is unclear are left unlabelled or marked confidence 1.

**中文翻译**

若区域内有划线车位，或在没有标线时存在停放车辆且车位—通道布局清楚显示停车用途，则标为停车。用途不明的区域不予标注，或标记为 confidence 1。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `Rules.md`；`manual/leeds_manual.gpkg`；Qiam et al.（2025）原文；本段核对值：1；译文对应位置：`08_appendix_a_annotation_protocol.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

**Include**

**中文翻译**

**纳入**

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `Rules.md`；`manual/leeds_manual.gpkg`；Qiam et al.（2025）原文；译文对应位置：`08_appendix_a_annotation_protocol.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

- Surface car parks, whatever use they serve.
- Parking bays and the internal aisles that connect them.
- Rooftop parking where the parking surface is visible from above.

**中文翻译**

- 各类用途的地面停车场。
- 停车位及连接车位的内部通道。
- 从上方能看见停车面的屋顶停车。

> **段落审读**
> - **逻辑用途：** 把并列规则或步骤拆成可执行清单
> - **核对状态：** 🟨 需人工复核：与相应代码、协议或实验日志一致。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `Rules.md`；`manual/leeds_manual.gpkg`；Qiam et al.（2025）原文；译文对应位置：`08_appendix_a_annotation_protocol.md`（仅作定位，不作为引文证据）
> - **可加强：** 必要时为每项补充通过／失败判据。

**英文原稿**

**Exclude**

**中文翻译**

**排除**

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `Rules.md`；`manual/leeds_manual.gpkg`；Qiam et al.（2025）原文；译文对应位置：`08_appendix_a_annotation_protocol.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

- On-street parking.
- Multi-storey or underground car parks with no visible parking surface.

**中文翻译**

- 路边停车。
- 看不见停车面的多层或地下停车场。

> **段落审读**
> - **逻辑用途：** 把并列规则或步骤拆成可执行清单
> - **核对状态：** 🟨 需人工复核：与相应代码、协议或实验日志一致。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `Rules.md`；`manual/leeds_manual.gpkg`；Qiam et al.（2025）原文；译文对应位置：`08_appendix_a_annotation_protocol.md`（仅作定位，不作为引文证据）
> - **可加强：** 必要时为每项补充通过／失败判据。

**英文原稿**

**Treated as non-parking**, and also the common look-alikes the model most often confuses:

**中文翻译**

**视为非停车**，同时也是模型最常混淆的相似地物：

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `Rules.md`；`manual/leeds_manual.gpkg`；Qiam et al.（2025）原文；译文对应位置：`08_appendix_a_annotation_protocol.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

- Sports courts, storage or depot yards, and other non-parking hardstanding.
- Buildings, roads, pavements and landscaping.

**中文翻译**

- 运动场、储料场或仓储／车场，以及其他非停车硬化地面。
- 建筑、道路、人行道与绿化。

> **段落审读**
> - **逻辑用途：** 把并列规则或步骤拆成可执行清单
> - **核对状态：** 🟨 需人工复核：与相应代码、协议或实验日志一致。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `Rules.md`；`manual/leeds_manual.gpkg`；Qiam et al.（2025）原文；译文对应位置：`08_appendix_a_annotation_protocol.md`（仅作定位，不作为引文证据）
> - **可加强：** 必要时为每项补充通过／失败判据。

## A.4 引道

**英文原稿**

Only very short entrances belonging to a car park are included. Longer access roads are excluded, so that the labels do not teach the model to recognise roads (Qiam, Devunuri and Lehe, 2025).

**中文翻译**

只纳入属于停车场的很短入口。较长的出入道路予以排除，避免标签把道路教成目标类别（Qiam, Devunuri and Lehe, 2025）。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L24](#l24) Qiam, Devunuri and Lehe (2025)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** `Rules.md`；`manual/leeds_manual.gpkg`；Qiam et al.（2025）原文；译文对应位置：`08_appendix_a_annotation_protocol.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

**Supplementary rule — residential parking.** Individual single-house driveways or forecourts — a few cars, clearly one household — are not labelled: they are private curtilage, not a car park. Shared or communal residential parking courts serving several dwellings are labelled. This extends the source authors' driveway rule rather than contradicting it: a single-house driveway is private access, like the driveways they exclude, whereas a communal court is genuine off-street surface parking under their target. This is the one point at which the protocol narrows the source definition, and the resulting difference is held separate in the error analysis of §4.2 rather than counted as model error.

**中文翻译**

**补充规则——住宅停车。** 单户住宅的私家车道或前院——车辆很少且明显只服务一户——不予标注，因为它们是私人宅地而非停车场。服务多户的共享或公共住宅停车院则予标注。这是对来源作者引道规则的延伸而非冲突：单户私家车道属于私人出入，与其排除的引道相似；公共停车院则符合其对象定义中的真正路外地面停车。这是规程唯一收窄来源定义之处，由此产生的差异在 §4.2 的误差分析中单独保留，而不计作模型错误。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `Rules.md`；`manual/leeds_manual.gpkg`；Qiam et al.（2025）原文；本段核对值：4.2；译文对应位置：`08_appendix_a_annotation_protocol.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

## A.5 边界

**英文原稿**

- Draw along the edge of the paving, not the parcel boundary.
- Keep one car park as one polygon, even where it is split by planting islands.
- Align to the current image. Where OpenStreetMap or another reference is out of date — a demolished building, for instance — follow the current image. OpenStreetMap parking is used only as a starting reference, never as ground truth.

**中文翻译**

- 沿铺装边缘而非地块边界绘制。
- 即使被绿化岛分隔，同一停车场仍画成一个多边形。
- 与当前影像对齐。若 OpenStreetMap 或其他参考已经过时——例如建筑已经拆除——则以当前影像为准。OpenStreetMap 停车数据只用作起始参照，绝不作为地面真值。

> **段落审读**
> - **逻辑用途：** 把目标类别边界转成可执行规则
> - **核对状态：** 🟨 需人工复核：与 Qiam et al.（2025）规程及项目 `Rules.md` 对照一致。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `Rules.md`；`manual/leeds_manual.gpkg`；Qiam et al.（2025）原文；译文对应位置：`08_appendix_a_annotation_protocol.md`（仅作定位，不作为引文证据）
> - **可加强：** 增加一组正反例图像以降低解释差异。

## A.6 属性

**英文原稿**

| Field | Description |
|---|---|
| `confidence` | 3 = clear, 2 = fairly clear, 1 = uncertain |
| `notes` | Optional note for ambiguous cases |

**中文翻译**

| 字段 | 说明 |
|---|---|
| `confidence` | 3 = 清楚，2 = 较清楚，1 = 不确定 |
| `notes` | 对模糊情形的可选说明 |

> **段落审读**
> - **逻辑用途：** 把本段论证的关键量化关系集中展示
> - **核对状态：** ✅ 已核对：表内核心数字已与项目结果 CSV 及正文恒等式复核。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `Rules.md`；`manual/leeds_manual.gpkg`；Qiam et al.（2025）原文；本段核对值：3, 2, 1；译文对应位置：`08_appendix_a_annotation_protocol.md`（仅作定位，不作为引文证据）
> - **可加强：** 终稿可补样本量、单位或不确定区间。

**英文原稿**

The main validation uses the full label set. Results for the confidence 2–3 subset are reported alongside it in Appendix B as a sensitivity analysis, so that the effect of the uncertain labels is visible rather than assumed.

**中文翻译**

主验证使用完整标签集。附录 B 另以 confidence 2–3 子集的结果作为敏感性分析并列报告，使不确定标签的影响可见，而不是被默认无影响。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `Rules.md`；`manual/leeds_manual.gpkg`；Qiam et al.（2025）原文；本段核对值：2, 3；译文对应位置：`08_appendix_a_annotation_protocol.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

## A.7 为什么采用这些规则，以及规则有多可靠

**英文原稿**

The model is validated against these labels, so the labels must match the definition the model was trained on. The rules therefore follow Qiam, Devunuri and Lehe (2025) as closely as possible: the same off-street surface target, pavement-edge boundaries, rooftop parking only where the deck is visible, and no minimum-size cut-off.

**中文翻译**

模型以这些标签为参照接受验证，因此标签必须匹配模型训练时的定义。规则尽量贴近 Qiam、Devunuri 和 Lehe（2025）：相同的路外地面停车对象、铺装边缘边界、仅在停车面可见时纳入屋顶停车，以及不设最小面积门槛。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L24](#l24) Qiam, Devunuri and Lehe (2025)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** `Rules.md`；`manual/leeds_manual.gpkg`；Qiam et al.（2025）原文；译文对应位置：`08_appendix_a_annotation_protocol.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

Annotating surface parking as a binary polygon class is an established approach in comparable aerial-imagery datasets — APKLOT (Hurst-Tarrab et al., 2020) and Grab-Pklot (Yin et al., 2022) are both built this way — so the approach is not ad hoc. APKLOT likewise fixes its target with an explicit include-and-exclude list, though it segments parking blocks rather than whole car parks, so the internal aisles labelled here fall outside its target; Grab-Pklot annotates whole carparks, the closer analogue to the target used here. The data were labelled by a single annotator, and no second labelling pass or inter-annotator agreement coefficient was produced; §5.5 treats this as a limitation, and Table 4.4 reports how far detection differs for the lots the annotator marked uncertain. Any point at which these rules differ from the source protocol is noted above, and error caused by such definitional difference is separated from model error in §4.2.

**中文翻译**

把地面停车标成二分类多边形，在可比的航空影像数据集中是已确立的做法——APKLOT（Hurst-Tarrab et al., 2020）与 Grab-Pklot（Yin et al., 2022）都是这样构建的——因此本方法并非任意设定。APKLOT 同样以显式的纳入与排除清单界定目标，但它分割的是停车区块而非整个停车场，因此本规程所标注的内部通道不在其目标之内；Grab-Pklot 标注的是整个停车场，与本研究采用的目标更为接近。数据由单一标注者绘制，未做第二轮复标，也未给出标注者间一致性系数；§5.5 将此列为局限，表 4.4 则报告标注者标记为不确定的停车场在检出率上的差距。凡本规程不同于来源规程之处，均已在上文标明；定义差异导致的误差也在 §4.2 中与模型错误分开。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：APKLOT 由 Hurst-Tarrab et al.（2020）建立（原文 “we also propose APKLOT”），其 §3.1–3.2 明列纳入与排除规则。原引 Yin et al.（2022）系 APKLOT 归属错误，已更正；两篇现并列引用，并明写 APKLOT 标停车区块、Grab-Pklot 标整个停车场的目标差异。
> - **文献原句：** 见 [L14](#l14) Hurst-Tarrab et al. (2020)、[L33](#l33) Yin et al. (2022)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** `Rules.md`；`manual/leeds_manual.gpkg`；Qiam et al.（2025）原文；本段核对值：4.3, 4.2；译文对应位置：`08_appendix_a_annotation_protocol.md`（仅作定位，不作为引文证据）
> - **可加强：** 书目信息、本地 PDF 与原句均已补齐（Yin et al. 2022 全文经 Poppler 抽出）；A.8 来源仍是独立小列表，可考虑并入主参考文献表，使全文只保留一份书目。

## A.8 来源

**英文原稿**

- Qiam, S., Devunuri, S. and Lehe, L.J. (2025) 'A pipeline and NIR-enhanced dataset for parking lot segmentation', *WACV*.
- Hurst-Tarrab, N., Chang, L., Gonzalez-Mendoza, M. and Hernandez-Gress, N. (2020) 'Robust parking block segmentation from a surveillance camera perspective', *Applied Sciences*, 10(15), 5364.
- Yin, Y., Hu, W., Tran, A., Kruppa, H., Zimmermann, R. and Ng, S.-K. (2022) 'A context-enriched satellite imagery dataset and an approach for parking lot detection', *WACV*, pp. 1371–1380.

**中文翻译**

- Qiam, S., Devunuri, S. and Lehe, L.J. (2025) 'A pipeline and NIR-enhanced dataset for parking lot segmentation', *WACV*.
- Hurst-Tarrab, N., Chang, L., Gonzalez-Mendoza, M. and Hernandez-Gress, N. (2020) 'Robust parking block segmentation from a surveillance camera perspective', *Applied Sciences*, 10(15), 5364.
- Yin, Y., Hu, W., Tran, A., Kruppa, H., Zimmermann, R. and Ng, S.-K. (2022) 'A context-enriched satellite imagery dataset and an approach for parking lot detection', *WACV*, pp. 1371–1380.

> **段落审读**
> - **逻辑用途：** 列明标注规程的直接依据
> - **核对状态：** ✅ 已核对：APKLOT 由 Hurst-Tarrab et al.（2020）建立（原文 “we also propose APKLOT”），其 §3.1–3.2 明列纳入与排除规则。原引 Yin et al.（2022）系 APKLOT 归属错误，已更正；两篇现并列引用，并明写 APKLOT 标停车区块、Grab-Pklot 标整个停车场的目标差异。
> - **文献原句：** 见 [L24](#l24) Qiam, Devunuri and Lehe (2025)、[L14](#l14) Hurst-Tarrab et al. (2020)、[L33](#l33) Yin et al. (2022)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** `Rules.md`；`manual/leeds_manual.gpkg`；Qiam et al.（2025）原文；译文对应位置：`08_appendix_a_annotation_protocol.md`（仅作定位，不作为引文证据）
> - **可加强：** 书目信息、本地 PDF 与原句均已补齐（Yin et al. 2022 全文经 Poppler 抽出）；A.8 来源仍是独立小列表，可考虑并入主参考文献表，使全文只保留一份书目。

# 附录 B——逐单元验证与按距离划分的准确率

**英文原稿**

Supporting tables for §4.1 and §4.5. The study area is a 10 × 10 grid of 1 km² cells; every cell is validated against the manual reference of Appendix A. `all` uses the complete label set, `c23` the confidence 2–3 subset, so that the effect of the confidence filter is visible throughout.

**中文翻译**

本附录提供 §4.1 与 §4.5 的支撑表。研究区是由 1 km² 单元组成的 10 × 10 网格；每个单元均以附录 A 的人工参考进行验证。`all` 使用完整标签集，`c23` 使用 confidence 2–3 子集，使置信度筛选的影响在所有结果中都可见。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；`analysis/accuracy_vs_distance_summary.csv`；本段核对值：4.1, 4.6, 1, 10, 3, 2；译文对应位置：`09_appendix_b_percell_and_distance.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

## B.1 总体验证

**英文原稿**

| Aggregation | Manual km² | Model km² | Model ÷ manual | Precision | Recall | IoU |
|---|---:|---:|---:|---:|---:|---:|
| Area-weighted, all labels | 3.2597 | 4.8785 | 1.497 | 0.5708 | 0.8543 | 0.5202 |
| Area-weighted, confidence 2–3 | 2.9790 | 4.8785 | 1.638 | 0.5287 | 0.8658 | 0.4886 |
| Mean of cells, all labels | — | — | — | 0.5136 | 0.8468 | 0.4697 |
| Mean of cells, confidence 2–3 | — | — | — | 0.4756 | 0.8617 | 0.4408 |

**中文翻译**

| 汇总方式 | 人工标注 km² | 模型 km² | 模型 ÷ 人工 | 精确率 | 召回率 | IoU |
|---|---:|---:|---:|---:|---:|---:|
| 面积加权，全部标签 | 3.2597 | 4.8785 | 1.497 | 0.5708 | 0.8543 | 0.5202 |
| 面积加权，confidence 2–3 | 2.9790 | 4.8785 | 1.638 | 0.5287 | 0.8658 | 0.4886 |
| 单元均值，全部标签 | — | — | — | 0.5136 | 0.8468 | 0.4697 |
| 单元均值，confidence 2–3 | — | — | — | 0.4756 | 0.8617 | 0.4408 |

> **段落审读**
> - **逻辑用途：** 给出正文汇总结果的完整数值底表
> - **核对状态：** ✅ 已核对：已与 `validation_summary.csv` 和两份 `accuracy_vs_distance*.csv` 的字段及行数核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；`analysis/accuracy_vs_distance_summary.csv`；本段核对值：3.2597, 4.8785, 1.497, 0.5708, 0.8543, 0.5202, 2；译文对应位置：`09_appendix_b_percell_and_distance.md`（仅作定位，不作为引文证据）
> - **可加强：** 正式排版时重复表头并注明空白召回率的含义。

## B.2 按距离环带划分的准确率

**英文原稿**

| Band (km) | Cells | Mean dist. km | Manual km² | Model km² | Mean parking share | Mean precision | Mean recall | Mean IoU |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| <1 | 2 | 0.503 | 0.107 | 0.128 | 0.053 | 0.584 | 0.698 | 0.462 |
| 1-2 | 11 | 1.52 | 0.782 | 1.139 | 0.071 | 0.545 | 0.828 | 0.489 |
| 2-3 | 14 | 2.504 | 0.672 | 1.007 | 0.048 | 0.553 | 0.86 | 0.509 |
| 3-4 | 22 | 3.471 | 0.989 | 1.436 | 0.045 | 0.533 | 0.837 | 0.485 |
| >4 | 51 | 5.36 | 0.71 | 1.169 | 0.014 | 0.485 | 0.858 | 0.449 |

**中文翻译**

| 环带（km） | 单元数 | 平均距离 km | 人工标注 km² | 模型 km² | 平均停车占比 | 平均精确率 | 平均召回率 | 平均 IoU |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| <1 | 2 | 0.503 | 0.107 | 0.128 | 0.053 | 0.584 | 0.698 | 0.462 |
| 1-2 | 11 | 1.52 | 0.782 | 1.139 | 0.071 | 0.545 | 0.828 | 0.489 |
| 2-3 | 14 | 2.504 | 0.672 | 1.007 | 0.048 | 0.553 | 0.86 | 0.509 |
| 3-4 | 22 | 3.471 | 0.989 | 1.436 | 0.045 | 0.533 | 0.837 | 0.485 |
| >4 | 51 | 5.36 | 0.71 | 1.169 | 0.014 | 0.485 | 0.858 | 0.449 |

> **段落审读**
> - **逻辑用途：** 给出正文汇总结果的完整数值底表
> - **核对状态：** ✅ 已核对：已与 `validation_summary.csv` 和两份 `accuracy_vs_distance*.csv` 的字段及行数核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；`analysis/accuracy_vs_distance_summary.csv`；本段核对值：1, 2, 0.503, 0.107, 0.128, 0.053, 0.584；译文对应位置：`09_appendix_b_percell_and_distance.md`（仅作定位，不作为引文证据）
> - **可加强：** 正式排版时重复表头并注明空白召回率的含义。

## B.3 与距离和停车占比的相关关系

**英文原稿**

Partial correlations control for the other predictor. `n = 99` for recall because one cell holds no reference parking and yields no recall value.

**中文翻译**

偏相关控制另一个预测变量。召回率的 `n = 99`，因为有一个单元不含参考停车，因而没有可定义的召回率。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；`analysis/accuracy_vs_distance_summary.csv`；本段核对值：99；译文对应位置：`09_appendix_b_percell_and_distance.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

| Test | n | Pearson r | p | Spearman ρ | p |
|---|---:|---:|---:|---:|---:|
| distance vs prec_all | 100 | -0.172 | 0.0873 | -0.186 | 0.0637 |
| parking_share vs prec_all | 100 | 0.536 | 0.0 | 0.653 | 0.0 |
| distance vs prec_all | controlling parking_share | 100 | 0.186 | 0.0646 | — | — |
| parking_share vs prec_all | controlling distance | 100 | 0.54 | 0.0 | — | — |
| distance vs rec_all | 99 | 0.181 | 0.073 | 0.161 | 0.1124 |
| parking_share vs rec_all | 99 | 0.103 | 0.3125 | 0.084 | 0.4097 |
| distance vs rec_all | controlling parking_share | 99 | 0.289 | 0.0037 | — | — |
| parking_share vs rec_all | controlling distance | 99 | 0.25 | 0.0127 | — | — |
| distance vs iou_all | 100 | -0.127 | 0.2081 | -0.16 | 0.1114 |
| parking_share vs iou_all | 100 | 0.515 | 0.0 | 0.639 | 0.0 |
| distance vs iou_all | controlling parking_share | 100 | 0.229 | 0.0222 | — | — |
| parking_share vs iou_all | controlling distance | 100 | 0.54 | 0.0 | — | — |
| distance vs parking_share | 100 | -0.562 | 0.0 | -0.66 | 0.0 |

**中文翻译**

| 检验 | n | Pearson r | p | Spearman ρ | p |
|---|---:|---:|---:|---:|---:|
| distance vs prec_all | 100 | -0.172 | 0.0873 | -0.186 | 0.0637 |
| parking_share vs prec_all | 100 | 0.536 | 0.0 | 0.653 | 0.0 |
| distance vs prec_all | 控制 parking_share | 100 | 0.186 | 0.0646 | — | — |
| parking_share vs prec_all | 控制 distance | 100 | 0.54 | 0.0 | — | — |
| distance vs rec_all | 99 | 0.181 | 0.073 | 0.161 | 0.1124 |
| parking_share vs rec_all | 99 | 0.103 | 0.3125 | 0.084 | 0.4097 |
| distance vs rec_all | 控制 parking_share | 99 | 0.289 | 0.0037 | — | — |
| parking_share vs rec_all | 控制 distance | 99 | 0.25 | 0.0127 | — | — |
| distance vs iou_all | 100 | -0.127 | 0.2081 | -0.16 | 0.1114 |
| parking_share vs iou_all | 100 | 0.515 | 0.0 | 0.639 | 0.0 |
| distance vs iou_all | 控制 parking_share | 100 | 0.229 | 0.0222 | — | — |
| parking_share vs iou_all | 控制 distance | 100 | 0.54 | 0.0 | — | — |
| distance vs parking_share | 100 | -0.562 | 0.0 | -0.66 | 0.0 |

> **段落审读**
> - **逻辑用途：** 给出正文汇总结果的完整数值底表
> - **核对状态：** ✅ 已核对：已与 `validation_summary.csv` 和两份 `accuracy_vs_distance*.csv` 的字段及行数核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；`analysis/accuracy_vs_distance_summary.csv`；本段核对值：100, 0.172, 0.0873, 0.186, 0.0637, 0.536, 0.0；译文对应位置：`09_appendix_b_percell_and_distance.md`（仅作定位，不作为引文证据）
> - **可加强：** 正式排版时重复表头并注明空白召回率的含义。

## B.4 逐单元结果

**英文原稿**

All 100 cells, ordered by grid column then row. Cell identifiers follow the `c<col>r<row>` convention used in the project repository.

**中文翻译**

以下列出全部 100 个单元，按网格列、再按行排序。单元标识符遵循项目仓库中的 `c<col>r<row>` 约定。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；`analysis/accuracy_vs_distance_summary.csv`；本段核对值：100；译文对应位置：`09_appendix_b_percell_and_distance.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

| Cell | Dist. km | Parking share | Model m² | Manual m² (all) | P | R | IoU | Manual m² (c23) | P | R | IoU |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| c0r0 | 7.44 | 0.0120 | 15166.2 | 11958.1 | 0.6213 | 0.788 | 0.5323 | 11438.8 | 0.6 | 0.7956 | 0.5199 |
| c0r1 | 6.65 | 0.0198 | 34517.6 | 19834.2 | 0.5264 | 0.9161 | 0.5022 | 14774.3 | 0.3933 | 0.9188 | 0.3801 |
| c0r2 | 5.93 | 0.0108 | 22064.7 | 10779.8 | 0.3869 | 0.7919 | 0.3512 | 10475.2 | 0.3731 | 0.7859 | 0.3387 |
| c0r3 | 5.30 | 0.0070 | 11121.2 | 7037.9 | 0.5534 | 0.8745 | 0.5127 | 6170.0 | 0.4827 | 0.8701 | 0.4502 |
| c0r4 | 4.79 | 0.0100 | 15406.5 | 9984.8 | 0.5688 | 0.8777 | 0.527 | 9589.1 | 0.5546 | 0.891 | 0.5193 |
| c0r5 | 4.46 | 0.0107 | 19572.6 | 10670.7 | 0.3885 | 0.7126 | 0.3359 | 10670.7 | 0.3885 | 0.7126 | 0.3359 |
| c0r6 | 4.33 | 0.0095 | 18793.0 | 9459.0 | 0.394 | 0.7827 | 0.3551 | 9459.0 | 0.394 | 0.7827 | 0.3551 |
| c0r7 | 4.43 | 0.0153 | 24464.7 | 15285.8 | 0.528 | 0.8451 | 0.4815 | 15285.8 | 0.528 | 0.8451 | 0.4815 |
| c0r8 | 4.75 | 0.0361 | 53584.5 | 36125.2 | 0.5597 | 0.8302 | 0.5022 | 33897.9 | 0.5209 | 0.8234 | 0.4686 |
| c0r9 | 5.24 | 0.0000 | 140.3 | 0.0 | 0.0 |  | 0.0 | 0.0 | 0.0 |  | 0.0 |
| c1r0 | 6.91 | 0.0071 | 16400.9 | 7052.4 | 0.3736 | 0.8689 | 0.3537 | 7052.4 | 0.3736 | 0.8689 | 0.3537 |
| c1r1 | 6.05 | 0.0335 | 39166.7 | 33469.1 | 0.7609 | 0.8904 | 0.6957 | 33105.2 | 0.7528 | 0.8907 | 0.6892 |
| c1r2 | 5.24 | 0.0067 | 13932.1 | 6665.4 | 0.383 | 0.8005 | 0.3496 | 6665.4 | 0.383 | 0.8005 | 0.3496 |
| c1r3 | 4.52 | 0.0120 | 19818.0 | 11971.5 | 0.5018 | 0.8307 | 0.4552 | 11971.5 | 0.5018 | 0.8307 | 0.4552 |
| c1r4 | 3.91 | 0.0478 | 61374.4 | 47794.3 | 0.6919 | 0.8885 | 0.6366 | 47667.6 | 0.6916 | 0.8904 | 0.6373 |
| c1r5 | 3.49 | 0.0145 | 21524.3 | 14536.1 | 0.546 | 0.8085 | 0.4835 | 13687.5 | 0.5079 | 0.7986 | 0.4502 |
| c1r6 | 3.33 | 0.0409 | 53347.6 | 40889.4 | 0.6298 | 0.8217 | 0.5541 | 34852.4 | 0.5428 | 0.8309 | 0.4888 |
| c1r7 | 3.46 | 0.0093 | 23073.3 | 9296.1 | 0.334 | 0.8289 | 0.3124 | 8714.3 | 0.3109 | 0.8231 | 0.2914 |
| c1r8 | 3.86 | 0.0539 | 70603.4 | 53947.6 | 0.6745 | 0.8827 | 0.619 | 49100.9 | 0.6361 | 0.9146 | 0.6004 |
| c1r9 | 4.45 | 0.0119 | 32059.6 | 11906.2 | 0.3188 | 0.8583 | 0.3028 | 9304.0 | 0.2773 | 0.9555 | 0.2738 |
| c2r0 | 6.48 | 0.0038 | 7350.5 | 3841.8 | 0.4445 | 0.8505 | 0.4123 | 2803.6 | 0.3573 | 0.9367 | 0.3489 |
| c2r1 | 5.56 | 0.0114 | 12243.9 | 11395.4 | 0.6691 | 0.7189 | 0.5304 | 11229.4 | 0.6613 | 0.721 | 0.5266 |
| c2r2 | 4.67 | 0.0131 | 22189.7 | 13104.5 | 0.5067 | 0.8579 | 0.4675 | 10796.4 | 0.4089 | 0.8404 | 0.3794 |
| c2r3 | 3.84 | 0.0150 | 19851.0 | 15031.1 | 0.584 | 0.7713 | 0.4978 | 12666.1 | 0.4883 | 0.7653 | 0.4247 |
| c2r4 | 3.11 | 0.0163 | 28269.3 | 16284.5 | 0.4806 | 0.8342 | 0.4387 | 14123.0 | 0.4397 | 0.8802 | 0.4149 |
| c2r5 | 2.56 | 0.0793 | 110231.0 | 79329.8 | 0.6645 | 0.9233 | 0.6297 | 71617.8 | 0.6047 | 0.9308 | 0.5787 |
| c2r6 | 2.33 | 0.0434 | 59548.0 | 43401.3 | 0.6351 | 0.8714 | 0.5807 | 38202.4 | 0.5722 | 0.8919 | 0.535 |
| c2r7 | 2.52 | 0.0250 | 51368.4 | 24978.6 | 0.3933 | 0.8088 | 0.3599 | 20950.9 | 0.3296 | 0.8082 | 0.3057 |
| c2r8 | 3.04 | 0.1881 | 221784.2 | 188065.4 | 0.7369 | 0.869 | 0.6633 | 181524.9 | 0.7184 | 0.8778 | 0.6531 |
| c2r9 | 3.76 | 0.0513 | 78303.1 | 51349.6 | 0.5808 | 0.8857 | 0.5403 | 41951.5 | 0.4872 | 0.9094 | 0.4647 |
| c3r0 | 6.20 | 0.0036 | 5654.1 | 3561.5 | 0.5241 | 0.8321 | 0.474 | 3561.5 | 0.5241 | 0.8321 | 0.474 |
| c3r1 | 5.22 | 0.0028 | 8997.8 | 2761.4 | 0.2832 | 0.9229 | 0.2767 | 2270.4 | 0.2444 | 0.9687 | 0.2425 |
| c3r2 | 4.26 | 0.0100 | 19307.0 | 10044.1 | 0.4725 | 0.9083 | 0.451 | 7148.7 | 0.3574 | 0.9652 | 0.3529 |
| c3r3 | 3.33 | 0.0069 | 18655.1 | 6909.9 | 0.2695 | 0.7277 | 0.2449 | 5584.4 | 0.2517 | 0.841 | 0.2403 |
| c3r4 | 2.45 | 0.0088 | 26811.0 | 8825.9 | 0.2744 | 0.8336 | 0.2601 | 5764.0 | 0.1926 | 0.896 | 0.1884 |
| c3r5 | 1.70 | 0.0410 | 60825.0 | 40990.3 | 0.5179 | 0.7685 | 0.448 | 37121.4 | 0.4885 | 0.8004 | 0.4354 |
| c3r6 | 1.33 | 0.0826 | 115977.8 | 82639.9 | 0.6104 | 0.8566 | 0.5538 | 74318.9 | 0.5814 | 0.9072 | 0.5487 |
| c3r7 | 1.64 | 0.1099 | 144298.8 | 109854.9 | 0.6497 | 0.8534 | 0.5844 | 96713.1 | 0.592 | 0.8833 | 0.549 |
| c3r8 | 2.36 | 0.0919 | 116265.6 | 91920.3 | 0.6954 | 0.8795 | 0.6349 | 86667.6 | 0.6601 | 0.8855 | 0.6082 |
| c3r9 | 3.24 | 0.0643 | 86001.4 | 64309.6 | 0.6535 | 0.874 | 0.5972 | 61277.8 | 0.6272 | 0.8803 | 0.5779 |
| c4r0 | 6.06 | 0.0128 | 28404.9 | 12762.7 | 0.431 | 0.9593 | 0.4233 | 12586.9 | 0.4263 | 0.962 | 0.4192 |
| c4r1 | 5.06 | 0.0326 | 41434.6 | 32632.8 | 0.737 | 0.9358 | 0.7015 | 32632.8 | 0.737 | 0.9358 | 0.7015 |
| c4r2 | 4.06 | 0.0086 | 20280.0 | 8609.0 | 0.3896 | 0.9177 | 0.3764 | 8224.2 | 0.3818 | 0.9415 | 0.373 |
| c4r3 | 3.07 | 0.0065 | 15801.8 | 6485.1 | 0.2926 | 0.713 | 0.2618 | 4163.0 | 0.1994 | 0.757 | 0.1874 |
| c4r4 | 2.08 | 0.0221 | 42681.3 | 22054.8 | 0.4017 | 0.7775 | 0.3603 | 15420.9 | 0.3044 | 0.8424 | 0.288 |
| c4r5 | 1.10 | 0.0265 | 45147.1 | 26483.0 | 0.4048 | 0.6902 | 0.3426 | 13962.9 | 0.1706 | 0.5516 | 0.1498 |
| c4r6 | 0.34 | 0.0523 | 73194.4 | 52323.1 | 0.5455 | 0.7631 | 0.4665 | 49832.5 | 0.5233 | 0.7686 | 0.452 |
| c4r7 | 1.01 | 0.0744 | 108407.4 | 74408.3 | 0.5631 | 0.8204 | 0.5013 | 69254.6 | 0.5235 | 0.8194 | 0.4693 |
| c4r8 | 1.98 | 0.0190 | 39586.4 | 19005.5 | 0.3983 | 0.8295 | 0.3681 | 13944.5 | 0.3059 | 0.8685 | 0.2924 |
| c4r9 | 2.97 | 0.0445 | 60551.9 | 44519.3 | 0.6357 | 0.8646 | 0.5781 | 40318.2 | 0.5859 | 0.8799 | 0.5425 |
| c5r0 | 6.09 | 0.0122 | 20515.7 | 12247.5 | 0.5183 | 0.8682 | 0.4805 | 11091.4 | 0.4823 | 0.8922 | 0.4558 |
| c5r1 | 5.09 | 0.0245 | 39582.4 | 24461.1 | 0.5634 | 0.9116 | 0.5342 | 23535.9 | 0.5451 | 0.9167 | 0.5193 |
| c5r2 | 4.11 | 0.0065 | 18888.5 | 6508.2 | 0.3102 | 0.9004 | 0.2999 | 5635.7 | 0.2778 | 0.931 | 0.2722 |
| c5r3 | 3.12 | 0.0187 | 38088.8 | 18675.5 | 0.4568 | 0.9316 | 0.442 | 17172.1 | 0.42 | 0.9316 | 0.4074 |
| c5r4 | 2.16 | 0.0394 | 55963.4 | 39397.6 | 0.6093 | 0.8655 | 0.5566 | 32451.8 | 0.5248 | 0.905 | 0.4974 |
| c5r5 | 1.25 | 0.0791 | 103149.1 | 79116.8 | 0.6085 | 0.7933 | 0.5252 | 77614.6 | 0.5982 | 0.795 | 0.5182 |
| c5r6 | 0.67 | 0.0544 | 55216.3 | 54359.5 | 0.6228 | 0.6326 | 0.4574 | 49707.3 | 0.5591 | 0.621 | 0.4168 |
| c5r7 | 1.16 | 0.1279 | 170632.8 | 127896.2 | 0.6489 | 0.8657 | 0.5896 | 122407.7 | 0.6195 | 0.8636 | 0.5643 |
| c5r8 | 2.06 | 0.0849 | 106885.7 | 84901.7 | 0.6696 | 0.843 | 0.5954 | 76658.7 | 0.6051 | 0.8437 | 0.5442 |
| c5r9 | 3.02 | 0.0631 | 96645.8 | 63078.9 | 0.5592 | 0.8568 | 0.5114 | 51522.8 | 0.4701 | 0.8817 | 0.4422 |
| c6r0 | 6.28 | 0.0106 | 15457.0 | 10638.6 | 0.5407 | 0.7856 | 0.4712 | 9415.1 | 0.4786 | 0.7858 | 0.4234 |
| c6r1 | 5.32 | 0.0107 | 24046.0 | 10676.7 | 0.418 | 0.9413 | 0.4073 | 9071.5 | 0.3667 | 0.9719 | 0.3628 |
| c6r2 | 4.38 | 0.0066 | 14804.4 | 6562.2 | 0.4222 | 0.9524 | 0.4134 | 6250.5 | 0.4016 | 0.9512 | 0.3935 |
| c6r3 | 3.48 | 0.0101 | 21438.4 | 10083.4 | 0.4152 | 0.8828 | 0.3935 | 9880.8 | 0.4073 | 0.8836 | 0.3865 |
| c6r4 | 2.64 | 0.0128 | 20717.7 | 12773.6 | 0.4962 | 0.8048 | 0.4429 | 12422.4 | 0.4896 | 0.8166 | 0.4411 |
| c6r5 | 1.97 | 0.1121 | 154368.5 | 112091.2 | 0.6247 | 0.8604 | 0.5672 | 110704.6 | 0.6174 | 0.861 | 0.5615 |
| c6r6 | 1.67 | 0.0392 | 81924.5 | 39192.8 | 0.4432 | 0.9264 | 0.4281 | 36860.7 | 0.4195 | 0.9324 | 0.4072 |
| c6r7 | 1.92 | 0.0701 | 114291.5 | 70136.6 | 0.5202 | 0.8476 | 0.4757 | 63122.6 | 0.4677 | 0.8469 | 0.4312 |
| c6r8 | 2.57 | 0.0876 | 144495.0 | 87560.7 | 0.5471 | 0.9028 | 0.5167 | 82108.3 | 0.5193 | 0.914 | 0.4951 |
| c6r9 | 3.39 | 0.0571 | 68407.9 | 57093.7 | 0.7282 | 0.8725 | 0.6582 | 46867.4 | 0.6224 | 0.9085 | 0.5857 |
| c7r0 | 6.61 | 0.0026 | 6096.2 | 2645.5 | 0.3109 | 0.7165 | 0.2768 | 1963.5 | 0.2814 | 0.8737 | 0.2704 |
| c7r1 | 5.71 | 0.0112 | 22925.0 | 11232.7 | 0.4032 | 0.8228 | 0.371 | 9185.3 | 0.3428 | 0.8556 | 0.3241 |
| c7r2 | 4.85 | 0.0112 | 21847.6 | 11221.7 | 0.4561 | 0.888 | 0.4313 | 8724.3 | 0.3444 | 0.8624 | 0.3265 |
| c7r3 | 4.05 | 0.0192 | 28391.2 | 19161.7 | 0.6356 | 0.9417 | 0.6115 | 17903.5 | 0.6039 | 0.9576 | 0.5882 |
| c7r4 | 3.37 | 0.0179 | 25632.2 | 17915.9 | 0.5632 | 0.8057 | 0.4958 | 15607.6 | 0.5282 | 0.8675 | 0.4888 |
| c7r5 | 2.87 | 0.0235 | 38779.4 | 23489.3 | 0.5371 | 0.8868 | 0.5027 | 22814.2 | 0.5267 | 0.8953 | 0.4962 |
| c7r6 | 2.67 | 0.0381 | 51079.0 | 38122.6 | 0.6698 | 0.8975 | 0.6222 | 33867.7 | 0.6162 | 0.9294 | 0.5887 |
| c7r7 | 2.83 | 0.0712 | 121748.1 | 71206.9 | 0.5135 | 0.8779 | 0.4792 | 66643.2 | 0.4805 | 0.8779 | 0.4504 |
| c7r8 | 3.30 | 0.0740 | 116222.5 | 73997.6 | 0.5255 | 0.8254 | 0.473 | 66556.4 | 0.4704 | 0.8214 | 0.4268 |
| c7r9 | 3.98 | 0.1069 | 193762.0 | 106906.7 | 0.4348 | 0.788 | 0.3892 | 99270.4 | 0.3987 | 0.7782 | 0.358 |
| c8r0 | 7.08 | 0.0010 | 3554.0 | 1023.6 | 0.2813 | 0.9768 | 0.2795 | 1023.6 | 0.2813 | 0.9768 | 0.2795 |
| c8r1 | 6.24 | 0.0012 | 1770.1 | 1237.9 | 0.6566 | 0.9389 | 0.6298 | 1237.9 | 0.6566 | 0.9389 | 0.6298 |
| c8r2 | 5.47 | 0.0065 | 12892.8 | 6488.1 | 0.4627 | 0.9195 | 0.4447 | 6185.9 | 0.4511 | 0.9402 | 0.4385 |
| c8r3 | 4.77 | 0.0110 | 21676.4 | 11033.1 | 0.4418 | 0.868 | 0.414 | 10725.7 | 0.4296 | 0.8682 | 0.4033 |
| c8r4 | 4.20 | 0.0134 | 22488.5 | 13368.7 | 0.4239 | 0.7131 | 0.3622 | 12605.3 | 0.3989 | 0.7117 | 0.3434 |
| c8r5 | 3.82 | 0.0095 | 18184.0 | 9507.3 | 0.3778 | 0.7226 | 0.33 | 8871.7 | 0.3626 | 0.7433 | 0.3223 |
| c8r6 | 3.67 | 0.0109 | 20163.5 | 10875.2 | 0.4902 | 0.9088 | 0.4672 | 10597.4 | 0.4798 | 0.913 | 0.4589 |
| c8r7 | 3.79 | 0.1060 | 138499.2 | 106006.9 | 0.696 | 0.9093 | 0.6508 | 92818.3 | 0.6171 | 0.9209 | 0.5861 |
| c8r8 | 4.15 | 0.0209 | 52887.4 | 20879.2 | 0.3179 | 0.8053 | 0.2952 | 20879.2 | 0.3179 | 0.8053 | 0.2952 |
| c8r9 | 4.71 | 0.0330 | 62589.3 | 32982.0 | 0.4151 | 0.7878 | 0.3734 | 22767.7 | 0.321 | 0.8824 | 0.3078 |
| c9r0 | 7.64 | 0.0008 | 2038.2 | 785.8 | 0.318 | 0.8248 | 0.2979 | 785.8 | 0.318 | 0.8248 | 0.2979 |
| c9r1 | 6.88 | 0.0073 | 9408.4 | 7265.2 | 0.6266 | 0.8115 | 0.547 | 7265.2 | 0.6266 | 0.8115 | 0.547 |
| c9r2 | 6.18 | 0.0021 | 4157.5 | 2101.8 | 0.4236 | 0.838 | 0.3915 | 2101.8 | 0.4236 | 0.838 | 0.3915 |
| c9r3 | 5.58 | 0.0108 | 14511.1 | 10764.1 | 0.6082 | 0.8199 | 0.5365 | 10588.4 | 0.5995 | 0.8216 | 0.5305 |
| c9r4 | 5.10 | 0.0093 | 14750.9 | 9343.8 | 0.4049 | 0.6393 | 0.3296 | 8420.7 | 0.4024 | 0.7048 | 0.3443 |
| c9r5 | 4.79 | 0.0327 | 51183.4 | 32712.9 | 0.5832 | 0.9125 | 0.5523 | 31635.8 | 0.5729 | 0.9269 | 0.5482 |
| c9r6 | 4.67 | 0.0135 | 24329.6 | 13546.5 | 0.4733 | 0.8501 | 0.4368 | 13101.2 | 0.4626 | 0.8591 | 0.43 |
| c9r7 | 4.76 | 0.0385 | 53547.4 | 38495.2 | 0.6762 | 0.9407 | 0.6486 | 38495.2 | 0.6762 | 0.9407 | 0.6486 |
| c9r8 | 5.06 | 0.0718 | 80152.4 | 71847.7 | 0.863 | 0.9628 | 0.8352 | 71847.7 | 0.863 | 0.9628 | 0.8352 |
| c9r9 | 5.52 | 0.0195 | 22122.4 | 19495.4 | 0.8564 | 0.9717 | 0.8356 | 19495.4 | 0.8564 | 0.9717 | 0.8356 |

**中文翻译**

| 单元 | 距离 km | 停车占比 | 模型 m² | 人工 m²（all） | P | R | IoU | 人工 m²（c23） | P | R | IoU |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| c0r0 | 7.44 | 0.0120 | 15166.2 | 11958.1 | 0.6213 | 0.788 | 0.5323 | 11438.8 | 0.6 | 0.7956 | 0.5199 |
| c0r1 | 6.65 | 0.0198 | 34517.6 | 19834.2 | 0.5264 | 0.9161 | 0.5022 | 14774.3 | 0.3933 | 0.9188 | 0.3801 |
| c0r2 | 5.93 | 0.0108 | 22064.7 | 10779.8 | 0.3869 | 0.7919 | 0.3512 | 10475.2 | 0.3731 | 0.7859 | 0.3387 |
| c0r3 | 5.30 | 0.0070 | 11121.2 | 7037.9 | 0.5534 | 0.8745 | 0.5127 | 6170.0 | 0.4827 | 0.8701 | 0.4502 |
| c0r4 | 4.79 | 0.0100 | 15406.5 | 9984.8 | 0.5688 | 0.8777 | 0.527 | 9589.1 | 0.5546 | 0.891 | 0.5193 |
| c0r5 | 4.46 | 0.0107 | 19572.6 | 10670.7 | 0.3885 | 0.7126 | 0.3359 | 10670.7 | 0.3885 | 0.7126 | 0.3359 |
| c0r6 | 4.33 | 0.0095 | 18793.0 | 9459.0 | 0.394 | 0.7827 | 0.3551 | 9459.0 | 0.394 | 0.7827 | 0.3551 |
| c0r7 | 4.43 | 0.0153 | 24464.7 | 15285.8 | 0.528 | 0.8451 | 0.4815 | 15285.8 | 0.528 | 0.8451 | 0.4815 |
| c0r8 | 4.75 | 0.0361 | 53584.5 | 36125.2 | 0.5597 | 0.8302 | 0.5022 | 33897.9 | 0.5209 | 0.8234 | 0.4686 |
| c0r9 | 5.24 | 0.0000 | 140.3 | 0.0 | 0.0 |  | 0.0 | 0.0 | 0.0 |  | 0.0 |
| c1r0 | 6.91 | 0.0071 | 16400.9 | 7052.4 | 0.3736 | 0.8689 | 0.3537 | 7052.4 | 0.3736 | 0.8689 | 0.3537 |
| c1r1 | 6.05 | 0.0335 | 39166.7 | 33469.1 | 0.7609 | 0.8904 | 0.6957 | 33105.2 | 0.7528 | 0.8907 | 0.6892 |
| c1r2 | 5.24 | 0.0067 | 13932.1 | 6665.4 | 0.383 | 0.8005 | 0.3496 | 6665.4 | 0.383 | 0.8005 | 0.3496 |
| c1r3 | 4.52 | 0.0120 | 19818.0 | 11971.5 | 0.5018 | 0.8307 | 0.4552 | 11971.5 | 0.5018 | 0.8307 | 0.4552 |
| c1r4 | 3.91 | 0.0478 | 61374.4 | 47794.3 | 0.6919 | 0.8885 | 0.6366 | 47667.6 | 0.6916 | 0.8904 | 0.6373 |
| c1r5 | 3.49 | 0.0145 | 21524.3 | 14536.1 | 0.546 | 0.8085 | 0.4835 | 13687.5 | 0.5079 | 0.7986 | 0.4502 |
| c1r6 | 3.33 | 0.0409 | 53347.6 | 40889.4 | 0.6298 | 0.8217 | 0.5541 | 34852.4 | 0.5428 | 0.8309 | 0.4888 |
| c1r7 | 3.46 | 0.0093 | 23073.3 | 9296.1 | 0.334 | 0.8289 | 0.3124 | 8714.3 | 0.3109 | 0.8231 | 0.2914 |
| c1r8 | 3.86 | 0.0539 | 70603.4 | 53947.6 | 0.6745 | 0.8827 | 0.619 | 49100.9 | 0.6361 | 0.9146 | 0.6004 |
| c1r9 | 4.45 | 0.0119 | 32059.6 | 11906.2 | 0.3188 | 0.8583 | 0.3028 | 9304.0 | 0.2773 | 0.9555 | 0.2738 |
| c2r0 | 6.48 | 0.0038 | 7350.5 | 3841.8 | 0.4445 | 0.8505 | 0.4123 | 2803.6 | 0.3573 | 0.9367 | 0.3489 |
| c2r1 | 5.56 | 0.0114 | 12243.9 | 11395.4 | 0.6691 | 0.7189 | 0.5304 | 11229.4 | 0.6613 | 0.721 | 0.5266 |
| c2r2 | 4.67 | 0.0131 | 22189.7 | 13104.5 | 0.5067 | 0.8579 | 0.4675 | 10796.4 | 0.4089 | 0.8404 | 0.3794 |
| c2r3 | 3.84 | 0.0150 | 19851.0 | 15031.1 | 0.584 | 0.7713 | 0.4978 | 12666.1 | 0.4883 | 0.7653 | 0.4247 |
| c2r4 | 3.11 | 0.0163 | 28269.3 | 16284.5 | 0.4806 | 0.8342 | 0.4387 | 14123.0 | 0.4397 | 0.8802 | 0.4149 |
| c2r5 | 2.56 | 0.0793 | 110231.0 | 79329.8 | 0.6645 | 0.9233 | 0.6297 | 71617.8 | 0.6047 | 0.9308 | 0.5787 |
| c2r6 | 2.33 | 0.0434 | 59548.0 | 43401.3 | 0.6351 | 0.8714 | 0.5807 | 38202.4 | 0.5722 | 0.8919 | 0.535 |
| c2r7 | 2.52 | 0.0250 | 51368.4 | 24978.6 | 0.3933 | 0.8088 | 0.3599 | 20950.9 | 0.3296 | 0.8082 | 0.3057 |
| c2r8 | 3.04 | 0.1881 | 221784.2 | 188065.4 | 0.7369 | 0.869 | 0.6633 | 181524.9 | 0.7184 | 0.8778 | 0.6531 |
| c2r9 | 3.76 | 0.0513 | 78303.1 | 51349.6 | 0.5808 | 0.8857 | 0.5403 | 41951.5 | 0.4872 | 0.9094 | 0.4647 |
| c3r0 | 6.20 | 0.0036 | 5654.1 | 3561.5 | 0.5241 | 0.8321 | 0.474 | 3561.5 | 0.5241 | 0.8321 | 0.474 |
| c3r1 | 5.22 | 0.0028 | 8997.8 | 2761.4 | 0.2832 | 0.9229 | 0.2767 | 2270.4 | 0.2444 | 0.9687 | 0.2425 |
| c3r2 | 4.26 | 0.0100 | 19307.0 | 10044.1 | 0.4725 | 0.9083 | 0.451 | 7148.7 | 0.3574 | 0.9652 | 0.3529 |
| c3r3 | 3.33 | 0.0069 | 18655.1 | 6909.9 | 0.2695 | 0.7277 | 0.2449 | 5584.4 | 0.2517 | 0.841 | 0.2403 |
| c3r4 | 2.45 | 0.0088 | 26811.0 | 8825.9 | 0.2744 | 0.8336 | 0.2601 | 5764.0 | 0.1926 | 0.896 | 0.1884 |
| c3r5 | 1.70 | 0.0410 | 60825.0 | 40990.3 | 0.5179 | 0.7685 | 0.448 | 37121.4 | 0.4885 | 0.8004 | 0.4354 |
| c3r6 | 1.33 | 0.0826 | 115977.8 | 82639.9 | 0.6104 | 0.8566 | 0.5538 | 74318.9 | 0.5814 | 0.9072 | 0.5487 |
| c3r7 | 1.64 | 0.1099 | 144298.8 | 109854.9 | 0.6497 | 0.8534 | 0.5844 | 96713.1 | 0.592 | 0.8833 | 0.549 |
| c3r8 | 2.36 | 0.0919 | 116265.6 | 91920.3 | 0.6954 | 0.8795 | 0.6349 | 86667.6 | 0.6601 | 0.8855 | 0.6082 |
| c3r9 | 3.24 | 0.0643 | 86001.4 | 64309.6 | 0.6535 | 0.874 | 0.5972 | 61277.8 | 0.6272 | 0.8803 | 0.5779 |
| c4r0 | 6.06 | 0.0128 | 28404.9 | 12762.7 | 0.431 | 0.9593 | 0.4233 | 12586.9 | 0.4263 | 0.962 | 0.4192 |
| c4r1 | 5.06 | 0.0326 | 41434.6 | 32632.8 | 0.737 | 0.9358 | 0.7015 | 32632.8 | 0.737 | 0.9358 | 0.7015 |
| c4r2 | 4.06 | 0.0086 | 20280.0 | 8609.0 | 0.3896 | 0.9177 | 0.3764 | 8224.2 | 0.3818 | 0.9415 | 0.373 |
| c4r3 | 3.07 | 0.0065 | 15801.8 | 6485.1 | 0.2926 | 0.713 | 0.2618 | 4163.0 | 0.1994 | 0.757 | 0.1874 |
| c4r4 | 2.08 | 0.0221 | 42681.3 | 22054.8 | 0.4017 | 0.7775 | 0.3603 | 15420.9 | 0.3044 | 0.8424 | 0.288 |
| c4r5 | 1.10 | 0.0265 | 45147.1 | 26483.0 | 0.4048 | 0.6902 | 0.3426 | 13962.9 | 0.1706 | 0.5516 | 0.1498 |
| c4r6 | 0.34 | 0.0523 | 73194.4 | 52323.1 | 0.5455 | 0.7631 | 0.4665 | 49832.5 | 0.5233 | 0.7686 | 0.452 |
| c4r7 | 1.01 | 0.0744 | 108407.4 | 74408.3 | 0.5631 | 0.8204 | 0.5013 | 69254.6 | 0.5235 | 0.8194 | 0.4693 |
| c4r8 | 1.98 | 0.0190 | 39586.4 | 19005.5 | 0.3983 | 0.8295 | 0.3681 | 13944.5 | 0.3059 | 0.8685 | 0.2924 |
| c4r9 | 2.97 | 0.0445 | 60551.9 | 44519.3 | 0.6357 | 0.8646 | 0.5781 | 40318.2 | 0.5859 | 0.8799 | 0.5425 |
| c5r0 | 6.09 | 0.0122 | 20515.7 | 12247.5 | 0.5183 | 0.8682 | 0.4805 | 11091.4 | 0.4823 | 0.8922 | 0.4558 |
| c5r1 | 5.09 | 0.0245 | 39582.4 | 24461.1 | 0.5634 | 0.9116 | 0.5342 | 23535.9 | 0.5451 | 0.9167 | 0.5193 |
| c5r2 | 4.11 | 0.0065 | 18888.5 | 6508.2 | 0.3102 | 0.9004 | 0.2999 | 5635.7 | 0.2778 | 0.931 | 0.2722 |
| c5r3 | 3.12 | 0.0187 | 38088.8 | 18675.5 | 0.4568 | 0.9316 | 0.442 | 17172.1 | 0.42 | 0.9316 | 0.4074 |
| c5r4 | 2.16 | 0.0394 | 55963.4 | 39397.6 | 0.6093 | 0.8655 | 0.5566 | 32451.8 | 0.5248 | 0.905 | 0.4974 |
| c5r5 | 1.25 | 0.0791 | 103149.1 | 79116.8 | 0.6085 | 0.7933 | 0.5252 | 77614.6 | 0.5982 | 0.795 | 0.5182 |
| c5r6 | 0.67 | 0.0544 | 55216.3 | 54359.5 | 0.6228 | 0.6326 | 0.4574 | 49707.3 | 0.5591 | 0.621 | 0.4168 |
| c5r7 | 1.16 | 0.1279 | 170632.8 | 127896.2 | 0.6489 | 0.8657 | 0.5896 | 122407.7 | 0.6195 | 0.8636 | 0.5643 |
| c5r8 | 2.06 | 0.0849 | 106885.7 | 84901.7 | 0.6696 | 0.843 | 0.5954 | 76658.7 | 0.6051 | 0.8437 | 0.5442 |
| c5r9 | 3.02 | 0.0631 | 96645.8 | 63078.9 | 0.5592 | 0.8568 | 0.5114 | 51522.8 | 0.4701 | 0.8817 | 0.4422 |
| c6r0 | 6.28 | 0.0106 | 15457.0 | 10638.6 | 0.5407 | 0.7856 | 0.4712 | 9415.1 | 0.4786 | 0.7858 | 0.4234 |
| c6r1 | 5.32 | 0.0107 | 24046.0 | 10676.7 | 0.418 | 0.9413 | 0.4073 | 9071.5 | 0.3667 | 0.9719 | 0.3628 |
| c6r2 | 4.38 | 0.0066 | 14804.4 | 6562.2 | 0.4222 | 0.9524 | 0.4134 | 6250.5 | 0.4016 | 0.9512 | 0.3935 |
| c6r3 | 3.48 | 0.0101 | 21438.4 | 10083.4 | 0.4152 | 0.8828 | 0.3935 | 9880.8 | 0.4073 | 0.8836 | 0.3865 |
| c6r4 | 2.64 | 0.0128 | 20717.7 | 12773.6 | 0.4962 | 0.8048 | 0.4429 | 12422.4 | 0.4896 | 0.8166 | 0.4411 |
| c6r5 | 1.97 | 0.1121 | 154368.5 | 112091.2 | 0.6247 | 0.8604 | 0.5672 | 110704.6 | 0.6174 | 0.861 | 0.5615 |
| c6r6 | 1.67 | 0.0392 | 81924.5 | 39192.8 | 0.4432 | 0.9264 | 0.4281 | 36860.7 | 0.4195 | 0.9324 | 0.4072 |
| c6r7 | 1.92 | 0.0701 | 114291.5 | 70136.6 | 0.5202 | 0.8476 | 0.4757 | 63122.6 | 0.4677 | 0.8469 | 0.4312 |
| c6r8 | 2.57 | 0.0876 | 144495.0 | 87560.7 | 0.5471 | 0.9028 | 0.5167 | 82108.3 | 0.5193 | 0.914 | 0.4951 |
| c6r9 | 3.39 | 0.0571 | 68407.9 | 57093.7 | 0.7282 | 0.8725 | 0.6582 | 46867.4 | 0.6224 | 0.9085 | 0.5857 |
| c7r0 | 6.61 | 0.0026 | 6096.2 | 2645.5 | 0.3109 | 0.7165 | 0.2768 | 1963.5 | 0.2814 | 0.8737 | 0.2704 |
| c7r1 | 5.71 | 0.0112 | 22925.0 | 11232.7 | 0.4032 | 0.8228 | 0.371 | 9185.3 | 0.3428 | 0.8556 | 0.3241 |
| c7r2 | 4.85 | 0.0112 | 21847.6 | 11221.7 | 0.4561 | 0.888 | 0.4313 | 8724.3 | 0.3444 | 0.8624 | 0.3265 |
| c7r3 | 4.05 | 0.0192 | 28391.2 | 19161.7 | 0.6356 | 0.9417 | 0.6115 | 17903.5 | 0.6039 | 0.9576 | 0.5882 |
| c7r4 | 3.37 | 0.0179 | 25632.2 | 17915.9 | 0.5632 | 0.8057 | 0.4958 | 15607.6 | 0.5282 | 0.8675 | 0.4888 |
| c7r5 | 2.87 | 0.0235 | 38779.4 | 23489.3 | 0.5371 | 0.8868 | 0.5027 | 22814.2 | 0.5267 | 0.8953 | 0.4962 |
| c7r6 | 2.67 | 0.0381 | 51079.0 | 38122.6 | 0.6698 | 0.8975 | 0.6222 | 33867.7 | 0.6162 | 0.9294 | 0.5887 |
| c7r7 | 2.83 | 0.0712 | 121748.1 | 71206.9 | 0.5135 | 0.8779 | 0.4792 | 66643.2 | 0.4805 | 0.8779 | 0.4504 |
| c7r8 | 3.30 | 0.0740 | 116222.5 | 73997.6 | 0.5255 | 0.8254 | 0.473 | 66556.4 | 0.4704 | 0.8214 | 0.4268 |
| c7r9 | 3.98 | 0.1069 | 193762.0 | 106906.7 | 0.4348 | 0.788 | 0.3892 | 99270.4 | 0.3987 | 0.7782 | 0.358 |
| c8r0 | 7.08 | 0.0010 | 3554.0 | 1023.6 | 0.2813 | 0.9768 | 0.2795 | 1023.6 | 0.2813 | 0.9768 | 0.2795 |
| c8r1 | 6.24 | 0.0012 | 1770.1 | 1237.9 | 0.6566 | 0.9389 | 0.6298 | 1237.9 | 0.6566 | 0.9389 | 0.6298 |
| c8r2 | 5.47 | 0.0065 | 12892.8 | 6488.1 | 0.4627 | 0.9195 | 0.4447 | 6185.9 | 0.4511 | 0.9402 | 0.4385 |
| c8r3 | 4.77 | 0.0110 | 21676.4 | 11033.1 | 0.4418 | 0.868 | 0.414 | 10725.7 | 0.4296 | 0.8682 | 0.4033 |
| c8r4 | 4.20 | 0.0134 | 22488.5 | 13368.7 | 0.4239 | 0.7131 | 0.3622 | 12605.3 | 0.3989 | 0.7117 | 0.3434 |
| c8r5 | 3.82 | 0.0095 | 18184.0 | 9507.3 | 0.3778 | 0.7226 | 0.33 | 8871.7 | 0.3626 | 0.7433 | 0.3223 |
| c8r6 | 3.67 | 0.0109 | 20163.5 | 10875.2 | 0.4902 | 0.9088 | 0.4672 | 10597.4 | 0.4798 | 0.913 | 0.4589 |
| c8r7 | 3.79 | 0.1060 | 138499.2 | 106006.9 | 0.696 | 0.9093 | 0.6508 | 92818.3 | 0.6171 | 0.9209 | 0.5861 |
| c8r8 | 4.15 | 0.0209 | 52887.4 | 20879.2 | 0.3179 | 0.8053 | 0.2952 | 20879.2 | 0.3179 | 0.8053 | 0.2952 |
| c8r9 | 4.71 | 0.0330 | 62589.3 | 32982.0 | 0.4151 | 0.7878 | 0.3734 | 22767.7 | 0.321 | 0.8824 | 0.3078 |
| c9r0 | 7.64 | 0.0008 | 2038.2 | 785.8 | 0.318 | 0.8248 | 0.2979 | 785.8 | 0.318 | 0.8248 | 0.2979 |
| c9r1 | 6.88 | 0.0073 | 9408.4 | 7265.2 | 0.6266 | 0.8115 | 0.547 | 7265.2 | 0.6266 | 0.8115 | 0.547 |
| c9r2 | 6.18 | 0.0021 | 4157.5 | 2101.8 | 0.4236 | 0.838 | 0.3915 | 2101.8 | 0.4236 | 0.838 | 0.3915 |
| c9r3 | 5.58 | 0.0108 | 14511.1 | 10764.1 | 0.6082 | 0.8199 | 0.5365 | 10588.4 | 0.5995 | 0.8216 | 0.5305 |
| c9r4 | 5.10 | 0.0093 | 14750.9 | 9343.8 | 0.4049 | 0.6393 | 0.3296 | 8420.7 | 0.4024 | 0.7048 | 0.3443 |
| c9r5 | 4.79 | 0.0327 | 51183.4 | 32712.9 | 0.5832 | 0.9125 | 0.5523 | 31635.8 | 0.5729 | 0.9269 | 0.5482 |
| c9r6 | 4.67 | 0.0135 | 24329.6 | 13546.5 | 0.4733 | 0.8501 | 0.4368 | 13101.2 | 0.4626 | 0.8591 | 0.43 |
| c9r7 | 4.76 | 0.0385 | 53547.4 | 38495.2 | 0.6762 | 0.9407 | 0.6486 | 38495.2 | 0.6762 | 0.9407 | 0.6486 |
| c9r8 | 5.06 | 0.0718 | 80152.4 | 71847.7 | 0.863 | 0.9628 | 0.8352 | 71847.7 | 0.863 | 0.9628 | 0.8352 |
| c9r9 | 5.52 | 0.0195 | 22122.4 | 19495.4 | 0.8564 | 0.9717 | 0.8356 | 19495.4 | 0.8564 | 0.9717 | 0.8356 |

> **段落审读**
> - **逻辑用途：** 给出正文汇总结果的完整数值底表
> - **核对状态：** ✅ 已核对：已与 `validation_summary.csv` 和两份 `accuracy_vs_distance*.csv` 的字段及行数核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；`analysis/accuracy_vs_distance_summary.csv`；本段核对值：3, 7.44, 0.0120, 15166.2, 11958.1, 0.6213, 0.788；译文对应位置：`09_appendix_b_percell_and_distance.md`（仅作定位，不作为引文证据）
> - **可加强：** 正式排版时重复表头并注明空白召回率的含义。

## B.5 源文件

**英文原稿**

Generated from `analysis/validation_summary.csv`, `analysis/accuracy_vs_distance.csv` and `analysis/accuracy_vs_distance_summary.csv` in the project repository (Appendix D).

**中文翻译**

本表由项目仓库中的 `analysis/validation_summary.csv`、`analysis/accuracy_vs_distance.csv` 和 `analysis/accuracy_vs_distance_summary.csv` 生成（附录 D）。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `analysis/validation_summary.csv`；`analysis/accuracy_vs_distance.csv`；`analysis/accuracy_vs_distance_summary.csv`；译文对应位置：`09_appendix_b_percell_and_distance.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

# 附录 C——补充适应实验

## C.1 目的与地位

**英文原稿**

The primary analysis in Chapters 4 and 5 measures the released checkpoint applied to Leeds without any UK training data. This appendix reports a bounded supplementary experiment that departs from that boundary alone, in order to ask a question the main study cannot: if a user does hold local pixel-level labels, what does the error typology of §4.2 buy them?

**中文翻译**

第 4、5 章的主分析测量的是在完全不使用英国训练数据的情况下，把已发布检查点应用于利兹的结果。本附录只偏离这一边界，报告一项范围受限的补充实验，以回答主研究无法回答的问题：如果使用者确实拥有本地像素级标签，§4.2 的误差类型学能带来什么？

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：4, 5, 4.2；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

Three interventions are compared against the zero-shot model: generic fine-tuning on Leeds labels, targeted fine-tuning that weights the loss by the attributed false-positive categories, and probability-threshold adjustment of the generic model with no retraining.

**中文翻译**

研究把三种干预与零样本模型比较：在利兹标签上进行普通微调；按已归因的假阳性类别对损失加权的定向微调；以及不重新训练、只调整普通模型的概率阈值。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

Nothing here enters the main analysis. All figures are raw pixel output on a fixed held-out split, without the post-processing that Chapter 4 applies throughout, and they are valid only for comparison with each other. They are not comparable with the headline figures of Chapter 4 and are not used to qualify them.

**中文翻译**

本附录的结果均不进入主分析。所有数字都是在固定留出划分上的原始像素输出，未经过第 4 章始终采用的后处理；它们只适合彼此比较，不能与第 4 章的核心数字相比，也不用于修正主分析结论。

> **段落审读**
> - **逻辑用途：** 限制结论适用范围，防止从城市尺度证据跳到地块判断
> - **核对状态：** 🟨 需人工复核：限制来自研究设计与已报告验证结果。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：4；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 区分可在本研究内量化的限制和只能在未来研究中检验的限制。

## C.2 数据与划分

**英文原稿**

The 100 cells of the study area are partitioned at cell level, so no patch from a training cell appears in evaluation:

**中文翻译**

研究区 100 个单元按单元层级划分，因此训练单元中的任何图块都不会出现在评估中：

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：100；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

| Role | Cells | Use |
|---|---:|---|
| Fit | 40 | gradient updates |
| Validation | 10 | epoch selection and threshold selection |
| Test | 50 | reported results only |

**中文翻译**

| 角色 | 单元数 | 用途 |
|---|---:|---|
| 拟合 | 40 | 梯度更新 |
| 验证 | 10 | 选择 epoch 与阈值 |
| 测试 | 50 | 只用于报告结果 |

> **段落审读**
> - **逻辑用途：** 把补充实验的比较转成可审计数值
> - **核对状态：** ✅ 已核对：已按附录 C.8 所列 CSV 对照。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：40, 10, 50；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 加入多随机种子均值与区间后再作稳定性判断。

**英文原稿**

Patch sampling keeps every patch containing labelled parking and an equal number of empty patches, giving 2,256 retained training patches. The validation set is the 438 retained patches of the ten validation cells — the same sample used to select checkpoints during training, so that threshold selection and epoch selection see identical data. The test set is the complete 3,200 patches of the fifty held-out cells, with no retention filter, so evaluation covers whole cells rather than a parking-enriched sample.

**中文翻译**

图块抽样保留所有包含标注停车的图块，并保留数量相等的空图块，最终得到 2,256 个训练图块。验证集包含十个验证单元中保留的 438 个图块——也就是训练期间选择检查点所用的同一样本，因此阈值与 epoch 选择看到完全相同的数据。测试集则包含 50 个留出单元的全部 3,200 个图块，不作保留筛选，因此评估覆盖完整单元，而非富集停车的样本。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：2,256, 438, 50, 3,200；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

The zero-shot arm reproduces precision 0.5190, recall 0.8819 and IoU 0.4853 on this split, which is the consistency check the other arms depend on: without it none of the comparisons below would be interpretable.

**中文翻译**

零样本分支在该划分上复现精确率 0.5190、召回率 0.8819 与 IoU 0.4853；这是其他分支赖以成立的一致性检查，否则下文比较均无法解释。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：0.5190, 0.8819, 0.4853；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

Tables C.1 to C.5 label the four arms A to D, following the result files listed in C.8. The text refers to them by description, so that arm letters are never confused with appendix letters.

**中文翻译**

表 C.1–C.5 按 C.8 所列结果文件把四个分支标为 A–D。正文使用描述性名称，避免分支字母与附录字母混淆。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：1, 5, 8；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

## C.3 普通微调与定向微调

**英文原稿**

Both fine-tuning arms start from the released checkpoint and share batch size, learning rate, optimiser and seed; only the loss differs. The targeted arm assigns per-pixel weights from the model's own zero-shot errors on the fit cells, coded against the reference layers of §4.2: standalone false positives on precise layers (road buffer, curtilage, OSM parking, sports) are weighted most heavily, those on broad land-use layers less so, and false negatives receive a counterweight computed from the observed code composition rather than chosen by hand. False positives within the boundary band are deliberately left at unit weight, since upweighting them is precisely how a model is taught to draw everything smaller.

**中文翻译**

两种微调均从已发布检查点开始，采用相同批大小、学习率、优化器和随机种子；唯一差异是损失函数。定向分支根据模型在拟合单元上的零样本错误，为每个像素赋予权重，并按照 §4.2 的参考图层编码：落在精细图层（道路缓冲区、宅地、OSM 停车、运动设施）上的独立 FP 权重最高，落在宽泛土地利用图层上的权重较低；FN 的反向权重由实际观察到的代码构成计算，而非人工指定。边界带内的 FP 刻意保持单位权重，因为提高其权重恰恰会教模型把所有对象画得更小。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：4.2；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

An earlier targeted configuration was run with a hand-set counterweight and is not reported here: its suppression and recovery terms were unbalanced, which confounds the comparison the arm was built to make. Only the rebalanced run is reported.

**中文翻译**

研究曾以人工设定的反向权重运行过更早的定向配置，但不在此报告：其抑制项与恢复项不平衡，会混淆该分支本来要进行的比较。因此这里只报告重新平衡后的运行。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

The two targeted checkpoints come from a single training trajectory, not from two independently trained models. Epoch 12 gave the best validation IoU (0.6105); among epochs within 0.02 of it, epoch 7 gave the highest validation recall (0.8385) at validation IoU 0.6093. The two differ by 0.0012 in validation IoU, which is within the epoch-to-epoch variation visible across epochs 7 to 12, so the pair should be read as two operating points on one trade-off curve rather than as a better and a worse model.

**中文翻译**

两个定向检查点来自同一条训练轨迹，而非两个独立训练模型。第 12 个 epoch 的验证 IoU 最佳（0.6105）；在与其差距不超过 0.02 的 epoch 中，第 7 个 epoch 的验证召回率最高（0.8385），验证 IoU 为 0.6093。两者的验证 IoU 只差 0.0012，处于第 7–12 个 epoch 可见的逐轮波动范围内，因此应把它们理解为同一条取舍曲线上的两个运行点，而非一优一劣的两个模型。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：12, 0.6105, 0.02, 7, 0.8385, 0.6093, 0.0012；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

**Table C.1 — Overall accuracy, 50 held-out cells, raw pixels (micro)**

**中文翻译**

**表 C.1——50 个留出单元的总体准确率，原始像素（micro）**

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：1, 50；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

| Arm | Precision | Recall | IoU | Predicted ÷ reference |
|---|---:|---:|---:|---:|
| A zero-shot | 0.5190 | 0.8819 | 0.4853 | 1.699 |
| B generic fine-tuning | 0.7664 | 0.7548 | **0.6136** | 0.985 |
| C targeted, epoch 12 (best validation IoU) | 0.7393 | 0.7168 | 0.5722 | 0.970 |
| D targeted, epoch 7 (best validation recall) | 0.6668 | 0.7852 | 0.5640 | 1.178 |

**中文翻译**

| 分支 | 精确率 | 召回率 | IoU | 预测 ÷ 参考 |
|---|---:|---:|---:|---:|
| A 零样本 | 0.5190 | 0.8819 | 0.4853 | 1.699 |
| B 普通微调 | 0.7664 | 0.7548 | **0.6136** | 0.985 |
| C 定向微调，第 12 epoch（验证 IoU 最佳） | 0.7393 | 0.7168 | 0.5722 | 0.970 |
| D 定向微调，第 7 epoch（验证召回率最佳） | 0.6668 | 0.7852 | 0.5640 | 1.178 |

> **段落审读**
> - **逻辑用途：** 把补充实验的比较转成可审计数值
> - **核对状态：** ✅ 已核对：已按附录 C.8 所列 CSV 对照。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：0.5190, 0.8819, 0.4853, 1.699, 0.7664, 0.7548, 0.6136；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 加入多随机种子均值与区间后再作稳定性判断。

**英文原稿**

**Table C.2 — The same arms under macro (per-cell mean) aggregation**

**中文翻译**

**表 C.2——相同分支采用 macro（逐单元均值）汇总**

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：2；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

| Arm | Precision | Recall | IoU |
|---|---:|---:|---:|
| A zero-shot | 0.4773 | 0.8777 | 0.4473 |
| B generic fine-tuning | 0.7553 | 0.7205 | **0.5833** |
| C targeted, epoch 12 | 0.7116 | 0.6839 | 0.5374 |
| D targeted, epoch 7 | 0.6391 | 0.7595 | 0.5322 |

**中文翻译**

| 分支 | 精确率 | 召回率 | IoU |
|---|---:|---:|---:|
| A 零样本 | 0.4773 | 0.8777 | 0.4473 |
| B 普通微调 | 0.7553 | 0.7205 | **0.5833** |
| C 定向微调，第 12 epoch | 0.7116 | 0.6839 | 0.5374 |
| D 定向微调，第 7 epoch | 0.6391 | 0.7595 | 0.5322 |

> **段落审读**
> - **逻辑用途：** 把补充实验的比较转成可审计数值
> - **核对状态：** ✅ 已核对：已按附录 C.8 所列 CSV 对照。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：0.4773, 0.8777, 0.4473, 0.7553, 0.7205, 0.5833, 12；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 加入多随机种子均值与区间后再作稳定性判断。

**英文原稿**

Generic fine-tuning raises IoU from 0.485 to 0.614, gaining 0.247 of precision at a cost of 0.127 of recall: standalone false-positive area falls by 74.5% while false-negative area doubles. Neither targeted checkpoint improves on it, under either aggregation.

**中文翻译**

普通微调把 IoU 从 0.485 提升至 0.614，以损失 0.127 召回率换来 0.247 精确率；独立 FP 面积下降 74.5%，而 FN 面积翻倍。无论采用何种汇总方式，两个定向检查点均未超过普通微调。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：0.485, 0.614, 0.127, 0.247, 74.5；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

The generic model's predicted area is within 1.5% of the reference total. This is arithmetic coincidence at this operating point, not a corrected bias: false-positive area (0.3736 km²) and false-negative area (0.3982 km²) happen to be close, and they cancel. The epoch-7 targeted checkpoint, from the same run, over-predicts by 17.8%. Nothing in this appendix supports a claim that fine-tuning corrects the area bias measured in Chapter 4, which concerns post-processed output over the whole study area.

**中文翻译**

普通模型预测总面积与参考总面积相差不到 1.5%。这只是该运行点上的算术巧合，而非偏差已经得到校正：FP 面积（0.3736 km²）与 FN 面积（0.3982 km²）恰好接近并相互抵消。同一运行中的第 7 epoch 定向检查点仍高估 17.8%。本附录不支持“微调修正了第 4 章面积偏差”的结论，因为后者针对全研究区的后处理输出。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：1.5, 0.3736, 0.3982, 7, 17.8, 4；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

**Table C.3 — Boundary decomposition at 5 m (km²)**

**中文翻译**

**表 C.3——5 m 边界分解（km²）**

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：3, 5；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

| Arm | FP dilation | FP standalone | FN erosion | FN standalone |
|---|---:|---:|---:|---:|
| A zero-shot | 0.3737 | 0.9537 | 0.0858 | 0.1059 |
| B generic fine-tuning | 0.1302 | 0.2434 | 0.1684 | 0.2298 |
| C targeted, epoch 12 | 0.1503 | 0.2602 | 0.1686 | 0.2913 |
| D targeted, epoch 7 | 0.2359 | 0.4013 | 0.1254 | 0.2233 |

**中文翻译**

| 分支 | FP 外扩 | FP 独立 | FN 内蚀 | FN 独立 |
|---|---:|---:|---:|---:|
| A 零样本 | 0.3737 | 0.9537 | 0.0858 | 0.1059 |
| B 普通微调 | 0.1302 | 0.2434 | 0.1684 | 0.2298 |
| C 定向微调，第 12 epoch | 0.1503 | 0.2602 | 0.1686 | 0.2913 |
| D 定向微调，第 7 epoch | 0.2359 | 0.4013 | 0.1254 | 0.2233 |

> **段落审读**
> - **逻辑用途：** 把补充实验的比较转成可审计数值
> - **核对状态：** ✅ 已核对：已按附录 C.8 所列 CSV 对照。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：0.3737, 0.9537, 0.0858, 0.1059, 0.1302, 0.2434, 0.1684；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 加入多随机种子均值与区间后再作稳定性判断。

**英文原稿**

Under every arm the added false negative is majority standalone rather than erosion — whole car parks missed, not edges trimmed. Bands at 2 m and 10 m are reported in `boundary_bands_arms.csv` and do not change this ordering.

**中文翻译**

所有分支新增的 FN 都以独立漏检为主，而非边缘内蚀——也就是整块停车场被漏掉，而不是边缘被削薄。2 m 与 10 m 带宽结果见 `boundary_bands_arms.csv`，排序不变。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：2, 10；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

## C.4 选择性

**英文原稿**

The targeted arm was designed to remove false positives from four categories specifically: road buffer, curtilage, OSM parking and sports. If positional weighting works as intended, the removal rate for those categories should exceed the removal rate for the others by more than it does under generic fine-tuning.

**中文翻译**

定向分支的设计目的，是专门去除四类 FP：道路缓冲区、宅地、OSM 停车和运动设施。如果位置加权按预期工作，那么它对这些类别的去除率相对于其他类别的优势，应大于普通微调的相应优势。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

**Table C.4 — Standalone false-positive removal against zero-shot (%)**

**中文翻译**

**表 C.4——相对于零样本的独立 FP 去除率（%）**

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：4；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

| Arm | Targeted categories | Other categories | Gap (pts) |
|---|---:|---:|---:|
| B generic fine-tuning | 72.5 | 62.8 | **9.7** |
| C targeted, epoch 12 | 71.6 | 63.2 | 8.4 |
| D targeted, epoch 7 | 58.3 | 50.6 | 7.8 |

**中文翻译**

| 分支 | 定向类别 | 其他类别 | 差距（百分点） |
|---|---:|---:|---:|
| B 普通微调 | 72.5 | 62.8 | **9.7** |
| C 定向微调，第 12 epoch | 71.6 | 63.2 | 8.4 |
| D 定向微调，第 7 epoch | 58.3 | 50.6 | 7.8 |

> **段落审读**
> - **逻辑用途：** 把补充实验的比较转成可审计数值
> - **核对状态：** ✅ 已核对：已按附录 C.8 所列 CSV 对照。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：72.5, 62.8, 9.7, 12, 71.6, 63.2, 8.4；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 加入多随机种子均值与区间后再作稳定性判断。

**英文原稿**

Neither targeted arm is more selective than generic fine-tuning. Per category, generic fine-tuning removes more standalone false positive than the epoch-12 targeted checkpoint on road buffer (81.4% against 78.0%), curtilage (75.8% against 70.6%) and OSM parking (42.7% against 40.1%); only sports favours the targeted arm (97.5% against 90.0%). Total standalone false-positive removal is also higher under generic fine-tuning (74.5% against 72.7% and 57.9%).

**中文翻译**

两个定向分支都没有比普通微调更具选择性。分类别看，普通微调对道路缓冲区（81.4% 对 78.0%）、宅地（75.8% 对 70.6%）和 OSM 停车（42.7% 对 40.1%）独立 FP 的去除率都高于第 12 epoch 定向检查点；只有运动设施类别偏向定向分支（97.5% 对 90.0%）。普通微调对全部独立 FP 的去除率也更高（74.5%，对比 72.7% 和 57.9%）。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：81.4, 78.0, 75.8, 70.6, 42.7, 40.1, 12；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 注明 OSM 获取日期、要素标签范围和完整性口径。

## C.5 阈值调整：方法

**英文原稿**

The targeted checkpoints differ from the generic model mainly in where they sit on a precision–recall trade-off. That raises a question the fine-tuning arms cannot settle on their own: whether those operating points require targeted training at all, or whether they are reachable by moving the decision threshold of the generic model.

**中文翻译**

定向检查点与普通模型的主要差异，是它们处于精确率—召回率取舍曲线的不同位置。这提出一个微调分支自身无法回答的问题：这些运行点是否必须通过定向训练获得，还是只需移动普通模型的决策阈值即可达到？

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

The released pipeline takes the argmax of the two output logits, equivalent to thresholding the parking probability at 0.50. The sweep replaces that rule and nothing else. No weights are retrained, and the generic checkpoint is used unmodified.

**中文翻译**

发布流程对两个输出 logit 取 argmax，等价于把停车概率阈值设为 0.50。阈值扫描只替换这一规则，不改动其他部分；不重新训练任何权重，普通检查点保持不变。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：0.50；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

1. Sweep the parking-class probability threshold from 0.05 to 0.95 in steps of 0.01 (91 values) on the 10 validation cells.
2. Select thresholds on validation only, under four rules: the default 0.50; the best validation IoU; the threshold matching the epoch-12 checkpoint's validation recall; and the threshold matching the epoch-7 checkpoint's validation recall.
3. Lock each selected threshold, then evaluate once on the 50 test cells.

**中文翻译**

1. 在 10 个验证单元上，把停车类别概率阈值从 0.05 扫描至 0.95，步长 0.01（共 91 个值）。
2. 只根据验证集按四项规则选择阈值：默认 0.50；验证 IoU 最佳；匹配第 12 epoch 检查点的验证召回率；匹配第 7 epoch 检查点的验证召回率。
3. 锁定各阈值后，只在 50 个测试单元上评估一次。

> **段落审读**
> - **逻辑用途：** 把并列规则或步骤拆成可执行清单
> - **核对状态：** 🟨 需人工复核：与相应代码、协议或实验日志一致。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：1, 10, 0.05, 0.95, 0.01, 91, 2；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 必要时为每项补充通过／失败判据。

**英文原稿**

Test labels play no part in selection. At threshold 0.50 the sweep reproduces the generic model's test figures exactly (0.7664 / 0.7548 / 0.6136), confirming that the sweep and the training evaluation share one pipeline.

**中文翻译**

测试标签不参与选择。阈值为 0.50 时，扫描精确复现普通模型的测试数字（0.7664 / 0.7548 / 0.6136），确认扫描与训练评估使用同一流程。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：0.50, 0.7664, 0.7548, 0.6136；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

## C.6 阈值调整：结果

**英文原稿**

**Table C.5 — Threshold-adjusted generic model against the targeted checkpoints, test cells**

**中文翻译**

**表 C.5——调整阈值后的普通模型与定向检查点，测试单元**

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：5；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

| Model and rule | Threshold | Precision | Recall | IoU |
|---|---:|---:|---:|---:|
| B generic, default | 0.50 | 0.7664 | 0.7548 | 0.6136 |
| B generic, best validation IoU | 0.48 | 0.7590 | 0.7625 | **0.6139** |
| B generic, matched to C's validation recall | 0.60 | 0.8020 | 0.7113 | 0.6051 |
| C targeted, epoch 12 | — | 0.7393 | 0.7168 | 0.5722 |
| B generic, matched to D's validation recall | 0.39 | 0.7227 | 0.7948 | 0.6090 |
| D targeted, epoch 7 | — | 0.6668 | 0.7852 | 0.5640 |

**中文翻译**

| 模型与规则 | 阈值 | 精确率 | 召回率 | IoU |
|---|---:|---:|---:|---:|
| B 普通，默认 | 0.50 | 0.7664 | 0.7548 | 0.6136 |
| B 普通，验证 IoU 最佳 | 0.48 | 0.7590 | 0.7625 | **0.6139** |
| B 普通，匹配 C 的验证召回率 | 0.60 | 0.8020 | 0.7113 | 0.6051 |
| C 定向，第 12 epoch | — | 0.7393 | 0.7168 | 0.5722 |
| B 普通，匹配 D 的验证召回率 | 0.39 | 0.7227 | 0.7948 | 0.6090 |
| D 定向，第 7 epoch | — | 0.6668 | 0.7852 | 0.5640 |

> **段落审读**
> - **逻辑用途：** 把补充实验的比较转成可审计数值
> - **核对状态：** ✅ 已核对：已按附录 C.8 所列 CSV 对照。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：0.50, 0.7664, 0.7548, 0.6136, 0.48, 0.7590, 0.7625；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 加入多随机种子均值与区间后再作稳定性判断。

**英文原稿**

At the threshold matched to the epoch-12 checkpoint, the generic model gives 0.063 more precision and 0.033 more IoU at recall within 0.006. At the threshold matched to the epoch-7 checkpoint, it is higher on all three measures: precision by 0.056, recall by 0.010, IoU by 0.045. The ordering holds under macro aggregation, where the matched generic thresholds give IoU 0.5707 against the epoch-12 checkpoint's 0.5374 and 0.5801 against the epoch-7 checkpoint's 0.5322.

**中文翻译**

在与第 12 epoch 检查点匹配的阈值上，普通模型在召回率差距不超过 0.006 的情况下，精确率高 0.063、IoU 高 0.033。在与第 7 epoch 检查点匹配的阈值上，普通模型三项指标均更高：精确率高 0.056、召回率高 0.010、IoU 高 0.045。macro 汇总下排序仍不变：匹配阈值的普通模型 IoU 分别为 0.5707 和 0.5801，对应定向检查点为 0.5374 和 0.5322。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：12, 0.006, 0.063, 0.033, 7, 0.056, 0.010；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

Threshold selection itself gains almost nothing: the best validation threshold, 0.48, improves test IoU by 0.0003 over the default. The released argmax rule is already close to optimal for this model, which is why the comparison is informative — the targeted checkpoints are being measured against a generic model that has not been tuned in its own favour.

**中文翻译**

阈值选择本身几乎没有增益：验证集最佳阈值 0.48，相比默认阈值只把测试 IoU 提高 0.0003。发布版 argmax 规则对该模型已经接近最优，因此这一比较具有信息量——定向检查点面对的普通模型并未被刻意调到对自己有利的位置。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：0.48, 0.0003；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

**英文原稿**

The conclusion this supports is that positional targeted weighting produced no overall performance gain that threshold adjustment of the generic model could not supply. It does not support the stronger claim that the targeted model learned no new features: these are aggregate accuracy measures, and they cannot observe what the network represents internally.

**中文翻译**

上述证据支持的结论是：位置定向加权没有产生普通模型仅靠阈值调整无法提供的总体性能增益。它不支持“定向模型没有学到新特征”这一更强说法，因为这些是汇总准确率指标，无法观察网络内部表征。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

## C.7 局限

**英文原稿**

- **One seed, one weighting scheme.** Every arm was trained once. The epoch-to-epoch spread in validation IoU across epochs 7 to 12 is comparable to the gap between the two targeted checkpoints, so the experiment cannot separate a small real effect from run-to-run variation.
- **Positional proxies are not visual categories.** Standalone false positives were weighted by the layer they fall on. A false positive on industrial land may be a roof, a hardstanding, a road or a vehicle storage yard; these are one location but not one appearance, and weighting them together may present the network with no consistent feature to learn. This is the most likely explanation for the negative result and is untested.
- **Raw pixels only.** No arm passes through the post-processing of §3.3. Comparison with Chapter 4 is invalid in both directions.
- **Validation is a parking-enriched sample.** Epoch and threshold selection used the 438 retained patches of ten cells, not whole cells, so the selected operating points are tuned on a distribution denser in parking than the test cells.
- **One city, one annotator.** Fit, validation and test cells are all Leeds, labelled by the same annotator against the same protocol. Nothing here tests whether a fine-tuned model transfers to a second British city, which remains the precondition identified in §5.5.
- **The threshold result is about aggregate accuracy.** It shows no measurable overall advantage from targeted weighting; it does not establish that the two models are equivalent, nor that targeted training is unproductive in general.

**中文翻译**

- **单一种子、单一加权方案。** 每个分支只训练一次。第 7–12 epoch 的验证 IoU 波动与两个定向检查点之间的差距相当，因此实验无法区分较小的真实效应与逐个 epoch 之间的波动。
- **位置代理不是视觉类别。** 独立 FP 按其落入的图层加权。工业用地上的 FP 可能是屋顶、硬化空地、道路或车辆存放场；它们位置相同、外观却不一致，将其共同加权可能无法向网络提供一致的可学习特征。这是阴性结果最可能但尚未检验的解释。
- **仅原始像素。** 所有分支均未经过 §3.3 的后处理，因此不能从任何方向与第 4 章比较。
- **验证集是停车富集样本。** epoch 与阈值选择使用十个单元中保留的 438 个图块，而非完整单元，因此所选运行点针对的是停车密度高于测试单元的分布。
- **单一城市、单一标注者。** 拟合、验证与测试单元都来自利兹，并由同一标注者按同一规程标注。本实验没有检验微调模型是否能迁移到第二座英国城市，而这仍是 §4.7 指出的前提。
- **阈值结论只针对汇总准确率。** 它只表明定向加权没有可测的总体优势；不能证明两个模型等价，也不能证明定向训练在一般情况下无效。

> **段落审读**
> - **逻辑用途：** 并列限定补充实验的外推边界
> - **核对状态：** 🟨 需人工复核：各项均可追溯到划分、日志或评估流程。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：7, 12, 3.4, 4, 438, 4.7；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 按影响严重度排序，并明确哪些会改变主结论。

## C.8 文件

**英文原稿**

Results are reproduced from `targeted-finetuning/Parking_targeted_run2/`: `evaluation_arms.csv` (Tables C.1–C.2), `boundary_bands_arms.csv` (C.3), `selectivity.csv` and `standalone_fp_by_category.csv` (C.4), `threshold_sweep/generic_threshold_selected.csv` (C.5), and `targeted_log.csv` for the epoch record. The notebooks are `run_targeted_colab.ipynb` and `threshold_sweep_colab.ipynb`.

**中文翻译**

结果复现自 `targeted-finetuning/Parking_targeted_run2/`：`evaluation_arms.csv`（表 C.1–C.2）、`boundary_bands_arms.csv`（C.3）、`selectivity.csv` 与 `standalone_fp_by_category.csv`（C.4）、`threshold_sweep/generic_threshold_selected.csv`（C.5），以及记录 epoch 的 `targeted_log.csv`。笔记本为 `run_targeted_colab.ipynb` 与 `threshold_sweep_colab.ipynb`。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv`；`boundary_bands_arms.csv`；`selectivity.csv`；`threshold_sweep/generic_threshold_selected.csv`；本段核对值：1, 2, 3, 4, 5；译文对应位置：`10_appendix_c_supplementary_experiment.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

# 附录 D——代码与数据可获得性

## D.1 仓库

**英文原稿**

All code written for this study is archived at **https://github.com/hou1020/Parking**. The directories referenced elsewhere in this dissertation are:

**中文翻译**

本研究编写的全部代码均归档于 **https://github.com/hou1020/Parking**。论文其他位置引用的目录如下：

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 附录 D 所列仓库目录、许可说明与结果文件路径；本段核对值：020；译文对应位置：`11_appendix_d_code_and_data.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

| Directory | Contents |
|---|---|
| `calculate/` | Agreement against the manual and OSM references, polygon filtering and result merging |
| `analysis/` | Validation, error attribution, sampling, ablation and calibration (§3.4–§3.9) |
| `manual/`, `fine-tuning/*.gpkg` | The manual reference labels and the 1 km² grid |
| `fine-tuning/` | Generic fine-tuning of the released checkpoint (Appendix C) |
| `targeted-finetuning/` | Targeted loss weighting and the threshold sweep (Appendix C) |
| `parking-lot-mapping-tool/` | The released pipeline, with the UK-specific tiling, inference and post-processing written for this study (§3.3) |

**中文翻译**

| 目录 | 内容 |
|---|---|
| `calculate/` | 与人工参考及 OSM 的一致性计算、多边形过滤与结果合并 |
| `analysis/` | 验证、误差归因、抽样、消融和校准（§3.4–§3.9） |
| `manual/`、`fine-tuning/*.gpkg` | 人工参考标签与 1 km² 网格 |
| `fine-tuning/` | 对已发布检查点的普通微调（附录 C） |
| `targeted-finetuning/` | 定向损失加权与阈值扫描（附录 C） |
| `parking-lot-mapping-tool/` | 已发布流程，含为本研究编写的英国专用切片、推理与后处理（§3.3） |

> **段落审读**
> - **逻辑用途：** 建立表格、代码与源文件的一一映射
> - **核对状态：** 🟨 需人工复核：路径均在当前项目中可定位。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 附录 D 所列仓库目录、许可说明与结果文件路径；本段核对值：100, 3.4, 3.5, 3.8, 1；译文对应位置：`11_appendix_d_code_and_data.md`（仅作定位，不作为引文证据）
> - **可加强：** 提交前核对公开仓库中的大小写和许可文件。

## D.2 影像

**英文原稿**

Getmapping aerial photography supplied through Digimap: 109 tiles at 0.25 m ground sample distance, three visible bands, EPSG:27700. The tile identifiers and version suffixes needed to reorder the same coverage are recorded in `parking-lot-mapping-tool/output_files/tif_processing_progress.csv` and in the download folder names under `parking-lot-mapping-tool/files/`, and every processing step from the raw tiles onward is reproducible from the code once the imagery is obtained under an equivalent licence.

**中文翻译**

通过 Digimap 提供的 Getmapping 航空摄影：109 个图块，地面采样距离 0.25 m，三个可见光波段，EPSG:27700。重新订购相同覆盖范围所需的图块标识符和版本后缀记录在 `parking-lot-mapping-tool/output_files/tif_processing_progress.csv` 及 `parking-lot-mapping-tool/files/` 下的下载目录名中；只要在同等许可下取得影像，从原始图块开始的每一步均可由代码复现。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 附录 D 所列仓库目录、许可说明与结果文件路径；本段核对值：109, 0.25, 27700；译文对应位置：`11_appendix_d_code_and_data.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

## D.3 参考数据

**英文原稿**

| Source | Use | Retrieved |
|---|---|---|
| OpenStreetMap building footprints, road centrelines | Post-processing inputs (§3.3) | 25 June 2026 |
| OpenStreetMap land use, brownfield, pitch, `amenity=parking` | Error attribution only (§4.2) | 25 June 2026 |
| Ordnance Survey Open Greenspace | Sports facilities in error attribution | — |

**中文翻译**

| 来源 | 用途 | 获取日期 |
|---|---|---|
| OpenStreetMap 建筑轮廓、道路中心线 | 后处理输入（§3.3） | 2026 年 6 月 25 日 |
| OpenStreetMap 土地利用、棕地、运动场、`amenity=parking` | 仅用于误差归因（§4.2） | 2026 年 6 月 25 日 |
| Ordnance Survey Open Greenspace | 误差归因中的运动设施 | — |

> **段落审读**
> - **逻辑用途：** 建立表格、代码与源文件的一一映射
> - **核对状态：** 🟨 需人工复核：路径均在当前项目中可定位。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 附录 D 所列仓库目录、许可说明与结果文件路径；本段核对值：3.4, 6, 25, 4.2；译文对应位置：`11_appendix_d_code_and_data.md`（仅作定位，不作为引文证据）
> - **可加强：** 提交前核对公开仓库中的大小写和许可文件。

**英文原稿**

OpenStreetMap data are © OpenStreetMap contributors, available under the Open Database Licence. Ordnance Survey Open Greenspace is published under the Open Government Licence. Neither is used as ground truth; the distinction is set out in §3.1.

**中文翻译**

OpenStreetMap 数据 © OpenStreetMap contributors，按 Open Database Licence 提供。Ordnance Survey Open Greenspace 按 Open Government Licence 发布。两者均不作为地面真值；§3.1 已说明这一区别。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 附录 D 所列仓库目录、许可说明与结果文件路径；本段核对值：3.1；译文对应位置：`11_appendix_d_code_and_data.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

## D.4 参考标签

**英文原稿**

The 2,037 manually labelled car parks are held in the repository as GeoPackage, together with the 1 km² validation grid and the confidence attribute described in Appendix A. These are the labels against which every accuracy figure in Chapter 4 is measured, and they are original to this study.

**中文翻译**

2,037 个手工标注停车场与 1 km² 验证网格，以及附录 A 所述 confidence 属性，均以 GeoPackage 存放于仓库。这些是第 4 章每个准确率数字所对照的标签，且为本研究原创。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 附录 D 所列仓库目录、许可说明与结果文件路径；本段核对值：2,037, 1, 4；译文对应位置：`11_appendix_d_code_and_data.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充置信区间或说明该数字是直接测量、估计还是逻辑上限。

## D.5 模型

**英文原稿**

The segmentation network is the published checkpoint of Qiam, Devunuri and Lehe (2025), obtained from the authors' release and used without modification in the primary analysis. The fine-tuned checkpoints produced for Appendix C are derived works of that release and are not redistributed; the training code and logs that generate them are in `fine-tuning/` for the generic arm and `targeted-finetuning/` for the targeted loss weighting and threshold sweep.

**中文翻译**

分割网络为 Qiam、Devunuri 和 Lehe（2025）的已发布检查点，从作者发布版本取得，在主分析中未经修改使用。附录 C 产生的微调检查点是该发布版本的衍生作品，不予再分发；生成它们的训练代码与日志分别位于 `fine-tuning/`（通用微调）与 `targeted-finetuning/`（定向损失加权与阈值扫描）。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L24](#l24) Qiam, Devunuri and Lehe (2025)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 附录 D 所列仓库目录、许可说明与结果文件路径；译文对应位置：`11_appendix_d_code_and_data.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

## D.6 结果文件

**英文原稿**

Each appendix table is generated from a file in the repository rather than transcribed:

**中文翻译**

附录中的每张表均由仓库文件生成，而非手工抄录：

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 附录 D 所列仓库目录、许可说明与结果文件路径；译文对应位置：`11_appendix_d_code_and_data.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

| Table | Source |
|---|---|
| Appendix B.1 | `analysis/validation_summary.csv` |
| Appendix B.2–B.4 | `analysis/accuracy_vs_distance.csv`, `analysis/accuracy_vs_distance_summary.csv` |
| Appendix C.1–C.2 | `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv` |
| Appendix C.3 | `targeted-finetuning/Parking_targeted_run2/boundary_bands_arms.csv` |
| Appendix C.4 | `targeted-finetuning/Parking_targeted_run2/selectivity.csv`, `standalone_fp_by_category.csv` |
| Appendix C.5 | `targeted-finetuning/Parking_targeted_run2/threshold_sweep/generic_threshold_selected.csv` |

**中文翻译**

| 表 | 来源 |
|---|---|
| 附录 B.1 | `analysis/validation_summary.csv` |
| 附录 B.2–B.4 | `analysis/accuracy_vs_distance.csv`、`analysis/accuracy_vs_distance_summary.csv` |
| 附录 C.1–C.2 | `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv` |
| 附录 C.3 | `targeted-finetuning/Parking_targeted_run2/boundary_bands_arms.csv` |
| 附录 C.4 | `targeted-finetuning/Parking_targeted_run2/selectivity.csv`、`standalone_fp_by_category.csv` |
| 附录 C.5 | `targeted-finetuning/Parking_targeted_run2/threshold_sweep/generic_threshold_selected.csv` |

> **段落审读**
> - **逻辑用途：** 建立表格、代码与源文件的一一映射
> - **核对状态：** 🟨 需人工复核：路径均在当前项目中可定位。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 附录 D 所列仓库目录、许可说明与结果文件路径；本段核对值：1, 2, 4, 3, 5；译文对应位置：`11_appendix_d_code_and_data.md`（仅作定位，不作为引文证据）
> - **可加强：** 提交前核对公开仓库中的大小写和许可文件。

## D.7 复现

**英文原稿**

The city-wide inference and the fine-tuning experiments require a GPU and were run in Google Colab; the notebooks (`run_finetuning_colab.ipynb`, `run_targeted_colab.ipynb`, `threshold_sweep_colab.ipynb`) pin `transformers==4.57.1`, otherwise running against the Colab environment's own package versions, and cache intermediate outputs, so a run interrupted partway resumes rather than restarting. All other analysis runs on CPU from the committed CSVs.

**中文翻译**

全城推理和微调实验需要 GPU，并在 Google Colab 中运行；笔记本（`run_finetuning_colab.ipynb`、`run_targeted_colab.ipynb`、`threshold_sweep_colab.ipynb`）固定了 `transformers==4.57.1`，其余依赖沿用 Colab 环境自带版本，并缓存中间输出，因此运行中断后可以续接而无需从头开始。其他所有分析均可在 CPU 上从已提交的 CSV 运行。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 附录 D 所列仓库目录、许可说明与结果文件路径；译文对应位置：`11_appendix_d_code_and_data.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

# 附录 E——研究日志

## E.1 日志说明

**英文原稿**

This log records the supervision meetings, tasks, problems and outputs of the dissertation project between April and August 2026. It is compiled from two sources: the record of supervision meetings held with CASA and Centre for Cities (Section E.2), and the commit history of the project repository, archived at **https://github.com/hou1020/Parking** (Section E.3).

**中文翻译**

本日志记录 2026 年 4–8 月论文项目的指导会议、任务、问题和产出。内容汇编自两个来源：与 CASA 和 Centre for Cities 举行的指导会议记录（E.2），以及项目仓库的提交历史；仓库归档于 **https://github.com/hou1020/Parking**（E.3）。

> **段落审读**
> - **逻辑用途：** 解释项目决策、产出或转向的时间关系
> - **核对状态：** 🟨 需人工复核：日期取自会议记录、提交历史或标注文件，且已注明提交可能滞后。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：4, 8, 2, 020, 3；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 为关键里程碑附 commit hash 或文件修改时间。

**英文原稿**

Two points on how the dates should be read. First, commit dates record when work was committed to the repository, which may lag when it was carried out. Second, the manual annotation described in Phase 4 was carried out in QGIS and stored outside the repository, so it leaves no commits; the dates given for that phase come from the annotation files themselves.

**中文翻译**

日期需要按两点理解。第一，提交日期记录工作何时进入仓库，可能晚于实际完成时间。第二，第 4 阶段的人工标注在 QGIS 中完成并存放于仓库外，因此没有提交记录；该阶段的日期取自标注文件本身。

> **段落审读**
> - **逻辑用途：** 解释项目决策、产出或转向的时间关系
> - **核对状态：** 🟨 需人工复核：日期取自会议记录、提交历史或标注文件，且已注明提交可能滞后。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：4；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 为关键里程碑附 commit hash 或文件修改时间。

## E.2 指导会议

**英文原稿**

Thirteen meeting recordings were made across ten meetings; the kick-off meeting of 27 April is recorded in four segments.

**中文翻译**

十次会议共形成十三段录音；4 月 27 日的启动会议分成四段录制。

> **段落审读**
> - **逻辑用途：** 解释项目决策、产出或转向的时间关系
> - **核对状态：** 🟨 需人工复核：日期取自会议记录、提交历史或标注文件，且已注明提交可能滞后。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：4, 27；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 为关键里程碑附 commit hash 或文件修改时间。

**英文原稿**

| # | Date | Attendees | Discussed |
|---|---|---|---|
| 1 | 27 Apr 2026 | Esra, Clara (CASA); Rob, Maurice (Centre for Cities); Khales, JiaYi | Project kick-off. My project was defined as deep-learning detection of off-street surface parking in UK cities, motivated by identifying unallocated land with housing potential; the transferability of a US-trained model to UK urban form was flagged as the main challenge, and a bi-weekly online sync plus a shared GitHub repository were agreed. |
| 2 | 5 May 2026 | Clara, Esra | Progress update during the coursework period: aerial data had been downloaded from Digimap but no model runs had been carried out yet. The 20 August submission deadline was confirmed and the CASA dissertation writing workshops were announced. |
| 3 | 19 May 2026 | Supervisors | Discussed model accuracy. Manual annotation and retraining were judged too compute-intensive at that stage, so spatial intersection with OpenStreetMap building polygons was recommended as post-processing, and the urban-policy framing of the project was restated over a computer-vision framing. |
| 4 | 2 Jun 2026 | Supervisors | Reported the first Leeds test results on nine tiles — high recall but low precision, with supermarket roofs a characteristic false positive — and asked how many tiles should be validated manually, given a compute cost of about seven minutes per image. |
| 5 | 16 Jun 2026 | Supervisors | Reviewed model outputs on edge cases, in particular industrial and logistics yards being flagged as parking. Agreed to define explicit filtering criteria and a low-confidence class in the methodology, so that the output reflects sites with genuine redevelopment potential. |
| 6 | 22 Jun 2026 | Supervisors | Compared the model output with Ordnance Survey mapping, which also omits informal and unallocated parking. I was asked to choose between a methodological error analysis and a land-potential and policy analysis for a single city, and to archive cleaned code on GitHub. |
| 7 | 9 Jul 2026 | Supervisors, Centre for Cities | Logistics check-in: confirmed the project would run mainly online, with a sync scheduled for the following Friday. |
| 8 | 14 Jul 2026 | Supervisors | Reported that the published, un-finetuned model transferred poorly to UK imagery, especially in distinguishing storage yards and lorry parks from ordinary car parks. Weighed retraining on my own annotations against further post-processing, noting that compute and time would restrict any retraining to a very small area. |
| 9 | 28 Jul 2026 | Supervisors | Advised against pursuing further computer-vision accuracy. The dissertation was refocused on why a US-trained model transfers poorly to UK urban form, what the gaps in OpenStreetMap are, and what the detected areas imply for planning and housing policy. |
| 10 | 11 Aug 2026 | Clara, Esra | With the 20 August deadline approaching and writing not yet started, it was agreed that I would stop running models and first draft the research questions, motivation and literature review, and that the model's limitations across different national and urban contexts would be written up as a substantive analysis chapter rather than treated as a failure. |

**中文翻译**

| # | 日期 | 与会者 | 讨论内容 |
|---|---|---|---|
| 1 | 2026-04-27 | Esra、Clara（CASA）；Rob、Maurice（Centre for Cities）；Khales、JiaYi | 项目启动。我的项目被界定为使用深度学习检测英国城市的路外地面停车，动机是识别具有住房潜力但未分配的土地；美国训练模型对英国城市形态的可迁移性被指出是主要挑战，并约定每两周线上同步一次及使用共享 GitHub 仓库。 |
| 2 | 2026-05-05 | Clara、Esra | 课程作业期间的进度更新：已经从 Digimap 下载航空数据，但尚未运行模型。确认 8 月 20 日提交截止日期，并通知 CASA 论文写作工作坊。 |
| 3 | 2026-05-19 | 导师 | 讨论模型准确率。当时认为人工标注和重新训练所需计算量过大，因此建议用 OpenStreetMap 建筑多边形的空间相交作后处理，并再次强调项目应采用城市政策而非计算机视觉框架。 |
| 4 | 2026-06-02 | 导师 | 汇报利兹 9 个图块的首次测试结果——高召回、低精确率，超市屋顶是典型 FP——并在每幅影像约需 7 分钟计算的条件下，询问应人工验证多少图块。 |
| 5 | 2026-06-16 | 导师 | 审查边缘案例中的模型输出，尤其是工业和物流场院被标成停车。决定在方法中制定明确筛选标准和低置信度类别，使输出反映确有再开发潜力的地点。 |
| 6 | 2026-06-22 | 导师 | 把模型输出与 Ordnance Survey 制图比较，后者同样漏记非正式和未分配停车。要求我在单城的方法误差分析与土地潜力／政策分析之间作选择，并把清理后的代码归档到 GitHub。 |
| 7 | 2026-07-09 | 导师、Centre for Cities | 项目安排检查：确认主要在线开展，并安排次周五同步。 |
| 8 | 2026-07-14 | 导师 | 汇报未经微调的发布模型在英国影像上迁移不佳，尤其难以区分仓储场院、货车停车与普通停车场。权衡使用自己的标注重新训练和继续后处理，并指出计算与时间只允许在很小区域内重新训练。 |
| 9 | 2026-07-28 | 导师 | 建议不要继续追求计算机视觉准确率。论文重新聚焦于美国训练模型为何难以迁移到英国城市形态、OpenStreetMap 存在哪些空缺，以及所识别面积对规划和住房政策意味着什么。 |
| 10 | 2026-08-11 | Clara、Esra | 在 8 月 20 日截止日期临近而写作尚未开始的情况下，决定停止运行模型，先起草研究问题、动机与文献综述；模型在不同国家和城市语境中的局限将作为实质性分析章节，而非当作失败处理。 |

> **段落审读**
> - **逻辑用途：** 以会议记录重建研究决策过程
> - **核对状态：** ✅ 已核对：会议日期与讨论摘要已和英文研究日志逐项对应；表中的 8 月 20 日只是当时确认的提交截止日期。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：1, 04, 27, 2, 05, 8, 20；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 涉及研究范围改变的决定可补充对应会议纪要链接。

## E.3 项目时间线

### 第 1 阶段——界定范围与获取数据（4 月 27 日–5 月 14 日）

**英文原稿**

The topic was agreed at the kick-off meeting: applying a published deep-learning segmentation model to detect off-street surface parking in a UK city, with the policy aim of identifying land that is not allocated in local development plans but has housing potential. Aerial imagery was ordered and downloaded from Digimap during this period. No code was written; the meeting of 5 May records that data had been obtained but no model runs attempted, with taught-module coursework and an examination on 14 May taking priority.

**中文翻译**

启动会议确定了主题：把已发表的深度学习分割模型应用于英国城市，检测路外地面停车；政策目标是识别未纳入地方开发规划但具有住房潜力的土地。期间从 Digimap 订购并下载航空影像。尚未编写代码；5 月 5 日会议记录表明数据已经取得、但模型还没有运行，因为当时优先完成课程作业及 5 月 14 日考试。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：5, 14；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

### 第 2 阶段——复现发布流程与首次英国迁移（5 月 15–29 日）

**英文原稿**

*Nine commits.*

**中文翻译**

*九次提交。*

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

The repository was initialised on 15 May with the published parking-lot mapping tool of Qiam et al. (2025), its trained checkpoint, and the core literature. The first obstacle was format rather than method: the published tool expects georeferenced GeoTIFF input, whereas Digimap delivers JPEG images with separate world and metadata files. `make_uk_geotiff.py` was written to convert them. The first inference was run on a single Edinburgh tile (`nt2774`).

**中文翻译**

5 月 15 日，以 Qiam et al.（2025）发布的停车场制图工具、训练检查点和核心文献初始化仓库。第一个障碍是格式而非方法：发布工具要求输入有地理配准的 GeoTIFF，而 Digimap 提供 JPEG 影像及分开的世界文件和元数据。为此编写 `make_uk_geotiff.py` 进行转换。第一次推理在一个爱丁堡图块（`nt2774`）上运行。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L24](#l24) Qiam, Devunuri and Lehe (2025)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：5, 15, 774；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

On 29 May the study area was moved to Leeds and nine tiles (`se2526`–`se2728`, a 3×3 block) were added and put through batch inference. Three defects surfaced and were fixed the same day: malformed output polygons, an incorrect coordinate reference, and a thread-pool worker limit that stalled batch runs.

**中文翻译**

5 月 29 日，研究区转移至利兹，加入九个图块（`se2526`–`se2728`，3×3 区块）并进行批量推理。同日发现并修复三项缺陷：输出多边形畸形、坐标参考系错误、线程池工作线程限制导致批处理停滞。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：5, 29, 526, 728, 3；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

The first post-processing was added at the end of the same day: minimum-area filters at 500, 1,000 and 2,500 m², merging of per-tile outputs into a single layer, and removal of predictions falling on OpenStreetMap buildings and roads. Agreement against OSM parking polygons was computed at each filter threshold, giving the first quantitative sense of how the model performed on UK imagery.

**中文翻译**

同日末加入第一版后处理：设置 500、1,000 和 2,500 m² 的最小面积筛选；把各图块输出合并为单一图层；删除落在 OpenStreetMap 建筑和道路上的预测。随后在每个筛选阈值下计算与 OSM 停车多边形的一致程度，首次定量了解模型在英国影像上的表现。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：500, 1,000, 2,500；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

### 第 3 阶段——验证基础设施（6 月 2–25 日）

**英文原稿**

*Six commits.*

**中文翻译**

*六次提交。*

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

The 2 June meeting established the central problem: recall was high but precision was low, with the flat roofs of large supermarkets the characteristic false positive. Reviewing outputs with supervisors on 16 June added a second systematic confusion — industrial and logistics yards, where vehicles cluster but redevelopment for housing is not realistic — and it became clear that agreement with OSM was not a sufficient basis for evaluation, since OSM parking is itself incomplete.

**中文翻译**

6 月 2 日会议确立核心问题：召回率高但精确率低，大型超市的平屋顶是典型 FP。6 月 16 日与导师共同审查输出时又发现第二种系统混淆——工业与物流场院；这些区域车辆聚集，但用于住房再开发并不现实。此时也明确，只与 OSM 比较不足以作为评估基础，因为 OSM 停车数据本身并不完整。

> **段落审读**
> - **逻辑用途：** 报告或解释支撑结论的实证量
> - **核对状态：** ✅ 已核对：数字已按正文表格、结果 CSV 与面积恒等式交叉核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：6, 2, 16；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 注明 OSM 获取日期、要素标签范围和完整性口径。

**英文原稿**

Work therefore turned to manual ground truth. A validation boundary was defined on 16 June, and on 23 June `calculate_manual_agreement.py` and a first manually annotated validation layer were committed, producing agreement metrics against manual labels rather than against OSM.

**中文翻译**

工作因此转向人工地面真值。6 月 16 日确定验证边界；6 月 23 日提交 `calculate_manual_agreement.py` 和第一版人工标注验证图层，从而开始计算相对于人工标签而非 OSM 的一致性指标。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：6, 16, 23；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

Three pieces of infrastructure were settled on 25 June: aerial data was moved onto Git LFS, OpenStreetMap retrieval was switched to the Overpass API in `post_processing_uk.py`, and Colab outputs were redirected to Drive so that results survived session resets.

**中文翻译**

6 月 25 日确定三项基础设施：航空数据转移到 Git LFS；`post_processing_uk.py` 中的 OpenStreetMap 获取方式改为 Overpass API；Colab 输出改存 Drive，使结果在会话重置后仍能保留。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：6, 25；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

### 第 4 阶段——人工标注与研究转向（6 月 26 日–8 月 2 日）

**英文原稿**

*No commits. Dates from annotation files.*

**中文翻译**

*无提交；日期来自标注文件。*

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

This is the longest stretch of the project without a commit, and the work in it was annotation rather than code. The sequence is recorded in the annotation files: the annotation frame and sampling grid were built on 26 June (`leeds_boundry.gpkg`, `leeds_grid.gpkg`); the proposal was revised on 30 June; the validation annotation set was completed on 19 July (`leeds_manual_validation.gpkg`); the annotation rules were written down on 21 July (`Rules.md`); and the main annotation set was completed on 28 July (`leeds_manual.gpkg`), together with `validate_removal_vs_manual.py`, which tests the OSM-removal step against the manual labels.

**中文翻译**

这是项目中没有提交记录的最长一段时间，期间开展的是标注而非编码。标注文件记录了过程：6 月 26 日建立标注范围与抽样网格（`leeds_boundry.gpkg`、`leeds_grid.gpkg`）；6 月 30 日修订研究计划；7 月 19 日完成验证标注集（`leeds_manual_validation.gpkg`）；7 月 21 日写下标注规则（`Rules.md`）；7 月 28 日完成主标注集（`leeds_manual.gpkg`），并完成 `validate_removal_vs_manual.py`，用于以人工标签检验 OSM 删除步骤。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：6, 26, 30, 7, 19, 21, 28；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

Writing the rules down was the more consequential of these steps. Because the model is validated against these labels, the labels have to match the definition the model was trained on, so the rules were aligned to Qiam et al. (2025) — the same off-street surface target, pavement-edge boundaries, rooftop parking included only where the surface is visible, and no minimum-size threshold — with any deviation recorded so that errors caused by definition differences could be separated from true model errors.

**中文翻译**

把规则写下来是其中影响更深远的一步。因为模型以这些标签为参照进行验证，标签必须匹配模型训练时的定义，所以规则与 Qiam et al.（2025）保持一致——相同的路外地面停车对象、铺装边缘边界、只有停车面可见时才纳入屋顶停车，以及不设最小面积阈值——并记录所有偏离，以便把定义差异造成的错误与真正模型错误分开。

> **段落审读**
> - **逻辑用途：** 用既有研究或政策为本段推论建立依据
> - **核对状态：** ✅ 已核对：相关引文已在 `citation_audit.md` 中对照 32 份本地原文逐条核实。
> - **文献原句：** 见 [L24](#l24) Qiam, Devunuri and Lehe (2025)；短引文、定位与本地 PDF 均列于上方索引。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 在关键强论断后保留精确页码、段号或表号。

**英文原稿**

Three meetings fell in this window. On 14 July I reported that the un-finetuned model transferred poorly to UK imagery and discussed whether to retrain on my own annotations or continue with post-processing; compute and time meant retraining could only cover a very small area. On 28 July the supervisors advised against pursuing further accuracy and redirected the dissertation towards the question of why the model fails in the UK context and what that implies for planning.

**中文翻译**

该阶段包括三次会议。7 月 14 日，我汇报未经微调的模型迁移到英国影像后表现不佳，并讨论是根据自己的标注重新训练，还是继续后处理；计算与时间意味着重新训练只能覆盖很小区域。7 月 28 日，导师建议不要再追求提高准确率，并把论文转向模型为何在英国语境下失败及其规划含义。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：7, 14, 28；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

### 第 5 阶段——全城运行与误差分析（8 月 3–10 日）

**英文原稿**

*Four commits.*

**中文翻译**

*四次提交。*

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

With the redirection settled, inference was extended from the nine-tile test block to the full Leeds study area on 3 August — 100 tiles, 413 output files — and the emphasis shifted from improving predictions to characterising their errors. False-positive analysis was added the same day, using OS Open Greenspace among the reference layers, alongside the results of validating the removal step against manual labels.

**中文翻译**

研究转向确定后，8 月 3 日把推理从九图块测试区扩展至完整利兹研究区——100 个图块、413 个输出文件——重点也从改善预测转向刻画错误。同日加入 FP 分析，参考图层包括 OS Open Greenspace，并加入以人工标签检验删除步骤的结果。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：8, 3, 100, 413；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

On 5 August three analyses were added: false negatives broken down by class, an ablation of the post-processing steps, and accuracy as a function of distance from the city centre — the last of these addressing the supervisors' question of whether the model fails differently in the centre and the suburbs. A stratified sampling design for error inspection followed on 7 August, and on 10 August 142 image chips were cut for visual inspection, together with a full mosaic and a parking-extent map.

**中文翻译**

8 月 5 日新增三项分析：按类别分解 FN、对后处理步骤作消融、分析准确率随距市中心距离的变化——最后一项回应导师关于模型在中心和郊区是否以不同方式失败的问题。8 月 7 日设计误差检查的分层抽样；8 月 10 日切出 142 个图像样本供人工检查，同时生成完整镶嵌图和停车范围图。

> **段落审读**
> - **逻辑用途：** 记录全城误差分析的形成过程
> - **核对状态：** ✅ 已核对：日志原写 143 系笔误，已改为 142。抽样设计（`sampling_strata.csv` 九层合计）、`sampling_worksheet.csv`、`chips/index.csv` 与实际切片文件均为 142，且 worksheet 与切片索引的 sample_id 完全一一对应，无样本被排除。git 历史显示配额为 145（8/5）→142（8/7），从未出现 143。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：8, 5, 7, 10, 142；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 日志可补一句说明 8 月 7 日配额由 145 调整为 142 的原因（fn_other 总体重算，且 1,000 m² 以上一层改为全查），使样本量的来龙去脉可追溯。

### 第 6 阶段——校准、微调与开始写作（8 月 11–12 日）

**英文原稿**

*Seven commits.*

**中文翻译**

*七次提交。*

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

**英文原稿**

The morning of 11 August was spent on a calibration-transfer analysis and a co-registration check, and on generating the first methods figures. A Colab fine-tuning notebook was then built and iterated through six commits in a single afternoon, using the manual annotations and grid produced in Phase 4.

**中文翻译**

8 月 11 日上午完成校准迁移分析、配准检查和第一批方法图。随后在一个下午的六次提交中建立并迭代 Colab 微调笔记本，使用第 4 阶段产生的人工标注和网格。

> **段落审读**
> - **逻辑用途：** 交代研究设计或处理步骤，使结果可解释和可复现
> - **核对状态：** ✅ 已核对：已与项目协议、脚本、日志和文件路径核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：8, 11, 4；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 补充关键参数、随机种子或失败判据，使第三方能独立复现。

**英文原稿**

The meeting later that day found that no writing had begun, and it was agreed to stop modelling and draft the research questions, motivation and literature review first. `02_background.md`, the first dissertation chapter in the repository, was committed the following day, 12 August, along with the results figures.

**中文翻译**

当天稍后的会议发现写作尚未开始，因此决定停止建模，先起草研究问题、动机和文献综述。仓库中的第一章 `02_background.md` 于次日 8 月 12 日提交，同时提交结果图。

> **段落审读**
> - **逻辑用途：** 推进本节论证并连接相邻段落
> - **核对状态：** ✅ 已核对：所述内容已与当前英文稿及项目内证据链核对。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：02, 8, 12；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 把本段核心判断写得更可检验，并在需要处补来源或不确定性。

### 第 7 阶段——写作与定向微调（8 月 13–20 日）

**英文原稿**

*Ten commits to date.*

**中文翻译**

*截至记录时十次提交。*

> **段落审读**
> - **逻辑用途：** 记录写作与补充实验的收尾阶段
> - **核对状态：** 🟨 需人工复核：以仓库提交为依据，但 8 月 20 日是阶段终点而非当前已发生日期。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 提交后更新最终提交数和实际完成日期。

**英文原稿**

The remaining chapters — abstract, introduction, results, discussion and conclusion — and the reference list were committed on 16 August. A targeted fine-tuning experiment was set up and iterated the same day, with the calibration-transfer error table added and the methods and results figures regenerated. The remaining time before submission is given to the front matter, reducing the manuscript to the word limit, and proofreading.

**中文翻译**

其余章节——摘要、引言、结果、讨论、结论——以及参考文献表于 8 月 16 日提交。同日设置并迭代定向微调实验，加入校准迁移误差表，并重新生成方法与结果图。提交前的剩余时间将用于完成前置材料、把论文压缩到字数限制并校对。

> **段落审读**
> - **逻辑用途：** 记录写作与补充实验的收尾阶段
> - **核对状态：** 🟨 需人工复核：以仓库提交为依据，但 8 月 20 日是阶段终点而非当前已发生日期。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：8, 16；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 提交后更新最终提交数和实际完成日期。

## E.4 反思

**英文原稿**

The log records a project that changed shape twice. It began as an attempt to apply a published US-trained model to UK imagery; when that transferred poorly, it became an attempt to fix the predictions through post-processing; and after the meeting of 28 July it became an analysis of why the transfer fails and what the result implies for planning policy. The final framing treats the model's limitations as the object of study rather than an obstacle to it, which is both more honest about what the evidence supports and better matched to a dissertation in urban research.

**中文翻译**

日志记录了项目两次改变形态。它起初试图把已发表的美国训练模型应用于英国影像；迁移不佳后，转而尝试通过后处理修复预测；7 月 28 日会议后，最终成为对迁移为何失败及其规划政策含义的分析。最终框架把模型局限当作研究对象，而非研究障碍；这既更诚实地贴合证据所支持的范围，也更符合一篇城市研究论文的定位。

> **段落审读**
> - **逻辑用途：** 解释项目决策、产出或转向的时间关系
> - **核对状态：** 🟨 需人工复核：日期取自会议记录、提交历史或标注文件，且已注明提交可能滞后。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：7, 28；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 为关键里程碑附 commit hash 或文件修改时间。

**英文原稿**

The single stretch without commits, from 26 June to 2 August, was the period of manual annotation. It produced no code, but it produced the ground truth on which every accuracy figure in this dissertation rests, and the rule set that makes those figures comparable to the study the model came from. The clearest effect of supervision is visible in the version history on 11–12 August: modelling stopped, and the first chapter entered the repository the following day.

**中文翻译**

6 月 26 日至 8 月 2 日是唯一没有提交的时段，也是人工标注阶段。它没有产生代码，却产生了全文所有准确率数字赖以成立的地面真值，以及让这些数字能与模型来源研究比较的规则集。指导工作的最清楚影响可见于 8 月 11–12 日的版本历史：建模停止，次日第一章进入仓库。

> **段落审读**
> - **逻辑用途：** 解释项目决策、产出或转向的时间关系
> - **核对状态：** 🟨 需人工复核：日期取自会议记录、提交历史或标注文件，且已注明提交可能滞后。
> - **文献原句：** 本段无外部引文；若为作者推论或实证结果，则以下列原始数据／文本依据核对。
> - **原始数据／文本依据：** 指导会议录音／纪要；项目仓库提交历史；QGIS 标注文件修改日期；本段核对值：6, 26, 8, 2, 11, 12；译文对应位置：`12_appendix_e_research_log.md`（仅作定位，不作为引文证据）
> - **可加强：** 为关键里程碑附 commit hash 或文件修改时间。
