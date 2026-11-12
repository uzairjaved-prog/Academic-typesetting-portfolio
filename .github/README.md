# GitHub configuration

This folder contains issue templates and the automated PDF workflow.
GitHub reads the issue templates when a visitor opens a new issue.
The workflow file under workflows/ lints Python and builds the sample documents.
The workflow runs on pushes to main, pull requests, tags, and manual dispatch.
The CI steps are documented in workflows/README.md.
Repository branch protection is configured in GitHub settings, not in these files.
Edit workflow or template files only when their behaviour needs to change.
Do not store tokens, credentials, or private client material in this folder.
