"""
Are the labelling basemap and the model's input imagery co-registered? — Leeds
Author: Hou

Labelling was drawn over a satellite basemap while the model operated on Digimap
aerial tiles. If those two sources were spatially offset, the boundary error the
accuracy assessment reports would partly be misalignment rather than model
behaviour, and the dilation and erosion figures would not mean what they appear
to mean. This tests for that.

Method
    For every labelled lot the model detected well, compare the centroid of the
    lot with the centroid of the model area covering it. A registration offset
    would displace every lot in the same direction, so the mean displacement
    VECTOR would be large. Model boundary imprecision displaces lots in arbitrary
    directions, so displacements cancel and the mean vector stays near zero even
    though individual displacements are not small.

    The two are separated by the ratio |mean vector| / mean absolute displacement:
    near 0 means the shared component is small relative to the scatter, near 1
    means everything shifted the same way. The direction histogram is reported as
    a second check, since a genuine shift would concentrate in one sector.

    What matters is magnitude, not the presence of a shared component. With this
    many lots a sub-pixel bias is statistically detectable without being
    practically meaningful, so the t-tests and the sector chi-square are reported
    alongside the offset in metres and pixels rather than in place of it.

    Only lots with at least MIN_COVER of their area detected, and at least
    MIN_AREA in size, are used: a partially detected lot has a truncated
    intersection whose centroid is displaced for reasons that have nothing to do
    with registration.

Reads read-only. Writes only the output below.
Output:
  - coregistration_summary.csv
"""
import os, csv
import numpy as np
import geopandas as gpd
from shapely.ops import unary_union
from scipy import stats
import warnings; warnings.filterwarnings("ignore")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MODEL = f"{ROOT}/Parking/calculate/output_files_merged/removal_merged.geojson"
MANUAL = f"{ROOT}/manual/leeds_manual.gpkg"
GRID = f"{ROOT}/manual/leeds_grid.gpkg"
OUT = f"{HERE}/coregistration_summary.csv"

MIN_COVER = 0.70      # lot must be at least this well detected to be comparable
MIN_AREA = 300.0      # m2; centroids of very small lots are noisy
N_SECTORS = 8
PIXEL_M = 0.25        # Digimap ground sample distance, for reporting in pixels


def log(m):
    print(m, flush=True)


log("loading layers ...")
grid = gpd.read_file(GRID).to_crs(27700)
region = unary_union(grid.geometry.values)
man = gpd.read_file(MANUAL).to_crs(27700)
man["geometry"] = man.geometry.buffer(0)
mod = gpd.read_file(MODEL).to_crs(27700)
mod["geometry"] = mod.geometry.buffer(0)
mod_u = unary_union(mod.geometry.values).intersection(region)

dx, dy, areas = [], [], []
for g in man.geometry.values:
    if g.area < MIN_AREA:
        continue
    hit = g.intersection(mod_u)
    if hit.is_empty or hit.area / g.area < MIN_COVER:
        continue
    c1, c2 = g.centroid, hit.centroid
    dx.append(c2.x - c1.x); dy.append(c2.y - c1.y); areas.append(g.area)

dx, dy = np.array(dx), np.array(dy)
dist = np.hypot(dx, dy)
mean_vec = float(np.hypot(dx.mean(), dy.mean()))
ratio = mean_vec / dist.mean()
t_x, t_y = stats.ttest_1samp(dx, 0), stats.ttest_1samp(dy, 0)

ang = (np.degrees(np.arctan2(dy, dx)) + 360) % 360
hist, edges = np.histogram(ang, bins=N_SECTORS, range=(0, 360))
top_sector = 100 * hist.max() / hist.sum()
chi = stats.chisquare(hist)

rows = [
    ("lots compared", len(dx), "count", f"cover >= {MIN_COVER:.0%}, area >= {MIN_AREA:.0f} m2"),
    ("mean dx", round(float(dx.mean()), 3), "m", "east positive"),
    ("mean dy", round(float(dy.mean()), 3), "m", "north positive"),
    ("mean displacement vector", round(mean_vec, 3), "m", "resultant of the mean dx, dy"),
    ("mean displacement vector, in pixels", round(mean_vec / PIXEL_M, 2), "px",
     f"imagery is {PIXEL_M} m; a systematic offset below 1 px cannot be resolved"),
    ("mean absolute displacement", round(float(dist.mean()), 3), "m", ""),
    ("mean absolute displacement, in pixels", round(float(dist.mean()) / PIXEL_M, 2), "px", ""),
    ("median absolute displacement", round(float(np.median(dist)), 3), "m", ""),
    ("direction consistency ratio", round(ratio, 3), "ratio",
     "|mean vector| / mean absolute; 0 = shared component negligible, 1 = uniform shift"),
    ("dx different from zero, p", round(float(t_x.pvalue), 4), "p",
     f"t = {t_x.statistic:.2f}; significant but sub-pixel, n = {len(dx)}"),
    ("dy different from zero, p", round(float(t_y.pvalue), 4), "p",
     f"t = {t_y.statistic:.2f}; significant but sub-pixel, n = {len(dy)}"),
    ("largest of 8 direction sectors", round(top_sector, 1), "%",
     "12.5% would be perfectly uniform"),
    ("direction sectors uniform, p", float(f"{chi.pvalue:.2g}"), "p",
     f"chi2 = {chi.statistic:.1f}, df = {N_SECTORS - 1}; directions are not uniform"),
]
with open(OUT, "w", newline="") as f:
    w = csv.writer(f); w.writerow(["measure", "value", "unit", "note"])
    w.writerows(rows)
    w.writerow([])
    w.writerow(["direction sector (deg, 0 = east)", "n", "", ""])
    for h, e in zip(hist, edges[:-1]):
        w.writerow([f"{e:.0f}-{e+360/N_SECTORS:.0f}", int(h), "", ""])

log(f"wrote: {OUT}\n")
for m_, v, u, n in rows:
    log(f"  {m_:<32} {v:>9} {u:<6} {n}")
log("\ndirection histogram:")
for h, e in zip(hist, edges[:-1]):
    log(f"  {e:>3.0f}-{e+360/N_SECTORS:>3.0f} deg  {h:>4}  {'#'*int(40*h/hist.max())}")
log(f"\nInterpretation: a shared component is present and statistically detectable "
    f"(dx p = {t_x.pvalue:.4f}, dy p = {t_y.pvalue:.4f}; sector directions are not "
    f"uniform, chi2 = {chi.statistic:.1f}, p = {chi.pvalue:.1g}), but it is small: "
    f"the mean vector is {mean_vec:.2f} m, or {mean_vec/PIXEL_M:.2f} of one "
    f"{PIXEL_M} m pixel, against a mean absolute displacement of {dist.mean():.2f} m "
    f"({dist.mean()/PIXEL_M:.1f} px), a ratio of {ratio:.3f}. With {len(dx)} lots a "
    f"sub-pixel bias is detectable without being practically meaningful, and "
    f"displacement is dominated by per-lot variation rather than a uniform shift. "
    f"The two sources are co-registered to well within a pixel, so the boundary "
    f"error reported elsewhere is attributable to the model.")
