# Demo Cases

These demo cases show how a small ecommerce operator can turn local CSV exports into weekly operating decisions.

All examples use synthetic data from the `examples/` directory. No private seller data is included.

## Weekly Profitability Review

Command:

```bash
dtcops roi examples/sales_sample.csv
dtcops profit examples/sales_sample.csv
```

What to review:

- Whether net profit is positive after COGS, shipping, platform fees, and ad spend.
- Whether ACOS is below break-even ACOS.
- Whether the account can increase ad spend without turning unprofitable.

Sample result:

- Revenue: 1,151.00
- Ad spend: 259.00
- ROAS: 4.44
- ACOS: 0.23
- Break-even ACOS: 0.45
- Net profit: 262.30
- Net margin: 0.23
- Status: Profitable

Operator decision:

- Keep current ads running because ACOS is below break-even ACOS.
- Review whether the best converting products can support a small budget increase.
- Do not scale blindly until inventory risk is checked.

## Inventory Reorder Review

Command:

```bash
dtcops inventory examples/inventory_sample.csv
```

What to review:

- Products marked `Reorder Now`.
- Products marked `Watch`.
- Whether reorder points reflect supplier lead time and safety stock.

Sample result:

| Product | Days Left | Reorder Point | Status |
| --- | ---: | ---: | --- |
| Car Seat Gap Organizer | 20.00 | 156.00 | Watch |
| Trunk Cargo Net | 16.25 | 92.00 | Reorder Now |
| Dashboard Phone Mount | 9.33 | 46.00 | Reorder Now |

Operator decision:

- Reorder `Trunk Cargo Net` and `Dashboard Phone Mount` before scaling ad spend.
- Monitor `Car Seat Gap Organizer` and review supplier lead time before the next weekly review.

## Product Research Review

Command:

```bash
dtcops score examples/product_research_sample.csv
```

What to review:

- Product ideas with strong demand and margin scores.
- Product ideas with lower competition or clearer pain points.
- Whether a product is good enough for a small test, not a large inventory bet.

Sample result:

| Product | Weighted Score | Rating |
| --- | ---: | --- |
| Car Seat Gap Organizer | 7.20 | Good |
| Trunk Cargo Net | 6.95 | Good |
| Dashboard Phone Mount | 6.50 | Good |
| Luxury Seat Back Protector | 7.10 | Good |

Operator decision:

- Shortlist `Car Seat Gap Organizer` and `Luxury Seat Back Protector` for small test orders.
- Use the scorecard as a first-pass filter, then validate with marketplace reviews, margins, and supplier terms.
- Avoid committing to large inventory until ad ROI and inventory flow are tested.

