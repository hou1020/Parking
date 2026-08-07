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
| `bare_ground` | 棕褐色裸土 | Unsurfaced brown or tan ground, compacted earth, cleared plot. 未铺装的棕褐色地面、压实土地、空地。 |
| `goods_yard` | 货物堆场 | Containers, pallets, stacked goods or machinery mistaken for rows of cars; often enclosed, no aisles. 集装箱、托盘、堆放的货物或机械被误认成成排车辆；通常封闭、无通行道。 |
| `sports_court` | 球场 | Basketball, tennis or multi-use court; painted court markings, fencing. 篮球、网球或综合球场；有球场标线、围网。 |
| `building_house` | 房屋/建筑 | A roof mistaken for pavement; house, shed or industrial unit. 屋顶被误判为铺装；住宅、棚屋或工业厂房。 |
| `on_street` | 路边停车 | Cars parked in or along the carriageway, not a separate off-street area. 停在车行道内或紧贴路缘，并非独立的路外场地。 |
| `real_parking_missed` | 真停车（标注遗漏） | Genuinely off-street surface parking that **meets** the annotation rules but was not labelled. 确属路外地面停车、**符合**标注规则，但当初漏标了。 |
| `other` | 其他 | None of the above — describe in `note`. 都不符合，在 `note` 里描述。 |

---

## B. `fn_other` — genuine model misses / 模型真实漏检

Real parking that the model failed to detect, and that post-processing did not remove.
确实是停车，模型没检出，且不是后处理删掉的。

| category | 中文 | What it looks like / 判断线索 |
|---|---|---|
| `lorry_van_lot` | 货车/厢式车场 | Occupied by lorries, vans or coaches rather than ordinary cars. 停放的是货车、厢式车或大巴，而非普通轿车。 |
| `unusual_surface` | 异色/非常规路面 | Surface colour or texture unlike typical asphalt: gravel, red, green, very pale. 路面颜色或质地不同于常见沥青：碎石、红色、绿色、极浅色。 |
| `shaded_occluded` | 阴影/遮挡 | Obscured by tree canopy or building shadow. 被树冠或建筑阴影遮蔽。 |
| `small_irregular` | 小而不规则 | Small or oddly shaped lot, few bays, tucked between buildings. 面积小或形状不规则，车位少，夹在建筑之间。 |
| `rooftop` | 屋顶停车 | Parking on top of a building, visible from above. 位于建筑顶部、从上方可见的停车。 |
| `other` | 其他 | None of the above — describe in `note`. 都不符合，在 `note` 里描述。 |

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
| `vehicle_storage` | 车辆存放/场站 | **Vehicles are present**, but it is storage, a depot, a bus station or a dealership forecourt, not parking as the rules define it. **有车辆停放**，但属于车辆存放、场站、公交站或经销商展场，不是规则所定义的停车。 |
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

**`vehicle_storage` vs `not_parking`.** The test is whether vehicles are actually standing
there. A dealership forecourt or depot full of vehicles is `vehicle_storage`: OSM's tag is
at least understandable, and the rules exclude it. A goods yard of containers and pallets,
an empty plot or a sports court has no vehicles at all, so OSM is simply wrong: use
`not_parking` and record the sub-type in `note`.
**`vehicle_storage` 与 `not_parking` 的区别**：看**是否真的停着车**。经销商展场、堆满车辆的
场站属于 `vehicle_storage`——OSM 这样标至少可以理解，只是规则将其排除。而集装箱托盘的货物堆场、
空地、球场根本没有车辆，说明 OSM 就是标错了：填 `not_parking`，并在 `note` 里记录细分类型。

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
