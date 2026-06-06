# Changelog

All notable changes to this project will be documented in this file.

The format follows a simple, human-readable release log. This project uses semantic versioning once releases begin.

## Unreleased

### Added

- CLI smoke tests that run every sample command against the sample CSV files.
- Python 3.9, 3.10, 3.11, and 3.12 CI matrix with CLI smoke tests.
- Maintainer responsibility documentation in `MAINTAINERS.md`.
- Security reporting and scope documentation in `SECURITY.md`.
- Project health badges in `README.md`.
- Public demo cases that connect CLI output to operator decisions.
- Public maintenance backlog with ready-to-file GitHub issues.
- Draft release notes for `v0.1.0`.
- Maintenance task issue template and ready-to-publish GitHub issue drafts.

## [0.1.0] - 2026-06-01

### Added

- Initial Typer CLI with `roi`, `profit`, `inventory`, and `score` commands.
- Pandas-based CSV loading and processing.
- Rich terminal tables for operator-friendly output.
- Required-column validation with helpful error messages.
- Pure calculation modules for ROI, profit, inventory, and product research scoring.
- Sample CSV files for sales, inventory, and product research.
- Pytest coverage for validators and every calculation module.
- Beginner-focused documentation for setup, CSV formats, formulas, and roadmap.
- MIT License, contribution guide, code of conduct, issue templates, pull request template, and GitHub Actions CI.

### Notes

- This is an MVP for local CSV analysis only.
- No database, web dashboard, scraping, platform login automation, or private seller data storage is included.
