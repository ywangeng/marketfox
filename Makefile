# ========= MarketFox Monorepo Makefile =========
# Usage examples:
#   make up            # start Postgres + Redis
#   make migrate       # apply DB migrations
#   make seed          # seed demo data
#   make api           # run FastAPI dev server
#   make web           # run Next.js dev server
#   make test          # run backend tests
#   make fmt lint type # format, lint, type-check backend
#   make down          # stop & remove containers/volumes
#   make help          # list targets

# -------- Variables (override with env or CLI: make api PORT=9000) --------
PORT        ?= 8000
WEB_PORT    ?= 3000
DB_HOST     ?= localhost
DB_PORT     ?= 5432
DB_NAME     ?= marketfox
DB_USER     ?= postgres
DB_PASS     ?= postgres

ASYNC_DB    ?= postgresql+asyncpg://$(DB_USER):$(DB_PASS)@$(DB_HOST):$(DB_PORT)/$(DB_NAME)
SYNC_DB     ?= postgresql+psycopg://$(DB_USER):$(DB_PASS)@$(DB_HOST):$(DB_PORT)/$(DB_NAME)

BACKEND_DIR := backend
FRONTEND_DIR:= frontend

# -------- Meta --------
.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo ""
	@echo "MarketFox Makefile targets:"
	@echo "  up           - Start Postgres + Redis (docker compose)"
	@echo "  down         - Stop and remove containers + volumes"
	@echo "  logs         - Follow docker compose logs"
	@echo "  api          - Run FastAPI dev server (uvicorn)"
	@echo "  worker       - (placeholder) Run Celery worker"
	@echo "  migrate      - Run Alembic migrations"
	@echo "  revision     - Create Alembic autogeneration revision"
	@echo "  seed         - Seed DB with demo FTSE data"
	@echo "  test         - Run backend tests (pytest)"
	@echo "  fmt          - Format backend (black + isort)"
	@echo "  lint         - Lint backend (ruff)"
	@echo "  type         - Type-check backend (mypy)"
	@echo "  web          - Run Next.js dev server"
	@echo "  web-build    - Build Next.js"
	@echo "  web-start    - Start Next.js production server"
	@echo "  env          - Print resolved DB URLs and ports"
	@echo ""

# -------- Docker services --------
.PHONY: up down logs
up:
	docker compose up -d

down:
	docker compose down -v

logs:
	docker compose logs -f

# -------- Backend: API / DB / Migrations / Seed --------
.PHONY: api worker migrate revision seed test fmt lint type

api:
	cd $(BACKEND_DIR) && DATABASE_URL=$(ASYNC_DB) uvicorn app.main:app --reload --port $(PORT)

# Placeholder for when Celery is added
worker:
	cd $(BACKEND_DIR) && REDIS_URL=redis://localhost:6379/0 celery -A worker.celery_app.celery worker -l INFO -c 4

migrate:
	cd $(BACKEND_DIR) && SYNC_DATABASE_URL=$(SYNC_DB) alembic upgrade head

revision:
	cd $(BACKEND_DIR) && SYNC_DATABASE_URL=$(SYNC_DB) alembic revision --autogenerate -m "update"

seed:
	cd $(BACKEND_DIR) && DATABASE_URL=$(ASYNC_DB) python3 app/seed.py

test:
	cd $(BACKEND_DIR) && pytest -q

# Code quality (install tools in backend venv: black isort ruff mypy)
fmt:
	cd $(BACKEND_DIR) && black app tests && isort app tests

lint:
	cd $(BACKEND_DIR) && ruff check app tests

type:
	cd $(BACKEND_DIR) && mypy app

# -------- Frontend: Next.js --------
.PHONY: web web-build web-start

web:
	cd $(FRONTEND_DIR) && npm run dev -- --port $(WEB_PORT)

web-build:
	cd $(FRONTEND_DIR) && npm run build

web-start:
	cd $(FRONTEND_DIR) && npm run start -p $(WEB_PORT)

# -------- Utilities --------
.PHONY: env
env:
	@echo "API PORT:        $(PORT)"
	@echo "WEB PORT:        $(WEB_PORT)"
	@echo "DB:              $(DB_USER)@$(DB_HOST):$(DB_PORT)/$(DB_NAME)"
	@echo "ASYNC_DATABASE:  $(ASYNC_DB)"
	@echo "SYNC_DATABASE:   $(SYNC_DB)"
