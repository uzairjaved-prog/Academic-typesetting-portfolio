# TikZ and PGFPlots source

This folder contains the vector diagrams and the standalone showcase.tex document.
tikz-styles.tex defines shared colours, node shapes, and arrow styles.
The other files draw the Transformer, finite-state machine, PID block diagram, and response plot.
Build the showcase from the repository root with make tikz.
The direct command is latexmk -pdf -cd -interaction=nonstopmode -halt-on-error src/tikz/showcase.tex.
The standalone PDF is src/tikz/showcase.pdf; make all copies it to dist/tikz-showcase.pdf.
The paper and thesis import some of these diagram sources directly.
Edit the .tex sources; do not edit compiled PDFs or auxiliary files.
