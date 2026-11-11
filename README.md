# Academic Typesetting Portfolio

[![Build PDFs](https://github.com/uzairjaved-prog/Academic-typesetting-portfolio/actions/workflows/build-pdf.yml/badge.svg)](https://github.com/uzairjaved-prog/Academic-typesetting-portfolio/actions/workflows/build-pdf.yml)
[![Latest release](https://img.shields.io/github/v/release/uzairjaved-prog/Academic-typesetting-portfolio)](https://github.com/uzairjaved-prog/Academic-typesetting-portfolio/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Academic document formatting · LaTeX typesetting · TikZ diagrams · Scientific figures**

A portfolio of academic document-production samples demonstrating structured LaTeX projects, publication-style layouts, mathematical typesetting, native vector diagrams, and reproducible research graphics.

> **Sample-content notice:** the research topic and sensor dataset are illustrative. All observations are synthetic and generated with a fixed seed. These files demonstrate typesetting and document-production skills; they are not real experimental findings, university submissions, or claims of academic affiliation.

![Academic Typesetting Portfolio — selected work](docs/previews/portfolio-overview.jpg)

## Selected work

The compiled PDF samples are included directly in this repository under **docs/samples/**. Open them in your browser or download them; no Actions artifact or external release download is required.

### 1. Journal paper — IEEE-style layout

A two-column research-paper example featuring mathematical notation, aligned equations, matrices, references, cross-references, figures, and publication-style tables.

[**View or download the journal paper (PDF)**](docs/samples/paper.pdf)

[![Journal paper preview](docs/previews/paper-page-1.jpg)](docs/samples/paper.pdf)

### 2. Thesis — multi-file document architecture

A thesis-layout demonstration featuring a designed title page, abstract, contents, lists of figures and tables, modular chapters, appendices, bibliography, page headers, and index.

[**View or download the thesis sample (PDF)**](docs/samples/thesis.pdf)

[![Thesis cover preview](docs/previews/thesis-cover.jpg)](docs/samples/thesis.pdf)

### 3. TikZ and PGFPlots — vector graphics

A gallery of native LaTeX vector illustrations, including a Transformer architecture, finite-state machine, feedback-control diagram, and plotted system responses.

[**View or download the TikZ showcase (PDF)**](docs/samples/tikz-showcase.pdf)

[![TikZ gallery preview](docs/previews/tikz-gallery.jpg)](docs/samples/tikz-showcase.pdf)

### 4. Scientific figures and tables

A reproducible Python workflow that generates time-series plots, correlation visualizations, site comparisons, scatter plots, and LaTeX-ready summary tables.

[View the scientific-figures preview](docs/previews/scientific-figures.jpg)

## Services demonstrated

| Service area | Examples of work |
|---|---|
| **LaTeX formatting and conversion** | Structured manuscript setup, document styling, equation formatting, references, and PDF production |
| **Thesis and dissertation formatting** | Title pages, front matter, chapter structures, headers, appendices, and bibliography |
| **Mathematical typesetting** | Aligned equations, matrices, theorems, operators, derivations, and notation |
| **TikZ and PGFPlots diagrams** | Flowcharts, architecture diagrams, control-system illustrations, and vector plots |
| **Research figures and tables** | Reproducible charts, publication-style tables, and LaTeX figure integration |

## Tools and workflow

- **LaTeX:** IEEEtran, AMS math, cleveref, BibTeX, booktabs, siunitx, and modular book-class documents.
- **TikZ / PGFPlots:** document-native vector diagrams with reusable shared styles.
- **Python:** NumPy, pandas, Matplotlib, seaborn, and Pillow for data preparation, figures, and preview generation.
- **GitHub Actions:** Python linting, PDF compilation, reference checks, preview rendering, and release publishing.

## Download options

| File | Repository copy | Release copy |
|---|---|---|
| Journal paper | [paper.pdf](docs/samples/paper.pdf) | [Release download](https://github.com/uzairjaved-prog/Academic-typesetting-portfolio/releases/latest) |
| Thesis | [thesis.pdf](docs/samples/thesis.pdf) | [Release download](https://github.com/uzairjaved-prog/Academic-typesetting-portfolio/releases/latest) |
| TikZ showcase | [tikz-showcase.pdf](docs/samples/tikz-showcase.pdf) | [Release download](https://github.com/uzairjaved-prog/Academic-typesetting-portfolio/releases/latest) |

The [latest GitHub Release](https://github.com/uzairjaved-prog/Academic-typesetting-portfolio/releases/latest) also includes preview images and SHA256 checksums.

## Build the samples

Requirements: Python 3.10+, TeX Live or MiKTeX, latexmk, Poppler utilities (pdftoppm), IEEEtran, and the LaTeX packages used by the source files.

~~~bash
pip install -r requirements.txt
make all
~~~

Individual build targets:

~~~bash
make figures
make paper
make tikz
make thesis
make previews
make clean
~~~

The demonstration dataset and generated figures are created by scripts/make_data.py and scripts/generate_figures.py. The preview generator renders selected PDF pages and assembles the README overview. Curated PDFs are committed separately in docs/samples/, while temporary compilation files remain excluded from version control.

## Repository structure

~~~text
.github/workflows/   Automated linting, PDF builds, previews, and releases
src/paper/           IEEE-style paper source and bibliography
src/thesis/          Multi-file thesis source
src/tikz/            TikZ and PGFPlots source diagrams
scripts/             Data, figure, and preview-generation scripts
data/                Synthetic-data notes
figures/             Generated figures and LaTeX tables (build output)
docs/samples/        Curated, compiled PDF samples
docs/previews/       Committed preview images used in this README
~~~

## Contact

For academic typesetting, LaTeX formatting, thesis layout, TikZ diagrams, or publication-ready research figures, contact the repository owner through the [GitHub profile](https://github.com/uzairjaved-prog).

---

*For any real project, the client's manuscript, institutional template, supplied data, citation style, and submission requirements should take precedence over these demonstration examples.*
