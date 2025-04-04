from pathlib import Path

from dagster import RunRequest, sensor


@sensor(job_name="insert_bets_job")
def new_file_sensor(context):
    data_path = Path("landed_files")
    for file in data_path.glob("*.csv"):
        return RunRequest(
            run_key=str(file),
            run_config={
                "ops": {"insert_csv_to_postgres": {"inputs": {"file_path": str(file)}}}
            },
        )
    return None
