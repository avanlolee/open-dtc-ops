# Release Checklist

Use this checklist before publishing a new release.

## Before Release

- Confirm `pytest` passes locally.
- Confirm all sample CLI commands run successfully:
  - `dtcops roi examples/sales_sample.csv`
  - `dtcops profit examples/sales_sample.csv`
  - `dtcops inventory examples/inventory_sample.csv`
  - `dtcops score examples/product_research_sample.csv`
- Update `CHANGELOG.md`.
- Confirm `README.md` install and CLI examples are current.
- Confirm no private seller data is included.
- Confirm the release does not add scraping, platform login automation, a database, or a dashboard unless explicitly planned.

## GitHub Release

- Create or confirm a version tag, for example `v0.1.0`.
- Copy release notes from `CHANGELOG.md`.
- Mark stable MVP releases as non-prerelease.

## Package Publishing

PyPI publishing should happen after install behavior and CLI smoke tests are stable.

Before publishing:

- Confirm package metadata in `pyproject.toml`.
- Build the package locally.
- Inspect the generated wheel and source distribution.
- Test install in a clean virtual environment.
- Publish to TestPyPI first when possible.
- Publish to PyPI only when the release is ready for external users.

