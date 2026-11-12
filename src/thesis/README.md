# Thesis source

main.tex is the root file; preamble.tex holds packages, page layout, and macros.
The title page and abstract are in frontmatter/.
The five chapters are in chapters/, and appendices are in backmatter/.
Build from the repository root with make thesis.
The direct command is latexmk -pdf -cd -interaction=nonstopmode -halt-on-error src/thesis/main.tex.
The PDF is created as src/thesis/main.pdf and copied to dist/thesis.pdf by make all.
The figure list is included; a separate list of tables is omitted because the sample has one table. Figures and numeric macros are generated in figures/ by make figures.
Chapter text belongs in the chapter files; shared formatting belongs in preamble.tex.
Do not edit generated PDFs, .aux, .toc, .lof, .lot, or .log files.
