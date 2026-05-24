from src.eda_utils import missing_values
import pandas as pd


def test_missing_values():
    df = pd.DataFrame({
        "A": [1, None, 3],
        "B": [None, 2, 3]
    })

    result = missing_values(df)

    assert result is not None