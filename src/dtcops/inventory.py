from __future__ import annotations

import pandas as pd

from dtcops.validators import validate_required_columns

INVENTORY_COLUMNS = [
    "product",
    "current_inventory",
    "avg_daily_sales",
    "lead_time_days",
    "safety_stock",
]


def calculate_inventory(dataframe: pd.DataFrame) -> list[dict[str, float | str]]:
    validate_required_columns(dataframe, INVENTORY_COLUMNS, "Inventory CSV")

    results: list[dict[str, float | str]] = []
    for _, row in dataframe.iterrows():
        current_inventory = float(row["current_inventory"])
        avg_daily_sales = float(row["avg_daily_sales"])
        lead_time_days = float(row["lead_time_days"])
        safety_stock = float(row["safety_stock"])

        days_left = (
            current_inventory / avg_daily_sales if avg_daily_sales > 0 else float("inf")
        )
        reorder_point = lead_time_days * avg_daily_sales + safety_stock

        if current_inventory <= reorder_point:
            status = "Reorder Now"
        elif days_left <= 30:
            status = "Watch"
        else:
            status = "Healthy"

        results.append(
            {
                "product": str(row["product"]),
                "days_left": days_left,
                "reorder_point": reorder_point,
                "status": status,
            }
        )

    return results
