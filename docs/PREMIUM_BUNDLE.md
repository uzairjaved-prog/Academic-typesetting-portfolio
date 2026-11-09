# Premium Complete Academic Bundle: how this repo maps to the offer

| Deliverable | Reference in this repo |
|---|---|
| Up to 30 pages of LaTeX conversion | `src/paper/` (journal) or `src/thesis/` (long-form) |
| 3 custom TikZ graphics | `src/tikz/transformer.tex`, `fsm.tex`, `control_loop.tex` (+ PGFPlots `pgfplot_demo.tex`) |
| 2 Python data plots | `scripts/generate_figures.py` -> `figures/` |
| Repo hosting + CI PDF build | `.github/workflows/build-pdf.yml`, `README.md` |
