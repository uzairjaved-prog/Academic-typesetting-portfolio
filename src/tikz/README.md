# TikZ and PGFPlots

These files provide the diagrams used by the paper, thesis and standalone showcase.

- [transformer.tex](transformer.tex) draws the encoder diagram.
- [fsm.tex](fsm.tex) draws the finite-state machine.
- [control_loop.tex](control_loop.tex) draws the feedback-control block diagram.
- [pgfplot_demo.tex](pgfplot_demo.tex) plots the second-order step responses.
- [tikz-styles.tex](tikz-styles.tex) defines shared drawing styles.
- [showcase.tex](showcase.tex) arranges the diagrams in a two-page document.

Build the showcase from the repository root with make tikz. It creates [showcase.pdf](showcase.pdf); make all also copies it to ../../dist/tikz-showcase.pdf.
