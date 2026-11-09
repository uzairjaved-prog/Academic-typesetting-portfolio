# Academic Typesetting Portfolio

A practical portfolio of academic typesetting and research-document production using **LaTeX, TikZ/PGFPlots, Python, and GitHub Actions**.

This repository demonstrates the workflow behind clean, reproducible, publication-style research documents. It includes an IEEE-style journal paper, a multi-file thesis, custom vector diagrams, and a reproducible scientific-figure pipeline.

> **Demonstration data:** the sensor dataset is synthetic and generated with a fixed random seed. It is included to demonstrate document production and reproducible figure generation, not to present real research findings.

## Portfolio projects

| Project | What it demonstrates | Source |
|---|---|---|
| Journal paper | IEEEtran structure, advanced equations, matrices, BibTeX, cross-references, booktabs and siunitx tables | [`src/paper/`](src/paper/) |
| TikZ graphics | Transformer architecture, finite-state machine, PID control loop and PGFPlots response curves | [`src/tikz/`](src/tikz/) |
| Python figures | pandas data preparation, Matplotlib/seaborn visualizations, vector PDF/SVG output and LaTeX-ready tables | [`scripts/`](scripts/) |
| Thesis | Multi-file architecture, reusable preamble, chapters, title page, TOC/LOF/LOT, bibliography, index and appendices | [`src/thesis/`](src/thesis/) |
| Automated production | Python linting, TeX compilation, reference checks and downloadable PDF build artifacts | [GitHub Actions](.github/workflows/build-pdf.yml) |

## Technologies

- **LaTeX:** IEEEtran, AMS math, cleveref, BibTeX, booktabs, siunitx, fancyhdr and modular thesis structure.
- **TikZ and PGFPlots:** custom vector diagrams and charts that inherit the document's typography.
- **Python:** pandas, NumPy, Matplotlib and seaborn.
- **Automation:** GitHub Actions for repeatable checks and PDF generation.

## View the generated PDFs

The GitHub Actions workflow compiles three PDFs and uploads them as a downloadable artifact named `pdfs`:

1. `paper.pdf` — IEEE-style research paper.
2. `thesis.pdf` — multi-file thesis example.
3. `tikz_showcase.pdf` — native TikZ and PGFPlots gallery.

Open the [latest successful workflow run](https://github.com/uzairjaved-prog/Academic-typesetting-portfolio/actions/workflows/build-pdf.yml) and download the `pdfs` artifact from its run.

## Build locally

Requirements: Python 3.10+, TeX Live or MiKTeX, `latexmk`, IEEEtran and the packages used in the source documents.

```bash
pip install -r requirements.txt
make all
```

Individual targets:

```bash
make figures
make paper
make tikz
make thesis
make clean
```

The data and figures are generated locally and the compiled outputs are excluded from version control. See `.gitignore` for the generated paths.

## Repository structure

```text
.github/workflows/   Automated build and validation
data/                Synthetic input-data generator notes
docs/                Portfolio notes and service-bundle mapping
scripts/             Data generation and figure pipeline
src/paper/           IEEE-style research paper
src/thesis/          Multi-file thesis
src/tikz/            Native TikZ/PGFPlots diagrams
```

## Contact

For academic typesetting, LaTeX formatting, TikZ diagrams, thesis formatting, or publication-ready research figures, contact the repository owner through the [GitHub profile](https://github.com/uzairjaved-prog).
