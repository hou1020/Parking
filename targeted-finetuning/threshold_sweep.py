#!/usr/bin/env python3
"""Threshold calibration for the generic Leeds fine-tuned checkpoint.

The ten validation cells select thresholds.  The fifty held-out test cells are
then scored without using their labels for threshold selection.  In Colab this
script expects the paths created by ``run_targeted_colab.ipynb``:

    /content/Parking
    /content/drive/MyDrive/Parking_finetuning_run/finetuned.ckpt
    /content/drive/MyDrive/Parking_targeted_run2

It writes three CSV files into ``Parking_targeted_run2/threshold_sweep``.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader


def default_repo() -> Path:
    colab = Path("/content/Parking")
    return colab if colab.exists() else Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    repo = default_repo()
    run2 = Path("/content/drive/MyDrive/Parking_targeted_run2")
    generic = Path("/content/drive/MyDrive/Parking_finetuning_run/finetuned.ckpt")
    parser = argparse.ArgumentParser(
        description="Select a probability threshold on 10 validation cells, then test it on 50 held-out cells."
    )
    parser.add_argument("--repo", type=Path, default=repo)
    parser.add_argument("--generic-checkpoint", type=Path, default=generic)
    parser.add_argument("--run2-dir", type=Path, default=run2)
    parser.add_argument("--output-dir", type=Path, default=run2 / "threshold_sweep")
    parser.add_argument("--threshold-start", type=float, default=0.05)
    parser.add_argument("--threshold-stop", type=float, default=0.95)
    parser.add_argument("--threshold-step", type=float, default=0.01)
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--num-workers", type=int, default=2)
    return parser.parse_args()


def log(message: str) -> None:
    print(message, flush=True)


def thresholds_from_args(args: argparse.Namespace) -> np.ndarray:
    if not 0 < args.threshold_start < args.threshold_stop < 1:
        raise SystemExit("threshold range must lie strictly between 0 and 1")
    if args.threshold_step <= 0:
        raise SystemExit("threshold step must be positive")
    values = np.arange(
        args.threshold_start,
        args.threshold_stop + args.threshold_step / 2,
        args.threshold_step,
    )
    return np.unique(np.round(np.append(values, 0.5), 6))


def prepared_ok(ft: Path) -> bool:
    index = ft / "patch_index.csv"
    train = ft / "patches/train/Masks"
    test = ft / "patches/test/Masks"
    return index.exists() and len(list(train.glob("*.png"))) == 2256 and len(list(test.glob("*.png"))) == 3200


def restore_prepared_data(ft: Path, run2: Path) -> None:
    if prepared_ok(ft):
        return
    candidates = [
        run2 / "prepared_data",
        Path("/content/drive/MyDrive/Parking_finetuning_run/prepared_data"),
    ]
    for source in candidates:
        if (source / "patch_index.csv").exists():
            log(f"restoring prepared masks from {source}")
            shutil.copy2(source / "patch_index.csv", ft / "patch_index.csv")
            shutil.copytree(source / "patches", ft / "patches", dirs_exist_ok=True)
            if prepared_ok(ft):
                return
    raise SystemExit(
        "prepared patches are missing; run the Drive/setup cells in run_targeted_colab.ipynb first"
    )


def metric(tp: int, fp: int, fn: int) -> tuple[float, float, float]:
    precision = tp / (tp + fp) if tp + fp else (0.0 if fn else float("nan"))
    recall = tp / (tp + fn) if tp + fn else float("nan")
    iou = tp / (tp + fp + fn) if tp + fp + fn else float("nan")
    return precision, recall, iou


def histogram_counts(scores: np.ndarray, truth: np.ndarray, thresholds: np.ndarray) -> np.ndarray:
    """Return TP, FP and FN for every threshold without materialising T masks."""
    # Use score > threshold.  For the two-class model, t=0.5 is therefore
    # exactly equivalent to argmax, including argmax's class-0 tie behaviour.
    strict_edges = np.nextafter(thresholds, np.inf)
    edges = np.concatenate(([-np.inf], strict_edges, [np.inf]))
    positives = scores[truth]
    negatives = scores[~truth]
    pos_hist = np.histogram(positives, bins=edges)[0]
    neg_hist = np.histogram(negatives, bins=edges)[0]
    tp = np.cumsum(pos_hist[::-1], dtype=np.int64)[::-1][1:]
    fp = np.cumsum(neg_hist[::-1], dtype=np.int64)[::-1][1:]
    fn = len(positives) - tp
    return np.column_stack((tp, fp, fn))


@torch.no_grad()
def score_thresholds(
    model,
    rows: list[dict],
    patch_root: Path,
    tif_root: Path,
    processor,
    device: torch.device,
    thresholds: np.ndarray,
    batch_size: int,
    num_workers: int,
):
    from patch_data import SourcePatchDataset

    dataset = SourcePatchDataset(
        rows,
        str(patch_root),
        str(tif_root),
        processor,
        return_index=True,
    )
    loader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=device.type == "cuda",
    )
    per_cell = {
        cell: np.zeros((len(thresholds), 3), dtype=np.int64)
        for cell in sorted({row["cell"] for row in rows})
    }
    done = 0
    for batch, ids in loader:
        pixels = batch["pixel_values"].to(device, non_blocking=True)
        labels = batch["labels"]
        logits = model(pixel_values=pixels)[0]
        upsampled = F.interpolate(
            logits,
            size=labels.shape[-2:],
            mode="bilinear",
            align_corners=False,
        )
        # Softmax is applied after interpolation.  With score > 0.5 this is
        # exactly the current two-class argmax rule, including exact ties.
        probabilities = upsampled.softmax(dim=1)[:, 1].cpu().numpy()
        truth = labels.numpy() == 1
        for batch_index, row_index in enumerate(ids.tolist()):
            row = rows[row_index]
            valid_h, valid_w = int(row["valid_h"]), int(row["valid_w"])
            scores = probabilities[batch_index, :valid_h, :valid_w].reshape(-1)
            target = truth[batch_index, :valid_h, :valid_w].reshape(-1)
            per_cell[row["cell"]] += histogram_counts(scores, target, thresholds)
        done += len(ids)
        if done % 400 < len(ids) or done == len(rows):
            log(f"  {done}/{len(rows)} patches")
    return per_cell


def summarise(per_cell: dict[str, np.ndarray], thresholds: np.ndarray, split: str) -> pd.DataFrame:
    records = []
    total = np.sum(list(per_cell.values()), axis=0)
    for index, threshold in enumerate(thresholds):
        tp, fp, fn = (int(x) for x in total[index])
        p, r, iou = metric(tp, fp, fn)
        cell_metrics = [metric(*(int(x) for x in counts[index])) for counts in per_cell.values()]
        records.append(
            {
                "split": split,
                "threshold": float(threshold),
                "precision": p,
                "recall": r,
                "iou": iou,
                "macro_precision": float(np.nanmean([x[0] for x in cell_metrics])),
                "macro_recall": float(np.nanmean([x[1] for x in cell_metrics])),
                "macro_iou": float(np.nanmean([x[2] for x in cell_metrics])),
                "tp": tp,
                "fp": fp,
                "fn": fn,
                "predicted_over_reference": (tp + fp) / (tp + fn),
            }
        )
    return pd.DataFrame(records)


def nearest_row(frame: pd.DataFrame, column: str, target: float) -> pd.Series:
    ranked = frame.assign(
        distance=(frame[column] - target).abs(),
        neg_precision=-frame["precision"],
        neg_iou=-frame["iou"],
    ).sort_values(["distance", "neg_precision", "neg_iou", "threshold"])
    return ranked.iloc[0]


def selection_rules(validation: pd.DataFrame, run2: Path) -> list[dict]:
    choices = []
    default = nearest_row(validation, "threshold", 0.5)
    choices.append({"rule": "default_0.5", "threshold": float(default.threshold)})

    best = validation.assign(distance=(validation.threshold - 0.5).abs()).sort_values(
        ["iou", "distance"], ascending=[False, True]
    ).iloc[0]
    choices.append({"rule": "best_validation_iou", "threshold": float(best.threshold)})

    log_path = run2 / "targeted_log.csv"
    table_path = run2 / "table1_overall.csv"
    if log_path.exists() and table_path.exists():
        history = pd.read_csv(log_path)
        arms = pd.read_csv(table_path)
        for prefix in ("C targeted", "D targeted"):
            match = arms[arms["model"].str.startswith(prefix)]
            if match.empty:
                continue
            epoch_match = re.search(r"e(\d+)", str(match.iloc[0]["model"]))
            if not epoch_match:
                continue
            epoch = int(epoch_match.group(1))
            target_row = history[history["epoch"] == epoch]
            if target_row.empty:
                continue
            target_recall = float(target_row.iloc[0]["val_recall"])
            selected = nearest_row(validation, "recall", target_recall)
            label = "match_" + prefix[0].lower() + f"_e{epoch}_validation_recall"
            choices.append(
                {
                    "rule": label,
                    "threshold": float(selected.threshold),
                    "target_validation_recall": target_recall,
                }
            )
    # A coarse grid can choose the same threshold under multiple rules; keep the
    # rules because their scientific meanings differ.
    return choices


def selected_summary(
    choices: list[dict], validation: pd.DataFrame, test: pd.DataFrame, run2: Path
) -> pd.DataFrame:
    rows = []
    for choice in choices:
        threshold = choice["threshold"]
        val = nearest_row(validation, "threshold", threshold)
        tst = nearest_row(test, "threshold", threshold)
        row = dict(choice)
        for prefix, source in (("val", val), ("test", tst)):
            for column in (
                "precision",
                "recall",
                "iou",
                "macro_precision",
                "macro_recall",
                "macro_iou",
                "predicted_over_reference",
            ):
                row[f"{prefix}_{column}"] = float(source[column])
        rows.append(row)

    summary = pd.DataFrame(rows)
    arms_path = run2 / "evaluation_arms.csv"
    if arms_path.exists():
        arms = pd.read_csv(arms_path)
        targets = arms[
            (arms["aggregation"] == "micro")
            & arms["model"].str.startswith(("C targeted", "D targeted"))
        ][["model", "precision", "recall", "iou"]]
        if not targets.empty:
            log("\nTargeted Run2 test points (for comparison only; never used to choose a threshold):")
            log(targets.to_string(index=False))
    return summary


def main() -> None:
    args = parse_args()
    repo = args.repo.resolve()
    ft = repo / "fine-tuning"
    tif_root = repo / "parking-lot-mapping-tool/files/tif"
    run2 = args.run2_dir
    restore_prepared_data(ft, run2)

    if not args.generic_checkpoint.exists():
        raise SystemExit(f"generic checkpoint not found: {args.generic_checkpoint}")
    if len(list(tif_root.rglob("*.tif"))) < 100:
        raise SystemExit(
            f"source TIFFs are incomplete under {tif_root}; run the clone/LFS setup cells in "
            "run_targeted_colab.ipynb first"
        )

    sys.path.insert(0, str(ft))
    from modeling import load_checkpoint, make_model, make_processor

    index = pd.read_csv(ft / "patch_index.csv")
    fit_val_path = run2 / "fit_val_split.csv"
    if not fit_val_path.exists():
        local = repo / "targeted-finetuning/Parking_targeted_run2/fit_val_split.csv"
        fit_val_path = local if local.exists() else fit_val_path
    if not fit_val_path.exists():
        raise SystemExit("fit_val_split.csv not found in Run2 or the repository")
    fit_val = pd.read_csv(fit_val_path)
    validation_cells = set(fit_val.loc[fit_val["role"] == "validation", "cell"])

    validation = index[
        (index["split"] == "train") & index["kept"] & index["cell"].isin(validation_cells)
    ].sort_values(["cell", "row_off", "col_off"])
    test = index[(index["split"] == "test") & index["kept"]].sort_values(
        ["cell", "row_off", "col_off"]
    )
    val_counts = validation.groupby("cell").size()
    test_counts = test.groupby("cell").size()
    # Match the validation sample used to select the generic and targeted
    # checkpoints: the training half retained every positive patch plus a
    # balanced sample of empty patches.  It therefore contains ten cells but
    # not all 64 patches from each cell (438 retained patches in Run2).
    if len(val_counts) != 10 or len(validation) != 438 or (val_counts == 0).any():
        raise SystemExit(
            "validation set must reproduce Run2: 10 cells / 438 retained training patches"
        )
    if len(test_counts) != 50 or not (test_counts == 64).all():
        raise SystemExit("test set must contain 50 complete cells x 64 patches")

    thresholds = thresholds_from_args(args)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    log(f"device: {device}")
    log(f"thresholds: {len(thresholds)} ({thresholds[0]:.2f} to {thresholds[-1]:.2f})")
    log(f"validation: {len(validation)} patches / {len(val_counts)} cells")
    log(f"test: {len(test)} patches / {len(test_counts)} cells")

    model = load_checkpoint(make_model(), args.generic_checkpoint, log=log).to(device).eval()
    processor = make_processor()

    log("\nscoring validation thresholds ...")
    validation_counts = score_thresholds(
        model,
        validation.to_dict("records"),
        ft / "patches/train",
        tif_root,
        processor,
        device,
        thresholds,
        args.batch_size,
        args.num_workers,
    )
    validation_curve = summarise(validation_counts, thresholds, "validation")
    choices = selection_rules(validation_curve, run2)
    log("\nthresholds selected without using test labels:")
    log(pd.DataFrame(choices).to_string(index=False))

    log("\nscoring held-out test thresholds ...")
    test_counts_by_threshold = score_thresholds(
        model,
        test.to_dict("records"),
        ft / "patches/test",
        tif_root,
        processor,
        device,
        thresholds,
        args.batch_size,
        args.num_workers,
    )
    test_curve = summarise(test_counts_by_threshold, thresholds, "test")
    summary = selected_summary(choices, validation_curve, test_curve, run2)

    default_test = nearest_row(test_curve, "threshold", 0.5)
    expected = np.array([0.7664, 0.7548, 0.6136])
    observed = default_test[["precision", "recall", "iou"]].to_numpy(dtype=float)
    if not np.all(np.abs(observed - expected) < 0.002):
        raise SystemExit(
            "t=0.5 did not reproduce generic B; stop before interpreting the sweep: "
            f"observed {observed}, expected {expected}"
        )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    validation_path = args.output_dir / "generic_threshold_validation.csv"
    test_path = args.output_dir / "generic_threshold_test.csv"
    summary_path = args.output_dir / "generic_threshold_selected.csv"
    validation_curve.to_csv(validation_path, index=False)
    test_curve.to_csv(test_path, index=False)
    summary.to_csv(summary_path, index=False)

    log("\nselected thresholds and held-out results:")
    display_columns = [
        "rule",
        "threshold",
        "val_precision",
        "val_recall",
        "val_iou",
        "test_precision",
        "test_recall",
        "test_iou",
        "test_predicted_over_reference",
    ]
    log(summary[display_columns].round(4).to_string(index=False))
    log(f"\nwrote {validation_path}")
    log(f"wrote {test_path}")
    log(f"wrote {summary_path}")


if __name__ == "__main__":
    main()
