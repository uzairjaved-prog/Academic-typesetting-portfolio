# Journal paper source

main.tex is the entry point for the IEEEtran journal-style example.
references.bib contains the bibliography records cited by the paper.
The text and figures describe a synthetic dataset, not real site measurements.
From the repository root, build it with make paper.
The equivalent command is latexmk -pdf -cd -interaction=nonstopmode -halt-on-error src/paper/main.tex.
The generated PDF is src/paper/main.pdf; make all copies it to dist/paper.pdf.
The paper imports shared TikZ styles and generated figure macros from sibling folders.
Run make figures before compiling if the CSV or figure outputs have been cleaned.
Do not edit main.pdf, .aux, .bbl, or .log files by hand.
