# Maintenance Backlog

This backlog is designed for public GitHub issues. It favors small, reviewable tasks that improve usefulness for small ecommerce operators and reduce maintainer workload.

Ready-to-publish issue bodies are available in `docs/github-issue-drafts.md`.

## Ready Issues

### Add CSV export for analysis results

Labels: `enhancement`, `help wanted`

Why it matters:

Operators often need to paste weekly ROI, profit, and inventory results into spreadsheets or operating reviews.

Acceptance criteria:

- Add an optional `--output` path to supported CLI commands.
- Write analysis results to CSV when `--output` is provided.
- Keep current terminal output unchanged.
- Add tests for output file creation and sample rows.

### Add Amazon sample CSV preset

Labels: `enhancement`, `good first issue`

Why it matters:

Many small marketplace sellers start with Amazon exports and need a concrete example before mapping their own data.

Acceptance criteria:

- Add `examples/amazon_sales_sample.csv` with synthetic data.
- Document column mapping in `docs/csv-format.md`.
- Add a short README or docs example showing how to run ROI and profit commands with the sample.

### Improve numeric validation for blank and non-numeric values

Labels: `bug`, `help wanted`

Why it matters:

CSV exports often include blanks, currency symbols, or text values. Clear validation prevents misleading financial output.

Acceptance criteria:

- Validate required numeric columns before calculations.
- Return helpful error messages that name the bad column.
- Add tests for blank, text, and invalid numeric inputs.

### Add Shopify sample CSV preset

Labels: `enhancement`, `good first issue`

Why it matters:

Small DTC operators often use Shopify exports and need a simple local way to review profitability.

Acceptance criteria:

- Add `examples/shopify_sales_sample.csv` with synthetic data.
- Document how Shopify-like columns map to the project sales CSV format.
- Add a smoke test or docs example for the sample.

### Add weekly review guide

Labels: `documentation`, `good first issue`

Why it matters:

The CLI is more useful when operators understand what decision to make after reading the output.

Acceptance criteria:

- Add a short guide under `docs/`.
- Cover ROI, profit, inventory, and product research review order.
- Include sample thresholds and follow-up actions.
- Keep the guide beginner-friendly and spreadsheet-oriented.

### Add GitHub release workflow documentation

Labels: `documentation`, `help wanted`

Why it matters:

The project needs repeatable release steps before publishing to PyPI.

Acceptance criteria:

- Expand `docs/release-checklist.md` with exact GitHub release steps.
- Include how to verify version, changelog, tag, and sample CLI output.
- Do not add automated publishing until manual releases are stable.

### Add TikTok Shop sample CSV preset

Labels: `enhancement`, `good first issue`

Why it matters:

TikTok Shop operators often make fast product and ad decisions, but exports still need to be reviewed against contribution profit and inventory risk.

Acceptance criteria:

- Add `examples/tiktok_shop_sales_sample.csv` with synthetic data.
- Document column mapping in `docs/csv-format.md`.
- Add a short docs example for the sample.
- Do not include private seller data.

### Add Walmart marketplace sample CSV preset

Labels: `enhancement`, `good first issue`

Why it matters:

Walmart marketplace sellers need the same simple local review loop for margin, ads, and fulfillment costs.

Acceptance criteria:

- Add `examples/walmart_sales_sample.csv` with synthetic data.
- Document column mapping in `docs/csv-format.md`.
- Add a short docs example for ROI and profit commands.
- Do not include private seller data.

## Triage Rules

- Prefer `good first issue` for docs, sample CSVs, and narrow validation tests.
- Prefer `help wanted` for tasks that benefit from external operator input.
- Reject requests for scraping, marketplace login automation, private data storage, or a database unless the project scope changes deliberately.
