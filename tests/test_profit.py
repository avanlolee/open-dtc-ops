import pandas as pd

from dtcops.profit import calculate_profit


def test_calculate_profit_summary():
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

    result = calculate_profit(dataframe)

    assert result["revenue"] == 100.0
    assert result["cogs"] == 30.0
    assert result["shipping"] == 10.0
    assert result["platform_fees"] == 5.0
    assert result["ad_spend"] == 20.0
    assert result["gross_profit"] == 70.0
    assert result["contribution_profit"] == 55.0
    assert result["net_profit"] == 35.0
    assert result["net_margin"] == 0.35

