import pandas as pd
import pytest

from midnite_pipeline.ops.validation import validate_bets_dataframe


def test_validate_valid_bets(valid_bets_df):
    validated_df = validate_bets_dataframe(valid_bets_df, context=None)
    assert isinstance(validated_df, pd.DataFrame)
    assert validated_df.equals(valid_bets_df)


@pytest.mark.parametrize(
    "modified_df,error_substring",
    [
        (pd.DataFrame({"user_id": [1]}), "Column mismatch"),
        (
            pd.DataFrame(
                {
                    "id": ["one"],  # string instead of int
                    "user_id": [1],
                    "bet_outcome_id": [1],
                    "game_id": [2],
                    "wager": [100.0],
                    "is_cash_wager": [True],
                    "winnings": [150.0],
                    "created_at": ["2020-01-01"],
                    "settled_at": ["2020-01-02"],
                }
            ),
            "Type conversion failed",
        ),
    ],
)
def test_validate_bets_failures(modified_df, error_substring):
    with pytest.raises(ValueError, match=error_substring):
        validate_bets_dataframe(modified_df, context=None)
