## Manual Annotation Rules: Off-Street Surface Parking

**Basis** These rules follow the annotation method of the US-trained model used here (Qiam et al., 2025). The same rules are used so the RO1 accuracy figures are valid: ground-truth labels must follow the definition the model was trained on. Labelling is done in QGIS over the Google Satellite basemap.

**Target** Off-street surface parking: open-air, ground-level areas used for parking, outside public roads. Labels are binary (parking / non-parking). The use served is not recorded, as it cannot be judged reliably from imagery. No minimum-size threshold is applied — all off-street surface parking is labelled regardless of size, to match the definition the model was trained on.

**Identifying parking** An area is labelled as parking where it has marked parking bays, or — where markings are absent — parked cars and a layout (bays and aisles) that clearly show parking use. Areas whose use is unclear are left unlabelled or marked confidence 1.

**Include**

- Surface car parks, whatever use they serve.
- Parking bays and the internal aisles that connect them.
- Rooftop parking where the parking surface is visible from above.

**Exclude**

- On-street parking.
- Multi-storey or underground car parks with no visible parking surface.

**Treated as non-parking** (also common look-alikes the model may confuse):

- Sports courts, storage or depot yards, and other non-parking hardstanding.
- Buildings, roads, pavements and landscaping.

**Driveways** Only very short entrances belonging to a car park are included. Longer access roads are excluded, so the labels do not teach the model to recognise roads (Qiam et al., 2025).

<span style="color:#c0392b">**Supplementary note — residential parking.** Individual single-house driveways or forecourts (a few cars, clearly one household) are not labelled — they are private curtilage, not a car park. Shared or communal residential parking courts (serving several dwellings) are labelled. This extends Qiam et al.'s driveway rule: a single-house driveway is private access, like the driveways they exclude, whereas a communal court is genuine off-street surface parking under their target. Where it narrows Qiam, the difference is kept separate in the error analysis.</span>

**Boundary**

- Draw along the edge of the pavement, not the parcel boundary.
- Keep one car park as one polygon, even if split by planting islands.
- Align to the current image. Where OSM or other references are out of date (e.g. a demolished building), follow the current image. OSM parking is used only as a starting reference, not as ground truth.

**Attributes**

| Field      | Description                                |
| ---------- | ------------------------------------------ |
| confidence | 3 = clear, 2 = fairly clear, 1 = uncertain |
| notes      | Optional notes for ambiguous cases         |

**Why these rules, and how reliable they are** The model is validated against these labels, so the labels must match the definition the model was trained on. The rules therefore follow Qiam et al. (2025) as closely as possible: the same off-street surface target, pavement-edge boundaries, rooftop-only garages, and no minimum-size cut-off. Annotating surface parking as a binary polygon class from aerial imagery is also standard in other datasets (e.g. APKLOT; Yin et al., 2022), which use similar include/exclude rules, so the approach is not ad hoc. Any point where the rules differ from Qiam et al. is noted, and errors caused by such definition differences are kept separate from true model errors in the error analysis.

**References**

- Qiam, S., Devunuri, S. and Lehe, L.J. (2025) 'A pipeline and NIR-enhanced dataset for parking lot segmentation', *WACV*.
- Yin, Y. et al. (2022) 'A context-enriched satellite imagery dataset and an approach for parking lot detection', *WACV*.
- APKLOT: a dataset for aerial parking block segmentation. https://github.com/langheran/APKLOT

---

## 手工标注规则：路外地面停车

**依据** 本规则遵循本研究所用美国训练模型的标注方法（Qiam et al., 2025）。采用同一套规则是为了让 RO1 的精度数字有效：真值标签必须符合模型训练时的定义。标注在 QGIS 中对照 Google 卫星底图完成。

**对象** 路外地面停车：露天、地面、位于公共道路之外、用于停车的区域。标签为二分类（停车/非停车）。不记录其服务用途，因为影像无法可靠判断。不设最小尺寸阈值——所有路外地面停车不论大小都标注，以匹配模型训练时的定义。

**识别停车** 一块区域在以下情况标为停车：有划设的车位线；或在没有标线时，有停放的车辆且布局（车位与通行道）清楚显示其为停车用途。用途不明的区域不标注，或标为 confidence 1。

**纳入**

- 地面停车场，无论其服务何种用途。
- 车位及连接车位的内部通行道。
- 从上方可见停车面的屋顶停车。

**排除**

- 路边停车。
- 无可见停车面的多层或地下车库。

**视为非停车**（也是模型常混淆的相似物）：

- 球场、堆料/堆场，及其他非停车硬化地。
- 建筑、道路、人行道与绿化。

**引道** 仅纳入属于停车场的很短的入口。较长的通行道排除，以免标签让模型学会识别道路（Qiam et al., 2025）。

<span style="color:#c0392b">**补充说明——住宅停车。** 单户住宅的私家车道或前院（几辆车、明显属于一户）不标注——它们是私人红线用地，不是停车场。共享或公用的住宅停车院（服务多户）则标注。这是对 Qiam et al. 引道规则的延伸：单户私家车道属于私人出入（如同 Qiam 排除的那类引道），而共享停车院在 Qiam 的对象定义下是真正的路外地面停车。当此规则收窄 Qiam 时，由此产生的差异在误差分析中单独处理。</span>

**边界**

- 沿铺装边缘描画，而非地块边界。
- 同一停车场画为一个多边形，即使被绿化岛分隔。
- 对齐当前影像。当 OSM 或其他参照过时（如已拆除的建筑），以当前影像为准。OSM 停车仅作为起点参照，而非真值。

**属性**

| 字段       | 说明                              |
| ---------- | --------------------------------- |
| confidence | 3 = 清晰，2 = 较清晰，1 = 不确定  |
| notes      | 疑难情形可选备注                  |

**为什么用这些规则、可靠性如何** 模型是对照这些标签验证的，所以标签必须匹配模型训练时的定义。因此规则尽量贴合 Qiam et al. (2025)：相同的路外地面停车对象、沿铺装边缘的边界、仅限可见的屋顶车库、以及不设最小尺寸下限。以二分类多边形方式从航拍影像标注地面停车，在其他数据集中也是标准做法（如 APKLOT；Yin et al., 2022），它们采用相似的纳入/排除规则，因此本方法并非随意而定。任何与 Qiam et al. 不同之处都会注明，且由此类定义差异导致的误差在误差分析中与真正的模型误差分开。

**参考文献**

- Qiam, S., Devunuri, S. and Lehe, L.J. (2025) 'A pipeline and NIR-enhanced dataset for parking lot segmentation', *WACV*.
- Yin, Y. et al. (2022) 'A context-enriched satellite imagery dataset and an approach for parking lot detection', *WACV*.
- APKLOT: a dataset for aerial parking block segmentation. https://github.com/langheran/APKLOT
