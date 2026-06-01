# open-dtc-ops

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

## Maintainer Automation

This repository is designed to be maintainable by Codex-style coding agents:

- Calculation logic is kept in pure functions.
- CLI code is separated from business formulas.
- Required CSV columns are validated with clear errors.
- Sample CSV files make smoke testing deterministic.
- Tests cover each calculation module.
- The roadmap favors small, reviewable improvements over large product jumps.

Good future agent tasks include adding CSV export, adding marketplace-specific sample formats, expanding tests, and improving documentation without adding scraping, platform login automation, a database, or a dashboard.

## Release Status

The first MVP is versioned as `0.1.0`. See `CHANGELOG.md` for release notes and the roadmap for planned improvements.

## License

MIT
