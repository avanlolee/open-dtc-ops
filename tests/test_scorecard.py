import pandas as pd

from dtcops.scorecard import calculate_scorecard


def test_calculate_scorecard_ratings():
    dataframe = pd.DataFrame(
        {
            "product": ["Strong Item", "Good Item", "Weak Item"],
            "demand_score": [9, 7, 4],
            "margin_score": [8, 7, 5],
            "competition_score": [8, 6, 5],
            "pain_point_score": [9, 6, 5],
            "differentiation_score": [8, 6, 5],
        }
    )

    result = calculate_scorecard(dataframe)

    assert result[0]["weighted_score"] == 8.4
    assert result[0]["rating"] == "Strong"
    assert result[1]["weighted_score"] == 6.5
    assert result[1]["rating"] == "Good"
    assert result[2]["weighted_score"] == 4.75
    assert result[2]["rating"] == "Weak"
