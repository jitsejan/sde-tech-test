from fabric import task
import os

PROJECT_ROOT = os.path.dirname(__file__)
SRC_PATH = os.path.join(PROJECT_ROOT, "src")


@task
def clean(c):
    """Remove pyc and Dagster state files."""
    print("🧹 Cleaning __pycache__ and Dagster state...")
    c.run(f"find {SRC_PATH} -type d -name '__pycache__' -exec rm -rf {{}} +", warn=True)
    c.run(f"find {SRC_PATH} -type f -name '*.pyc' -delete", warn=True)
    c.run(f"rm -rf {SRC_PATH}/midnite_pipeline/.dagster", warn=True)


@task
def kill(c):
    """Stop all containers and remove volumes."""
    print("🛑 Stopping containers...")
    c.run("podman-compose down -v", warn=True)


@task
def up(c):
    """Start Dagster via podman-compose."""
    print("🚀 Starting Dagster...")
    c.run("podman-compose up --build")


@task
def restart(c):
    """Kill, clean, and bring up fresh containers."""
    kill(c)
    clean(c)
    up(c)