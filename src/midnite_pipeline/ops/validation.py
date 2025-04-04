import pandas as pd

EXPECTED_COLUMNS = {
    "id": "int64",
    "user_id": "int64",
    "bet_outcome_id": "float64",  # can be NaN
    "game_id": "int64",
    "wager": "float64",
    "is_cash_wager": "bool",
    "winnings": "float64",  # can be NaN
    "created_at": "datetime64[ns]",
    "settled_at": "datetime64[ns]",  # can be NaT
}


def validate_bets_dataframe(df: pd.DataFrame, context) -> pd.DataFrame:
    actual_columns = set(df.columns)
    expected_columns = set(EXPECTED_COLUMNS.keys())

    if actual_columns != expected_columns:
        raise ValueError(
            f"Column mismatch:\n Expected: {expected_columns}\n Actual: {actual_columns}"
        )

    try:
        # Parse datetimes (allow NaT for settled_at)
        df["created_at"] = pd.to_datetime(df["created_at"], errors="raise")
        df["settled_at"] = pd.to_datetime(df["settled_at"], errors="coerce")

        # Cast remaining columns
        df = df.astype(
            {
                "id": "int64",
                "user_id": "int64",
                "bet_outcome_id": "float64",  # float64 handles NaN
                "game_id": "int64",
                "wager": "float64",
                "is_cash_wager": "bool",
                "winnings": "float64",
            }
        )

    except Exception as e:
        raise ValueError(f"Type conversion failed: {e}")

    return df
