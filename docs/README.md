# Portfolio files

This folder holds the files visitors can open without running the build.

- [samples/](samples/) contains the paper, thesis and TikZ showcase PDFs.
- [previews/](previews/) contains the five JPG images used in the root README.
- [PREMIUM_BUNDLE.md](PREMIUM_BUNDLE.md) describes the work shown in the examples and the information needed to scope a project.

The build creates fresh PDFs in the repository-root dist/ folder and JPGs in dist/previews/. After checking the results, copy them into the tracked folders with:

    make refresh-samples

The PDFs and JPGs here are committed copies of generated output. Rebuild them from the LaTeX and Python sources rather than editing the binary files directly.
