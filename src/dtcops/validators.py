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


def validate_numeric_columns(
    dataframe: pd.DataFrame,
    numeric_columns: list[str],
    dataset_name: str = "CSV",
    *,
    allow_negative: bool = False,
) -> None:
    for column in numeric_columns:
        if column not in dataframe.columns:
            continue

        for row_number, value in enumerate(dataframe[column].tolist(), start=2):
            if pd.isna(value) or (isinstance(value, str) and not value.strip()):
                raise CSVValidationError(
                    f"{dataset_name} has a blank value in numeric column "
                    f"'{column}' at row {row_number}. Fill it with 0 or a "
                    "valid number before running calculations."
                )

            try:
                numeric_value = float(value)
            except (TypeError, ValueError):
                raise CSVValidationError(
                    f"{dataset_name} has a non-numeric value in column "
                    f"'{column}' at row {row_number}: {value!r}. Use a plain "
                    "number without currency symbols or text."
                )

            if not allow_negative and numeric_value < 0:
                raise CSVValidationError(
                    f"{dataset_name} has a negative value in column '{column}' "
                    f"at row {row_number}: {value!r}. Replace it with 0 or a "
                    "positive number."
                )
