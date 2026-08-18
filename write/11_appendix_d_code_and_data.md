# Appendix D — Code and data availability

## D.1 Repository

All code written for this study is archived at **https://github.com/hou1020/Parking**. The directories referenced elsewhere in this dissertation are:

| Directory | Contents |
|---|---|
| `calculate/` | Agreement against the manual and OSM references, polygon filtering and result merging |
| `analysis/` | Validation, error attribution, sampling, ablation and calibration (§3.4–§3.9) |
| `manual/`, `fine-tuning/*.gpkg` | The manual reference labels and the 1 km² grid |
| `fine-tuning/` | Generic fine-tuning of the released checkpoint (Appendix C) |
| `targeted-finetuning/` | Targeted loss weighting and the threshold sweep (Appendix C) |
| `parking-lot-mapping-tool/` | The released pipeline, with the UK-specific tiling, inference and post-processing written for this study (§3.3) |

## D.2 Imagery

Getmapping aerial photography supplied through Digimap: 109 tiles at 0.25 m ground sample distance, three visible bands, EPSG:27700. The tile identifiers and version suffixes needed to reorder the same coverage are recorded in `parking-lot-mapping-tool/output_files/tif_processing_progress.csv` and in the download folder names under `parking-lot-mapping-tool/files/`, and every processing step from the raw tiles onward is reproducible from the code once the imagery is obtained under an equivalent licence.

## D.3 Reference data

| Source | Use | Retrieved |
|---|---|---|
| OpenStreetMap building footprints, road centrelines | Post-processing inputs (§3.3) | 25 June 2026 |
| OpenStreetMap land use, brownfield, pitch, `amenity=parking` | Error attribution only (§4.2) | 25 June 2026 |
| Ordnance Survey Open Greenspace | Sports facilities in error attribution | — |

OpenStreetMap data are © OpenStreetMap contributors, available under the Open Database Licence. Ordnance Survey Open Greenspace is published under the Open Government Licence. Neither is used as ground truth; the distinction is set out in §3.1.

## D.4 Reference labels

The 2,037 manually labelled car parks are held in the repository as GeoPackage, together with the 1 km² validation grid and the confidence attribute described in Appendix A. These are the labels against which every accuracy figure in Chapter 4 is measured, and they are original to this study.

## D.5 Model

The segmentation network is the published checkpoint of Qiam, Devunuri and Lehe (2025), obtained from the authors' release and used without modification in the primary analysis. The fine-tuned checkpoints produced for Appendix C are derived works of that release and are not redistributed; the training code and logs that generate them are in `fine-tuning/` for the generic arm and `targeted-finetuning/` for the targeted loss weighting and threshold sweep.

## D.6 Result files

Each appendix table is generated from a file in the repository rather than transcribed:

| Table | Source |
|---|---|
| Appendix B.1 | `analysis/validation_summary.csv` |
| Appendix B.2–B.4 | `analysis/accuracy_vs_distance.csv`, `analysis/accuracy_vs_distance_summary.csv` |
| Appendix C.1–C.2 | `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv` |
| Appendix C.3 | `targeted-finetuning/Parking_targeted_run2/boundary_bands_arms.csv` |
| Appendix C.4 | `targeted-finetuning/Parking_targeted_run2/selectivity.csv`, `standalone_fp_by_category.csv` |
| Appendix C.5 | `targeted-finetuning/Parking_targeted_run2/threshold_sweep/generic_threshold_selected.csv` |

## D.7 Reproduction

The city-wide inference and the fine-tuning experiments require a GPU and were run in Google Colab; the notebooks (`run_finetuning_colab.ipynb`, `run_targeted_colab.ipynb`, `threshold_sweep_colab.ipynb`) pin `transformers==4.57.1`, otherwise running against the Colab environment's own package versions, and cache intermediate outputs, so a run interrupted partway resumes rather than restarting. All other analysis runs on CPU from the committed CSVs.
