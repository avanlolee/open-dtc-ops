# GitHub Issue Drafts

These drafts are ready to publish as public GitHub issues. They create a visible maintenance queue for contributors and for program reviewers evaluating project activity.

## 1. Add CSV export for analysis results

Labels: `enhancement`, `help wanted`

```markdown
## Why it matters

Operators often need to paste weekly ROI, profit, and inventory results into spreadsheets or operating reviews.

## Scope

Add an optional output path to supported CLI commands so analysis results can be saved as CSV while keeping the current terminal output unchanged.

## Acceptance criteria

- Add an optional `--output` path to supported CLI commands.
- Write analysis results to CSV when `--output` is provided.
- Keep current terminal output unchanged.
- Add tests for output file creation and sample rows.

## Notes

Keep the MVP local and CSV-based. Do not add a database, dashboard, scraping, login automation, or private data storage.
```

## 2. Add Amazon sample CSV preset

Labels: `enhancement`, `good first issue`

```markdown
## Why it matters

Many small marketplace sellers start with Amazon exports and need a concrete example before mapping their own data.

## Scope

Add a synthetic Amazon-style sample and document how an operator can map marketplace export columns into the project format.

## Acceptance criteria

- Add `examples/amazon_sales_sample.csv` with synthetic data.
- Document column mapping in `docs/csv-format.md`.
- Add a short docs example showing how to run ROI and profit commands with the sample.
- Do not include private seller data.
```

## 3. Improve numeric validation for blank and non-numeric values

Labels: `bug`, `help wanted`

```markdown
## Why it matters

CSV exports often include blanks, currency symbols, or text values. Clear validation prevents misleading financial output.

## Scope

Validate required numeric columns before calculations and return helpful errors when values cannot be interpreted safely.

## Acceptance criteria

- Validate required numeric columns before calculations.
- Return helpful error messages that name the bad column.
- Add tests for blank, text, and invalid numeric inputs.
- Keep existing valid sample CSV behavior unchanged.
```

## 4. Add Shopify sample CSV preset

Labels: `enhancement`, `good first issue`

```markdown
## Why it matters

Small DTC operators often use Shopify exports and need a simple local way to review profitability.

## Scope

Add a synthetic Shopify-style sample and document how a Shopify operator should map export columns into the project format.

## Acceptance criteria

- Add `examples/shopify_sales_sample.csv` with synthetic data.
- Document how Shopify-like columns map to the project sales CSV format.
- Add a smoke test or docs example for the sample.
- Do not include private seller data.
```

## 5. Add weekly review guide

Labels: `documentation`, `good first issue`

```markdown
## Why it matters

The CLI is more useful when operators understand what decision to make after reading the output.

## Scope

Create a beginner-friendly weekly operating review guide that explains the order of reviewing ROI, profit, inventory, and product research output.

## Acceptance criteria

- Add a short guide under `docs/`.
- Cover ROI, profit, inventory, and product research review order.
- Include sample thresholds and follow-up actions.
- Keep the guide beginner-friendly and spreadsheet-oriented.
```

## 6. Add GitHub release workflow documentation

Labels: `documentation`, `help wanted`

```markdown
## Why it matters

The project needs repeatable release steps before publishing to PyPI.

## Scope

Expand the release checklist so a maintainer can publish a GitHub release consistently from a clean local checkout.

## Acceptance criteria

- Expand `docs/release-checklist.md` with exact GitHub release steps.
- Include how to verify version, changelog, tag, and sample CLI output.
- Do not add automated publishing until manual releases are stable.
```

## 7. Add TikTok Shop sample CSV preset

Labels: `enhancement`, `good first issue`

```markdown
## Why it matters

TikTok Shop operators often make fast product and ad decisions, but exports still need to be reviewed against contribution profit and inventory risk.

## Scope

Add a synthetic TikTok Shop-style sample and document how operators can use it with the existing ROI and profit commands.

## Acceptance criteria

- Add `examples/tiktok_shop_sales_sample.csv` with synthetic data.
- Document column mapping in `docs/csv-format.md`.
- Add a short docs example for the sample.
- Do not include private seller data.
```

## 8. Add Walmart marketplace sample CSV preset

Labels: `enhancement`, `good first issue`

```markdown
## Why it matters

Walmart marketplace sellers need the same simple local review loop for margin, ads, and fulfillment costs.

## Scope

Add a synthetic Walmart-style sample and document how operators can map marketplace exports into the project format.

## Acceptance criteria

- Add `examples/walmart_sales_sample.csv` with synthetic data.
- Document column mapping in `docs/csv-format.md`.
- Add a short docs example for ROI and profit commands.
- Do not include private seller data.
```

