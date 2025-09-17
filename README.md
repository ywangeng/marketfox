# MarketFox 🦊 — Stock Screener & Smart Alert (MVP)

A modern SaaS platform for **stock screening, smart alerts, and analytics**.  
Built with **FastAPI**, **Postgres**, **Redis**, and **Next.js**.

## 🚀 Features (MVP)
- Symbol search (FTSE sample tickers included)
- Historical OHLCV price API
- Basic technical indicators (RSI, moving averages)
- Demo data seeding (no external APIs needed to start)
- Healthcheck + tests

## 📂 Repository Structure
```bash 
marketfox/
├─ backend/ # FastAPI + Postgres + Redis + Alembic + tests
│ └─ README.md # Backend-specific docs
├─ frontend/ # Next.js frontend (placeholder for now)
│ └─ README.md
├─ docker-compose.yml# Local dev: Postgres + Redis
├─ Makefile # Dev shortcuts
├─ .editorconfig # Editor consistency
├─ .gitignore
├─ LICENSE
└─ README.md # This file
```

## 🛠 Tech Stack
**Backend**
- FastAPI (Python 3.11)
- SQLAlchemy 2.0 (async ORM)
- Alembic (migrations)
- Postgres (database)
- Redis (cache, task queue)
- pytest (testing)

**Frontend (planned)**
- Next.js (React)
- TailwindCSS
- shadcn/ui components

**Infrastructure**
- Docker Compose (local dev)
- Makefile (commands)
- `.env` for config

---

## 🔧 Prerequisites
- Python 3.11+
- Node.js 20+ (for frontend later)
- Docker + Docker Compose
- Git

---

## 🚀 Quick Start (Backend Only)
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

## 📌 Roadmap
- Add /screener endpoint (basic strategies: RSI oversold, MA crossovers)
- Add Redis caching
- Add Celery workers for alerts
- Build Next.js frontend
- Deploy to cloud (GCP/AWS/Azure)

## 📜 License
MIT License © 2025 MarketFox
