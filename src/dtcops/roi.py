from __future__ import annotations

import pandas as pd

from dtcops.validators import validate_numeric_columns, validate_required_columns

SALES_COLUMNS = [
    "date",
    "product",
    "revenue",
    "ad_spend",
    "cogs",
    "shipping",
    "platform_fee",
    "units_sold",
]


def calculate_roi(dataframe: pd.DataFrame) -> dict[str, float | str]:
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

    total_revenue = float(dataframe["revenue"].sum())
    total_ad_spend = float(dataframe["ad_spend"].sum())
    total_cogs = float(dataframe["cogs"].sum())
    total_shipping = float(dataframe["shipping"].sum())
    total_platform_fee = float(dataframe["platform_fee"].sum())

    gross_profit = total_revenue - total_cogs
    net_profit = gross_profit - total_shipping - total_platform_fee - total_ad_spend
    roas = total_revenue / total_ad_spend if total_ad_spend else 0.0
    acos = total_ad_spend / total_revenue if total_revenue else 0.0
    net_margin = net_profit / total_revenue if total_revenue else 0.0
    break_even_acos = (
        (gross_profit - total_shipping - total_platform_fee) / total_revenue
        if total_revenue
        else 0.0
    )
    status = "Profitable" if net_profit >= 0 else "Unprofitable"

    return {
        "total_revenue": total_revenue,
        "total_ad_spend": total_ad_spend,
        "roas": roas,
        "acos": acos,
        "gross_profit": gross_profit,
        "net_profit": net_profit,
        "net_margin": net_margin,
        "break_even_acos": break_even_acos,
        "status": status,
    }
