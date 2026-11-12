# Thesis front matter

This folder contains the title page and abstract used before the main chapters.
main.tex loads both files near the start of the document.
The title, author, and date commands are defined in ../preamble.tex.
Build the complete document from the repository root with make thesis.
The compiled front matter appears in src/thesis/main.pdf.
The abstract reports the generated dataset and its in-sample model statistic.
The title page identifies this as a portfolio example, not a university submission.
Keep institution and degree claims out unless a real client supplies them.
Edit the .tex files; do not edit the generated PDF.
