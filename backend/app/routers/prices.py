from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from app.db import SessionLocal
from app.models import Symbol, DailyBar
from app.schemas import PricePoint

router = APIRouter()


async def get_session():
    async with SessionLocal() as s:
        yield s


@router.get("/{ticker}")
async def get_prices(ticker: str, session=Depends(get_session)) -> dict:
    sym = (await session.execute(select(Symbol).where(Symbol.ticker == ticker))).scalar_one_or_none()
    if not sym:
        raise HTTPException(404, "Symbol not found")

    bars = (
        await session.execute(
            select(DailyBar).where(DailyBar.symbol_id == sym.id).order_by(DailyBar.date.asc())
        )
    ).scalars().all()

    data: list[PricePoint] = [
        PricePoint(
            date=b.date.isoformat(),
            o=b.open, h=b.high, l=b.low, c=b.close, v=b.volume
        ) for b in bars
    ]
    return {"ticker": ticker, "data": [d.model_dump() for d in data]}
