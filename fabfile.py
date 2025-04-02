from fabric import task
import os
import subprocess


@task
def dagster_dev(c):
    """Start Dagster dev server met juiste omgeving"""
    project_root = os.getcwd()
    dagster_home = f"{project_root}/src/midnite_pipeline/.dagster"
    pythonpath = f"{project_root}/src"

    env = {
        "PYTHONPATH": pythonpath,
        "DAGSTER_HOME": dagster_home,
    }

    cmd = "dagster dev -f src/midnite_pipeline/midnite_pipeline/definitions.py"
    c.run(cmd, env=env, pty=True)


@task
def dbt_compile(c):
    """Run dbt compile inside core container"""
    subprocess.run(
        'podman exec senior-data-engineer-technical-test_core_1 bash -c "cd /opt/src/analytics && dbt deps && dbt compile"',
        shell=True,
        check=True,
    )