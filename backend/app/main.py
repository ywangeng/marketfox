from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import health, symbols, prices, analysis

app = FastAPI(title="MarketFox API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173","http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router,  prefix="/health",  tags=["health"])
app.include_router(symbols.router, prefix="/symbols", tags=["symbols"])
app.include_router(prices.router,  prefix="/prices",  tags=["prices"])
app.include_router(analysis.router)  # 👈 no extra prefix here
