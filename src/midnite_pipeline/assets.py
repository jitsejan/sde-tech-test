from dagster import AssetExecutionContext
from dagster_dbt import dbt_assets

from midnite_pipeline.constants import dbt_manifest_path


@dbt_assets(
    manifest=dbt_manifest_path,
    required_resource_keys={"dbt"},
)
def dynamic_dbt_assets(context: AssetExecutionContext):
    dbt_command = ["build"]
    context.log.debug(f"{dbt_command=}")

    dbt_resource = context.resources.dbt
    yield from dbt_resource.cli(dbt_command, context=context).stream()
