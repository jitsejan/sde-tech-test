# Submission notes

Feel free to add anything you would like to this document to help explain your submission. Things like presumptions that you made, other features and best practices that you would implement in a production grade system etc. Some suggested headings are below.

- Moved from Docker to Podman. Podman is **much** lighter and doesn't slow down my laptop as much. To make this work I had to run:

```bash
brew install podman podman-compose
```

and update the `Makefile` and replace `docker-*` commands with `podman-*`. 

## Presumptions made

- Better Betting only operates in Ireland and the UK. Any users from other countries are filtered out in `core_users`.
- Only `EUR` and `GBP` currencies are supported — we rely on `fx_rates` to convert to USD using daily exchange rates.
- The volume of raw files is not large, so for now, we're triggering the ingestion + dbt transformation with each file manually.
- Some fields in the raw data (like `winnings`, `settled_at`) can be null — this is expected and handled in tests.
- File watching is limited to the `bets.csv` file for now, but we acknowledge we could extend the system to handle other input types.

## Additional production grade considerations

### Logging & monitoring

- Structured logs from Dagster, dbt, and Python ingestion could be routed to a central log aggregator like ELK, Datadog, or OpenTelemetry.
- Basic Dagster logging is in place now (e.g., rows ingested, validation failures), but we would expand this with standard logging middleware.

### Testing & quality

- A unit test is in place for validation logic with `pytest` and `pytest.mark.parametrize`.
- `dbt` tests ensure the integrity of source and transformed data (e.g., not null, unique, accepted values).
- A `pre-commit` config runs `black`, `ruff`, `isort`, and `mypy`. We excluded running tests here to speed up local development.
- Tests are exposed via the `fabfile.py` for consistency and automation.

### Modular architecture

- The pipeline is structured in stages: `raw` → `core` → `reporting`, following dbt’s medallion architecture principles.
- Additional data sources could be integrated by building modular DAGs and `@asset` or `@job` definitions in Dagster.

### CI/CD

- In a full setup, we’d include:
  - CI: Run `pytest` and `dbt test` on every PR using GitHub Actions or Azure Pipelines. Much like the pre-commit setup.
  - CD: Deploy jobs and dbt models to staging/prod environments with controlled approvals.

### Scheduling & orchestration

- In the future `@job` runs ingestion followed by a dbt transformation. Currently the ingest and transform step are decoupled.
- File sensors can be expanded to dispatch different jobs depending on the filename or path. I.e. we could have a 'user' input job for a new users.csv that loads new users to the database.

### Error handling & alerting

- Validation failures currently raise exceptions and are logged.
- In production, we’d integrate Dagster failure hooks or external alerting (Slack, PagerDuty, etc.) for failed runs.

### Scalability

- For larger volumes or multiple file types, we’d:
  - Enable file pattern filtering in the sensor
  - Use selectors in dbt (e.g., only rebuild relevant models)
  - Enable partial parsing and state-based builds in dbt

### Data quality

- The tests include basic dbt checks (`unique`, `not_null`, `accepted_values`, etc.).
- For richer checks, we have introduced `dbt-expectations`.

## Notes on choices

- We run `dbt build` via the dagster-dbt package from Dagster. While this is pragmatic, it could be replaced with `dbt-core` API usage for tighter integration.
- We chose to trigger `dbt` manually after a file is ingested. Another valid approach would be to decouple this and run `dbt` on a schedule or sensor.
- Similarly, we opted for Dagster `@op` jobs instead of `@asset`s to stay close to the idea of modeling discrete steps.

## Future enhancements

- Add `dbt build --select` logic to run only impacted models.
- Store file metadata (e.g., filename, timestamp) in a manifest table for traceability.
- Replace `if_exists='replace'` with an upsert logic or deduplication strategy.
- Extend the reporting layer to include retention metrics, conversion funnel analysis, etc.