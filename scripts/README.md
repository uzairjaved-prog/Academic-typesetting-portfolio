# Python scripts

[make_data.py](make_data.py) writes the synthetic CSV at [../data/](../data/). It creates 2,880 hourly rows for 120 days and three example sites.

[generate_figures.py](generate_figures.py) fills the 50 inserted missing values by time-ordered interpolation. It writes four figure panels, a combined chart, the summary table and key_numbers.tex under the repository-root figures/ folder.

[make_previews.py](make_previews.py) renders the built PDFs and combined chart as JPGs in the repository-root dist/previews/ folder.

From the repository root, run:

    make clean
    make all

make before-after creates a separate SVG comparison in dist/previews/before-after/. These CSV, chart, table and preview files are generated outputs.
