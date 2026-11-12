# Python scripts

make_data.py creates the fixed-seed synthetic hourly dataset in data/.
generate_figures.py interpolates the inserted gaps and creates the PDF/SVG panels and LaTeX tables.
Its scatter panel shows a grid-searched hinge fit and a dashed linear baseline.
The generated key_numbers.tex includes the observation count, correlation, and hinge-fit R-squared.
Run make data to create the CSV and make figures to generate the charts and table.
Run make previews to render the PDFs into dist/previews/.
Run make before-after to create the unstyled and styled scatter comparison under dist/previews/before-after/.
make all runs the complete production pipeline.
Generated CSV, figures, tables, and preview files are outputs; do not edit them by hand.
