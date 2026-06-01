# Contributing

Thanks for helping improve `open-dtc-ops`.

## Local Setup

```bash
python -m pip install -e ".[dev]"
pytest
```

## Guidelines

- Keep the MVP simple and beginner-friendly.
- Prefer pure functions for calculation logic.
- Add tests for every calculation change.
- Do not add scraping, login automation, private seller data, or a database.
- Use sample CSV files for examples and tests.

## Pull Requests

Before opening a pull request:

```bash
pytest
dtcops roi examples/sales_sample.csv
dtcops profit examples/sales_sample.csv
dtcops inventory examples/inventory_sample.csv
dtcops score examples/product_research_sample.csv
```

