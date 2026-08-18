# 文献引用逐条核对报告

**核对日期**：2026-08-17
**范围**：`07_references.md` 全部 32 条文献 × 正文 58 个含引用的句子（第一轮，2026-08-17）；**附录 08–12 于本报告完成后才写出，未在第一轮范围内，已于第二轮（2026-08-18，见第八节）补核**
**方法**：用 ghostscript 从 `resource/`（及 `Parking/literature/`）的原文 PDF 抽取全文，将正文中归给每条文献的论断与原文逐一比对
**覆盖率**：32/32 条文献均找到对应 PDF 并完成抽取，**无一条无法核对**

---

## 一、总体结论

| 项目 | 结果 |
|---|---|
| 文献条目 | 32 |
| 有对应原文 PDF | 32 / 32 |
| 含引用的正文句子 | 58 |
| 论断与原文一致 | 55（第一轮）→ 第二轮复核后修正 1 条误判，详见第八节 |
| **需修改** | **1（[34] 模型配置的出处）— 已于 2026-08-17 修正**；第二轮另发现 3 处，已于 2026-08-18 修正 |
| 措辞不够精确、建议微调 | 2 — 已于 2026-08-17 修正 |
| 参考文献表与正文互相对应 | 无遗漏、无多余 |

> **修改状态（2026-08-17）**：第二、三节所列四处均已应用到正文，详见本文件第七节。

**未发现任何虚构文献。**多处直接引语（Bates & Leibling 的 p.99 原句、NPPF 的 para 124 原句、Lange et al. 的 "located just beyond the city centre"）与原文逐字一致。

> **⚠️ 本段结论已于 2026-08-18 部分推翻。** 第一轮原写「没有发现任何张冠李戴或原文不支持的论断」；第二轮在附录 A 发现一处张冠李戴（APKLOT 归属），并复核出第五节一条被误判为 ✅ 的过度引用（Sehra）。详见第八节。

---

## 二、必须修改：[34] 模型配置的出处

**正文原句**（`03_methodology.md`）：

> The model is the SegFormer (Xie et al., 2021) parking-lot segmentation network released by Qiam, Devunuri and Lehe (2025), a **B5 configuration** whose backbone was initialised from **Cityscapes weights** and fine-tuned by those authors on their parking dataset.

**问题**：这句话在事实上是对的，但**无法从所引的论文中得到验证**。

- Qiam et al. (2025) 论文的结果表里，SegFormer 那一行写的是 **`SegFormer MiT-B0 ADE20K`**——即 B0 配置、ADE20K 预训练权重。
- 论文中 **Cityscapes** 只出现两处：一处属于 **另一个模型** 的表行（`Mask2Former Swin-L CityScapes`），另一处是参考文献里 Cityscapes 数据集的著录。
- 论文全文**没有出现 "B5"**。

**但你实际跑的模型确实是 B5 + Cityscapes**，依据在代码里：

```
parking-lot-mapping-tool/inference.py:93
    "nvidia/segformer-b5-finetuned-cityscapes-1024-1024"
```

`parking-lot-mapping-tool/README.md` 也写明用的是 "SegFormer-large" 模型，权重托管在 `UTEL-UIUC/SegFormer-large-parking`。

**结论**：你描述的是**发布出来的工具/权重**（这是对的，因为那才是你实际运行的东西），但把它归给了**论文**，而论文里跑的基准是另一个配置。考官若去查论文会对不上。

**建议改法**：把出处拆开，明确指向代码仓库/模型卡，例如——

> …the parking-lot segmentation network released by Qiam, Devunuri and Lehe (2025). The released implementation builds on `nvidia/segformer-b5-finetuned-cityscapes-1024-1024` (UTEL-UIUC, 2025), a B5 configuration initialised from Cityscapes weights; note that the paper's own benchmark table reports a MiT-B0 configuration pretrained on ADE20K, so the released artefact and the paper's experiments differ in configuration.

顺带一提：这个差异本身**对你的论文是有利的**。你的核心论点是"发布的模型迁移到英国表现不佳"，而"发布的权重与论文基准并非同一配置"正是评估可复现性时值得写进 limitations 的一笔。

---

## 三、建议微调的两处措辞

### 1. [45] `05_discussion.md` — "roughly 60% IoU" 偏低

正文：「Maggiori et al. (2017) judged a network reaching **roughly 60% IoU** on building footprints in cities it had never seen to generalise satisfactorily」

原文 Table 2 实际值：MLP 整体 IoU = **64.67**，分城市 51.50（Kitsap Co.）– 72.13（Vienna）。

论断方向没错（确实是建筑物类、确实是未见过的城市），但 64.67 说成 "roughly 60%" 偏低。改成 "roughly 65%" 或 "between 52% and 72% across cities, 64.7% overall" 更稳，也更有利于你自己的对比。

### 2. [54] `05_discussion.md` — 伦敦调查的年代

正文：「the British alternative of ground survey has not been repeated at that scale since **the London exercise of the early 2000s**」

Bates & Leibling 原文一律称其为 **"the 1999 study"**（报告为 MVA 2000，2005 年以 50 个方格做过部分复查）。"early 2000s" 不算错（出版年是 2000），但与原文口径不一致。建议改为 "the London exercise of 1999" 或 "of 1999–2000"。

### 3. 附带一处小的引用精度问题

[10] `02_background.md` 一句话里放了两个来源，但只标了一个段号：

> …instructs authorities to make "as much use as possible of previously-developed or 'brownfield' land" **(MHCLG, 2024, para. 124)** and to give substantial weight to brownfield development within settlements.

前半句的直接引语确在 **para 124** ✓；后半句"give substantial weight"出自 **para 125(c)**。建议写成 `(MHCLG, 2024, paras 124–125)` 或分别标注。

---

## 四、一条重要的正面确认

摘要里这句我此前标记为"需你自行核实"的强论断，**已核实成立**：

> national planning policy names car parks **explicitly** among the under-utilised land authorities should bring forward

NPPF (December 2024) **para 125(d)** 原文：

> d) promote and support the development of under-utilised land and buildings, especially if this would help to meet identified needs for housing where land supply is constrained and available sites could be used more effectively (for example converting space above shops, and building on or above service yards, **car parks**, lock-ups and railway infrastructure)

"explicitly" 一词站得住。**建议在正文中把 para 125(d) 的段号明确标出**——这是全篇的政策支点，给出确切段号只有好处。

---

## 五、逐条核对明细

✅ = 论断与原文一致

| # | 文献 | 正文论断 | 核对结果 |
|---|---|---|---|
| 01, 09, 56 | Shoup (2005) | 最低停车配建要求；停车应作为土地利用问题 | ✅ |
| 02, 11, 55 | Lange et al. (2026) | 五大城市密度差距最大；"just beyond the city centre"；战后街区密度低至 40% | ✅ 逐字一致 |
| 03, 13, 54 | Scharnhorst (2018) | 五个美国城市清单（New York / Philadelphia / Seattle / Des Moines / Jackson） | ✅ 五城全对 |
| 03, 14, 54 | Hoehne et al. (2019) | 凤凰城 2017 年 1,220 万车位 vs 286 万登记车辆 | ✅ 逐字一致 |
| 04, 15, 16, 33, 53 | Bates & Leibling (2012) | p.99 直接引语；伦敦 300 个 500 m 方格抽样、2005 年部分复查、680 万车位 | ✅ 直接引语逐字一致 |
| 05, 22, 32 | Qiam et al. (2025) | 发布了 pipeline 与 NIR 增强数据集；标注规则依据 | ✅ |
| 34 | Qiam et al. (2025) | B5 配置 / Cityscapes 权重 | ⚠️ **见第二节** |
| 06, 24, 50 | Maggiori et al. (2017) | Inria 基准跨城市测试；分城市报告 IoU | ✅ |
| 45 | Maggiori et al. (2017) | "roughly 60% IoU" | 🟡 实为 64.67，见第三节 |
| 07, 19, 46 | Xie et al. (2021) | SegFormer 无位置编码；zero-shot 鲁棒性针对图像退化 | ✅ |
| 08, 49 | Devillers et al. (2007) | internal / external quality 之分；fitness for use | ✅ |
| 10 | MHCLG (2024) | NPPF para 124 直接引语 | ✅ 逐字一致（段号见第三节） |
| 12 | Habermehl & McFarlane (2025) | 密度作为 hard / gentle 的辩证 | ✅ |
| 12 | Livingstone et al. (2021) | 伦敦密集化政策的实际效果与代价 | ✅ |
| 17, 48 | Jiao (2015) | 城市土地密度随距市中心距离呈规律函数 | ✅ |
| 18 | Lv et al. (2023) | 编码器–解码器架构主导 | ✅ |
| 20 | Berry et al. (2019) | 相邻停车场粘连；associative embeddings 实例分割 | ✅ |
| 21, 45；附录 A.7、A.8 | Hurst-Tarrab et al. (2020) | APKLOT 数据集；IoU 超过 50%；APKLOT 的纳入／排除规则 | ✅ 摘要原文 "more than 50% IoU"；§3.1 "we also propose APKLOT"；§3.2 列出排除项 |
| 23, 47, 51 | Lyu et al. (2025) | 域偏移综述；传感器/分辨率/光照/对象差异 | ✅ |
| 25, 51 | Hong et al. (2023) | 单城市成功、跨城市遇瓶颈 | ✅ |
| 26 | Goodchild (2007) | 提出 volunteered geographic information | ✅ 原文 "I term this volunteered geographic information (VGI)" |
| 27, 57 | Haklay (2010) | 位置精度尚可、完整度因地而异、贡献者多则更好 | ✅ |
| 28, 57 | Sehra et al. (2013) | ~~城市比乡村完整~~ → 完整度随地点与要素类型变化，**方向不一致** | ❌→✅ 第一轮误判（见第八节 #1）；原文记载美国案例「showed an opposite tendency」，正文已于 2026-08-18 改写 |
| 29, 57 | Zhou et al. (2022) | 土地利用类别间精度/完整度差异大 | ✅ |
| 30 | Openshaw (1984) | 可变面元问题 | ✅ |
| 35, 58 | Foody (2002) | 面积法对照独立参照；参照数据质量构成上界 | ✅ |
| 36 | Stehman & Wickham (2011); Stehman & Foody (2019) | 评估单元本身是设计选择，无普适正确解 | ✅ |
| 37 | Foody (2005) | 局部精度宜作全局精度的补充而非替代 | ✅ 原文用词即 "accompaniment" |
| 38 | Csurka et al. (2013) | 面积型度量无法区分边界误差与位置错误 | ✅ |
| 39, 40 | Cheng et al. (2021) | Boundary IoU 对大目标边界更敏感；带宽敏感性是已知性质 | ✅ 原文 "significantly more sensitive… for large objects" |
| 41, 43, 52 | Olofsson et al. (2014) | 抽样设计/响应设计/分析三段式；面积校正 | ✅ |
| 42 | Cochran (1977) | 分层比率估计量 | ✅ |
| 44 | Roberts et al. (2017) | 空间依赖下随机切分低估误差，应按块留出 | ✅ |

---

## 六、说明

- 抽取用 ghostscript `txtwrite`。双栏排版会在断行/断栏处产生连字符与空格丢失，核对时已做去连字符、去空格归一化处理后再比对，因此匹配结果不受排版影响。
- `07_references.md` 表头原有一行「32 条已全部对照原文核实」的说明——本次核对**独立复核了这一说明**，结论是它基本成立，但第二、三节的三处需要按上述修改。

---

## 七、已应用的修改（2026-08-17）

| 位置 | 原文 | 改后 |
|---|---|---|
| `03_methodology.md:41` | …released by Qiam, Devunuri and Lehe (2025), **a B5 configuration whose backbone was initialised from Cityscapes weights** and fine-tuned by those authors… | …released by Qiam, Devunuri and Lehe (2025). **The released checkpoint is** a B5 configuration whose backbone was initialised from Cityscapes weights and fine-tuned by those authors on their parking dataset, **as documented in the released model card and repository**. |
| `05_discussion.md:16` | roughly **60%** IoU | roughly **65%** IoU |
| `05_discussion.md:66` | the London exercise of **the early 2000s** | the London exercise of **1999** |
| `02_background.md:18` | (MHCLG, 2024, **para. 124**) | (MHCLG, 2024, **paras 124–125**) |
| `03_methodology_中文详解.md:133` | 同步更新引述的中文译文 | 同上 |

**说明**：模型配置一处仅改出处，指向已发布的模型卡与代码仓库（依据 `parking-lot-mapping-tool/inference.py:93` 的 `nvidia/segformer-b5-finetuned-cityscapes-1024-1024` 与 `README.md` 所载 Hugging Face 权重 `UTEL-UIUC/SegFormer-large-parking`），措辞与 `02_background.md:52` 既有写法保持一致。未在正文中点明论文基准表与发布权重的配置差异。

**未新增参考文献条目**——改后的句子以「the released model card and repository」作描述性溯源，与第 2 章既有写法一致，不引入新的著录信息。若日后希望为权重单列一条正式文献，需先确认模型卡的发布年份。

### 顺带核实（本次一并完成，无需修改）

| 位置 | 论断 | 结果 |
|---|---|---|
| `02_background.md:44` | SegFormer 的 zero-shot 鲁棒性在 **Cityscapes-C** 上验证，含 noise、blur、weather、digital 四类退化 | ✅ Xie et al. (2021) 原文逐字一致（"16 types of algorithmically generated corruptions from noise, blur, weather and digital categories"） |
| `02_background.md:52` | 已发布检查点为 SegFormer-B5 / Cityscapes 权重，「as documented in the released model card and repository」 | ✅ 出处本已正确，无需改动 |

---

## 八、第二轮核对（2026-08-18）

**触发**：附录 `08`–`12` 于 2026-08-17 晚间才写出，不在第一轮范围内。本轮补核附录，并顺带复核第五节中一条被误判的条目。

| # | 位置 | 问题 | 性质 | 处理 |
|---|---|---|---|---|
| 1 | `02_background.md:85` | 引 Sehra et al. (2013) 断言「OSM 在城市比乡村完整」，但该综述记载美国案例方向相反 | 过度引用：原文**部分反对**所引论断 | 已改写为「方向不一致」 |
| 2 | `08_appendix_a_annotation_protocol.md:58` 及 A.8 | APKLOT 归给 Yin et al. (2022)，实为 Hurst-Tarrab et al. (2020) 所建 | **张冠李戴**，且与 `02_background.md:48` 自相矛盾 | 已改为 Hurst-Tarrab et al. (2020)；两篇现并列引用（见下「#2 补充」） |
| 3 | `12_appendix_e_research_log.md:68` | 日志写「143 个图像切片」，各处数据均为 142 | 数字笔误 | 已改为 142 |

### #1 Sehra — 原文证据

综述第 18 页论美国案例：

> In comparison to the results for Germany or England, the discrepancies between the rural and urban areas in the USA **showed an opposite tendency**. In Florida, the rural data was, in parts, even **more complete** than that of the proprietary datasets.

该综述双向都记录：德、英一个方向，美国相反。第一轮把它记为 ✅「城市比乡村完整」，等于取其一半。改后正文只主张「完整度随地点与要素类型变化，方向不一致」，与原文完全对应。

`05_discussion.md:72` 处未改：该句为 "confirm the pattern by area and by feature type"，不指定方向，本就成立。

### #2 APKLOT — 原文证据

Hurst-Tarrab et al. (2020), *Applied Sciences* 10(15), 5364：

> Given the lack of a suitable dataset, **we also propose APKLOT**, a dataset of roughly 7000 polygons for segmenting parking blocks from the satellite perspective and from the camera perspective.

其 §3.1–3.2 亦明列纳入／排除规则（"Complete parking blocks were annotated i.e., we are not considering the following: Parking spots outside the parking lot…"；"Edge structures that do not correspond to parking spots and traffic lanes can be safely excluded"），因此附录原句「uses similar include and exclude rules」在改换出处后**内容仍有据**，非把无法核实的论断转挂他人。

Yin et al. (2022)（Yifang Yin 等，WACV 2022，doi:10.1109/WACV51458.2022.00146）确为真实论文，但其数据集是 **Grab-Pklot**，非 APKLOT。

#### #2 补充（同日，两篇并列）

原件已取得并置于 `resource/`，故改为两篇并列引用，并在正文中明写目标差异：

| | APKLOT (Hurst-Tarrab et al., 2020) | Grab-Pklot (Yin et al., 2022) |
|---|---|---|
| 标注单元 | parking **block**（车位阵列，不含通道） | **carpark**（整个停车场） |
| 规模 | 500 影像 / 7,000+ 多边形 | 1,344 卫星影像（新加坡） |
| 视角 | 卫星 + 监控摄像头 | 卫星（含道路／建筑上下文通道） |
| 与本研究目标（含内部通道）的关系 | 单元较窄 | **更接近** |

正文改后不再笼统称「similar include and exclude rules」，而是分别陈述：APKLOT 同样以显式纳入／排除清单界定目标、但单元为区块；Grab-Pklot 标注整个停车场、为更接近的类比。此举同时兑现 A.7 既有承诺「Any point at which these rules differ from the source protocol is noted above」。

**核对限度（已解除，2026-08-18）**：Yin et al. (2022) 的正文其后经 Poppler 抽出全部十页（约 58 KB 文字），论断已逐条对照原文核实：p. 1372 “the focus of this paper is to detect the location and the polygon of the parking lot”；§3 “it can be modeled as a binary semantic segmentation problem”；Table 1 将 APKLOT 目标列为 `Parking Block`、Grab-Pklot 列为 `Parking Lot`；§4.2.2 记述候选生成与人工修正流程，最终 2,883 个停车场多边形、1,344 组影像—掩膜。**Yin 全文并无 APKLOT §3.1–3.2 那样逐项的纳入／排除清单**，因此正文未用该文支撑「规则清单」一说，此分工经原文确认成立。

### #3 研究日志 143 — 数据证据

| 证据来源 | 数值 |
|---|---|
| `analysis/sampling_strata.csv` 九层 `n_sampled` 合计 | 142 |
| `analysis/sampling_worksheet.csv` 行数 | 142 |
| `analysis/chips/index.csv` 行数 | 142 |
| `analysis/chips/` 下实际切片文件数 | 142 |
| worksheet 与切片索引的 `sample_id` 差集 | 两个方向均为空 |

git 历史显示配额为 145（`761a04a`，8/5）→ 142（`61076d9`，8/7，`fn_other` 总体重算、1,000 m² 以上一层改为全查），**从未出现过 143**。切片在 8/10 生成，晚于 8/7 的修订，故只可能是 142。**无样本被排除，不存在需要解释的剔除。**

### 本轮同步更新的文件

`02_background.md`、`07_references.md`（新增 Yin et al. 2022，共 33 条）、`08_appendix_a_annotation_protocol.md`、`12_appendix_e_research_log.md`、`dissertation_zh_translation.md`（英文原稿段、中文译段、证据索引 L27、L33 先删后依新证据恢复、锚点补指 L14 与 L33、5 处段落审读状态、17 处「原文待补」清除）、本报告。
