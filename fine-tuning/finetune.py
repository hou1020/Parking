"""
Fine-tune the released checkpoint on the training half — Leeds fine-tuning experiment
Author: Hou

Runs on Colab. The local machine has an Intel integrated GPU and 8 GB of memory, which is
not enough to train a B5 encoder, so this follows the same route the original inference took
(main.ipynb mounts Drive and uses CUDA).

    !pip -q install transformers
    !python finetune.py --patches patches --ckpt best_model.ckpt

One run, one hyperparameter setting, no search. The experiment asks which error class local
supervision moves, not how well the model can be made to perform, and a tuned result would
not answer that question any better while costing days.

Design notes

    Validation cells are held out from the training cells, not sampled from the training
    patches, for the same reason the test half is split by cell: neighbouring patches share
    car parks. The test half defined in split.csv is never touched here.

    The learning rate matches the value already in the project's SegformerFinetuner
    (Adam, 2e-5). Fine-tuning all parameters on roughly two thousand patches risks washing
    out the pretrained representation, so training is short and the best epoch is selected
    on validation IoU rather than running to a fixed end.

    Parking is the minority class by a wide margin, so validation is scored on parking-class
    IoU. Pixel accuracy would sit above 0.95 for a model that predicted nothing. Synthetic
    padding is assigned label 255 and excluded from both loss and validation metrics.

Reads the patch folder and the released checkpoint. Writes only into this folder.
Outputs:
  - finetuned.ckpt
  - finetune_log.csv
  - fit_val_split.csv
"""
import os, argparse, random
import numpy as np
import pandas as pd
import torch
from torch.utils.data import DataLoader
from modeling import BASE_MODEL, PATCH_SIZE, make_processor, make_model, load_checkpoint
from patch_data import SourcePatchDataset, TileBatchSampler

HERE = os.path.dirname(os.path.abspath(__file__))
TIF_ROOT = f"{os.path.dirname(HERE)}/parking-lot-mapping-tool/files/tif"
def log(m):
    print(m, flush=True)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--patches", default=f"{HERE}/patches")
    p.add_argument("--index", default=f"{HERE}/patch_index.csv")
    p.add_argument("--tif-root", default=TIF_ROOT,
                   help="source GeoTIFF tree; image patches are read from here when not materialised")
    p.add_argument("--ckpt", default=f"{HERE}/best_model.ckpt",
                   help="released weights; Parking/model/best_model.ckpt is an LFS pointer, "
                        "so fetch the real file first")
    p.add_argument("--out", default=f"{HERE}/finetuned.ckpt")
    p.add_argument("--epochs", type=int, default=6)
    p.add_argument("--batch-size", type=int, default=2)
    p.add_argument("--lr", type=float, default=2e-5)
    p.add_argument("--val-cells", type=float, default=0.2,
                   help="share of training CELLS held back for validation")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--num-workers", type=int, default=2)
    p.add_argument("--no-amp", action="store_true",
                   help="disable CUDA mixed precision (enabled by default on GPU)")
    return p.parse_args()


@torch.no_grad()
def parking_iou(model, loader, device):
    """IoU of the parking class over a loader, at the label resolution."""
    model.eval()
    tp = fp = fn = 0
    for batch in loader:
        px = batch["pixel_values"].to(device)
        gt = batch["labels"].to(device)
        logits = model(pixel_values=px)[0]
        up = torch.nn.functional.interpolate(logits, size=gt.shape[-2:],
                                             mode="bilinear", align_corners=False)
        pred = up.argmax(1)
        valid = gt != 255
        tp += int(((pred == 1) & (gt == 1) & valid).sum())
        fp += int(((pred == 1) & (gt == 0) & valid).sum())
        fn += int(((pred != 1) & (gt == 1) & valid).sum())
    return tp / (tp + fp + fn) if (tp + fp + fn) else 0.0


def main():
    args = parse_args()
    if not 0 < args.val_cells < 1:
        raise SystemExit("--val-cells must be strictly between 0 and 1")
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(args.seed)
    rng = np.random.default_rng(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    log(f"device: {device}")
    if device.type == "cpu":
        raise SystemExit("no CUDA GPU — SegFormer-B5 fine-tuning must run on Colab/GPU")

    idx = pd.read_csv(args.index)
    tr = idx[(idx["split"] == "train") & idx["kept"]]
    cells = np.array(sorted(tr["cell"].unique()))
    rng.shuffle(cells)
    n_val = max(1, int(round(args.val_cells * len(cells))))
    val_cells, fit_cells = set(cells[:n_val]), set(cells[n_val:])

    fit_rows = tr[tr["cell"].isin(fit_cells)].to_dict("records")
    val_rows = tr[tr["cell"].isin(val_cells)].to_dict("records")
    log(f"training cells {len(fit_cells)} -> {len(fit_rows)} patches | "
        f"validation cells {len(val_cells)} -> {len(val_rows)} patches")
    log(f"held-out test half is untouched: {idx[idx['split'] == 'test']['cell'].nunique()} cells")
    pd.DataFrame([
        {"cell": c, "role": "fit" if c in fit_cells else "validation"}
        for c in sorted(fit_cells | val_cells)
    ]).to_csv(f"{HERE}/fit_val_split.csv", index=False)

    proc = make_processor()
    root = f"{args.patches}/train"
    loader_kw = dict(num_workers=args.num_workers, pin_memory=True)
    fit_ds = SourcePatchDataset(fit_rows, root, args.tif_root, proc, ignore_padding=True)
    val_ds = SourcePatchDataset(val_rows, root, args.tif_root, proc, ignore_padding=True)
    fit_batches = TileBatchSampler(fit_rows, args.batch_size, args.seed, drop_last=True)
    fit_dl = DataLoader(fit_ds, batch_sampler=fit_batches, **loader_kw)
    val_dl = DataLoader(val_ds, batch_size=args.batch_size, shuffle=False, **loader_kw)

    log("\nbuilding model ...")
    model = load_checkpoint(make_model(), args.ckpt, log=log).to(device)

    base_iou = parking_iou(model, val_dl, device)
    log(f"\nzero-shot validation parking IoU: {base_iou:.4f}")

    # Match SegformerFinetuner.configure_optimizers in the released project exactly.
    opt = torch.optim.Adam([p for p in model.parameters() if p.requires_grad],
                           lr=args.lr, eps=1e-8)
    history = [{"epoch": 0, "train_loss": None, "val_parking_iou": round(base_iou, 4),
                "note": "zero-shot"}]
    # Select among genuinely fine-tuned epochs.  Even if all degrade from zero-shot, save
    # the least-bad trained epoch so evaluate.py can produce the required comparable pair.
    best, best_epoch = -1.0, None
    use_amp = not args.no_amp
    scaler = torch.cuda.amp.GradScaler(enabled=use_amp)

    for ep in range(1, args.epochs + 1):
        model.train()
        losses = []
        for step, batch in enumerate(fit_dl, 1):
            opt.zero_grad(set_to_none=True)
            with torch.cuda.amp.autocast(enabled=use_amp):
                out = model(pixel_values=batch["pixel_values"].to(device, non_blocking=True),
                            labels=batch["labels"].to(device, non_blocking=True))
                loss = out[0]
            scaler.scale(loss).backward()
            scaler.step(opt)
            scaler.update()
            losses.append(float(loss.detach()))
            if step % 50 == 0:
                log(f"  epoch {ep} step {step}/{len(fit_dl)} loss {np.mean(losses[-50:]):.4f}")
        iou = parking_iou(model, val_dl, device)
        log(f"epoch {ep}: train loss {np.mean(losses):.4f} | val parking IoU {iou:.4f}"
            + ("  <- best" if iou > best else ""))
        history.append({"epoch": ep, "train_loss": round(float(np.mean(losses)), 4),
                        "val_parking_iou": round(iou, 4), "note": ""})
        if iou > best:
            best, best_epoch = iou, ep
            torch.save({"state_dict": model.state_dict(), "epoch": ep,
                        "val_parking_iou": iou, "zero_shot_val_parking_iou": base_iou,
                        "base_model": BASE_MODEL, "processor_size": PATCH_SIZE,
                        "seed": args.seed}, args.out)

    pd.DataFrame(history).to_csv(f"{HERE}/finetune_log.csv", index=False)
    log(f"\nbest epoch {best_epoch}, validation parking IoU {base_iou:.4f} -> {best:.4f}")
    if best <= base_iou:
        log("no fine-tuned epoch beat zero-shot on validation; the best trained epoch was "
            "still saved so the held-out comparison remains possible")
    log(f"wrote: {args.out}")
    log(f"wrote: {HERE}/fit_val_split.csv")
    log(f"wrote: {HERE}/finetune_log.csv")


if __name__ == "__main__":
    main()
