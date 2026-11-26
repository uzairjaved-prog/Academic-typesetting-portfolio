# README preview images

The JPGs in this folder include the images used by the root README:

- `repository-social-preview-q68.jpg` is the wide portfolio banner shown near the top of the root README. It can also be uploaded separately under the repository's **Settings → General → Social preview**.
- `paper-page-1.jpg` shows the first page of the paper sample.
- `thesis-cover.jpg` shows the thesis title page.
- `tikz-gallery.jpg` shows the TikZ diagram showcase.
- `scientific-figures.jpg` shows the Python-generated scientific figures.

`portfolio-overview.jpg` is an earlier overview image retained in the repository; the root README now uses the social-preview banner instead.

The preview-generation script writes new images to the repository-root `dist/previews/` folder, not here. Rebuild the PDFs and previews with:

    make clean
    make all

Then copy the reviewed images into this folder with `make refresh-samples`. The before-and-after SVG comparison is a separate local output in `dist/previews/before-after/`; it is not one of the committed JPG previews.
