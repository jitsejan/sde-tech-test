#!/bin/bash
set -e

echo "Running dbt compile to ensure latest manifest is available."
cd /opt/src/analytics
dbt deps
dbt compile

echo "Launching Dagster UI."
cd /opt/src
exec dagster dev -h 0.0.0.0 -f midnite_pipeline/definitions.py