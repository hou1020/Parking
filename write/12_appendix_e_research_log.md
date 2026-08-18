# Appendix E — Research log

## E.1 Note on this log

This log records the supervision meetings, tasks, problems and outputs of the dissertation project between April and August 2026. It is compiled from two sources: the record of supervision meetings held with CASA and Centre for Cities (Section E.2), and the commit history of the project repository, archived at **https://github.com/hou1020/Parking** (Section E.3).

Two points on how the dates should be read. First, commit dates record when work was committed to the repository, which may lag when it was carried out. Second, the manual annotation described in Phase 4 was carried out in QGIS and stored outside the repository, so it leaves no commits; the dates given for that phase come from the annotation files themselves.

## E.2 Supervision meetings

Thirteen meeting recordings were made across ten meetings; the kick-off meeting of 27 April is recorded in four segments.

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

## E.3 Project timeline

### Phase 1 — Scoping and data acquisition (27 April – 14 May)

The topic was agreed at the kick-off meeting: applying a published deep-learning segmentation model to detect off-street surface parking in a UK city, with the policy aim of identifying land that is not allocated in local development plans but has housing potential. Aerial imagery was ordered and downloaded from Digimap during this period. No code was written; the meeting of 5 May records that data had been obtained but no model runs attempted, with taught-module coursework and an examination on 14 May taking priority.

### Phase 2 — Replicating the published pipeline and first UK transfer (15 – 29 May)

*Nine commits.*

The repository was initialised on 15 May with the published parking-lot mapping tool of Qiam et al. (2025), its trained checkpoint, and the core literature. The first obstacle was format rather than method: the published tool expects georeferenced GeoTIFF input, whereas Digimap delivers JPEG images with separate world and metadata files. `make_uk_geotiff.py` was written to convert them. The first inference was run on a single Edinburgh tile (`nt2774`).

On 29 May the study area was moved to Leeds and nine tiles (`se2526`–`se2728`, a 3×3 block) were added and put through batch inference. Three defects surfaced and were fixed the same day: malformed output polygons, an incorrect coordinate reference, and a thread-pool worker limit that stalled batch runs.

The first post-processing was added at the end of the same day: minimum-area filters at 500, 1,000 and 2,500 m², merging of per-tile outputs into a single layer, and removal of predictions falling on OpenStreetMap buildings and roads. Agreement against OSM parking polygons was computed at each filter threshold, giving the first quantitative sense of how the model performed on UK imagery.

### Phase 3 — Validation infrastructure (2 – 25 June)

*Six commits.*

The 2 June meeting established the central problem: recall was high but precision was low, with the flat roofs of large supermarkets the characteristic false positive. Reviewing outputs with supervisors on 16 June added a second systematic confusion — industrial and logistics yards, where vehicles cluster but redevelopment for housing is not realistic — and it became clear that agreement with OSM was not a sufficient basis for evaluation, since OSM parking is itself incomplete.

Work therefore turned to manual ground truth. A validation boundary was defined on 16 June, and on 23 June `calculate_manual_agreement.py` and a first manually annotated validation layer were committed, producing agreement metrics against manual labels rather than against OSM.

Three pieces of infrastructure were settled on 25 June: aerial data was moved onto Git LFS, OpenStreetMap retrieval was switched to the Overpass API in `post_processing_uk.py`, and Colab outputs were redirected to Drive so that results survived session resets.

### Phase 4 — Manual annotation and redirection (26 June – 2 August)

*No commits. Dates from annotation files.*

This is the longest stretch of the project without a commit, and the work in it was annotation rather than code. The sequence is recorded in the annotation files: the annotation frame and sampling grid were built on 26 June (`leeds_boundry.gpkg`, `leeds_grid.gpkg`); the proposal was revised on 30 June; the validation annotation set was completed on 19 July (`leeds_manual_validation.gpkg`); the annotation rules were written down on 21 July (`Rules.md`); and the main annotation set was completed on 28 July (`leeds_manual.gpkg`), together with `validate_removal_vs_manual.py`, which tests the OSM-removal step against the manual labels.

Writing the rules down was the more consequential of these steps. Because the model is validated against these labels, the labels have to match the definition the model was trained on, so the rules were aligned to Qiam et al. (2025) — the same off-street surface target, pavement-edge boundaries, rooftop parking included only where the surface is visible, and no minimum-size threshold — with any deviation recorded so that errors caused by definition differences could be separated from true model errors.

Three meetings fell in this window. On 14 July I reported that the un-finetuned model transferred poorly to UK imagery and discussed whether to retrain on my own annotations or continue with post-processing; compute and time meant retraining could only cover a very small area. On 28 July the supervisors advised against pursuing further accuracy and redirected the dissertation towards the question of why the model fails in the UK context and what that implies for planning.

### Phase 5 — City-wide run and error analysis (3 – 10 August)

*Four commits.*

With the redirection settled, inference was extended from the nine-tile test block to the full Leeds study area on 3 August — 100 tiles, 413 output files — and the emphasis shifted from improving predictions to characterising their errors. False-positive analysis was added the same day, using OS Open Greenspace among the reference layers, alongside the results of validating the removal step against manual labels.

On 5 August three analyses were added: false negatives broken down by class, an ablation of the post-processing steps, and accuracy as a function of distance from the city centre — the last of these addressing the supervisors' question of whether the model fails differently in the centre and the suburbs. A stratified sampling design for error inspection followed on 7 August, and on 10 August 142 image chips were cut for visual inspection, together with a full mosaic and a parking-extent map.

### Phase 6 — Calibration, fine-tuning and the start of writing (11 – 12 August)

*Eight commits.*

The morning of 11 August was spent on a calibration-transfer analysis and a co-registration check, and on generating the first methods figures. A Colab fine-tuning notebook was then built and iterated through six commits in a single afternoon, using the manual annotations and grid produced in Phase 4.

The meeting later that day found that no writing had begun, and it was agreed to stop modelling and draft the research questions, motivation and literature review first. `02_background.md`, the first dissertation chapter in the repository, was committed the following day, 12 August, along with the results figures.

### Phase 7 — Write-up and targeted fine-tuning (13 – 20 August)

*Five commits to date.*

The remaining chapters — abstract, introduction, results, discussion and conclusion — and the reference list were committed on 16 August. A targeted fine-tuning experiment was set up and iterated the same day, with the calibration-transfer error table added and the methods and results figures regenerated. The remaining time before submission was given to the front matter, reducing the manuscript to the word limit, and proofreading.

## E.4 Reflection

The log records a project that changed shape twice. It began as an attempt to apply a published US-trained model to UK imagery; when that transferred poorly, it became an attempt to fix the predictions through post-processing; and after the meeting of 28 July it became an analysis of why the transfer fails and what the result implies for planning policy. The final framing treats the model's limitations as the object of study rather than an obstacle to it, which is both more honest about what the evidence supports and better matched to a dissertation in urban research.

The single stretch without commits, from 26 June to 2 August, was the period of manual annotation. It produced no code, but it produced the ground truth on which every accuracy figure in this dissertation rests, and the rule set that makes those figures comparable to the study the model came from. The clearest effect of supervision is visible in the version history on 11–12 August: modelling stopped, and the first chapter entered the repository the following day.
