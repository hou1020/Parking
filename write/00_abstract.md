# Abstract

> **草稿 v1**｜目标 ~250 词
> 四个头条数字（0.854 / 0.571 / 1.50× / 3.26%）已全部落入正文

---

The United Kingdom holds no consistent spatial record of off-street surface parking, so the land it occupies is missing from densification debates — even as national planning policy names car parks explicitly among the under-utilised land authorities should bring forward. Segmentation of aerial imagery offers a route needing neither institutional records nor fieldwork, and a model trained for the task has been published, but whether it transfers to British cities has not been tested.

This dissertation applies that US-trained model, exactly as released and with no UK training data, to 100 km² of Leeds, evaluating it against 2,037 manually labelled car parks drawn to the source model's own target definition. Rather than reporting accuracy alone, it decomposes the error: attributed against independent reference layers, characterised by stratified sampling of 142 image chips adjudicated on the imagery the model actually consumed, and tested by ablating the post-processing stage.

Transfer proves asymmetric. Recall is **0.854** and spatially even; precision is **0.571**, and predicted area is **1.50 times** the labelled area. Error is concentrated in boundary placement rather than misrecognition — the genuine blind spot is at most 2.1% of labelled area — and the post-processing pipeline creates a blind spot of its own, deleting four fifths of the rooftop parking that the raw model detects more reliably than parking at ground level.

Measured against that reliability, the labelled reference puts surface parking at **3.26%** of the study area, concentrated in the inner 2 km and declining sharply beyond it. The over-prediction is systematic and correctable to within about ±7% at half-city scale, though not at the scale of a single square kilometre. A transferred map cannot measure how much land a city gives to parking on its own; paired with one local validation, it can — a materially different claim from either accepting or dismissing it.
