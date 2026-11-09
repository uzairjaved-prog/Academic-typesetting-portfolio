# Contributing

1. Fork and create a branch from `main`.
2. Install prerequisites (see README) and run `make all`.
3. Keep generated outputs (`figures/`, `dist/`, `data/*.csv`) out of commits; they are rebuilt by script and CI.
4. LaTeX: one sentence per source line where practical, no hard-coded fonts in TikZ, shared styles in `src/tikz/tikz-styles.tex`.
5. Python: `ruff check scripts` must pass; keep figure code deterministic (fixed seeds).
6. Open a pull request; CI must be green.

Commit messages follow Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`).
