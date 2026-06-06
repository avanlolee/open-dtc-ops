# Maintainers

This file documents who is responsible for review, triage, releases, and security decisions.

## Primary Maintainer

- Jack Lee / `avanlolee`

## Maintainer Responsibilities

- Review pull requests for correctness, simplicity, and operator usefulness.
- Triage issues and label beginner-friendly work where possible.
- Keep formulas, CSV requirements, and sample files documented.
- Run the release checklist before tagging a release.
- Avoid features that add private seller data storage, scraping, marketplace login automation, or unnecessary platform complexity.

## Review Priorities

Changes should be small, testable, and useful for small ecommerce operators working from CSV exports.

Priority areas:

- Correct ROI, profit, inventory, and product research calculations.
- Helpful validation errors for missing or invalid CSV inputs.
- Marketplace-specific sample CSV formats.
- Documentation that helps non-technical operators run the CLI safely.
- Maintainer automation that reduces issue triage, review, and release workload.

## Release Ownership

The primary maintainer owns version tags, changelog updates, GitHub releases, and package publishing decisions.

Before a release:

- Confirm CI passes.
- Confirm local tests pass.
- Run all sample CLI commands.
- Update `CHANGELOG.md`.
- Confirm no private seller data is included.
