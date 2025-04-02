# Submission Notes

Feel free to add anything you would like to this document to help explain your submission. Things like presumptions that you made, other features and best practices that you would implement in a production grade system etc. Some suggested headings are below.


- Moved from Docker to Podman. Podman is **much** lighter and doesn't slow down my laptop as much. To make this work I had to run

```bash
$ brew install podman podman-compose
```

and update the `Makefile` and replace `docker-*` commands with `podman-*`. 


## Presumptions Made

Any presumptions made about the business, data, use case etc

- I would like to avoid using Docker / containers in development to make developing code quicker and would replace the need for Postgres with DuckDB. It works well in a development environment, stores its data locally like SQLite and integrates great with dbt.
- 

## Additional Production Grade Considerations

Any best practices or anything else that you would consider if this were a production grade solution

