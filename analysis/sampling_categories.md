# Sampling Categories / 抽样类别对照表

Reference sheet for filling the `category` field in `sampling_worksheet.gpkg`.
填写 `sampling_worksheet.gpkg` 中 `category` 字段时的对照表。

**Type the English value exactly as written below.** The `options` field in the
worksheet lists the valid values for each row.
**请照抄下面的英文值。** 工作表里的 `options` 字段也列出了该行的可选值。

---

## Rules / 规则

1. **Do not invent categories.** If nothing fits, use `other` and describe it in `note`.
   **不要临时新增类别。** 都不符合就填 `other`，并在 `note` 里描述。
2. **Judge from the imagery, not from what the model or OSM says.** The model's
   output and OSM are what is being tested, so they cannot be the evidence.
   **依据影像判断，而不是模型或 OSM 说了什么。** 它们正是被检验的对象，不能拿来当证据。
3. **Apply the annotation rules in `Rules.md`**, the same ones used for labelling.
   **沿用 `Rules.md` 的标注规则**，与标注时保持一致。
4. **Always pick the closest category, and record how sure you are in `conf`.**
   Never leave `category` blank because a case is hard: an unfilled row cannot be
   weighted, whereas a low-confidence call can.
   **总要选一个最接近的类别，并在 `conf` 里记录把握程度。** 不要因为难判就空着：空行无法参与加权，
   而低把握的判断可以。

   | `conf` | meaning / 含义 |
   |---|---|
   | `3` | Clear — the imagery settles it. 清晰，影像足以判定。 |
   | `2` | Fairly clear — likely, some doubt. 较清晰，基本确定但有疑问。 |
   | `1` | Uncertain — a best guess; say why in `note`. 不确定，只是最佳猜测；在 `note` 里说明原因。 |

   This mirrors the `confidence` field used when labelling, and lets the results be
   reported both over all calls and over confident calls only, as a sensitivity range.
   这与标注时使用的 `confidence` 字段一致，可使结果同时按"全部判断"和"仅高把握判断"两种口径报告，
   形成敏感性区间。

   Expect the `osm_disagree` population to be the hardest: it is defined by cases where
   OSM and the labelling disagreed, so clear-cut features are largely absent from it by
   construction. Frequent `conf = 1` there is an expected result, not a failure.
   `osm_disagree` 这一层预计最难判：它按定义就是"OSM 与标注分歧"的样本，清楚明白的地物本就不会
   进入其中。该层出现较多 `conf = 1` 是**预期结果**，而非失误。

---

## A. `fp_other` — unexplained false positives / 未解释的误检

The model called this parking; the manual labels did not; no reference layer explains it.
模型判为停车、手工未标注、且没有任何参考图层能解释。

| category | 中文 | What it looks like / 判断线索 |
|---|---|---|
| `grey_hardstanding` | 灰色水泥/硬化地 | Plain concrete or asphalt surface, no bays, no cars, no clear function. 平整的水泥或沥青地，无车位线、无车辆、用途不明。 |
| `unpaved_ground` | 未铺装的自然地面 | Any unsurfaced open ground the model called parking: bare earth, compacted ground, grass, scrub, cleared plots. 任何未铺装、却被模型判为停车的开阔地面：裸土、压实土地、草地、灌丛、空地。 |
| `goods_yard` | 货物堆场 | Containers, pallets, stacked goods or machinery mistaken for rows of cars; often enclosed, no aisles. 集装箱、托盘、堆放的货物或机械被误认成成排车辆；通常封闭、无通行道。 |
| `sports_court` | 球场 | Basketball, tennis or multi-use court; painted court markings, fencing. 篮球、网球或综合球场；有球场标线、围网。 |
| `building_house` | 房屋/建筑 | A roof mistaken for pavement; house, shed or industrial unit. 屋顶被误判为铺装；住宅、棚屋或工业厂房。 |
| `on_street` | 路边停车 | Cars parked in or along the carriageway, not a separate off-street area. 停在车行道内或紧贴路缘，并非独立的路外场地。 |
| `private_driveway` | 私人车道 | The driveway or forecourt of a single household — real parking, but excluded by the rules as private curtilage. 单户住宅的私家车道或前院——确实是停车，但规则将其作为私人红线用地排除。 |
| `real_parking_missed` | 真停车（标注遗漏） | Genuinely off-street surface parking that **meets** the annotation rules but was not labelled. 确属路外地面停车、**符合**标注规则，但当初漏标了。 |
| `other` | 其他 | None of the above — describe in `note`. 都不符合，在 `note` 里描述。 |

The categories fall into three groups. `grey_hardstanding`, `unpaved_ground`, `goods_yard`,
`sports_court` and `building_house` are genuine misdetections: the model called something
parking that is not. `on_street` and `private_driveway` are real parking that the
annotation rules exclude, so they are definition differences rather than model failures,
and can be reported separately as an effective precision. `real_parking_missed` points to
the reference rather than the model.
这些类别分为三组。`grey_hardstanding`、`unpaved_ground`、`goods_yard`、`sports_court`、
`building_house` 是**真正的误检**：模型把不是停车的东西判成了停车。`on_street` 与
`private_driveway` 是**确实存在的停车、但被标注规则排除**，属于定义差异而非模型失败，可单独
report 为"有效 precision"。`real_parking_missed` 指向的则是参考数据本身。

---

## B. `fn_other` — car parks the model missed / 模型漏掉的停车场

Whole labelled lots the model essentially did not find (coverage <= 10%, shown in
`model_cov`), excluding those the original model did find and post-processing then
deleted. The question is **why the model did not see this car park**.
模型基本没找到的**完整**停车场（覆盖率 ≤10%，见 `model_cov` 字段），已排除"原始模型检出、被后处理
删掉"的那些。要回答的是：**模型为什么没看见这个停车场**。

> **Check `label_conf` first / 先看 `label_conf`.** This is the confidence recorded when
> the lot was first labelled. The missed population is enriched in low-confidence lots
> (44% are `1`, against 21% of all labels), which is itself consistent with the missing-cue
> account: a lot with no markings and no cars is hard for a person to call and impossible
> for the model. Judge by what is visible in the image, not by how it reads now knowing the
> model failed on it.
> 该字段是**你当初标注这个停车场时**给出的把握度。漏检总体明显富集低把握标注（44% 为 `1`，而全体
> 只有 21%），这本身就与"线索缺失"的解释一致：无标线、无车的场地，人难判、模型更不可能识别。请以
> 影像中可见的内容为准，不要因为"已知模型漏了它"而事后觉得清楚。

| category | 中文 | What it looks like / 判断线索 |
|---|---|---|
| `no_markings` | 无车位线／标线不清 | The cue is **absent**: no painted bays at all, or markings so worn they are barely visible. Identified as parking only from the vehicles and the layout. 线索**缺失**：完全没有画车位线，或标线磨损到几乎看不见。只能靠车辆与布局才认出是停车场。 |
| `irregular_layout` | 排布／画线方式不规则 | The cue is **present but does not match the template**: the arrangement departs from regular rows and aisles. Covers cars parked ad hoc at varying angles or spacing with no rows; and bays that are marked but laid out unusually — echelon or herringbone, odd proportions, non-standard marking style or colour. 线索**存在但与模板不符**：排布偏离规整的"成排＋通道"。既包括车辆随意停放、角度间距不一、无行列，也包括**有画线但画法反常**——斜列或人字形、比例异常、标线样式或颜色非常规。 |
| `unusual_surface` | 路面颜色／材质不常见 | Block paving, gravel, compacted stone, red or green surfacing, very pale concrete — unlike the asphalt that dominates the training data. 块石铺装、碎石、压实石屑、红色或绿色铺面、极浅色混凝土——与训练数据中占主导的沥青不同。 |
| `no_cars_present` | 拍摄时无车 | Empty at the time of capture, so the vehicle cue is unavailable as well. 影像拍摄时空置，因此连"有车"这一线索也没有。 |
| `obscured` | 阴影／遮挡 | Surface hidden by tree canopy or building shadow. 路面被树冠或建筑阴影遮蔽。 |
| `small_awkward_lot` | 场地小／形状别扭 | The **lot itself** is small or has an awkward outline: few spaces, wedged between buildings, long and thin. This is about the size and shape of the car park, not about how the cars within it are arranged — compare `irregular_layout`. **停车场本身**面积小或轮廓别扭：车位少、夹在建筑之间、狭长。指的是**场地的大小与形状**，不是里面车辆如何排列——与 `irregular_layout` 相对。 |
| `lorry_van_lot` | 货车／厢式车 | Occupied by lorries, vans or coaches rather than ordinary cars. 停放的是货车、厢式车或大巴，而非普通轿车。 |
| `no_obvious_reason` | 无明显原因 | Marked bays, cars present, ordinary asphalt — nothing unusual, and the model still missed it. 有车位线、有车、普通沥青路面——毫无异常，模型却仍然漏了。 |
| `other` | 其他 | None of the above — describe in `note`. 都不符合，在 `note` 里描述。 |

Several of these often apply at once, for example an unmarked gravel yard. Put the main
cause in `category` and list the rest in `note`, such as `no_markings + gravel`.
这些原因常常同时出现，例如无标线的碎石场地。把**主因**填进 `category`，其余写在 `note`，
例如 `no_markings + gravel`。

**The lost-pattern family / "图式缺失"这一机制家族.** `no_markings` and `irregular_layout`
divide the same mechanism by whether the cue is **missing** or **mismatched**: what the model learned from US lots is a repeating
bay-and-aisle pattern — aligned rows of vehicles, even spacing, painted bays, a circulation
aisle between. Unmarked ground and ad-hoc parking each break part of that pattern, and they
often occur together, since without bays drivers do not line up. They are kept as separate
categories so the data can show which aspect dominates, because the implication differs: if
markings are the binding cue, fine-tuning needs unmarked examples; if the row structure is,
the model depends on spatial arrangement and needs examples of informal layouts.
`no_markings` 与 `irregular_layout` 按线索是**缺失**还是**不匹配**来划分同一个机制：模型从美国停车场学到的是一套**重复的
"车位＋通道"图式**——车辆成行对齐、间距均匀、有画线、行列间有通行道。无标线的地面与随意停放各自破坏了
这套图式的一部分，且二者常同时出现（没有画线，司机自然不会停齐）。之所以仍分成两类，是为了让数据显示
**哪一方面主导**，因为含义不同：若关键在标线，微调需补无标线样本；若关键在行列结构，说明模型依赖的是
**空间排布**，需补非规整布局的样本。

**Why the cue matters / 为什么以"缺哪个线索"划分.** The model was trained on US lots that
are predominantly asphalt with painted bays, so painted markings are the cue it relies on.
The annotation rules used here are deliberately wider: a lot counts as parking if it has
marked bays **or**, where markings are absent, parked cars and a layout that clearly show
parking use. The reference is therefore broader than what the model can recognise, and that
gap is a precise mechanism for the drop in recall — not a vague appeal to domain shift.
模型是在**以沥青路面加白色车位线为主**的美国停车场上训练的，因此**标线**是它依赖的线索。而本研究的
标注规则有意更宽：有车位线**或**（在无标线时）有停放车辆且布局清楚显示停车用途，均算停车。也就是说
**真值的范围比模型能识别的范围更宽**，这个落差正是 recall 下降的精确机制，而不是笼统地归因于
domain shift。

**`no_obvious_reason` is the important residual / `no_obvious_reason` 是关键残差.** If a
lot has markings, cars and an ordinary surface and was still missed, the failure cannot be
attributed to any UK–US difference. A large share in this category would mean the model has
unexplained blind spots; a small share would mean the missing-cue account is close to
complete.
若一个停车场有标线、有车、路面普通却仍被漏掉，这种失败无法归因于任何英美差异。该类占比高，说明模型
存在**无法解释的盲点**；占比低，说明"线索缺失"这一解释已基本完备。

**Why these categories / 这些类别的意义.** Every error here is, by definition, error from
transferring a US-trained model to the UK. Saying "it is domain shift" only names the
problem; these categories are what gives that claim content, by tying each failure to a
specific difference — UK vehicle fleets, block paving and gravel surfaces, denser tree
cover and the longer shadows of a city at 53.8°N compared with the mostly 30–42°N US
training cities, and the smaller, more irregular lots typical of British urban form.
**为什么用这些类别**：这里的每一处误差，按定义都是"美国模型迁移到英国"的误差。但只说"这是 domain
shift"仅仅是给问题起了个名字；这些类别才为该论断填入内容——把每一种失败对应到具体差异：英国的车辆
构成、块石与碎石铺装、更密的树冠、以及 Leeds 位于 53.8°N 所带来的更长阴影（美国训练城市多在
30–42°N），还有英国城市形态中更小、更不规则的停车场。

---

## C. `osm_disagree` — OSM car parks the labelling barely covered / 手工几乎未覆盖的 OSM 停车场

OSM tags a whole polygon `amenity=parking`, and the manual labels cover at most 10% of
it (see the `labelled_frac` field). The question is whether the rules correctly excluded
it, or whether it should have been labelled and was missed.
OSM 把整块多边形标为 `amenity=parking`，而手工标注最多只覆盖了它的 10%（见 `labelled_frac`
字段）。要判断的是：规则**正确地**排除了它，还是本该标注却漏了。

> **Note / 说明.** An earlier version of this stratum used false-positive fragments more
> than 5 m from labelled parking. That was the wrong unit: many were simply the parcel
> margin around a car park that *had* been labelled correctly, because OSM outlines follow
> parcel boundaries rather than the pavement (Qiam et al., 2025). Whole OSM polygons are
> used instead, so a margin around a labelled lot can no longer be mistaken for an omission.
> 本层早先用的是"距标注 5 米以外的误检碎片"，单位选错了：其中很多只是**已正确标注**的停车场
> 周围的地块边缘——因为 OSM 沿地块边界画，而非沿铺装边缘（Qiam et al., 2025）。现改用完整的
> OSM 多边形，边缘碎片便不会再被误当成漏标。

| category | 中文 | What it looks like / 判断线索 |
|---|---|---|
| `on_street` | 路边停车 | Parking within or alongside the carriageway. 位于车行道内或紧贴路缘的停车。 |
| `multi_storey` | 多层/地下车库（顶部不可见） | A parking structure whose top is an ordinary roof, with **no parking surface visible from above**. If the top deck is open and cars or bays can be seen, it is **not** this category — see below. 顶部是普通屋顶、**从上方看不到停车面**的车库建筑。若顶层露天、能看到车辆或车位线，则**不属于**本类，见下。 |
| `private_driveway` | 私人车道 | Driveway or forecourt of a single household. 单户住宅的私家车道或前院。 |
| `not_parking` | 明显不是停车场 | The imagery shows something that is plainly not a car park — empty ground, a sports court, a park, a building plot, any other land use — so OSM is out of date or mis-tagged. **Name what it actually is in `note`.** 影像显示的明显不是停车场——空地、球场、公园、建设用地或任何其他用途——即 OSM 过时或标错。**在 `note` 里写明它实际是什么。** |
| `real_parking_missed` | 真停车（标注遗漏） | Off-street surface parking meeting the rules that was not labelled. 符合规则的路外地面停车，但当初漏标。 |
| `other` | 其他 | None of the above — describe in `note`. 都不符合，在 `note` 里描述。 |

**Multi-storey car parks with an open top deck.** The annotation rules include rooftop
parking wherever the parking surface is visible from above, so a multi-storey whose top
deck shows cars or bays should have been labelled: record it as `real_parking_missed` and
write `rooftop` in `note`. Use `multi_storey` only when the structure is covered and no
parking surface can be seen. This mirrors Qiam et al. (2025), whose dataset includes only
garages with parking visible on top.
**顶层露天的多层车库。** 标注规则规定：只要从上方能看到停车面，屋顶停车就应纳入。因此顶层能看到
车辆或车位线的多层车库属于**该标未标**——填 `real_parking_missed`，并在 `note` 里写 `rooftop`。
只有当车库封闭、完全看不到停车面时才填 `multi_storey`。这与 Qiam et al. (2025) 一致：其数据集
只收录顶部可见停车的车库。

Categories other than `real_parking_missed` all mean the labelling was correct: either a
rule excluded the feature, or OSM records parking that the imagery does not support.
除 `real_parking_missed` 外的所有类别都意味着标注是正确的：要么规则排除了它，要么 OSM 记录的停车
在影像上并不成立。

### Sub-types for `not_parking` / `not_parking` 的细分

When the category is `not_parking`, put one of these keywords in `note` to record what the
feature actually is. Keeping to a fixed list means the sub-types can be counted later;
add free text after the keyword if useful.
类别填 `not_parking` 时，在 `note` 里写下面**其中一个关键词**，记录它实际是什么。用固定词表是为了
之后能统计；需要补充说明可写在关键词之后。

| note keyword | 中文 | Example / 例子 |
|---|---|---|
| `sports_court` | 球场 | Basketball, tennis, multi-use court; painted markings, fencing. 篮球、网球、综合球场；有标线、围网。 |
| `vacant_ground` | 空地/裸地 | Empty ground, no bays, no cars, no readable use. 空地，无车位线、无车辆、看不出用途。 |
| `park_green` | 公园/绿地 | Grass, planting, paths. 草地、绿化、步道。 |
| `construction` | 工地/建设用地 | Cleared or active building site, plant and materials. 已清理或在建的场地，有机械与材料。 |
| `building` | 建筑 | A roof or structure occupies the polygon. 多边形范围内是屋顶或建筑物。 |
| `goods_yard` | 货物堆场 | Containers, pallets or materials, no vehicles. 集装箱、托盘或建材，无车辆。 |
| `other_landuse` | 其他用途 | Anything else — describe after the keyword. 其他情况，在关键词后描述。 |

These sub-types describe **OSM's error**, not the model's. Together with the omission rate
they give both sides of OSM quality: parking OSM records that is not there, and parking on
the ground that OSM does not record.
这些细分刻画的是 **OSM 的错误**，而非模型的错误。它与漏标率一起，构成 OSM 质量的两面：OSM 记录了
但地上没有的停车，以及地上有而 OSM 未记录的停车。

---

## Why `real_parking_missed` matters / 为什么这一类很关键

Omissions push measured precision **down**, because the model is credited with a false
positive where the reference is actually wrong. Reported precision is therefore a lower
bound, and the sampled omission rate is what allows an adjusted figure to be reported.
漏标会**压低**测得的 precision——参考数据本身错了，却记在模型头上。因此所报 precision 是下界；
只有测出漏标比例，才能给出修正后的数值。

Keep the distinction clear: excluding on-street parking, multi-storey car parks and
single-house driveways is the rules working **correctly**, not an omission. Only areas
that the rules say should have been labelled count as `real_parking_missed`.
务必区分：排除路边停车、多层车库、单户私家车道是规则**正确执行**，不算漏标。只有按规则本应标注却未标的，
才算 `real_parking_missed`。

---

## Workflow in QGIS / QGIS 操作流程

1. Load the aerial imagery, `sampling_worksheet.gpkg`, `leeds_manual.gpkg` and
   `removal_merged.geojson`.
   加载航拍影像、`sampling_worksheet.gpkg`、`leeds_manual.gpkg` 与 `removal_merged.geojson`。
2. Right-click the worksheet layer → **Toggle Editing**.
   工作表图层右键 → **切换编辑模式**。
3. Open the attribute table, select a row, **Zoom to Feature**.
   打开属性表，选中一行，**缩放到要素**。
4. Read `options` for the valid values, judge from the imagery, type into `category`.
   查看 `options` 中的可选值，依据影像判断，填入 `category`。
5. Save the layer when finished.
   完成后保存图层。

Suggested order: `osm_disagree` (30) first, since it settles whether omissions are a
problem; then `fn_other` (45); then `fp_other` (70). Filter the layer by the `source`
field to work through one population at a time.
建议顺序：先做 `osm_disagree`（30 个，可直接判明漏标是否成问题），再 `fn_other`（45 个），
最后 `fp_other`（70 个）。用 `source` 字段筛选，一次只做一批。
