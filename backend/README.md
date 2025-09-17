# MarketFox Backend 🦊

FastAPI + SQLAlchemy + Alembic + Postgres + Redis

This service powers the MarketFox stock screener and alerting system.

---

## 🚀 Quick Start

### 1. Start dependencies (Postgres + Redis)
From the repo root:
```bash
make up
```

### 2. Create a virtual environment 
```bash 
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

### 3. Configure environment variables 
Copy the example file:
```bash 
cp .env.example .env
```
Edit .env with your own values if needed (DB creds, secret key, etc.).

### 4. Run migrations
```bash 
make migrate
```

### 5. Seed demo data 
```bash 
make seed
```
This will insert a few FTSE tickers and generate fake OHLCV price history.

### 6. Run API 
```bash 
make api
```
Open Swagger docs: http://localhost:8000/docs. 

## 🧪 Tests
Run tests with:
```bash 
make test
```

## 📂 Project Structure
```bash 
backend/
├─ app/
│  ├─ main.py        # FastAPI entrypoint
│  ├─ config.py      # Settings / env vars
│  ├─ db.py          # DB engine + session
│  ├─ models.py      # SQLAlchemy models
│  ├─ schemas.py     # Pydantic schemas
│  ├─ indicators.py  # TA indicators
│  ├─ routers/       # API endpoints
│  ├─ seed.py        # Demo data seeding
│  └─ seed_ftse.csv  # Seed symbols
├─ migrations/       # Alembic migrations
├─ tests/            # Pytest tests
├─ pyproject.toml    # Python deps
└─ Dockerfile        # Container build
```

## 🔑 Key Endpoints
- /health → healthcheck
- /symbols?q=bar → search symbols
- /prices/{ticker} → fetch OHLCV data

## 🛠 Tooling
- FastAPI — API framework
- SQLAlchemy 2.0 (async) — ORM
- Alembic — migrations
- Postgres — database
- Redis — cache & task queue
- pytest — testing

## 📌 Next Steps
- Add screener endpoints
- Add Redis caching layer
- Add Celery workers for alerts


