from dagster import job

from midnite_pipeline.ops.insert_ops import insert_csv_to_postgres


@job
def insert_bets_job():
    insert_csv_to_postgres()
