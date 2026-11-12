# Committed preview images

This folder contains the JPG previews embedded in the root README.
The preview generator writes build outputs to dist/previews/, not to this folder.
Run make all from the repository root to rebuild PDFs and generate those preview images.
Run make refresh-samples to copy the new JPGs from dist/previews/ into this folder.
The overview, paper page, thesis cover, TikZ gallery, and scientific-figure preview are committed.
The before-and-after SVG comparison is a separate local output under dist/previews/before-after/.
Do not edit the committed JPGs by hand; regenerate them from the PDFs and figure script.\nThe five tracked images are overview, paper page, thesis cover, TikZ page, and scientific figures.
The README embeds these images using relative paths in the repository.
