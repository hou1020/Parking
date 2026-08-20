# Submission build

LaTeX source for the CASA0010 dissertation. The body is generated from the
markdown draft in `../write/`; nothing in `chapters/` should be edited by hand,
because the next build overwrites it. Edit the markdown, then rebuild.

## Build

```sh
./build.sh
```

That runs `md2tex.py` (markdown → `chapters/*.tex`) and then `latexmk -xelatex`,
producing `main.pdf`. XeLaTeX is required: the text uses characters (§, ², ρ, ≤,
−) that need Unicode font handling.

After a build, check that LaTeX's numbering still agrees with the draft:

```sh
python3 check_numbering.py
```

## Layout

| Path | Contents |
|---|---|
| `main.tex` | Preamble, title page, front matter, chapter order |
| `chapters/` | Generated — one `.tex` per markdown source |
| `figures/` | Copied from `../write/figures/` |
| `md2tex.py` | The converter |
| `check_numbering.py` | Verifies PDF numbering against the draft |

## How the conversion works

`md2tex.py` strips the manual numbers from headings (`## 3.4 Validation design`)
and lets LaTeX number the document. That keeps the contents page, the headings
and the cross-references in the prose consistent with one another, but it is
only safe while LaTeX's numbers match the ones the author wrote, since the prose
cites sections by number. `check_numbering.py` asserts exactly that, and is the
check to run after any change to the draft's heading structure.

A heading the draft did **not** number -- the phase headings in the research log
-- is set unnumbered and kept out of the contents, so LaTeX never invents a
number the draft does not use. Numbering a heading in the markdown is therefore
what puts it in the contents.

The draft uses bold for two different things, and only one of them survives.
A bold span that opens a paragraph or a list item is a run-in sub-heading and is
kept; bold inside a sentence is emphasis on a number or a phrase, and is
removed. Position separates the two reliably here: all 35 paragraph-initial
spans are headings and no mid-sentence span is. The abstract is stripped
outright, run-ins included, since it has none. Bold in tables, in captions and
in headings is untouched -- the stripping happens after the floats have already
become raw LaTeX, and the handbook asks for bold headings.

Figures and tables are pulled out of the markdown and emitted as LaTeX floats so
they appear in the List of Figures and List of Tables. Tables get one of three
treatments, chosen per table:

- **numeric grids** keep their natural column widths inside `adjustbox`, which
  scales them down only if they would otherwise be too wide;
- **prose-in-cells tables** are given proportional `p{}` widths computed from
  actual cell contents, so they wrap;
- the **100-row per-cell dump** in Appendix B is set landscape at `\scriptsize`.

## Handbook conformance

Built against the CASA Dissertation Handbook 2025–26:

- §4.2 title page carries title, name, date, module name and code, supervisors,
  code URL and word count, plus the prescribed submission statement; abstract,
  declaration, contents, lists of figures and tables, acronyms and
  acknowledgements all present. Nothing beyond what §4.2 asks for: no partner
  organisation, no signature block on the declaration
- §4.3 bold headings, generous spacing, each chapter starts a new page
- §4.8 simple section numbering; continuous arabic pagination from the title
  page to the end of the appendices
- §4.9 Harvard references, typeset from the draft's verified list

## Word count

11,941 words, Chapters 1–6 inclusive. Excludes the abstract, figures, tables,
footnotes, references and appendices, per §2.4. The declaration on page 2 states
this figure; if the draft changes, recount and update `\wordcount` in
`main.tex`.
