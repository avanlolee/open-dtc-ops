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

Start from a clean checkout of the commit you plan to release:

```bash
git status --short
```

Confirm the package metadata version and package module version agree:

```bash
python -c "import tomllib; print(tomllib.load(open('pyproject.toml', 'rb'))['project']['version'])"
python -c "import runpy; print(runpy.run_path('src/dtcops/__init__.py')['__version__'])"
```

Confirm the changelog has release notes for the same version:

```bash
grep -n "## \\[0.1.0\\]" CHANGELOG.md
```

Run the sample CLI commands and keep the output in the release notes draft if it changed:

```bash
dtcops roi examples/sales_sample.csv
dtcops profit examples/sales_sample.csv
dtcops inventory examples/inventory_sample.csv
dtcops score examples/product_research_sample.csv
```

Create or confirm the release tag:

```bash
git tag --list "v0.1.0"
git tag -a v0.1.0 -m "open-dtc-ops v0.1.0"
git push origin v0.1.0
```

Draft the GitHub release manually:

1. Open **Releases** in the GitHub repository.
2. Choose **Draft a new release**.
3. Select or create the `v0.1.0` tag.
4. Use `open-dtc-ops v0.1.0` as the release title.
5. Copy the matching `CHANGELOG.md` notes into the release body.
6. Include the sample CLI output only when it helps verify user-visible behavior.
7. Mark stable MVP releases as **not** prerelease.
8. Publish only after the version, changelog, tag, and sample command output all match.

Do not add automated publishing until manual releases are stable and repeatable.

## Package Publishing

PyPI publishing should happen after install behavior and CLI smoke tests are stable.

Before publishing:

- Confirm package metadata in `pyproject.toml`.
- Build the package locally.
- Inspect the generated wheel and source distribution.
- Test install in a clean virtual environment.
- Publish to TestPyPI first when possible.
- Publish to PyPI only when the release is ready for external users.

