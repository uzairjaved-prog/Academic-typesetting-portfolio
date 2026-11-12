# README preview images

The five JPGs in this folder are used by the root README: the portfolio overview, paper first page, thesis title page, TikZ gallery and scientific-figures panel.

The preview script writes new images to the repository-root dist/previews/ folder, not here. Rebuild the PDFs and previews with:

    make clean
    make all

Then copy the new images into this folder with make refresh-samples. The before-and-after SVG comparison is a separate local output in dist/previews/before-after/; it is not one of the five committed JPGs.
