from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from app.db import SessionLocal
from app.models import Symbol, DailyBar
from collections import deque

router = APIRouter(prefix="/analysis", tags=["analysis"])


async def get_session():
    async with SessionLocal() as s:
        yield s


def simple_sma(values: list[float], window: int) -> list[float]:
    q, total, out = deque(maxlen=window), 0.0, []
    for v in values:
        if len(q) == q.maxlen: total -= q[0]
        q.append(v)
        total += v
        if len(q) == window: out.append(total / window)
    return out


@router.get("/{ticker}")
async def moving_average_analysis(ticker: str, window: int = Query(20, ge=2, le=365), session=Depends(get_session)):
    sym = (await session.execute(select(Symbol).where(Symbol.ticker == ticker))).scalar_one_or_none()
    if not sym:
        raise HTTPException(404, "Symbol not found")
    closes = (await session.execute(
        select(DailyBar.close).where(DailyBar.symbol_id == sym.id).order_by(DailyBar.date.asc())
    )).scalars().all()
    return {"ticker": ticker, "window": window, "ma": simple_sma(closes, window) if closes else []}
