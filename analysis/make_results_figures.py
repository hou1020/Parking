"""
Figures for the results chapter — Leeds
Author: Hou

    fig_accuracy_maps.png   precision, recall and IoU per 1 km cell (4.1)
    fig_error_composition.png   what the FP and FN area is made of, two levels deep (4.2, 4.3)
    fig_error_chips.png     one worked example of each failure category (4.2, 4.3)
    fig_ablation.png        the post-processing trade-off on the precision-recall plane (4.4)

Reads read-only. Writes only into write/figures/.
"""
import os, glob
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon
from matplotlib.lines import Line2D
from PIL import Image
import warnings; warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUTDIR = f"{ROOT}/Parking/write/figures"
os.makedirs(OUTDIR, exist_ok=True)

CENTRE = (429832.0, 433449.0)
INK, MUTED = "#1f2933", "#7b8794"
BOUNDARY, ATTRIB, RESID = "#8fb3d9", "#4878a8", "#c9412e"
WARM, GREY = "#d98f4a", "#b8b2a7"


def log(m):
    print(m, flush=True)


# ------------------------------------------------- figure 4.1  accuracy maps
log("fig_accuracy_maps ...")
grid = gpd.read_file(f"{ROOT}/manual/leeds_grid.gpkg").to_crs(27700)
per = pd.read_csv(f"{HERE}/validation_percell.csv")
g = grid.merge(per, on=["col_index", "row_index"], how="left")

fig, axes = plt.subplots(1, 3, figsize=(13.6, 5.2))
for ax, col, name in zip(axes, ["prec_all", "rec_all", "iou_all"],
                         ["Precision", "Recall", "IoU"]):
    empty = g[g["manual_all_m2"].fillna(0) == 0]
    filled = g[g["manual_all_m2"].fillna(0) > 0]
    filled.plot(ax=ax, column=col, cmap="RdYlBu", vmin=0.2, vmax=1.0,
                edgecolor="white", linewidth=.4)
    if len(empty):
        empty.plot(ax=ax, facecolor="#e8e6e1", edgecolor="white", linewidth=.4,
                   hatch="///")
    ax.plot(*CENTRE, marker="o", ms=6, mfc="white", mec=INK, mew=1.5, zorder=5)
    med = filled[col].median()
    ax.set_title(f"{name}\nmedian {med:.2f}", fontsize=10, color=INK)
    ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)

sm = plt.cm.ScalarMappable(cmap="RdYlBu", norm=plt.Normalize(0.2, 1.0))
cb = fig.colorbar(sm, ax=axes, orientation="horizontal", fraction=.04, pad=.04,
                  aspect=45)
cb.set_label("per-cell value, common scale", fontsize=9)
fig.legend(handles=[
    Line2D([], [], marker="o", color="none", mfc="white", mec=INK, mew=1.5,
           label="city centre"),
    MplPolygon([(0, 0)], facecolor="#e8e6e1", hatch="///", edgecolor="white",
               label="no labelled parking in cell (recall and IoU undefined)")],
    loc="lower center", ncol=2, fontsize=8.5, frameon=False, bbox_to_anchor=(.5, -.02))
fig.savefig(f"{OUTDIR}/fig_accuracy_maps.png", dpi=200, bbox_inches="tight",
            facecolor="white")
log(f"  wrote {OUTDIR}/fig_accuracy_maps.png")


# ------------------------------------- figure 4.2  error composition, 2 levels
log("fig_error_composition ...")
FP_L1 = [("boundary dilation (≤5 m)", 28.8, BOUNDARY),
         ("industrial / commercial", 29.6, ATTRIB),
         ("road-adjacent", 11.6, ATTRIB),
         ("OSM parking", 4.7, ATTRIB),
         ("sports courts", 2.5, ATTRIB),
         ("brownfield", 1.7, ATTRIB),
         ("unexplained", 21.0, RESID)]
FP_L2 = [("genuine misdetection", 44.5, RESID),
         ("definitional difference\n(driveways, on-street)", 34.9, WARM),
         ("real parking the\nlabelling missed", 17.2, GREY),
         ("other", 3.3, "#dcd8d0")]
FN_L1 = [("fringe of a detected lot", 44.4, BOUNDARY),
         ("partly detected lot", 31.8, "#6f9dc9"),
         ("whole lot missed", 23.8, RESID)]
FN_L2 = [("deleted by post-processing", 31.9, WARM),
         ("genuinely not detected", 61.8, RESID),
         ("rooftop", 2.9, GREY), ("inside OSM buildings", 3.4, "#dcd8d0")]


def stacked(ax, segs, y, h, label_min=4.0, fs=8.0):
    x = 0.0
    spans = {}
    for name, val, colour in segs:
        ax.barh(y, val, left=x, height=h, color=colour, edgecolor="white", lw=1.2)
        if val >= label_min:
            ax.text(x + val / 2, y, f"{val:.1f}%", ha="center", va="center",
                    fontsize=fs, color="white" if colour in (ATTRIB, RESID, WARM) else INK,
                    fontweight="bold")
        spans[name] = (x, x + val)
        x += val
    return spans


def place_labels(ax, segs, spans, y, h, up, fs=8.2, wide=13.0):
    """Name each segment. Wide ones sit centred against the bar; narrow ones are
    staggered outwards on leader lines, which is the only way rows like the 2.9%
    and 3.4% tails stay legible next to each other."""
    sign = 1 if up else -1
    edge = y + sign * h / 2
    tier = 0
    for name, val, _ in segs:
        a, b = spans[name]
        mid = (a + b) / 2
        if b - a >= wide:
            ax.text(mid, edge + sign * .12, name, ha="center",
                    va="bottom" if up else "top", fontsize=fs, color=INK,
                    linespacing=1.3)
        else:
            depth = .34 + .30 * (tier % 3)
            ax.plot([mid, mid], [edge + sign * .05, edge + sign * depth],
                    color=MUTED, lw=.7, zorder=1)
            text = name if val >= label_pct_floor else f"{name}  {val:.1f}%"
            ax.text(mid, edge + sign * (depth + .04), text, ha="center",
                    va="bottom" if up else "top", fontsize=fs - .4, color=INK,
                    linespacing=1.3)
            tier += 1


label_pct_floor = 4.0


fig, axes = plt.subplots(2, 1, figsize=(12.4, 7.6))
for ax, l1, l2, expand, total, title in [
        (axes[0], FP_L1, FP_L2, "unexplained", "2.0937 km²",
         "False positives — what the over-prediction is made of"),
        (axes[1], FN_L1, FN_L2, "whole lot missed", "0.4749 km²",
         "False negatives — what the missed area is made of")]:
    spans = stacked(ax, l1, 1.0, .42)
    spans2 = stacked(ax, l2, -0.4, .42)
    x0, x1 = spans[expand]
    ax.add_patch(MplPolygon([(x0, 1.0 - .21), (x1, 1.0 - .21), (100, -.19), (0, -.19)],
                            closed=True, facecolor=RESID, alpha=.09, lw=0, zorder=0))
    place_labels(ax, l1, spans, 1.0, .42, up=True)
    place_labels(ax, l2, spans2, -0.4, .42, up=False)
    ax.text(-2, 1.0, f"all\n{total}", ha="right", va="center", fontsize=8.6,
            color=INK, fontweight="bold", linespacing=1.3)
    ax.text(-2, -0.4, f"of the\n{expand}", ha="right", va="center", fontsize=8.6,
            color=MUTED, linespacing=1.3)
    ax.set_xlim(-1, 101); ax.set_ylim(-2.0, 2.5)
    ax.axis("off")
    ax.set_title(title, fontsize=10.5, color=INK, loc="left", pad=6)

fig.tight_layout(h_pad=2.4)
fig.savefig(f"{OUTDIR}/fig_error_composition.png", dpi=200, bbox_inches="tight",
            facecolor="white")
log(f"  wrote {OUTDIR}/fig_error_composition.png")


# --------------------------------------------- figure 4.3  worked chip examples
log("fig_error_chips ...")
idx = pd.read_csv(f"{HERE}/chips/index.csv")
res = pd.read_csv(f"{HERE}/sampling_results.csv")
share = {(r.source, r.category): r.pct_of_population for r in res.itertuples()}

WANT = [("fp_other", "grey_hardstanding"), ("fp_other", "goods_yard"),
        ("fp_other", "sports_court"), ("fp_other", "unpaved_ground"),
        ("fp_other", "private_driveway"), ("fp_other", "on_street"),
        ("fn_other", "irregular_layout"), ("fn_other", "obscured"),
        ("fn_other", "unusual_surface"), ("fn_other", "no_cars_present"),
        ("fn_other", "lorry_van_lot"), ("fn_other", "no_markings")]

def black_fraction(path):
    """Some samples sit on a tile edge and half the chip is empty. Those are useless
    as worked examples, so candidates are screened before the largest is chosen."""
    a = np.array(Image.open(path).convert("RGB"))
    return float((a.sum(axis=2) < 24).mean())


fig, axes = plt.subplots(4, 3, figsize=(11.4, 15.4))
for ax, (src, cat) in zip(axes.ravel(), WANT):
    sel = idx[(idx["source"] == src) & (idx["category"] == cat)].copy()
    if sel.empty:
        ax.axis("off"); continue
    sel["path"] = sel["sample_id"].map(lambda s: f"{HERE}/chips/{src}/{s}.png")
    sel["black"] = sel["path"].map(black_fraction)
    usable = sel[sel["black"] < 0.06]
    row = (usable if len(usable) else sel.sort_values("black")).sort_values(
        "area_m2", ascending=False).iloc[0]
    if row["black"] >= 0.06:
        log(f"  note: every {cat} chip has imagery gaps; using the cleanest")
    ax.imshow(np.array(Image.open(row["path"])))
    pct = share.get((src, cat))
    tag = "FP" if src == "fp_other" else "FN"
    ax.set_title(f"{tag} · {cat.replace('_', ' ')}\n"
                 f"{pct:.1f}% of the residual · {row['area_m2']:.0f} m²",
                 fontsize=9, color=INK, linespacing=1.35)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color(RESID if src == "fp_other" else ATTRIB); s.set_linewidth(2)

fig.suptitle("Worked examples of each failure category, on the Digimap imagery the model saw\n"
             "red = the sampled polygon   ·   blue = the model's prediction   ·   "
             "yellow = other labelled parking nearby", fontsize=10.5, y=.995)
fig.tight_layout(rect=[0, 0, 1, .985])
fig.savefig(f"{OUTDIR}/fig_error_chips.png", dpi=140, bbox_inches="tight",
            facecolor="white")
log(f"  wrote {OUTDIR}/fig_error_chips.png")


# ------------------------------------------------------- figure 4.4  ablation
log("fig_ablation ...")
ab = pd.read_csv(f"{HERE}/ablation_summary.csv")
ab = ab[~ab["variant"].str.startswith("D*")].copy()
ab["tag"] = ab["variant"].str.extract(r"^([A-H])")

fig, ax = plt.subplots(figsize=(8.8, 6.4))
XLIM, YLIM = (.18, 1.0), (.455, .635)
rr, pp = np.meshgrid(np.linspace(*XLIM, 400), np.linspace(*YLIM, 400))
iou = 1.0 / (1.0 / pp + 1.0 / rr - 1.0)
LEVELS = [.20, .25, .30, .35, .40, .45, .50, .55]
ax.contour(rr, pp, iou, levels=LEVELS, colors=MUTED, linewidths=.7, alpha=.5,
           zorder=0)
# Label the iso-lines by hand: clabel places them wherever a contour is longest,
# which here is off the visible axes.
p_lab = YLIM[1] - .004
for lv in LEVELS:
    r_lab = 1.0 / (1.0 / lv + 1.0 - 1.0 / p_lab)
    if XLIM[0] + .03 < r_lab < XLIM[1] - .02:
        ax.text(r_lab, p_lab, f"IoU {lv:.2f}", fontsize=7.2, color=MUTED,
                rotation=78, ha="center", va="top",
                bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=.85))

core = ab[ab["tag"].isin(list("ABCD"))].set_index("tag").loc[list("ABCD")]
ax.annotate("", xy=(core.loc["D", "recall"], core.loc["D", "precision"]),
            xytext=(core.loc["A", "recall"], core.loc["A", "precision"]),
            arrowprops=dict(arrowstyle="-|>", color=ATTRIB, lw=1.6,
                            connectionstyle="arc3,rad=0.28"), zorder=2)
ax.scatter(core["recall"], core["precision"], s=95, marker="o", facecolor="white",
           edgecolor=ATTRIB, linewidth=1.8, zorder=3)
rev = ab[ab["tag"].isin(list("EFGH"))]
ax.scatter(rev["recall"], rev["precision"], s=95, marker="s", facecolor="white",
           edgecolor=RESID, linewidth=1.8, zorder=3)

NOTE = {"A": "raw model", "B": "− buildings", "C": "− roads",
        "D": "− buildings − roads", "E": "− sports pitches",
        "F": "− industrial land", "G": "− wider roads", "H": "− all three"}
PLACE = {"A": (.010, -.004, "left", "top"), "B": (-.011, -.003, "right", "top"),
         "C": (.010, .003, "left", "bottom"), "D": (.010, .004, "left", "bottom"),
         "E": (-.011, .001, "right", "center"), "F": (.014, 0, "left", "center"),
         "G": (0, .006, "center", "bottom"), "H": (.014, 0, "left", "center")}
for r in ab.itertuples():
    dx, dy, ha, va = PLACE[r.tag]
    ax.text(r.recall + dx, r.precision + dy, f"{r.tag}  {NOTE[r.tag]}",
            ha=ha, va=va, fontsize=8.4, color=INK)

ax.annotate("post-processing\n+0.043 precision, −0.040 recall",
            xy=(.893, .543), xytext=(.74, .505), fontsize=8.2, color=ATTRIB,
            ha="center", linespacing=1.35,
            arrowprops=dict(arrowstyle="-", color=ATTRIB, lw=.8, alpha=.55))
ax.annotate("filtering by broad land use\ncollapses recall",
            xy=(.29, .500), xytext=(.36, .553), fontsize=8.2, color=RESID,
            ha="left", linespacing=1.35,
            arrowprops=dict(arrowstyle="-", color=RESID, lw=.8, alpha=.55))

ax.set_xlabel("Recall"); ax.set_ylabel("Precision")
ax.set_xlim(*XLIM); ax.set_ylim(*YLIM)
ax.grid(alpha=.15)
ax.legend(handles=[
    Line2D([], [], color=ATTRIB, marker="o", mfc="white", mew=1.8, ms=9,
           label="post-processing factorial (A–D)"),
    Line2D([], [], color="none", marker="s", mfc="white", mec=RESID, mew=1.8,
           ms=9, label="reference layers used as filters (E–H)")],
    loc="upper left", fontsize=8.6, frameon=True, framealpha=.95)
ax.set_title("Post-processing buys precision with recall; land-use filters destroy the map",
             fontsize=10.5, color=INK, pad=12)
fig.tight_layout()
fig.savefig(f"{OUTDIR}/fig_ablation.png", dpi=200, bbox_inches="tight",
            facecolor="white")
log(f"  wrote {OUTDIR}/fig_ablation.png")
log("\ndone")
