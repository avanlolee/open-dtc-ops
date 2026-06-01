from __future__ import annotations

import pandas as pd

from dtcops.roi import SALES_COLUMNS
from dtcops.validators import validate_numeric_columns, validate_required_columns


def calculate_profit(dataframe: pd.DataFrame) -> dict[str, float]:
    validate_required_columns(dataframe, SALES_COLUMNS, "Sales CSV")
    validate_numeric_columns(
        dataframe,
        [
            "revenue",
            "ad_spend",
            "cogs",
            "shipping",
            "platform_fee",
            "units_sold",
        ],
        "Sales CSV",
    )

    revenue = float(dataframe["revenue"].sum())
    cogs = float(dataframe["cogs"].sum())
    shipping = float(dataframe["shipping"].sum())
    platform_fees = float(dataframe["platform_fee"].sum())
    ad_spend = float(dataframe["ad_spend"].sum())

    gross_profit = revenue - cogs
    contribution_profit = gross_profit - shipping - platform_fees
    net_profit = contribution_profit - ad_spend
    net_margin = net_profit / revenue if revenue else 0.0

    return {
        "revenue": revenue,
        "cogs": cogs,
        "shipping": shipping,
        "platform_fees": platform_fees,
        "ad_spend": ad_spend,
        "gross_profit": gross_profit,
        "contribution_profit": contribution_profit,
        "net_profit": net_profit,
        "net_margin": net_margin,
    }
