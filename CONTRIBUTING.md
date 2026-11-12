# Contributing

Thank you for taking the time to improve this repository. Useful contributions include corrections to the LaTeX examples, clearer diagrams, reproducible figure scripts, build fixes and documentation updates.

## Before making a change

- Check the existing source and open issues to avoid duplicating work.
- Keep the synthetic-data notice accurate. Do not present generated observations as real measurements or results.
- Do not add client manuscripts, private data, credentials, access tokens or unpublished work.
- Do not add a university affiliation, degree, testimonial or client claim unless it is verified and explicitly supplied for inclusion.

## Set up the project

Use Python 3.10 or newer and install the Python requirements:

    python -m pip install -r requirements.txt

A full build also requires TeX Live or MiKTeX with latexmk, and Poppler's pdftoppm utility for preview rendering.

## Checks to run

From the repository root, run:

    ruff check scripts
    make clean
    make all

The build generates the dataset and figures, compiles the paper, thesis and TikZ showcase, then renders the previews. Check the PDFs before submitting a change. In particular, look for blank pages, clipped diagrams, unresolved references and unexpected layout changes.

If a source change affects the PDFs or preview images, refresh the committed copies after reviewing the output:

    make refresh-samples

The generated files under figures/, dist/, and the source directories' LaTeX auxiliary files are build outputs. Change their source scripts or .tex files rather than editing generated outputs directly.

## Pull requests

1. Create a feature branch from the latest main.
2. Make a focused change and use a commit message that describes it, such as fix(thesis): correct chapter spacing or docs: clarify PDF build steps.
3. Run the checks above and inspect the changed output.
4. Open a pull request against main. Explain the reason for the change, list the files affected, and include the commands and results of the checks you ran.
5. Wait for the required Lint Python and Build documents checks to pass before merging.

Do not push commits directly to main. Keep pull requests small enough to review. If the change intentionally affects the sample PDFs, include the refreshed files from docs/samples/ and docs/previews/.

## Documentation and examples

Use plain, specific language. Describe what the sample actually contains; do not claim that an illustrative diagram demonstrates a real system or that synthetic values establish a research conclusion. Keep paths and build commands consistent with the Makefile.

## Questions

For a bug report or feature request, use the repository's GitHub issue templates. For a suspected security issue, do not open a public issue; follow SECURITY.md.
