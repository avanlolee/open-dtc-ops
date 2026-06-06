# Release Notes: v0.1.0

`open-dtc-ops` v0.1.0 is the first MVP release of a local CSV-based ecommerce operations toolkit for small DTC and marketplace sellers.

## Highlights

- Analyze ad ROI from local sales CSV files.
- Calculate profit and net margin after COGS, shipping, platform fees, and ad spend.
- Flag inventory reorder risk from local inventory CSV files.
- Score product research opportunities with simple weighted criteria.
- Keep formulas transparent and documented for spreadsheet-oriented operators.

## Included Commands

```bash
dtcops roi examples/sales_sample.csv
dtcops profit examples/sales_sample.csv
dtcops inventory examples/inventory_sample.csv
dtcops score examples/product_research_sample.csv
```

## Project Scope

This release does not include scraping, marketplace login automation, a database, a web dashboard, or private seller data storage.

## Verification

Before publishing this release, run:

```bash
pytest
dtcops roi examples/sales_sample.csv
dtcops profit examples/sales_sample.csv
dtcops inventory examples/inventory_sample.csv
dtcops score examples/product_research_sample.csv
```

## Next Priorities

- CSV export for analysis results.
- Marketplace-specific sample CSV files.
- Better numeric validation for real-world CSV exports.
- Public demo cases and weekly review guides.

