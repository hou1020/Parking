#!/usr/bin/env python3
"""
Verify that the numbers LaTeX assigned match the numbers written by hand in
the markdown draft.

md2tex.py strips the manual numbers from headings and lets LaTeX number the
document. That is only safe if the two agree, because the prose refers to
sections by their manual numbers ("as set out in section 3.4"). This compares
main.toc against the headings in ../write/*.md and reports any divergence.

Run after a build:  python3 check_numbering.py
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WRITE = HERE.parent / "write"

SOURCES = [
    "01_introduction", "02_background", "03_methodology",
    "04_results", "05_discussion", "06_conclusion",
    "08_appendix_a_annotation_protocol", "09_appendix_b_percell_and_distance",
    "10_appendix_c_supplementary_experiment", "11_appendix_d_code_and_data",
    "12_appendix_e_research_log",
]


# main.tex lists sections but not subsections, so only headings at these
# levels are expected to appear in main.toc.
TOC_LEVELS = (1, 2)


def manual_headings():
    """(number, title) for every draft heading deep enough to reach the toc."""
    out = []
    for src in SOURCES:
        for line in (WRITE / f"{src}.md").read_text(encoding="utf-8").split("\n"):
            hashes = re.match(r"^(#{1,6})\s+\S", line)
            if not hashes or len(hashes.group(1)) not in TOC_LEVELS:
                continue
            app = re.match(r"^#\s+Appendix\s+([A-Z])\s*[—-]\s*(.*)$", line)
            num = re.match(r"^#{1,2}\s+([0-9]+|[A-Z])((?:\.[0-9]+)*)\.?\s+(.*)$", line)
            if app:
                out.append((app.group(1), app.group(2).strip()))
            elif num:
                out.append((num.group(1) + num.group(2), num.group(3).strip()))
            else:
                out.append((None, re.sub(r"^#+\s+", "", line).strip()))
    return out


def toc_headings():
    """(number, title) for every numbered entry LaTeX put in the contents."""
    toc = (HERE / "main.toc").read_text(encoding="utf-8")
    out = []
    for m in re.finditer(
        r"\\contentsline \{(chapter|section|subsection)\}"
        r"\{\\numberline \{([^}]*)\}([^}]*(?:\{[^}]*\}[^}]*)*)\}",
        toc,
    ):
        num, title = m.group(2), m.group(3)
        title = re.sub(r"\\[a-zA-Z]+\s*", "", title).replace("{", "").replace("}", "")
        out.append((num.rstrip("."), title.strip()))
    return out


def norm(s):
    s = s.replace("---", "—").replace("--", "–").replace("\\&", "&")
    s = re.sub(r"[`*]", "", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def main():
    manual, toc = manual_headings(), toc_headings()
    bad = 0
    if len(manual) != len(toc):
        print(f"heading count differs: draft {len(manual)}, contents {len(toc)}")
        bad += 1
    for (mn, mt), (tn, tt) in zip(manual, toc):
        if (mn is not None and mn != tn) or norm(mt) != norm(tt):
            print(f"  draft: {mn:<6} {mt}")
            print(f"  latex: {tn:<6} {tt}")
            print()
            bad += 1
    if bad:
        print(f"{bad} heading(s) differ")
        return 1
    numbered = sum(1 for n, _ in manual if n is not None)
    print(f"{len(manual)} headings checked; {numbered} carry a number in the "
          f"draft and all of them match the PDF")
    return 0


if __name__ == "__main__":
    sys.exit(main())
