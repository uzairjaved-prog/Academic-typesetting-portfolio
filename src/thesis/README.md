# Thesis source

[main.tex](main.tex) sets the order of the title page, abstract, contents, chapters, appendices, bibliography and index. [preamble.tex](preamble.tex) holds the packages, page layout, metadata and shared commands.

The [front matter](frontmatter/README.md), [five chapters](chapters/README.md) and [appendices](backmatter/README.md) are kept in separate folders.

From the repository root, build the thesis with:

    make thesis

The command also generates the figures and numeric macros imported by the thesis. It creates main.pdf in this folder and, with make all, a copy at the repository-root dist/thesis.pdf.

Change the .tex source files rather than the generated PDF or LaTeX auxiliary files.
