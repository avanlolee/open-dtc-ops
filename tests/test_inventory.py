import pandas as pd
import pytest

from dtcops.inventory import calculate_inventory
from dtcops.validators import CSVValidationError


def test_calculate_inventory_statuses():
    dataframe = pd.DataFrame(
        {
            "product": ["Healthy Item", "Watch Item", "Reorder Item"],
            "current_inventory": [200, 80, 20],
            "avg_daily_sales": [4, 4, 4],
            "lead_time_days": [10, 10, 10],
            "safety_stock": [10, 10, 10],
        }
    )

    result = calculate_inventory(dataframe)

    assert result[0]["days_left"] == 50
    assert result[0]["reorder_point"] == 50
    assert result[0]["status"] == "Healthy"
    assert result[1]["status"] == "Watch"
    assert result[2]["status"] == "Reorder Now"


def test_calculate_inventory_rejects_negative_values():
    dataframe = pd.DataFrame(
        {
            "product": ["Reorder Item"],
            "current_inventory": [-1],
            "avg_daily_sales": [4],
            "lead_time_days": [10],
            "safety_stock": [10],
        }
    )

    with pytest.raises(CSVValidationError, match="negative value.*current_inventory"):
        calculate_inventory(dataframe)
