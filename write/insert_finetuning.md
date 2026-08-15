# 微调实验插入稿（自包含版）

> **本文件不改动任何现有 md。** 所有改动都以「原文整段 → 改后整段」成对列出，整段复制粘贴替换即可，不需要在原文里做零碎追加。
> 共 6 处必改 + 3 处可选。净增约 **+733 词**（正文现约 12,670，上限 12,000）——见文末「字数账」。
> 数值来自 `fine_tuning_experiment.md`，已与 `make_split.py` / `finetune.py` / `evaluate.py` 核对一致。

## 改动清单

| # | 文件 | 行 | 性质 | 净增 |
|---|---|---:|---|---:|
| 1 | `02_background.md` | 64 | 段末加一句 | +20 |
| 2 | `03_methodology.md` | 41 | 段末加一句 | +38 |
| 3 | `04_results.md` | 10 | 章首导语加一句 | +15 |
| 4 | `04_results.md` | 末尾 | **新增 §4.8** | +400 |
| 5 | `05_discussion.md` | 50/52 之间 | 新增一段 | +155 |
| 6 | `05_discussion.md` | 86 | 末句替换 | +55 |
| 7 | `06_conclusion.md` | 18 | 末句替换 | +50 |
| A | `01_introduction.md` | 37 | 可选括注 | +12 |
| B | `00_abstract.md` | 10 | 可选括注（建议不改） | +8 |
| C | `04_results.md` | §4.8 末 | 可选附录指引 | +28 |

---

# 1 — `02_background.md` 行 64（§2.5）

### 原文

> Most of that literature is concerned with *correcting* domain shift through adaptation. That option is not open to the user this study has in mind. Adaptation presupposes either labelled data in the target domain or substantial engineering to exploit unlabelled data, and a planner who wants to know how much land in their city is car park has neither; their realistic option is to run the published checkpoint on the imagery they hold. The uncorrected output is therefore the object of study here, and the question is what it can still be trusted to do.

### 改后

> Most of that literature is concerned with *correcting* domain shift through adaptation. That option is not open to the user this study has in mind. Adaptation presupposes either labelled data in the target domain or substantial engineering to exploit unlabelled data, and a planner who wants to know how much land in their city is car park has neither; their realistic option is to run the published checkpoint on the imagery they hold. The uncorrected output is therefore the object of study here, and the question is what it can still be trusted to do. What such adaptation would buy, in the case where the labels do happen to exist, is tested as a bounded supplement in §4.8.

---

# 2 — `03_methodology.md` 行 41（§3.3）

### 原文

> The model is the SegFormer (Xie et al., 2021) parking-lot segmentation network released by Qiam, Devunuri and Lehe (2025), a B5 configuration whose backbone was initialised from Cityscapes weights and fine-tuned by those authors on their parking dataset. The published checkpoint is used exactly as released. **No UK imagery was used to adjust the weights**, so what is measured here is zero-shot transfer: the accuracy a UK user would obtain by taking the model off the shelf.

### 改后

> The model is the SegFormer (Xie et al., 2021) parking-lot segmentation network released by Qiam, Devunuri and Lehe (2025), a B5 configuration whose backbone was initialised from Cityscapes weights and fine-tuned by those authors on their parking dataset. The published checkpoint is used exactly as released. **No UK imagery was used to adjust the weights**, so what is measured here is zero-shot transfer: the accuracy a UK user would obtain by taking the model off the shelf. One bounded supplementary experiment departs from this, fine-tuning the same checkpoint on half the study area to establish which error class local labels move; it is reported separately in §4.8 and enters no figure in §§4.1–4.7.

---

# 3 — `04_results.md` 行 10（章首导语）

### 原文

> This chapter reports the measured transfer. Section 4.1 gives the headline accuracy and how it varies across the city, answering the first half of RQ1. Sections 4.2 to 4.4 decompose the error and test the post-processing stage, answering RQ2. Section 4.5 returns to spatial variation and shows the apparent location effect to be confounded. Section 4.6 reports the sampled corrections and what the reference data itself is worth. Section 4.7 answers RQ3 within the reliability the preceding sections establish.

### 改后

> This chapter reports the measured transfer. Section 4.1 gives the headline accuracy and how it varies across the city, answering the first half of RQ1. Sections 4.2 to 4.4 decompose the error and test the post-processing stage, answering RQ2. Section 4.5 returns to spatial variation and shows the apparent location effect to be confounded. Section 4.6 reports the sampled corrections and what the reference data itself is worth. Section 4.7 answers RQ3 within the reliability the preceding sections establish. Section 4.8 reports a bounded supplementary experiment on local fine-tuning, on a basis deliberately separate from all of the above.

---

# 4 — `04_results.md` 文件末尾：新增 §4.8

**位置** 现 §4.7 之后，即 `**Figure 4.7** Distribution of calibrated-estimate error under the three hold-out schemes.` 这一行之下。
**表号** 现有表至 4.10，新表取 **4.11**，无冲突。本节不配图。

### 新增全文（整段复制）

```markdown
## 4.8 What local supervision changes

The sections above measure the model as released. This one reports a bounded supplementary experiment asking what a small amount of UK supervision would change — not because fine-tuning is the method of this study, but because the decomposition developed above is the instrument that can say *which* error class local labels move.

**The figures below are not comparable with the rest of this chapter.** Both models are scored on raw pixel output, without polygonisation, the 1,000 px² minimum or the OSM subtraction, so the zero-shot row here is not the 0.571 and 0.854 of Table 4.1. Only the two models within Table 4.11 are comparable, and only with each other.

The 100 cells were halved at cell level — patches within a cell share car parks, so a patch-level split would leak — balanced on distance band and on labelled area, the two variables §4.5 shows to track accuracy. Forty cells were used for fitting, ten for selecting the epoch, and fifty held out entirely from both. This is one run at one hyperparameter setting, with no search and no repeated seeds.

**Table 4.11** Zero-shot and locally fine-tuned models on the 50 held-out cells. Raw pixel output; see the caveat above.

| Aggregation | Model | Precision | Recall | IoU |
|---|---|---:|---:|---:|
| Micro | Zero-shot | 0.5190 | 0.8819 | 0.4853 |
| **Micro** | **Fine-tuned** | **0.7664** | **0.7548** | **0.6136** |
| Macro | Zero-shot | 0.4773 | 0.8777 | 0.4473 |
| Macro | Fine-tuned | 0.7553 | 0.7205 | 0.5834 |

IoU rises by 0.128, but not by uniform improvement. Precision gains 0.247 while recall loses 0.127: false-positive area falls by **71.9%** and false-negative area rises by **107.7%**. At the 5 m threshold, standalone false positives — those lying beyond any labelled car park — fall by **74.5%**, which is consistent with local labels teaching the narrower Leeds scope of §4.2. Boundary-associated false positives fall too, by 65.2% in area. But false-negative erosion rises over the same interval, from 0.0858 to 0.1685 km².

**The pattern is a contraction, not a correction.** The model draws less parking everywhere: the overreach beyond real lots is removed, and so is coverage of the lots themselves. Total predicted area moves from 69.9% above the reference to 1.5% below it, and that near-balance is the caution of §4.7 in its sharpest form — the fine-tuned model still adds 0.3736 km² in the wrong place and misses 0.3982 km², two errors that happen to cancel. Aggregate agreement is not spatial agreement.
```

---

# 5 — `05_discussion.md` §5.2：新增一段

**位置** 第 50 行那段之后、第 52 行那段之前。两侧原文如下，中间即为新增段。

### 上文（第 50 行，不动）

> There is a practical corollary worth stating plainly. Because *p/r* reduces to the ratio of labelled to predicted area, calibrating the model in a second city requires only a labelled *total area* over a sample of cells — not a full object-level error analysis of the kind undertaken here. The expensive part of this study does not have to be repeated to reuse its output.

### ★ 新增段（插在这里）

> That corollary also frames what §4.8 found. If a user is going to label cells at all, the alternative to fitting a correction factor is to fine-tune on them — and on cost the comparison is not close: calibration needs a labelled *total area* over a sample of cells, where the fine-tuning run used fifty cells of complete polygon labelling. Nor is it clearly better on accuracy. Fine-tuning did remove most of the over-prediction, but by contracting the map rather than by locating parking better: recall fell by 0.127 and missed area more than doubled, and its near-unbiased total conceals compensating errors of exactly the kind this section warns against. For a user who wants to find surface parking, or to measure it over tens of square kilometres, the cheaper intervention is also the one that preserves what transferred best. Where an individual false positive is costly, the trade would look different — but that is a different user from the one in §1.1.

### 下文（第 52 行，不动）

> It does **not** support uncorrected area measurement, per-cell values, or any site-level judgement. The 1.50× over-prediction is large enough that an uncorrected figure would be wrong by half, and a third of the unexplained over-prediction is not error at all but parking the annotation rules exclude by design.

---

# 6 — `05_discussion.md` 行 86（§5.5 末段）

### 原文（整段）

> Beyond these, the most specific opportunity comes from the typology itself. If irregular arrangement is the mechanism most often identified among the genuine misses, then training data would be better extended with irregularly arranged car parks than simply with unmarked ones — though on eleven sampled chips that is a direction to test rather than a settled quantity. Whether local supervision moves the boundary component, the definitional component, or neither, is a question the error decomposition developed here is well placed to answer.

### 改后（整段）

> Beyond these, the most specific opportunity comes from the typology itself. If irregular arrangement is the mechanism most often identified among the genuine misses, then training data would be better extended with irregularly arranged car parks than simply with unmarked ones — though on eleven sampled chips that is a direction to test rather than a settled quantity. Whether local supervision moves the boundary component or the definitional component is answered in part by §4.8, on a single run: it moves both, but by contracting the map rather than by improving its geometry. Settling it properly would need repeated seeds and alternative spatial splits, and a comparison against simple probability-threshold calibration — because the released workflow uses argmax rather than a tuned threshold, part of the same precision gain may be available without touching the weights at all.

---

# 7 — `06_conclusion.md` 行 18（Future work 段）

### 原文（整段）

> **Future work.** The calibration factor reduces to a ratio of labelled to predicted area, so testing whether it transfers between cities requires only labelled totals over a sample of cells rather than a repeat of the full error analysis undertaken here — which makes multi-city validation affordable and is the obvious next step. The typology points to a direction for training data: irregularly arranged car parks rather than simply unmarked ones, on the strength of eleven sampled chips. Imagery carrying a near-infrared band would test the one expected failure this study could not examine. And whether local fine-tuning moves the boundary component, the definitional component or neither is a question the decomposition developed here is well placed to answer.

### 改后（整段）

> **Future work.** The calibration factor reduces to a ratio of labelled to predicted area, so testing whether it transfers between cities requires only labelled totals over a sample of cells rather than a repeat of the full error analysis undertaken here — which makes multi-city validation affordable and is the obvious next step. The typology points to a direction for training data: irregularly arranged car parks rather than simply unmarked ones, on the strength of eleven sampled chips. Imagery carrying a near-infrared band would test the one expected failure this study could not examine. And the supplementary fine-tuning test (§4.8) shows the decomposition working on a second model: a gain of 0.13 in IoU that turns out, once decomposed, to be a contraction of the map rather than an improvement in it. Repeating that across seeds and splits, and against threshold calibration rather than argmax alone, would establish what a UK user with some labelling capacity should actually do with it.

---

# A（可选）— `01_introduction.md` 行 37（§1.3 Scope）

### 原文

> Three boundaries apply throughout. The target is off-street surface parking as the source model defines it, so on-street parking and enclosed structures are outside it by rule. The model is used exactly as released, with no UK training data, because what is being measured is what an off-the-shelf user would obtain. And the study identifies where parking is and how much land it occupies; it does not judge whether any site should be redeveloped, a question requiring ownership, access, demand and viability information that none of the data used here contains.

### 改后

> Three boundaries apply throughout. The target is off-street surface parking as the source model defines it, so on-street parking and enclosed structures are outside it by rule. The model is used exactly as released, with no UK training data, because what is being measured is what an off-the-shelf user would obtain (§4.8 tests the alternative on half the study area, and is reported separately). And the study identifies where parking is and how much land it occupies; it does not judge whether any site should be redeveloped, a question requiring ownership, access, demand and viability information that none of the data used here contains.

---

# B（可选，**建议不改**）— `00_abstract.md` 行 10

摘要描述的是主分析，四个头条数字（0.854 / 0.571 / 1.50× / 3.26%）完全未受补充实验影响，且摘要已 308 词。**建议维持原样。**

若审阅口径严格要求摘要覆盖全部实验，可在该段末追加：

> A bounded fine-tuning supplement is reported separately.

---

# C（可选）— `04_results.md` §4.8 末尾：附录指引

> The experimental design, training history, the full boundary-band table at 2, 5 and 10 m, and the limitations of a single unreplicated run are set out in Appendix D.

附录 D 直接收 `fine_tuning_experiment.md` 全文（附录不计入字数）。

---

# 字数账

正文（第 1–6 章，剔除表格、图表标题、标题行、参考文献、中文批注）现约 **12,670 词**。
上限 10,000–12,000，**超 12,000 罚 10%**。

- 必改 6 处合计：**+733 词** → 约 13,400
- 需净删：**约 1,400 词**

## 配套删减候选（按性价比排序）

**1. 删除整个 §5.3（`05_discussion.md` 行 54–62，约 430 词）— 最干净的一刀**

该节三条方法学观察：
- 第一条（"同样的 IoU 可对应不同可用性"）现在被新 §4.8 **直接演示**，比原来的断言有力得多；
- 第二条（"精度数字混合了不同性质的差异"）与 §5.1 RQ2 及 §5.5 的 "A definitional boundary doing real work" 重复；
- 第三条（"校正因子的空间迁移"）与 §5.2 的校正段重复。

删掉后第 6 章的四项贡献列表照旧成立，不需要改动。

**2. 压缩 §5.4 末段 OSM（行 72，约 190 词 → 60 词，省 130）**
复述 §4.6 的数字，只多出一句 VGI 文献定位。保留 Haklay 的定位句 + 63.5%/中位数面积一致这一个结论即可。

**3. 压缩 §2.2 的美国清查细节（约省 150 词）**
Scharnhorst 的 68% 空位率、Hoehne 的 1,220 万车位对 286 万登记车辆——论文后文用不到这两个具体数字，只需保留"数量远超实际使用"这一句判断。

**4. 压缩 §5.1 的两处文献对照（各约 120 词，各压三成，省 70）**
RQ1 的 Maggiori / Hurst-Tarrab IoU 比较、RQ3 的 Jiao 径向密度对照。

四项合计约 **1,100–1,300 词**，接近所需；再从各节收紧冗句即可落到 12,000 以内。

---

# 保底方案：若字数压不下来

**只采纳改动 6 和 7**（两处末句替换，净 +105 词），实验全文进附录 D，正文其余一律不动。

理由：这样至少消除了"论文最后承诺去做一件已经做完的事"这个硬伤，而 10% 的罚分远大于一个补充实验能带来的边际得分。
