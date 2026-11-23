# GitHub repository files

This folder contains the Actions workflow and the issue templates used by the repository.

- workflows/build-pdf.yml runs Python linting, generates the data and figures, builds the PDFs and uploads the build artifact.
- ISSUE_TEMPLATE/ contains the bug-report and feature-request forms.
- ISSUE_TEMPLATE/config.yml links issue authors to the security-reporting instructions.

The workflow runs for pull requests, pushes to main, version tags, published releases and manual dispatches. Branch protection is configured in the repository settings, not in these files.

Do not put credentials, private manuscripts or client datasets in GitHub templates or workflow files. See the root CONTRIBUTING.md and SECURITY.md for repository procedures.
