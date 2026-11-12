# GitHub Actions workflows

build-pdf.yml runs Ruff, generates the synthetic data and figures, and compiles three PDFs.
The build also checks logs for undefined references and citations.
It uses TeX Live, Poppler, Python dependencies, and scripts/make_previews.py.
The PDF files and preview JPGs are uploaded as the pdfs artifact for 30 days.
A version tag such as v1.1.0 also publishes PDFs, checksums, and previews to a GitHub Release.
Run the same main build locally with make clean && make all.
The workflow does not commit generated outputs; use make refresh-samples locally for that.
Edit this YAML file to change CI behaviour; do not edit run artifacts.
