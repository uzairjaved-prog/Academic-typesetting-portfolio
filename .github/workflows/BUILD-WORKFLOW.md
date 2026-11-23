# PDF build workflow

[build-pdf.yml](build-pdf.yml) runs Ruff, generates the sensor data and figures, then compiles the paper, thesis and TikZ showcase.

The build uses TeX Live, latexmk, Poppler and the Python packages listed in [requirements.txt](../../requirements.txt). It checks the LaTeX logs for undefined references and citations.

Successful runs upload the PDFs, checksums and generated previews as an artifact named pdfs. Version tags also publish those files to a GitHub Release.

Run the build from the repository root:

    make clean
    make all

The workflow uploads build results; it does not update the committed files under docs/.
