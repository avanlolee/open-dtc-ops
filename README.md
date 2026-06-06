# open-dtc-ops

[![CI](https://github.com/avanlolee/open-dtc-ops/actions/workflows/ci.yml/badge.svg)](https://github.com/avanlolee/open-dtc-ops/actions/workflows/ci.yml)
[![Python Versions](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://github.com/avanlolee/open-dtc-ops)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Open-source ecommerce operations toolkit for small DTC and marketplace sellers.

`open-dtc-ops` helps non-technical ecommerce operators analyze CSV exports for ad ROI, profitability, inventory risk, and product research scoring.

## Why This Matters

Small ecommerce sellers often run on spreadsheets, exported marketplace reports, and limited operating time. Many cannot justify a full business intelligence stack, but they still need reliable answers to basic operating questions:

- Are ads profitable after COGS, fees, and shipping?
- Which products need reordering before stockouts happen?
- Which product ideas are strong enough to test with limited cash?
- Which metrics should be reviewed every week?

This project keeps the workflow simple: local CSV files, transparent formulas, and terminal output that is easy to copy into an operating review.

## What It Does

- Analyze ad ROI from sales CSV files.
- Calculate contribution profit and net margin.
- Flag inventory reorder risk.
- Score product research opportunities with simple weighted criteria.

## Example Output Areas

- ROI: revenue, ad spend, ROAS, ACOS, break-even ACOS, net margin, and profitability status.
- Profit: gross profit, contribution profit, net profit, and net margin.
- Inventory: days left, reorder point, and reorder status.
- Product research: weighted score and rating.

## What It Does Not Do

- No database.
- No web dashboard yet.
- No scraping.
- No platform login automation.
- No private business data.

Use sample CSV files or your own local exports with the documented columns.

For concrete operator workflows, see `docs/demo-cases.md`.

## Install

```bash
python -m pip install -e ".[dev]"
```

## CLI Commands

```bash
dtcops roi examples/sales_sample.csv
dtcops profit examples/sales_sample.csv
dtcops inventory examples/inventory_sample.csv
dtcops score examples/product_research_sample.csv
```

## Development

```bash
pytest
```

CI runs the test suite and all sample CLI commands across Python 3.9, 3.10, 3.11, and 3.12.

## Maintainer Automation

This repository is designed to be maintainable by Codex-style coding agents:

- Calculation logic is kept in pure functions.
- CLI code is separated from business formulas.
- Required CSV columns are validated with clear errors.
- Sample CSV files make smoke testing deterministic.
- Tests cover each calculation module.
- The roadmap favors small, reviewable improvements over large product jumps.

Good future agent tasks include adding CSV export, adding marketplace-specific sample formats, expanding tests, and improving documentation without adding scraping, platform login automation, a database, or a dashboard.

Maintainer responsibilities are documented in `MAINTAINERS.md`. Security reporting and scope are documented in `SECURITY.md`.

The public maintenance backlog is documented in `docs/maintenance-backlog.md` so contributors can pick up small, useful issues. Ready-to-publish issue drafts are available in `docs/github-issue-drafts.md`.

## Release Status

The first MVP is versioned as `0.1.0` and tagged as `v0.1.0`. See `CHANGELOG.md` and `docs/release-notes-v0.1.0.md` for release notes, and the roadmap for planned improvements.

## License

MIT
