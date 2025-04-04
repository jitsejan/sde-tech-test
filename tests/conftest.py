import pandas as pd
import pytest

from midnite_pipeline.ops.validation import EXPECTED_COLUMNS


@pytest.fixture
def valid_bets_df():
    df = pd.DataFrame(
        {
            "id": [1],
            "user_id": [10],
            "bet_outcome_id": [1],
            "game_id": [2],
            "wager": [20.0],
            "is_cash_wager": [True],
            "winnings": [30.0],
            "created_at": [pd.to_datetime("2025-04-01 12:00:00")],
            "settled_at": [pd.to_datetime("2025-04-02 14:00:00")],
        }
    )
    return df.astype(EXPECTED_COLUMNS)
