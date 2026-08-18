# Appendix D — Code and data availability

## D.1 Repository

All code written for this study is archived at **https://github.com/hou1020/Parking**. The directories referenced elsewhere in this dissertation are:

| Directory | Contents |
|---|---|
| `calculate/` | Tiling, inference and post-processing over the 100 km² study area (§3.4) |
| `analysis/` | Validation, error attribution, sampling, ablation and calibration (§3.5–§3.8) |
| `manual/`, `fine-tuning/*.gpkg` | The manual reference labels and the 1 km² grid |
| `fine-tuning/` | Generic fine-tuning of the released checkpoint (Appendix C) |
| `targeted-finetuning/` | Targeted loss weighting and the threshold sweep (Appendix C) |
| `parking-lot-mapping-tool/` | The released pipeline as obtained from its authors, unmodified |

## D.2 Imagery

Getmapping aerial photography supplied through Digimap: 109 tiles at 0.25 m ground sample distance, three visible bands, EPSG:27700. This imagery is licensed to UCL for academic use and **cannot be redistributed**, so it is not held in the repository. The tile identifiers and version suffixes needed to reorder the same coverage are recorded in `calculate/`, and every processing step from the raw tiles onward is reproducible from the code once the imagery is obtained under an equivalent licence.

## D.3 Reference data

| Source | Use | Retrieved |
|---|---|---|
| OpenStreetMap building footprints, road centrelines | Post-processing inputs (§3.4) | 25 June 2026 |
| OpenStreetMap land use, brownfield, pitch, `amenity=parking` | Error attribution only (§4.2) | 25 June 2026 |
| Ordnance Survey Open Greenspace | Sports facilities in error attribution | — |

OpenStreetMap data are © OpenStreetMap contributors, available under the Open Database Licence. Ordnance Survey Open Greenspace is published under the Open Government Licence. Neither is used as ground truth; the distinction is set out in §3.1.

## D.4 Reference labels

The 2,037 manually labelled car parks are held in the repository as GeoPackage, together with the 1 km² validation grid and the confidence attribute described in Appendix A. These are the labels against which every accuracy figure in Chapter 4 is measured, and they are original to this study.

## D.5 Model

The segmentation network is the published checkpoint of Qiam, Devunuri and Lehe (2025), obtained from the authors' release and used without modification in the primary analysis. The fine-tuned checkpoints produced for Appendix C are derived works of that release and are not redistributed; the training code and logs that generate them are in `targeted-finetuning/`.

## D.6 Result files

Each table in this dissertation is generated from a file in the repository rather than transcribed:

| Table | Source |
|---|---|
| Appendix B.1 | `analysis/validation_summary.csv` |
| Appendix B.2–B.4 | `analysis/accuracy_vs_distance.csv`, `analysis/accuracy_vs_distance_summary.csv` |
| Appendix C.1–C.2 | `targeted-finetuning/Parking_targeted_run2/evaluation_arms.csv` |
| Appendix C.3 | `targeted-finetuning/Parking_targeted_run2/boundary_bands_arms.csv` |
| Appendix C.4 | `targeted-finetuning/Parking_targeted_run2/selectivity.csv`, `standalone_fp_by_category.csv` |
| Appendix C.5 | `targeted-finetuning/Parking_targeted_run2/threshold_sweep/generic_threshold_selected.csv` |

## D.7 Reproduction

The city-wide inference and the fine-tuning experiments require a GPU and were run in Google Colab; the notebooks (`run_finetuning_colab.ipynb`, `run_targeted_colab.ipynb`, `threshold_sweep_colab.ipynb`) pin the package versions they depend on and cache intermediate outputs, so a run interrupted partway resumes rather than restarting. All other analysis runs on CPU from the committed CSVs.
