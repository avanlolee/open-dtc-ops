# open-dtc-ops

Open-source ecommerce operations toolkit for small DTC and marketplace sellers.

`open-dtc-ops` helps non-technical ecommerce operators analyze CSV exports for ad ROI, profitability, inventory risk, and product research scoring.

## What It Does

- Analyze ad ROI from sales CSV files.
- Calculate contribution profit and net margin.
- Flag inventory reorder risk.
- Score product research opportunities with simple weighted criteria.

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

## License

MIT

