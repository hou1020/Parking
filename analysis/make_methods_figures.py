"""
Figures for the methodology chapter — Leeds
Author: Hou

Two figures that belong to the methods chapter rather than to any analysis:

    fig_study_area.png   the 100 km2 grid, the city centre, distance rings and
                         the labelled parking, so the reader can see what was
                         labelled and how the per-cell unit is defined.
    fig_pipeline.png     the processing chain from Digimap tile to evaluated
                         map, with the two post-processing subtractions and the
                         two outputs that the ablation compares.

Reads read-only. Writes only into write/figures/.
"""
import os
import geopandas as gpd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
from matplotlib.lines import Line2D
import warnings; warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUTDIR = f"{ROOT}/Parking/write/figures"
os.makedirs(OUTDIR, exist_ok=True)

CENTRE = (429832.0, 433449.0)          # Leeds City Square, EPSG:27700
INK, MUTED, ACCENT = "#1f2933", "#7b8794", "#4878a8"
FILL = "#c9412e"


def log(m):
    print(m, flush=True)


# ----------------------------------------------------------------- figure 3.1
log("figure 3.1: study area ...")
grid = gpd.read_file(f"{ROOT}/manual/leeds_grid.gpkg").to_crs(27700)
man = gpd.read_file(f"{ROOT}/manual/leeds_manual.gpkg").to_crs(27700)

fig, ax = plt.subplots(figsize=(7.2, 7.4))
grid.plot(ax=ax, facecolor="none", edgecolor=MUTED, linewidth=0.5, zorder=2)
man.plot(ax=ax, facecolor=FILL, edgecolor="none", zorder=3)

HALO = dict(boxstyle="round,pad=0.18", fc="white", ec="none", alpha=0.88)

for r in (1000, 2000, 3000, 4000, 5000):
    ax.add_patch(Circle(CENTRE, r, fill=False, ec=ACCENT, lw=0.8, ls=(0, (4, 3)), zorder=4))
    ax.text(CENTRE[0], CENTRE[1] + r, f"{r//1000} km", color=ACCENT, fontsize=7.5,
            zorder=5, ha="center", va="center", bbox=HALO)

ax.plot(*CENTRE, marker="o", ms=7, mfc="white", mec=INK, mew=1.6, zorder=6)
ax.text(CENTRE[0] + 260, CENTRE[1] - 520, "City Square\nE 429832  N 433449",
        fontsize=8, color=INK, zorder=6, ha="left", va="top", bbox=HALO,
        linespacing=1.35)

minx, miny, maxx, maxy = grid.total_bounds
bar = 2000
x0, y0 = minx + 600, miny + 800
ax.add_patch(FancyBboxPatch((x0 - 300, y0 - 400), bar + 600, 1250,
                            boxstyle="round,pad=0,rounding_size=120",
                            fc="white", ec="none", alpha=0.88, zorder=5))
ax.plot([x0, x0 + bar], [y0, y0], color=INK, lw=2.6, solid_capstyle="butt", zorder=6)
for xt in (x0, x0 + bar):
    ax.plot([xt, xt], [y0 - 130, y0 + 130], color=INK, lw=1.2, zorder=6)
ax.text(x0 + bar / 2, y0 + 300, "2 km", ha="center", fontsize=8, color=INK, zorder=6)

nx, ny = maxx - 800, maxy - 2600
ax.add_patch(FancyBboxPatch((nx - 500, ny - 200), 1000, 2100,
                            boxstyle="round,pad=0,rounding_size=120",
                            fc="white", ec="none", alpha=0.88, zorder=5))
ax.annotate("", xy=(nx, ny + 1250), xytext=(nx, ny),
            arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.4), zorder=6)
ax.text(nx, ny + 1450, "N", ha="center", fontsize=9.5, color=INK, zorder=6)

ax.legend(handles=[
    Line2D([], [], color=MUTED, lw=0.8, label="1 km² validation cells (n = 100)"),
    Line2D([], [], color=FILL, lw=6, label="labelled surface parking (2,037 polygons)"),
    Line2D([], [], color=ACCENT, lw=0.9, ls=(0, (4, 3)), label="distance from city centre"),
], loc="upper left", fontsize=8, frameon=True, framealpha=.95, edgecolor=MUTED)

ax.set_xlim(minx - 400, maxx + 400); ax.set_ylim(miny - 400, maxy + 400)
ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values():
    s.set_visible(False)
ax.set_title("Study area: 100 km² on the British National Grid, Leeds",
             fontsize=10.5, color=INK, pad=10)
fig.tight_layout()
fig.savefig(f"{OUTDIR}/fig_study_area.png", dpi=200, bbox_inches="tight",
            facecolor="white")
log(f"  wrote {OUTDIR}/fig_study_area.png")


# ----------------------------------------------------------------- figure 3.2
log("figure 3.2: pipeline ...")
fig, ax = plt.subplots(figsize=(10.2, 6.2))
ax.set_xlim(-16, 122); ax.set_ylim(-2, 104); ax.axis("off")

BW, BH = 30, 7.6
GOLD = "#b4884a"


def box(x, y, text, fc="white", ec=INK, lw=1.0, w=BW, h=BH, fs=8.2, weight="normal"):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                                boxstyle="round,pad=0.3,rounding_size=1.2",
                                fc=fc, ec=ec, lw=lw, zorder=2))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=INK,
            zorder=3, linespacing=1.5, fontweight=weight)


def arrow(x1, y1, x2, y2, style="-|>", lw=1.2, color=INK, ls="-", rad=None):
    ax.add_patch(FancyArrowPatch(
        (x1, y1), (x2, y2), arrowstyle=style, mutation_scale=11, lw=lw,
        color=color, linestyle=ls, zorder=1, shrinkA=1, shrinkB=1,
        connectionstyle=f"arc3,rad={rad}" if rad else None))


L, M, R = 24, 63, 100
ys = [93, 80.5, 68, 55.5, 43]
box(L, ys[0], "Digimap aerial tiles\n109 tiles · 0.25 m · RGB")
box(L, ys[1], "Georeferenced GeoTIFF\nEPSG:27700")
box(L, ys[2], "512 × 512 patches\nzero-padded at edges")
box(L, ys[3], "SegFormer-B5\nQiam et al. (2025), unmodified",
    fc="#eef3f8", ec=ACCENT, lw=1.6, weight="bold", fs=7.5, w=34)
box(L, ys[4], "Vectorise and merge\nmode filter · >1,000 px² · holes", fs=7.7, w=32)
for a, b in zip(ys[:-1], ys[1:]):
    arrow(L, a - BH / 2, L, b + BH / 2)

box(L, 29, "original output\n6,814 polygons", fc="#f2f2ef", lw=1.5, weight="bold")
arrow(L, ys[4] - BH / 2, L, 29 + BH / 2)

box(L, 16, "− OSM building footprints\n− road buffers, 14–5 m by class", fs=7.5, w=34)
arrow(L, 29 - BH / 2, L, 16 + BH / 2)

box(L, 3, "removal output\n8,180 polygons", fc="#f2f2ef", lw=1.5, weight="bold")
arrow(L, 16 - BH / 2, L, 3 + BH / 2)

# ablation bracket, square, clear of the left column
bx = L - BW / 2 - 5
ax.plot([bx, bx], [3, 29], color=ACCENT, lw=1.2, zorder=1)
for yb in (3, 29):
    arrow(bx, yb, L - BW / 2 - 0.5, yb, color=ACCENT, lw=1.2)
ax.text(bx - 2.5, 16, "ablation\ncompares\nthese two\n(3.7)", ha="right",
        va="center", fontsize=7.6, color=ACCENT, style="italic", linespacing=1.5)

# evaluation inputs
box(R, ys[1], "Satellite basemap\nannotation protocol (App. A)", w=32, fs=8.0)
box(R, ys[2], "Manual reference\n2,037 polygons · 3.2597 km²", w=32, lw=1.5,
    weight="bold", fs=8.0)
arrow(R, ys[1] - BH / 2, R, ys[2] + BH / 2)

box(R, 29, "Reference layers\nOSM land use · OS Greenspace", w=32, ec=MUTED, fs=8.0)

# centre column
box(M, 43, "Accuracy\nprecision · recall · IoU  (3.4)", w=30, h=8.4,
    fc="#fdf6e8", ec=GOLD, lw=1.5, fs=8.0)
box(M, 16, "Error typology\nattribution (3.5) · sampling (3.6)", w=30, h=8.4,
    ec=MUTED, fs=8.0)

arrow(L + BW / 2, 29, M - 15, 41, color=GOLD, rad=0.12)
arrow(L + BW / 2, 3, M - 15, 39, color=GOLD, rad=-0.18)
arrow(R - 16, ys[2], M + 15, 45, color=GOLD, rad=0.12)
arrow(M, 43 - 4.2, M, 16 + 4.2, color=MUTED)
arrow(R - 16, 29, M + 15, 18, color=MUTED, rad=-0.12)

ax.text(L, 101, "Prediction", ha="center", fontsize=10, fontweight="bold", color=INK)
ax.text(M, 101, "Evaluation", ha="center", fontsize=10, fontweight="bold", color=INK)
ax.text(R, 101, "Reference", ha="center", fontsize=10, fontweight="bold", color=INK)

fig.savefig(f"{OUTDIR}/fig_pipeline.png", dpi=200, bbox_inches="tight",
            facecolor="white")
log(f"  wrote {OUTDIR}/fig_pipeline.png")
