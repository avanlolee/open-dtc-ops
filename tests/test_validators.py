import pandas as pd
import pytest

from dtcops.validators import (
    CSVValidationError,
    validate_numeric_columns,
    validate_required_columns,
)


def test_validate_required_columns_passes_when_columns_exist():
    dataframe = pd.DataFrame({"product": ["A"], "revenue": [100]})

    validate_required_columns(dataframe, ["product", "revenue"])


def test_validate_required_columns_raises_helpful_error():
    dataframe = pd.DataFrame({"product": ["A"]})

    with pytest.raises(CSVValidationError, match="missing required column"):
        validate_required_columns(dataframe, ["product", "revenue"], "Sales CSV")


def test_validate_numeric_columns_rejects_blank_values():
    dataframe = pd.DataFrame({"revenue": [""]})

    with pytest.raises(CSVValidationError, match="blank value.*revenue"):
        validate_numeric_columns(dataframe, ["revenue"], "Sales CSV")


def test_validate_numeric_columns_rejects_non_numeric_values():
    dataframe = pd.DataFrame({"revenue": ["ten dollars"]})

    with pytest.raises(CSVValidationError, match="non-numeric value.*revenue"):
        validate_numeric_columns(dataframe, ["revenue"], "Sales CSV")


def test_validate_numeric_columns_rejects_negative_values_by_default():
    dataframe = pd.DataFrame({"revenue": [-1]})

    with pytest.raises(CSVValidationError, match="negative value.*revenue"):
        validate_numeric_columns(dataframe, ["revenue"], "Sales CSV")


def test_validate_numeric_columns_allows_negative_values_when_requested():
    dataframe = pd.DataFrame({"adjustment": [-1]})

    validate_numeric_columns(
        dataframe,
        ["adjustment"],
        "Adjustment CSV",
        allow_negative=True,
    )
