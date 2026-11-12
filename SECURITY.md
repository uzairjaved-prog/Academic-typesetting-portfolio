# Security policy

This repository contains LaTeX source, Python scripts and synthetic example data. It is not a hosted application. Do not use it to store credentials, private manuscripts, client datasets or production secrets.

## Reporting a vulnerability

Please do not report a suspected vulnerability in a public issue, discussion or pull request. A public report can expose details before the issue is understood or fixed.

**Private vulnerability reporting is currently disabled for this repository.** To report a concern, contact the repository owner through the [GitHub profile](https://github.com/uzairjaved-prog) and ask for a private reporting channel. Do not include exploit steps, access tokens or sensitive details in a public issue while requesting that channel.

The repository owner can enable GitHub's private vulnerability reporting in the repository settings. Once it is enabled, reports can be submitted from the Security tab using GitHub's Report a vulnerability option.

When a private channel is available, include:

- A short description of the issue and its possible impact.
- The affected file, workflow or dependency.
- Steps to reproduce the behaviour, using synthetic or otherwise non-sensitive examples.
- A suggested mitigation, if known.

Do not include passwords, access tokens, private client files or personal information.

## Supported scope

Reports are relevant to the Python scripts, dependency configuration, GitHub Actions workflow and document build process. The PDFs and synthetic dataset are portfolio samples; this repository does not operate a production service.

## Dependency and workflow changes

Identify the affected package or workflow step and provide a minimal reproduction. Security-related changes should be tested with the Python lint and PDF build checks before merging.
