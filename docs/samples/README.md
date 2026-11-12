# PDF samples

This folder contains the compiled examples linked from the root README:

- [paper.pdf](paper.pdf) — three-page IEEEtran paper.
- [thesis.pdf](thesis.pdf) — sixteen-page thesis-layout sample.
- [tikz-showcase.pdf](tikz-showcase.pdf) — two-page collection of TikZ and PGFPlots diagrams.

The LaTeX sources are in [../../src/](../../src/). Rebuild the PDFs from the repository root with:

    make clean
    make all

After inspecting the output, run make refresh-samples to update these committed copies. The PDFs are compiled output, not editable source.
