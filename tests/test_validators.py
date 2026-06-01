import pandas as pd
import pytest

from dtcops.validators import CSVValidationError, validate_required_columns


def test_validate_required_columns_passes_when_columns_exist():
    dataframe = pd.DataFrame({"product": ["A"], "revenue": [100]})

    validate_required_columns(dataframe, ["product", "revenue"])


def test_validate_required_columns_raises_helpful_error():
    dataframe = pd.DataFrame({"product": ["A"]})

    with pytest.raises(CSVValidationError, match="missing required column"):
        validate_required_columns(dataframe, ["product", "revenue"], "Sales CSV")

