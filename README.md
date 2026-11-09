# Academic Typesetting Portfolio

[![Build PDFs](https://github.com/uzairjaved-prog/Academic-typesetting-portfolio/actions/workflows/build-pdf.yml/badge.svg)](https://github.com/uzairjaved-prog/Academic-typesetting-portfolio/actions/workflows/build-pdf.yml) ![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)

Five portfolio projects in one reproducible repository: journal-paper typesetting, native TikZ/PGFPlots diagrams, a Python figure pipeline, a multi-file thesis architecture, and automated PDF delivery via GitHub Actions.

> **All data is synthetic** (fixed random seed, `scripts/make_data.py`). The documents demonstrate typesetting and tooling, not real research findings.

## Contents

| # | Project | Where | Output |
|---|---------|-------|--------|
| 1 | IEEEtran journal paper: `align`/`gather`/subequations, matrices, `\\DeclareMathOperator`, booktabs + siunitx table, BibTeX, `cleveref` | `src/paper/` | `dist/paper.pdf` (built by CI) |
| 2 | Native TikZ: Transformer, finite state machine, PID loop, plus PGFPlots step response; shared `tikzset` styles, `positioning` library | `src/tikz/` | `dist/tikz_showcase.pdf` |
| 3 | pandas + matplotlib + seaborn pipeline: cleaning, aggregation, 2x2 figure, vector PDF/SVG, 300 dpi PNG, Okabe-Ito palette, Computer Modern fonts, LaTeX `subfigure` integration | `scripts/`, `figures/` | `figures/*.pdf` |
| 4 | Multi-file thesis: root `main.tex`, `preamble.tex`, `\\include` chapters, fancyhdr, title page, TOC/LOF/LOT, index, appendices | `src/thesis/` | `dist/thesis.pdf` |
| 5 | Repo layout, CI workflow, this README | `.github/workflows/`, `Makefile` | PDFs as build artifacts |

## Before / after

`python scripts/before_after.py` writes `docs/previews/figure_before.svg` (Matplotlib defaults: overplotted markers, raw column names, no site information) and `docs/previews/figure_after.svg` (publication style: Computer Modern fonts matching the paper, colour-blind-safe palette, sampled points, fit line, legend). These are build outputs and are not committed.

## Build locally

Requirements: TeX Live or MiKTeX (with `latexmk`, `texlive-publishers` for IEEEtran, `texlive-science`, `texlive-pictures`, `texlive-bibtex-extra`) and Python 3.10+.

```bash
pip install -r requirements.txt
make all          # data -> figures -> all PDFs
make paper        # or: make tikz / make thesis / make figures
make clean
```

Without `make`:

```bash
python scripts/make_data.py && python scripts/generate_figures.py
latexmk -pdf -cd src/paper/main.tex
latexmk -pdf -cd src/thesis/main.tex
```

For fast thesis drafts, uncomment `\\includeonly{...}` in `src/thesis/main.tex`.

## Continuous integration

`.github/workflows/build-pdf.yml` installs TeX Live, regenerates data and figures, builds all three documents, fails on undefined references/citations, and uploads the PDFs as the `pdfs` artifact on every push.

## Layout

```
data/      CSV (generated)  figures/  generated vector figures + tables
scripts/   Python pipeline  src/      LaTeX sources (paper, tikz, thesis)
dist/      built PDFs (CI)  docs/     previews, offer description
```

## Releases

Pushing a tag such as `v1.0.0` publishes the compiled PDFs and a `SHA256SUMS` file as GitHub Release assets.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License

MIT, see [LICENSE](LICENSE).
