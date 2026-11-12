# Thesis appendices

[appendix_a.tex](appendix_a.tex) lists the commands used to reproduce the sample. [appendix_b.tex](appendix_b.tex) derives the covariance expression for the ordinary least-squares estimator.

[../main.tex](../main.tex) includes both appendices after the five chapters. Their labels are used in cross-references from the thesis text.

Build from the repository root with:

    make thesis

Edit the appendix source files. The compiled pages appear in [../main.pdf](../main.pdf); the bibliography and index are generated during the build.
