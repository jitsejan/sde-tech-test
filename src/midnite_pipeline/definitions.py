import os

from dagster import Definitions
from dagster_dbt import DbtCliResource
from dotenv import load_dotenv

from midnite_pipeline.assets import dynamic_dbt_assets
from midnite_pipeline.jobs.insert_jobs import insert_bets_job
from midnite_pipeline.resources import PostgresResource
from midnite_pipeline.sensors.file_sensor import new_file_sensor
from midnite_pipeline.constants import dbt_manifest_path, dbt_project_dir

load_dotenv()

defs = Definitions(
    assets=[dynamic_dbt_assets],
    jobs=[insert_bets_job],
    sensors=[new_file_sensor],
    resources={
        "db": PostgresResource(
            user=os.getenv("POSTGRESUSER"),
            password=os.getenv("POSTGRESPASS"),
            host=os.getenv("POSTGRESHOST"),
            port=int(os.getenv("POSTGRESPORT", "5432")),
            database=os.getenv("POSTGRESDB"),
        ),
        "dbt": DbtCliResource(
            project_dir=dbt_project_dir,
            manifest=dbt_manifest_path,
        ),
    },
)