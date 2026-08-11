"""
Compare the two models on the held-out half — Leeds fine-tuning experiment
Author: Hou

Runs on Colab, after finetune.py.

    !python evaluate.py --patches patches --zero-shot best_model.ckpt --finetuned finetuned.ckpt

The comparison is zero-shot against fine-tuned on the SAME 50 held-out cells, under
identical preprocessing. It is not a comparison against the 0.571 / 0.854 figures in
Chapter 4: those were computed over all 100 cells with polygonisation, the 1,000 px²
minimum and the OSM subtraction applied. Setting a fine-tuned half against a whole-area
baseline is the usual way this experiment produces a fake improvement, so the numbers here
are internally comparable to each other and to nothing else.

What is reported, and why each row is there

    micro          area-weighted over all held-out pixels; answers whether total predicted
                   area improved
    macro          per cell, then averaged; every cell counts equally, so it is sensitive to
                   the sparse cells where the main analysis found performance worst
    boundary band  FP is split by distance from the label; FN is split by distance from the
                   prediction, exactly as in Chapter 3. The complete 1 km cell is rebuilt
                   before distances are measured, so 512 px patch seams are not mistaken
                   for parking boundaries. This is the comparison the experiment exists for.

Padding is excluded everywhere using valid_h / valid_w from the index: the last patch in
each row and column of a 4000 px tile carries 96 px of zeros, and counting predictions there
would penalise whichever model is more willing to predict on black.

Reads the patch folder and both checkpoints. Writes only into this folder.
Output:
  - evaluation.csv
  - boundary_bands.csv (2, 5 and 10 m sensitivity thresholds)
"""
import os, argparse
import numpy as np
import pandas as pd
import torch
from torch.utils.data import DataLoader
from scipy import ndimage
from modeling import make_processor, make_model, load_checkpoint
from patch_data import SourcePatchDataset

HERE = os.path.dirname(os.path.abspath(__file__))
TIF_ROOT = f"{os.path.dirname(HERE)}/parking-lot-mapping-tool/files/tif"
PIXEL_M = 0.25
BANDS_M = (2, 5, 10)              # same sensitivity thresholds as the main analysis


def log(m):
    print(m, flush=True)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--patches", default=f"{HERE}/patches")
    p.add_argument("--index", default=f"{HERE}/patch_index.csv")
    p.add_argument("--tif-root", default=TIF_ROOT,
                   help="source GeoTIFF tree; image patches are read from here when not materialised")
    p.add_argument("--zero-shot", default=f"{HERE}/best_model.ckpt")
    p.add_argument("--finetuned", default=f"{HERE}/finetuned.ckpt")
    p.add_argument("--batch-size", type=int, default=4)
    p.add_argument("--num-workers", type=int, default=2)
    p.add_argument("--out", default=f"{HERE}/evaluation.csv")
    p.add_argument("--boundary-out", default=f"{HERE}/boundary_bands.csv")
    p.add_argument("--allow-zero-only", action="store_true",
                   help="permit a diagnostic zero-shot run when the fine-tuned file is absent")
    return p.parse_args()


def load_model(path, device):
    return load_checkpoint(make_model(), path, log=log).to(device).eval()


def add_cell_scores(pred, gt, per_cell, bands, cell):
    """Score one complete 1 km cell, so patch seams never become artificial boundaries."""
    tp_mask = pred & gt
    fp_mask = pred & ~gt
    fn_mask = ~pred & gt
    tp, fp, fn = int(tp_mask.sum()), int(fp_mask.sum()), int(fn_mask.sum())
    per_cell[cell] = [tp, fp, fn]

    if gt.any():
        distance_to_gt = ndimage.distance_transform_edt(~gt)
        for metres in BANDS_M:
            near = distance_to_gt <= metres / PIXEL_M
            n = int((fp_mask & near).sum())
            bands[metres]["fp_dilation"] += n
            bands[metres]["fp_standalone"] += fp - n
        del distance_to_gt
    else:
        for metres in BANDS_M:
            bands[metres]["fp_standalone"] += fp

    # The dissertation defines erosion against the PREDICTION: missed reference area
    # within d of something detected.  Eroding the reference itself would incorrectly
    # call the outer edge of a completely missed lot a boundary error.
    if pred.any():
        distance_to_pred = ndimage.distance_transform_edt(~pred)
        for metres in BANDS_M:
            near = distance_to_pred <= metres / PIXEL_M
            n = int((fn_mask & near).sum())
            bands[metres]["fn_erosion"] += n
            bands[metres]["fn_standalone"] += fn - n
        del distance_to_pred
    else:
        for metres in BANDS_M:
            bands[metres]["fn_standalone"] += fn


@torch.no_grad()
def score(model, rows, root, tif_root, proc, device, batch_size, num_workers):
    """Infer patches, rebuild each cell, then compute confusion and distance terms."""
    dataset = SourcePatchDataset(rows, root, tif_root, proc, return_index=True)
    dl = DataLoader(dataset, batch_size=batch_size,
                    shuffle=False, num_workers=num_workers, pin_memory=device.type == "cuda")
    per_cell = {}
    bands = {m: {"fp_dilation": 0, "fp_standalone": 0,
                 "fn_erosion": 0, "fn_standalone": 0} for m in BANDS_M}
    shapes = {}
    for r in rows:
        h, w = shapes.get(r["cell"], (0, 0))
        shapes[r["cell"]] = (max(h, r["row_off"] + r["valid_h"]),
                              max(w, r["col_off"] + r["valid_w"]))

    active = None
    pred_cell = gt_cell = None
    done = 0
    for batch, ids in dl:
        px = batch["pixel_values"].to(device, non_blocking=True)
        gt = batch["labels"].to(device, non_blocking=True)
        logits = model(pixel_values=px)[0]
        up = torch.nn.functional.interpolate(logits, size=gt.shape[-2:],
                                             mode="bilinear", align_corners=False)
        pred = up.argmax(1).cpu().numpy()
        gtn = gt.cpu().numpy()

        for b, i in enumerate(ids.tolist()):
            r = rows[i]
            if active != r["cell"]:
                if active is not None:
                    add_cell_scores(pred_cell, gt_cell, per_cell, bands, active)
                active = r["cell"]
                pred_cell = np.zeros(shapes[active], dtype=bool)
                gt_cell = np.zeros(shapes[active], dtype=bool)
            vh, vw = r["valid_h"], r["valid_w"]
            p = pred[b][:vh, :vw] == 1
            g = gtn[b][:vh, :vw] == 1
            rr, cc = r["row_off"], r["col_off"]
            pred_cell[rr:rr + vh, cc:cc + vw] = p
            gt_cell[rr:rr + vh, cc:cc + vw] = g
        done += len(ids)
        if done % 400 < batch_size:
            log(f"    {done}/{len(rows)} patches")
    if active is not None:
        add_cell_scores(pred_cell, gt_cell, per_cell, bands, active)
    return per_cell, bands


def metrics(tp, fp, fn):
    # A labelled cell with no predictions has precision 0, not a free pass in the macro
    # average.  Only a genuinely empty union is undefined.
    p = tp / (tp + fp) if tp + fp else (0.0 if fn else float("nan"))
    r = tp / (tp + fn) if tp + fn else float("nan")
    i = tp / (tp + fp + fn) if tp + fp + fn else float("nan")
    return p, r, i


def main():
    args = parse_args()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    log(f"device: {device}")

    idx = pd.read_csv(args.index)
    test = idx[(idx["split"] == "test") & idx["kept"]].copy()
    counts = test.groupby("cell").size()
    if len(counts) != 50 or not (counts == 64).all():
        raise SystemExit("held-out set is incomplete: expected 50 cells × 64 patches; "
                         "run make_patches.py without --limit")
    test = test.sort_values(["cell", "row_off", "col_off"])
    rows = test.to_dict("records")
    log(f"held-out: {len(rows)} patches across {idx[idx['split']=='test']['cell'].nunique()} cells")

    proc = make_processor()
    root = f"{args.patches}/test"

    todo = [("zero-shot", args.zero_shot)]
    if os.path.exists(args.finetuned):
        todo.append(("fine-tuned", args.finetuned))
    elif not args.allow_zero_only:
        raise SystemExit(f"fine-tuned checkpoint not found: {args.finetuned}; run finetune.py "
                         "or pass --allow-zero-only for a diagnostic baseline")
    else:
        log(f"note: {args.finetuned} not found — scoring the zero-shot model only")

    out, boundary_out = [], []
    for name, path in todo:
        log(f"\nscoring {name} ...")
        model = load_model(path, device)
        per_cell, bands = score(model, rows, root, args.tif_root, proc, device, args.batch_size,
                                args.num_workers)
        del model
        if device.type == "cuda":
            torch.cuda.empty_cache()

        tp = sum(v[0] for v in per_cell.values())
        fp = sum(v[1] for v in per_cell.values())
        fn = sum(v[2] for v in per_cell.values())
        mp, mr, mi = metrics(tp, fp, fn)
        cell_m = [metrics(*v) for v in per_cell.values() if sum(v)]
        px_km2 = PIXEL_M * PIXEL_M / 1e6
        working = bands[5]

        out.append({
            "model": name, "aggregation": "micro",
            "precision": round(mp, 4), "recall": round(mr, 4), "iou": round(mi, 4),
            "tp_km2": round(tp * px_km2, 4), "fp_km2": round(fp * px_km2, 4),
            "fn_km2": round(fn * px_km2, 4),
            "fp_dilation_km2": round(working["fp_dilation"] * px_km2, 4),
            "fp_dilation_pct": round(100 * working["fp_dilation"] / max(fp, 1), 1),
            "fn_erosion_km2": round(working["fn_erosion"] * px_km2, 4),
            "fn_erosion_pct": round(100 * working["fn_erosion"] / max(fn, 1), 1),
            "fp_standalone_km2": round(working["fp_standalone"] * px_km2, 4),
            "fn_standalone_km2": round(working["fn_standalone"] * px_km2, 4)})
        out.append({
            "model": name, "aggregation": "macro",
            "precision": round(float(np.nanmean([m[0] for m in cell_m])), 4),
            "recall": round(float(np.nanmean([m[1] for m in cell_m])), 4),
            "iou": round(float(np.nanmean([m[2] for m in cell_m])), 4)})
        for metres, terms in bands.items():
            boundary_out.append({
                "model": name, "distance_m": metres,
                "fp_dilation_km2": round(terms["fp_dilation"] * px_km2, 4),
                "fp_dilation_pct": round(100 * terms["fp_dilation"] / max(fp, 1), 1),
                "fp_standalone_km2": round(terms["fp_standalone"] * px_km2, 4),
                "fn_erosion_km2": round(terms["fn_erosion"] * px_km2, 4),
                "fn_erosion_pct": round(100 * terms["fn_erosion"] / max(fn, 1), 1),
                "fn_standalone_km2": round(terms["fn_standalone"] * px_km2, 4),
            })

    df = pd.DataFrame(out)
    df.to_csv(args.out, index=False)
    pd.DataFrame(boundary_out).to_csv(args.boundary_out, index=False)
    log(f"\nwrote: {args.out}")
    log(f"wrote: {args.boundary_out}\n")
    log(df.to_string(index=False))

    if len(todo) == 2:
        z = df[(df.model == "zero-shot") & (df.aggregation == "micro")].iloc[0]
        f = df[(df.model == "fine-tuned") & (df.aggregation == "micro")].iloc[0]
        log("\nwhat moved (micro, held-out half only)")
        for k in ["precision", "recall", "iou"]:
            log(f"  {k:<10} {z[k]:.4f} -> {f[k]:.4f}   ({f[k]-z[k]:+.4f})")
        log(f"  boundary dilation as a share of FP  {z.fp_dilation_pct:.1f}% -> {f.fp_dilation_pct:.1f}%")
        log(f"  boundary erosion as a share of FN   {z.fn_erosion_pct:.1f}% -> {f.fn_erosion_pct:.1f}%")
        log(f"  standalone FP  {z.fp_standalone_km2:.4f} -> {f.fp_standalone_km2:.4f} km²")
        log("\nRead the standalone terms, not just IoU: the experiment is about which error "
            "class moved, and a rise in IoU driven entirely by the boundary band would mean "
            "something quite different from one driven by standalone false positives.")


if __name__ == "__main__":
    main()
