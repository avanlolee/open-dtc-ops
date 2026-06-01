import pandas as pd
import pytest

from dtcops.roi import calculate_roi
from dtcops.validators import CSVValidationError


def test_calculate_roi_summary():
    dataframe = pd.DataFrame(
        {
            "date": ["2026-05-01"],
            "product": ["Organizer"],
            "revenue": [100.0],
            "ad_spend": [20.0],
            "cogs": [30.0],
            "shipping": [10.0],
            "platform_fee": [5.0],
            "units_sold": [2],
        }
    )

    result = calculate_roi(dataframe)

    assert result["total_revenue"] == 100.0
    assert result["total_ad_spend"] == 20.0
    assert result["roas"] == 5.0
    assert result["acos"] == 0.2
    assert result["gross_profit"] == 70.0
    assert result["net_profit"] == 35.0
    assert result["net_margin"] == 0.35
    assert result["break_even_acos"] == 0.55
    assert result["status"] == "Profitable"


def test_calculate_roi_rejects_invalid_numeric_values():
    dataframe = pd.DataFrame(
        {
            "date": ["2026-05-01"],
            "product": ["Organizer"],
            "revenue": [""],
            "ad_spend": [20.0],
            "cogs": [30.0],
            "shipping": [10.0],
            "platform_fee": [5.0],
            "units_sold": [2],
        }
    )

    with pytest.raises(CSVValidationError, match="blank value.*revenue"):
        calculate_roi(dataframe)
