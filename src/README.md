# LaTeX sources

This folder contains the source for the journal paper, thesis and standalone TikZ showcase.
The [paper](paper/README.md) uses IEEEtran.
The [thesis](thesis/README.md) uses the book class and is split into a preamble, front matter, chapters and appendices.
The [TikZ showcase](tikz/README.md) compiles the diagrams without either document.

From the repository root, build everything with:

    make all

Build one document with make paper, make thesis or make tikz. The Makefile copies the PDFs to the repository-root dist/ folder. Edit the .tex source files; LaTeX auxiliary files and compiled PDFs are build outputs.
