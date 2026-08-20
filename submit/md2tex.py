#!/usr/bin/env python3
"""
Convert the markdown draft in ../write into LaTeX chapter files.

Handles the two float constructs used in the draft:

    ![alt](figures/x.png)          -> figure environment, caption below
    **Figure 4.1** caption text

    **Table 4.1** caption text     -> longtable with caption above
    | a | b |

Manual heading numbers ("## 3.4 Validation design") are stripped so that
LaTeX numbers the sections itself; the source numbering is gapless, so the
numbers LaTeX assigns are identical to the ones the prose refers to.
Run check_numbering.py to verify that invariant.
"""
import re
import subprocess
import sys
from pathlib import Path

WRITE = Path(__file__).resolve().parent.parent / "write"
OUT = Path(__file__).resolve().parent / "chapters"

# source stem -> (output stem, chapter title)
FILES = [
    ("01_introduction", "01_introduction", "Introduction"),
    ("02_background", "02_background", "Background"),
    ("03_methodology", "03_methodology", "Methodology"),
    ("04_results", "04_results", "Results"),
    ("05_discussion", "05_discussion", "Discussion"),
    ("06_conclusion", "06_conclusion", "Conclusion"),
    ("08_appendix_a_annotation_protocol", "app_a", "Manual annotation protocol"),
    ("09_appendix_b_percell_and_distance", "app_b", "Per-cell validation and accuracy by distance"),
    ("10_appendix_c_supplementary_experiment", "app_c", "Supplementary adaptation experiment"),
    ("11_appendix_d_code_and_data", "app_d", "Code and data availability"),
    ("12_appendix_e_research_log", "app_e", "Research log"),
]



def pandoc(text, extra=()):
    """Convert a markdown fragment to LaTeX."""
    cmd = ["pandoc", "-f", "markdown+raw_tex", "-t", "latex",
           "--top-level-division=chapter", "--columns=1000", *extra]
    r = subprocess.run(cmd, input=text, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"pandoc failed: {r.stderr}")
    return r.stdout


def inline(text, url=False):
    """Convert an inline fragment (a caption, a reference) to LaTeX.

    url=True turns bare URLs into \\url{}, which xurl can then break; left as
    plain text they overrun the margin in the reference list."""
    fmt = ("-f", "markdown+raw_tex+autolink_bare_uris") if url else ()
    return pandoc(text, extra=("--wrap=none", *fmt)).strip()


# Caption styles used in the draft:
#   **Table 4.1** caption          (body chapters)
#   **Table C.1 — caption**        (appendix C)
CAPTION_RE = (
    r"(?:\*\*Table (?P<num1>[0-9A-Z.]+)\*\*[ \t]*(?P<cap1>[^\n]+)\n\s*\n"
    r"|\*\*Table (?P<num2>[0-9A-Z.]+)[ \t]*[—–-][ \t]*(?P<cap2>[^\n]*?)\*\*\n\s*\n)?"
)
TABLE_RE = re.compile(CAPTION_RE + r"(?P<body>\|[^\n]*\n(?:\|[^\n]*\n)+)")


def split_row(row):
    """Split a pipe-table row on unescaped pipes."""
    return [c.strip() for c in re.split(r"(?<!\\)\|", row.strip())[1:-1]]


def column_widths(body):
    """Longest content in each column, in characters."""
    rows = [r for r in body.strip().split("\n") if r.startswith("|")]
    grid = [split_row(r) for r in rows]
    grid = [g for g in grid if g and set("".join(g)) - set("-: ")]  # drop alignment row
    ncol = max(len(g) for g in grid)
    widths = [0] * ncol
    for g in grid:
        for i, c in enumerate(g[:ncol]):
            widths[i] = max(widths[i], len(re.sub(r"\*\*|`", "", c)))
    return widths


# A cell longer than this holds running prose rather than a label or a number.
PROSE_CELL = 60

# Characters of body text that fit on one line at 12pt in this geometry.
LINE_CHARS = 78

# A column no wider than this can be set on one line, so it is given its
# natural width instead of a share of the page.
SHORT_COL = 14


def table_style(body):
    """Pick a layout for one table.

    Two families occur in this draft and they need opposite treatment.
    Numeric grids are narrow enough to keep their natural column widths, and
    adjustbox can absorb a small overshoot; prose-in-cells tables are far too
    wide for that and must be given proportional p{} widths so they wrap.
    """
    widths = column_widths(body)
    cols = len(widths)
    rows = len([r for r in body.strip().split("\n") if r.startswith("|")])
    if cols >= 10:
        return "natural", "scriptsize", True, False   # per-cell dump: landscape
    if max(widths) <= PROSE_CELL and rows <= 25:
        # No cell holds a sentence, so the table has a sensible natural width;
        # adjustbox keeps it full size when it fits and scales it down when it
        # does not. Nothing in this draft shrinks below about 65%.
        return "natural", "normalsize", False, True
    # A cell holds running prose: it has to be allowed to wrap.
    return "wrap", "normalsize", False, False


def set_column_widths(tex, body):
    """Replace pandoc's p{} proportions with ones based on actual cell content.

    Pandoc derives its widths from how wide each column is written in the
    markdown source, which here bears little relation to what the column holds
    -- a 29-character label column can end up the same width as a column of
    six-digit numbers, and then overruns the margin.
    """
    reals = re.findall(r"\\real\{([\d.]+)\}", tex)
    widths = column_widths(body)
    if len(reals) != len(widths):
        return tex
    props = [p / sum(column_shares(widths)) * 0.98 for p in column_shares(widths)]
    out = iter(f"{p:.4f}" for p in props)
    # a callable repl is used literally, so this needs a single backslash
    return re.sub(r"\\real\{[\d.]+\}", lambda _: "\\real{" + next(out) + "}", tex)


def column_shares(widths):
    """How much of the text block each column should get, in characters.

    Splitting the page in proportion to the longest cell starves the short
    columns whenever one column holds a paragraph: a 430-character column of
    prose would take 84% of the width and leave a name column wrapping one
    word per line. Columns short enough to set on one line are given their
    natural width, and the rest share what remains in proportion to the square
    root of their length -- a column that wraps over many lines needs more room
    than a narrow one, but not proportionally more.
    """
    short = [w if w <= SHORT_COL else 0 for w in widths]
    rest = LINE_CHARS - sum(short) - 2 * len(widths)
    long_idx = [i for i, w in enumerate(widths) if w > SHORT_COL]
    if not long_idx or rest <= len(long_idx):
        return [max(w, 1) for w in widths]
    weights = [widths[i] ** 0.5 for i in long_idx]
    out = list(short)
    for i, wt in zip(long_idx, weights):
        out[i] = rest * wt / sum(weights)
    return out


def longtable_to_tabular(tex):
    """Turn pandoc's longtable into a tabular so it can go inside adjustbox."""
    tex = re.sub(r"\\begin\{longtable\}\[\]\{(.*?)\}\n", r"\\begin{tabular}{\1}\n", tex, flags=re.S)
    tex = tex.replace("\\end{longtable}", "\\end{tabular}")
    tex = re.sub(r"^\\endhead\n", "", tex, flags=re.M)
    return tex


def breakable_paths(tex):
    """Allow long \\texttt{} file paths to break; they otherwise run into the
    margin inside narrow table columns."""

    def fix(m):
        return "\\texttt{" + re.sub(r"([/_.-])", r"\1\\allowbreak{}", m.group(1)) + "}"

    return re.sub(r"\\texttt\{([^{}]*[/_][^{}]*)\}", fix, tex)


def convert_tables(md):
    """Replace every pipe table (and its caption, if any) with raw LaTeX.

    The caption is set with \\captionof outside the longtable rather than as a
    \\caption inside it: a caption placed inside a longtable belongs to the
    repeating head, so both it and its \\label are re-emitted on every
    continuation page.
    """

    def one(m):
        body = m.group("body")
        num = m.group("num1") or m.group("num2")
        cap = m.group("cap1") or m.group("cap2")
        mode, size, landscape, shrinkable = table_style(body)
        cols_opt = "--columns=1000" if mode == "natural" else "--columns=20"
        tex = pandoc(body, extra=(cols_opt,))
        tex = (
            tex.replace("\\toprule()", "\\toprule")
            .replace("\\midrule()", "\\midrule")
            .replace("\\bottomrule()", "\\bottomrule")
        )
        # Identifiers like parking_share are single unbreakable tokens and
        # overrun narrow wrapped columns; permit a break after the underscore.
        # Scoped to table cells so prose keeps its normal hyphenation.
        tex = tex.replace("\\_", "\\_\\allowbreak{}")
        if mode == "wrap":
            tex = set_column_widths(tex, body)
        caption = (f"\\caption{{{inline(cap.strip())}}}\\label{{tab:{num}}}\n") if num else ""
        if shrinkable:
            # A tabular fits on one page, so it can go in a real float. That
            # keeps the caption with the table instead of stranding it at the
            # foot of the previous page.
            body_tex = ("\\centering\n" + caption
                        + "\\begin{adjustbox}{max width=\\textwidth}\n"
                        + longtable_to_tabular(tex) + "\\end{adjustbox}\n")
            if size != "normalsize":
                body_tex = f"\\{size}\n" + body_tex
            tex = "\\begin{table}[htbp]\n" + body_tex + "\\end{table}\n"
            if landscape:
                tex = f"\\begin{{landscape}}\n{tex}\\end{{landscape}}\n"
            return "\n```{=latex}\n" + tex + "\\restoreparskip\n```\n\n"

        # A longtable breaks across pages, so it cannot be floated; keep its
        # caption above it and reserve enough room that the two do not split.
        if size != "normalsize":
            tex = f"\\begingroup\\{size}\n{tex}\\endgroup\n"
        if num:
            tex = ("\\needspace{6\\baselineskip}\n"
                   + caption.replace("\\caption", "\\captionof{table}") + tex)
        if landscape:
            tex = f"\\begin{{landscape}}\n{tex}\\end{{landscape}}\n"
        # keep the table clear of the surrounding paragraphs, and put \parskip
        # back: longtable and adjustbox both zero it and neither restores it
        return ("\n```{=latex}\n\\par\\addvspace{\\medskipamount}\\noindent\n"
                + tex
                + "\\par\\addvspace{\\medskipamount}\\restoreparskip\n```\n\n")

    return TABLE_RE.sub(one, md)


BOLD_RE = re.compile(r"\*\*([^*\n]+?)\*\*")
RUNIN_RE = re.compile(r"^[ \t]*(?:[-*+][ \t]+)?\*\*[^*\n]+?\*\*")


def strip_prose_bold(md, keep_runin=True):
    """Drop bold emphasis from running text.

    The draft uses bold for two different things. A bold span that opens a
    paragraph or a list item is a run-in sub-heading and is kept; bold inside a
    sentence is emphasis on a number or a phrase, and is not. Position alone
    separates them reliably here -- every one of the 35 paragraph-initial spans
    is a heading, and no mid-sentence span is.

    Raw LaTeX blocks are skipped, so the bold inside tables and in the captions
    already converted above is untouched, as is the bold of headings.
    """
    parts = re.split(r"(```\{=latex\}.*?```)", md, flags=re.S)
    for i, part in enumerate(parts):
        if part.startswith("```{=latex}"):
            continue
        out, prev_blank = [], True
        for line in part.split("\n"):
            m = RUNIN_RE.match(line) if keep_runin else None
            is_item = re.match(r"^[ \t]*[-*+][ \t]", line)
            if m and (prev_blank or is_item):
                out.append(line[: m.end()] + BOLD_RE.sub(r"\1", line[m.end():]))
            else:
                out.append(BOLD_RE.sub(r"\1", line))
            prev_blank = not line.strip()
        parts[i] = "\n".join(out)
    return "".join(parts)


def renumber_heading(m):
    """Hand a heading over to LaTeX's numbering, or take it out of it.

    The draft numbers its own headings. Those numbers are stripped so LaTeX
    supplies them, which keeps the contents page and the prose consistent.
    A heading the author did not number -- the phase headings in the research
    log -- is made unnumbered here too, so LaTeX does not invent a number for
    it and it stays out of the contents.
    """
    hashes, text = m.group(1), m.group(2)
    stripped = re.sub(r"^(?:Appendix [A-Z]\s*[—-]\s*|[0-9A-Z]+(?:\.[0-9]+)*\.?\s+)", "", text)
    if stripped != text:
        return f"{hashes} {stripped}"
    return f"{hashes} {text} {{-}}"


def preprocess(md, stem):
    """Pull figure/table captions out into raw-LaTeX blocks."""
    # ---- drop draft-note blockquotes anywhere before the first real paragraph
    md = re.sub(r"^(#[^\n]*\n)(?:\s*\n|>[^\n]*\n)+(?:---\s*\n)?", r"\1\n", md)

    # ---- drop the markdown section dividers: they are a reading aid in the
    # source, and typeset as a stray rule between a heading and its text
    md = re.sub(r"\n---+[ \t]*\n", "\n", md)

    # ---- figures: image line followed by a bold "Figure N.M" caption
    def fig(m):
        path, num, cap = m.group("path"), m.group("num"), m.group("cap")
        cap = inline(cap.strip())
        return (
            "\n```{=latex}\n"
            "\\begin{figure}[htbp]\n\\centering\n"
            f"\\includegraphics[width=\\linewidth,height=0.82\\textheight,keepaspectratio]{{{path}}}\n"
            f"\\caption{{{cap}}}\n\\label{{fig:{num}}}\n"
            "\\end{figure}\\restoreparskip\n```\n"
        )

    md = re.sub(
        r"!\[[^\]]*\]\((?P<path>[^)]+)\)\s*\n\s*\n"
        r"\*\*Figure (?P<num>[0-9A-Z.]+)\*\*\s*(?P<cap>[^\n]+)\n",
        fig,
        md,
    )

    md = convert_tables(md)

    md = re.sub(r"^(#+)[ \t]+(.*)$", renumber_heading, md, flags=re.M)

    md = strip_prose_bold(md)
    return md


def postprocess(tex, stem):
    """Tidy anything pandoc emitted outside the pre-converted tables."""
    tex = (
        tex.replace("\\toprule()", "\\toprule")
        .replace("\\midrule()", "\\midrule")
        .replace("\\bottomrule()", "\\bottomrule")
        .replace(
            "\\subsection*{Phase 4 --- Manual annotation and redirection (26 June -- 2 August)}",
            "\\subsection*{Phase 4 --- Manual annotation and\\\\redirection (26 June -- 2 August)}",
        )
    )
    # pandoc adds an \addcontentsline for every unnumbered heading, which puts
    # the research-log phase headings back into the contents; main.tex lists
    # the front matter itself, so no chapter file needs one.
    tex = re.sub(r"^\\addcontentsline\{toc\}\{[^}]*\}\{.*\}%?\n", "", tex, flags=re.M)
    return breakable_paths(tex)


def main():
    OUT.mkdir(exist_ok=True)
    for src, stem, title in FILES:
        md = (WRITE / f"{src}.md").read_text(encoding="utf-8")
        md = preprocess(md, stem)
        # drop the H1 - main.tex issues \chapter{} itself
        md = re.sub(r"^#\s+[^\n]*\n", "", md, count=1)
        tex = pandoc(md)
        tex = postprocess(tex, stem)
        (OUT / f"{stem}.tex").write_text(tex, encoding="utf-8")
        print(f"  {src}.md -> chapters/{stem}.tex  ({len(tex.splitlines())} lines)")

    # references: a plain hanging-indent list, formatting preserved verbatim
    md = (WRITE / "07_references.md").read_text(encoding="utf-8")
    md = re.sub(r"^(#[^\n]*\n)(?:\s*\n|>[^\n]*\n)+(?:---\s*\n)?", "", md)
    md = re.sub(r"^#\s+[^\n]*\n", "", md, count=1)
    entries = [p.strip() for p in md.split("\n\n") if p.strip()]
    body = ["\\begin{hangparas}{1.5em}{1}"]
    for e in entries:
        body.append(inline(e, url=True) + "\n")
    body.append("\\end{hangparas}")
    (OUT / "07_references.tex").write_text("\n".join(body), encoding="utf-8")
    print(f"  07_references.md -> chapters/07_references.tex  ({len(entries)} entries)")

    # abstract
    md = (WRITE / "00_abstract.md").read_text(encoding="utf-8")
    md = re.sub(r"^#\s+[^\n]*\n", "", md, count=1)
    md = strip_prose_bold(md, keep_runin=False)
    (OUT / "00_abstract.tex").write_text(pandoc(md), encoding="utf-8")
    print("  00_abstract.md -> chapters/00_abstract.tex")


if __name__ == "__main__":
    main()
