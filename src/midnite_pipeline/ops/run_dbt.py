from dagster import op
from dagster_dbt import DbtCliResource

@op(required_resource_keys={"dbt"})
def run_dbt_build(context):
    context.log.info("Running dbt build...")
    result = context.resources.dbt.cli(["build"], context=context)
    for log in result.stream():
        context.log.info(log)