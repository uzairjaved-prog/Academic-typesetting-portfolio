# Security policy

This repository contains LaTeX source files, Python scripts, build configuration and synthetic example data. It is a portfolio project, not a hosted application or production service.

## Reporting a vulnerability

**Private vulnerability reporting is enabled for this repository.**

Please do not report suspected vulnerabilities in a public issue, discussion or pull request. Instead:

1. Open the repository's **Security** tab.
2. Select **Report a vulnerability**.
3. Describe the affected file, workflow, dependency or build behaviour.
4. Include a minimal reproduction using synthetic or otherwise non-sensitive examples, along with the possible impact and any suggested mitigation.

GitHub sends the report through its private vulnerability-reporting process. Do not include passwords, access tokens, private manuscripts, client data or other personal information in a report unless they are essential to explain the issue; redact them whenever possible.

There is no guaranteed response or resolution time. The report will be reviewed based on its scope and severity.

## Supported scope

Reports are relevant to security issues in:

- Python scripts in `scripts/`.
- Dependency declarations and project configuration.
- GitHub Actions workflows in `.github/workflows/`.
- The document build process and generated build outputs.

The committed PDFs and synthetic dataset are portfolio samples. The repository does not run a production service, process live sensor feeds or store client documents.

## Dependency and workflow reports

For a dependency or workflow concern, identify the affected package or workflow step and provide a minimal reproduction. Security-related changes should be checked with:

~~~bash
ruff check scripts
make clean
make all
~~~

Do not attach confidential or unpublished client material to demonstrate a problem.