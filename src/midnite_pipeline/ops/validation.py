import pandas as pd

EXPECTED_COLUMNS = {
    "bet_id": "int64",
    "user_id": "int64",
    "stake": "float64",
    "profit_and_loss": "float64",
    "game_id": "int64",
    "currency": "object",
    "bet_timestamp": "datetime64[ns]"
}

def validate_bets_dataframe(df: pd.DataFrame, context) -> pd.DataFrame:
    actual_columns = set(df.columns)
    expected_columns = set(EXPECTED_COLUMNS.keys())

    if actual_columns != expected_columns:
        raise ValueError(f"Column mismatch:\n Expected: {expected_columns}\n Actual: {actual_columns}")

    try:
        df = df.astype(EXPECTED_COLUMNS)
    except Exception as e:
        raise ValueError(f"Type conversion failed: {e}")

    return df