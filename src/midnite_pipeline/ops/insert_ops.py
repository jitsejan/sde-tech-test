from dagster import op
import pandas as pd
from midnite_pipeline.resources import PostgresResource
from midnite_pipeline.ops.validation import validate_bets_dataframe

@op(required_resource_keys={"db"})
def insert_csv_to_postgres(context, file_path: str):
    df = pd.read_csv(file_path)
    context.log.info(f"Received file: {file_path}")

    try:
        df = validate_bets_dataframe(df, context)
    except Exception as e:
        context.log.error(f"Validation error: {e}")
        raise

    engine = context.resources.db.get_engine()

    try:
        df.to_sql("bet",
                  con=engine,
                  schema="raw",
                  if_exists="replace",
                  index=False)
        context.log.info(f"{len(df)} rows added to raw.bet")
    except Exception as e:
        context.log.error(f"Insert failed: {e}")
        raise