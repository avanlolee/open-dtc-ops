from __future__ import annotations

from pathlib import Path

import pandas as pd


class CSVValidationError(ValueError):
    """Raised when a CSV file is missing required columns."""


def read_csv(path: str | Path) -> pd.DataFrame:
    csv_path = Path(path)
    if not csv_path.exists():
        raise CSVValidationError(f"CSV file not found: {csv_path}")
    if not csv_path.is_file():
        raise CSVValidationError(f"Path is not a file: {csv_path}")
    try:
        return pd.read_csv(csv_path)
    except Exception as exc:
        raise CSVValidationError(f"Could not read CSV file: {csv_path}") from exc


def validate_required_columns(
    dataframe: pd.DataFrame,
    required_columns: list[str],
    dataset_name: str = "CSV",
) -> None:
    missing_columns = [
        column for column in required_columns if column not in dataframe.columns
    ]
    if missing_columns:
        missing = ", ".join(missing_columns)
        expected = ", ".join(required_columns)
        raise CSVValidationError(
            f"{dataset_name} is missing required column(s): {missing}. "
            f"Expected columns: {expected}"
        )
