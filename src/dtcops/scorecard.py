from __future__ import annotations

import pandas as pd

from dtcops.validators import validate_numeric_columns, validate_required_columns

PRODUCT_RESEARCH_COLUMNS = [
    "product",
    "demand_score",
    "margin_score",
    "competition_score",
    "pain_point_score",
    "differentiation_score",
]

SCORE_WEIGHTS = {
    "demand_score": 0.25,
    "margin_score": 0.25,
    "competition_score": 0.20,
    "pain_point_score": 0.15,
    "differentiation_score": 0.15,
}


def calculate_scorecard(dataframe: pd.DataFrame) -> list[dict[str, float | str]]:
    validate_required_columns(
        dataframe, PRODUCT_RESEARCH_COLUMNS, "Product research CSV"
    )
    validate_numeric_columns(
        dataframe,
        list(SCORE_WEIGHTS),
        "Product research CSV",
    )

    results: list[dict[str, float | str]] = []
    for _, row in dataframe.iterrows():
        weighted_score = round(
            sum(
                float(row[column]) * weight
                for column, weight in SCORE_WEIGHTS.items()
            ),
            2,
        )

        if weighted_score >= 8:
            rating = "Strong"
        elif weighted_score >= 6:
            rating = "Good"
        else:
            rating = "Weak"

        results.append(
            {
                "product": str(row["product"]),
                "weighted_score": weighted_score,
                "rating": rating,
            }
        )

    return results
