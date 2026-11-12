# Compiled PDF samples

This folder contains the committed PDF versions of the journal paper, thesis, and TikZ showcase.
These files let visitors read the examples without downloading an Actions artifact.
The PDFs are produced from the LaTeX sources under src/.
From the repository root, run make clean && make all to rebuild the documents.
After reviewing the output, run make refresh-samples to copy the new PDFs here.
The files are paper.pdf, thesis.pdf, and tikz-showcase.pdf.\nThe PDFs are binary build outputs and should not be edited by hand.
If a source file changes, rebuild all documents and update the samples in a separate commit.
The research scenario and sensor data in these PDFs are synthetic examples.
