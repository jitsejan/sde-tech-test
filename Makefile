.PHONY: build up down shell reset-db set-permissions shell postgres-shell

# HOME := /opt/src/

reset-db: down set-permissions
	rm -rfv db-data

build: reset-db
	podman-compose down
	podman-compose build --no-cache

set-permissions:
	mkdir -p db-data
	chmod -R 777 db-data

up: set-permissions
	podman-compose up -d

down:
	podman-compose down

shell:
	podman-compose exec core bash -c "cd /opt/src; exec bash"

postgres-shell:
	podman-compose exec postgres bash