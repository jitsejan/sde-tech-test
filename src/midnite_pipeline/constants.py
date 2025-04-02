from dagster_dbt import DbtProject

dbt_project_dir = "/opt/src/analytics"
dbt_profiles_dir = dbt_project_dir

dbt_manifest_path = f"{dbt_project_dir}/target/manifest.json"

DBT_PROJECT = DbtProject(
    project_dir=dbt_project_dir,
    profiles_dir=dbt_profiles_dir,
)