# Journal paper

[main.tex](main.tex) is the entry point. [references.bib](references.bib) contains the bibliography records cited in the paper.

The document uses the IEEEtran journal class. It includes a two-column layout, mathematical notation, references, a summary table and four data panels. The research scenario and observations are synthetic.

From the repository root, run:

    make paper

The build first runs the data and figure targets. It creates main.pdf in this folder and copies a second copy to the repository-root dist/paper.pdf when make all is used.

Edit main.tex and references.bib. The PDF, .aux, .bbl and .log files are produced by the build.
