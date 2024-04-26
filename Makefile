# ==================================================================================== #
# HELPERS
# ==================================================================================== #

## help: print this help message
.PHONY: help
help:
	@echo 'Usage:'
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^/ /'

# ==================================================================================== #
# QUALITY CONTROL
# ==================================================================================== #

## format: format the code
.PHONY: format
format:
	black .

# ==================================================================================== #
# DEVELOPMENT
# ==================================================================================== #

## test: run all tests
.PHONY: test
test:
	pytest .

## test/re: run tests locally with a fresh database
.PHONY: test/re
test/re:
	dropdb merchant_test -f && \
	createdb merchant_test && \
	make migrations/up && \
	pytest -s -x --pdb --cov=app.api.v1.repositories.ekyb --cov-report=html:coverage_re

## install: install dependencies
.PHONY: install
install:
	pip install poetry && \
	poetry install


## build: build the app with docker compose
.PHONY: build
build:
	docker-compose build

## run: run the app with docker compose
.PHONY: run
run: build
	docker-compose up

## run/local: run the app locally
.PHONY: run/local
run/local:
	uvicorn main:app --reload


# ==================================================================================== #
# SQL MIGRATIONS
# ==================================================================================== #


## migrations/new msg=$1: Create a new migration
.PHONY: migrations/new
migrations/new:
	alembic revision --autogenerate -m "$(msg)"

## migrations/migrate: Apply all migrations
.PHONY: migrations/migrate
migrations/up:
	alembic upgrade head

## migrations/down: Revert the last migration
.PHONY: migrations/down
migrations/down:
	alembic downgrade -1

## migrations/goto version=$1: Go to a specific migration
.PHONY: migrations/goto
migrations/goto:
	alembic upgrade $(version)

## migrations/version: Show the current migration
.PHONY: migrations/version
migrations/version:
	alembic current

## migrations/history: Show the migration history
.PHONY: migrations/history
migrations/history:
	alembic history
