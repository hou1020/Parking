"""Shared SegFormer construction and strict checkpoint loading for this experiment.

The released model is a PyTorch Lightning checkpoint whose network parameters are stored
under ``model.*``.  Fine-tuned checkpoints written here contain the bare Hugging Face model
state dict.  Both training and evaluation use this module so the zero-shot and fine-tuned
models cannot silently drift onto different preprocessing or loading paths.
"""
from pathlib import Path

import torch
from transformers import SegformerForSemanticSegmentation

try:
    from transformers import SegformerImageProcessor as Processor
except ImportError:  # transformers versions used by the original project
    from transformers import SegformerFeatureExtractor as Processor


BASE_MODEL = "nvidia/segformer-b5-finetuned-cityscapes-1024-1024"
PATCH_SIZE = 512
ID2LABEL = {0: "background", 1: "parking_lot"}
LABEL2ID = {v: k for k, v in ID2LABEL.items()}


def make_processor():
    """Reproduce the processor configuration in the original inference notebook."""
    processor = Processor.from_pretrained(BASE_MODEL)
    processor.do_reduce_labels = False
    # main.ipynb sets this after from_pretrained; retain that exact contract rather than
    # relying on a version-dependent Transformers default.
    processor.size = PATCH_SIZE
    return processor


def make_model():
    """Build the exact SegFormer-B5 wrapper used by the released Lightning module."""
    return SegformerForSemanticSegmentation.from_pretrained(
        BASE_MODEL,
        return_dict=False,
        num_labels=2,
        id2label=ID2LABEL,
        label2id=LABEL2ID,
        ignore_mismatched_sizes=True,
    )


def _torch_load(path):
    """Load on both older project-era torch and newer torch with weights_only support."""
    try:
        return torch.load(path, map_location="cpu", weights_only=False)
    except TypeError:
        return torch.load(path, map_location="cpu")


def load_checkpoint(model, path, log=print):
    """Load every model tensor or fail; never evaluate silently partial weights."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"checkpoint not found: {path}")
    head = path.read_bytes()[:200]
    if head.startswith(b"version https://git-lfs.github.com/spec/v1"):
        raise RuntimeError(
            f"{path} is a Git LFS pointer, not the 1 GB checkpoint; download the real "
            "UTEL-UIUC/SegFormer-large-parking best_model.ckpt first"
        )
    if path.stat().st_size < 1024:
        raise RuntimeError(f"checkpoint is unexpectedly small ({path.stat().st_size} bytes): {path}")

    blob = _torch_load(path)
    if not isinstance(blob, dict):
        raise RuntimeError(f"checkpoint has unsupported type {type(blob).__name__}: {path}")
    state = blob.get("state_dict", blob)
    if not isinstance(state, dict):
        raise RuntimeError(f"checkpoint state_dict is not a mapping: {path}")

    # Released Lightning weights: model.segformer... / model.decode_head...
    # Local fine-tuned weights: segformer... / decode_head...
    lightning = {k[len("model."):]: v for k, v in state.items() if k.startswith("model.")}
    state = lightning or state

    expected = model.state_dict()
    missing = sorted(set(expected) - set(state))
    unexpected = sorted(set(state) - set(expected))
    wrong_shape = sorted(
        k for k in set(expected).intersection(state)
        if getattr(state[k], "shape", None) != expected[k].shape
    )
    if missing or unexpected or wrong_shape:
        sample = lambda xs: ", ".join(xs[:4]) + (" ..." if len(xs) > 4 else "")
        raise RuntimeError(
            "checkpoint does not exactly match SegFormer-B5: "
            f"{len(missing)} missing [{sample(missing)}], "
            f"{len(unexpected)} unexpected [{sample(unexpected)}], "
            f"{len(wrong_shape)} wrong shape [{sample(wrong_shape)}]"
        )
    model.load_state_dict(state, strict=True)
    log(f"  checkpoint verified: {len(state)} tensors loaded exactly from {path}")
    return model
