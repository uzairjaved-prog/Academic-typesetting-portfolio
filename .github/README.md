# GitHub configuration

This folder contains the repository's GitHub-specific files.
The PDF build is defined in [workflows/build-pdf.yml](workflows/build-pdf.yml).
It runs Ruff, creates the sample data and figures, compiles the three PDFs and checks the LaTeX logs.
The workflow runs for pull requests, pushes to main, version tags, releases and manual dispatches.
Its steps are described in [workflows/README.md](workflows/README.md).
Branch protection is configured in the repository settings, not in this folder.
Changes to the workflow should be tested with a pull request before merging.
Do not put credentials or private client files in the repository configuration.
