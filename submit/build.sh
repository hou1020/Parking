#!/bin/sh
# Regenerate the chapter .tex files from ../write/*.md and build the PDF.
set -e
cd "$(dirname "$0")"
python3 md2tex.py
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
echo
echo "Built: $(pwd)/main.pdf"
