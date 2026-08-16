# 导师会议记录（Supervision Meeting Notes）

**项目**：Off-Street Surface Parking Detection（CASA × Centre for Cities）
**学生**：JiaYi
**CASA 导师**：Esra、Clara
**Centre for Cities 合作方**：Maurice（住房与城市规划，本项目对口）、Rob（交通、技能与创新，对口 Khales 的交通项目）

**来源**：`Camley Street*.m4a` 会议录音整理。
**用途**：作为后续撰写论文附录「研究日志（Research Log）」的素材。手册 §3.7 要求研究日志必须作为附录，列出每次指导会面的日期，并用至少一句话说明讨论内容——因此每次会议下方附一条英文一句话记录，可直接搬入附录。

> **录音编号说明**：项目相关录音共 **13 段**，编号 1–9 与 12–15；编号 10、11 为无关内容，不属于本项目会议。13 段录音对应 **10 次会议**（录音 1–4 为同一次启动会的四段）。会面日期列表至此完整。

> **数据口径**：凡具体数字（瓦片数、文件数等）与 git 提交记录不一致处，一律**以 git 为准**，并在本文档同步更正；更正处标注 ⟨已按 git 更正⟩。

---

## 一、会议一览

| # | 日期 | 星期 | 录音文件 | 主题 |
|---|---|---|---|---|
| 1 | 2026-04-27 | 周一 | Camley Street 1–4 | 项目启动会：课题分配、研究动机、协作与沟通安排 |
| 2 | 2026-05-05 | 周二 | Camley Street 5 | 学业进度同步；确认 8/20 提交日；写作研讨会预告 |
| 3 | 2026-05-19 | 周二 | Camley Street 6 | 模型精度问题；建议改用 OSM 空间相交后处理 |
| 4 | 2026-06-02 | 周二 | Camley Street 7 | Leeds 9 瓦片初测：高召回、低精确；验证样本量与算力瓶颈 |
| 5 | 2026-06-16 | 周二 | Camley Street 8 | 边缘案例审视：工业仓储区误判；过滤标准与低置信度标记 |
| 6 | 2026-06-22 | 周一 | Camley Street 9 | 与 OS 官方测绘数据对比；分析路径二选一；代码归档 |
| 7 | 2026-07-09 | 周四 | Camley Street 12 | 会面形式与线上同步安排 |
| 8 | 2026-07-14 | 周二 | Camley Street 13 | 模型跨国迁移效果差；重训练 vs. 后处理的路径抉择 |
| 9 | 2026-07-28 | 周二 | Camley Street 14 | 界定论文重点：城市研究导向，而非计算机视觉导向 |
| 10 | 2026-08-11 | 周二 | Camley Street 15 | 写作进度告急；紧急冲刺计划；论文「故事线」设计 |

会议节奏与启动会上商定的「每两周一次 45 分钟线上同步」基本一致，多数安排在周二。

---

## 二、逐次会议记录

### 1. 2026-04-27（周一）｜项目启动会
**录音**：Camley Street 1、2、3、4（同一次会议的四段）
**参会**：Esra、Clara、Rob、Maurice、Khales、JiaYi

**开场与角色分工**
- CASA 与 Centre for Cities 合作项目的启动会议。
- Rob：Centre for Cities 高级分析师，负责交通、技能与创新等非规划类议题，对口 Khales。
- Maurice：负责住房与城市规划，对口 JiaYi。

**Khales 的交通课题（录音 1–2，背景信息）**
- 核心问题：英国主要大城市（伦敦除外）的公共交通连通性为何远落后于同等规模的欧洲城市。
- Rob 的判断：问题不在网络规模，而在城市形态（低密度）与公交系统缺乏整合（票务碎片化、多运营商竞争）。
- 既有模型结果：优化公交频率与网络整合后，可在 30 分钟内为市中心额外带来 120 万通勤人口。
- 数据：拟使用 BODS（公交开放数据服务）的实时或排班数据；此前用的是插值实时数据，排班数据同样适用。
- 范围：Rob 建议先聚焦布里斯托（Bristol）单一城市，而非铺开六个候选城市。
- 视角：政策建议应从经济学视角出发（如何连接经济活动中心与交通不便的郊区），而非纯交通规划的技术视角。
- 数据局限：2021 年英国普查的 OD 通勤数据受疫情期间 WFH 影响严重，反映真实通勤模式的准确性打折扣。

**JiaYi 的停车场课题（录音 3）**
- Maurice 介绍课题：利用深度学习识别地面停车场。（他最初提议的内部移民课题未被选中。）
- 灵感来源：一篇利用深度学习在美国城市识别大面积地面停车场的论文。
- 主要挑战：美国城市高度依赖汽车，英国城市历史更悠久、路网更复杂，模型直接迁移到英国是核心难点。
- **核心政策动机**：研究目的不是找停车场本身，而是找出尚未纳入地方开发规划（unallocated）、但具备改造为住房潜力的闲置土地，以回应住房短缺问题。Maurice 同时解释了英国「自由裁量权」（discretionary）规划系统与地方规划机制。

**协作安排（录音 4）**
- 线下办公：Centre for Cities 办公室周二至周四工位紧张（轮用办公桌制），学生可选周一或周五前往集中办公。
- 沟通机制：每两周（bi-weekly）一次 45 分钟线上跟进会议。
- 资源：日常沟通以电子邮件为主；建立共享 GitHub 仓库管理项目代码。

> *Log line*: Project kick-off with CASA supervisors and Centre for Cities. My project was defined as deep-learning detection of off-street surface parking in UK cities, motivated by identifying unallocated land with housing potential; the transferability of a US-trained model to UK urban form was flagged as the main challenge, and a bi-weekly online sync plus a shared GitHub repository were agreed.

---

### 2. 2026-05-05（周二）｜学业进度同步
**录音**：Camley Street 5
**参会**：Clara、Esra、JiaYi（及项目组）

- JiaYi 汇报近期学业极度繁忙：刚熬夜（仅睡 4 小时）提交一门课程作业，5 月 14 日（周四）还有一场线下考试。
- 项目进度：目前仅在 Digimap 平台下载了部分数据，尚未正式运行模型。导师表示理解。
- **确认毕业论文最终提交日期为 8 月 20 日。**
- Clara 宣布：CASA 计划在 5 月 18 日（周一）前后为硕士生举办两次论文写作指导研讨会，帮助厘清研究问题与方法论结构。

> *Log line*: Progress update during the coursework period — data had been downloaded from Digimap but no model runs had been carried out yet; the 20 August submission deadline was confirmed and the CASA dissertation writing workshops were announced.

---

### 3. 2026-05-19（周二）｜模型精度与后处理路线
**录音**：Camley Street 6

- 导师询问能否自行手动标注图像来训练模型；JiaYi 回复这需要更强的计算资源支持。
- **导师强烈建议改走「空间相交」后处理路线**，避免陷入耗时的模型微调：利用 OpenStreetMap 等现成的建筑物多边形数据，直接过滤掉覆盖在建筑物屋顶上的错误识别区域。
- 重申研究动机：这不是单纯的计算机视觉项目，必须把「找出大面积停车场」与「释放土地潜力以应对住房危机」的城市政策导向紧密结合；建议忽略无法用于开发的小型停车场。

> *Log line*: Discussed model accuracy — manual annotation and retraining were judged too compute-intensive, so spatial intersection with OpenStreetMap building polygons was recommended as post-processing, and the supervisors restated the urban-policy framing of the project over a computer-vision framing.

---

### 4. 2026-06-02（周二）｜Leeds 初步测试结果
**录音**：Camley Street 7

- JiaYi 汇报深度学习模型在利兹（Leeds）**9 个图像瓦片**（`se2526`–`se2728`，3×3 网格）上的测试情况。
  ⟨已按 git 更正：录音记录为「5 个瓦片」；2026-05-29 提交 *Add Leeds imagery and batch inference* 显示实际入库并完成推理的为 9 块瓦片⟩
- **结果：高召回率、低精确率**——能找出大部分区域，但误判很多。最典型的误判是把类似 Tesco 大型超市的平坦屋顶识别为地面停车场。
- 后处理效果有限。
- 算力瓶颈：处理单张图像需耗时 7 分钟。
- 提问：手动验证应在多大样本量上进行（例如 10 到 50 个瓦片）最为合适。

> *Log line*: Reported the first Leeds test results on nine tiles — high recall but low precision, with supermarket roofs a typical false positive — and asked how many tiles to validate manually given a compute cost of seven minutes per image.

---

### 5. 2026-06-16（周二）｜边缘案例与过滤标准
**录音**：Camley Street 8

- 团队共同审视模型输出的红色高亮区域，探讨模型在复杂城市形态中的误判案例。
- **工业仓储区问题**：模型将停放大型货车/卡车的工业仓储区、物流集散地也标记为停车场。讨论认为，这证明模型能识别车辆聚集地，但这些工业用地通常不适合直接转型为住宅开发。
- **方法论建议**：在论文方法论中建立严格的过滤标准（例如剔除工业用地），或引入「低置信度」区域标记，明确界定哪些类型的停车场对本研究有实际政策意义。

> *Log line*: Reviewed model outputs on edge cases — in particular industrial and logistics yards being flagged as parking — and agreed to define explicit filtering criteria and a low-confidence class in the methodology, so that the output reflects sites with genuine redevelopment potential.

---

### 6. 2026-06-22（周一）｜与官方测绘数据对比、分析路径抉择
**录音**：Camley Street 9

- **与 OS 数据对比**：对比 AI 模型输出与官方 Ordnance Survey 测绘数据的优劣。OS 数据虽权威，但在标注非正式或未分配的停车区域时同样存在遗漏——这为使用 AI 模型提供了合理性依据。
- **分析路径二选一**（导师建议做出取舍）：
  1. 投入精力深入分析模型在不同城市区域（如市中心 vs. 郊外）的失败原因——偏方法论探讨；
  2. 接受现有误差，将精力放在某一特定城市（如利兹）进行宏观的土地潜力计算与政策讨论。
- **文档与代码**：必须在论文中诚实记录模型在真实世界应用中的局限性；建议将清理后的代码归档至 GitHub 以供日后使用或审查。

> *Log line*: Compared the model output with Ordnance Survey mapping, which also omits informal and unallocated parking; the supervisors asked me to choose between a methodological error analysis and a land-potential and policy analysis for a single city, and to archive cleaned code on GitHub.

---

### 7. 2026-07-09（周四）｜会面形式与同步安排
**录音**：Camley Street 12

- 由于各方都有全职工作或学业压力，沟通了在 Centre for Cities 线下或线上会面的可能性。
- 确认项目主要通过线上合作，团队安排在接下来的周五进行线上进度同步（sync），有条件时也支持线下碰头。

> *Log line*: Logistics check-in — confirmed the project would run mainly online, with a sync scheduled for the following Friday.

---

### 8. 2026-07-14（周二）｜模型迁移效果与训练路径
**录音**：Camley Street 13

- JiaYi 反馈：基于现有论文的模型（未经微调或重训练）直接检测英国数据，效果很不理想，尤其难以区分工业仓储区（storage yards / lorry parks）与普通停车场。
- **路径讨论**：下一步是自行标注数据「重新训练（retrain）」模型，还是继续在「后处理（post-processing）」上发力。
- JiaYi 表示：若要自行标注并重训练，受限于算力与时间，可能只能覆盖极小的一块区域。

> *Log line*: Reported that the published, un-finetuned model transferred poorly to UK imagery — especially in distinguishing storage yards and lorry parks from ordinary car parks — and weighed retraining on my own annotations against further post-processing, noting that compute and time would restrict any retraining to a very small area.

---

### 9. 2026-07-28（周二）｜界定论文核心重点
**录音**：Camley Street 14

- **导师明确建议**：不要陷入「无止尽提升计算机视觉模型精度」的技术泥潭。这是一篇**城市研究论文，不是计算机科学论文**。
- **重点应放在**：
  - 为什么现有的（基于美国数据的）模型在英国水土不服？
  - 英国的城市形态有什么特殊性？
  - 现有开源数据（如 OpenStreetMap）存在什么缺陷？
  - 识别出这些区域后，对城市规划与住房政策有何启示？

> *Log line*: The supervisors advised against pursuing further computer-vision accuracy and refocused the dissertation on why a US-trained model transfers poorly to UK urban form, what the gaps in OpenStreetMap are, and what the detected areas imply for planning and housing policy.

---

### 10. 2026-08-11（周二）｜写作冲刺与故事线
**录音**：Camley Street 15
**参会**：Clara、Esra、JiaYi

- **进度担忧**：导师发现 JiaYi 尚未开始撰写论文大纲与内容，距 8 月 20 日最终提交期限所剩时间不多。
- **紧急冲刺计划**：立即停止跑模型，先花几天时间把「研究问题（Research Questions）」「研究动机（Motivation）」「文献综述（Literature Review）」的骨架搭起来，避免最后几周因时间不够导致论文结构崩塌。
- **论文「故事线」**：即使模型表现不佳，也可以在论文中大方承认，并把**「模型在不同国家／城市形态下的局限性」作为一个重要的分析章节**来写。

> *Log line*: With the 20 August deadline approaching and writing not yet started, it was agreed that I would stop running models and first draft the research questions, motivation and literature review, and that the model's limitations across different national and urban contexts would be written up as a substantive analysis chapter rather than treated as a failure.

---

## 三、贯穿全程的几条主线

1. **定位**：城市研究论文，不是计算机视觉论文——导师在 5/19、7/28 两次明确重申。
2. **政策落点**：识别未纳入地方开发规划（unallocated）、具备住房改造潜力的地面停车场，回应住房短缺；小型及工业用地停车场不在政策视野内。
3. **技术路线的收敛**：手动标注 + 重训练（算力受限）→ OSM 空间相交后处理（5/19）→ 承认迁移局限并转为分析对象（7/28、8/11）。
4. **误差的处理方式**：从「设法消除」转为「明确界定 + 诚实记录」——过滤标准、低置信度标记、局限性专章。
5. **数据合理性论证**：OS 官方测绘同样遗漏非正式／未分配停车区域，构成使用 AI 模型的正当性依据（6/22）。

---

## 四、相关日期（非会议）

| 日期 | 事项 |
|---|---|
| 2026-05-14（周四） | 线下考试 |
| 2026-05-18（周一）前后 | CASA 硕士论文写作指导研讨会（两次） |
| 2026-08-20（周四）10:00 | **论文最终提交截止**（Moodle / Turnitin） |
