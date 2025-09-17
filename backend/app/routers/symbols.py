from fastapi import APIRouter, Depends
from sqlalchemy import select, or_
from app.db import SessionLocal
from app.models import Symbol
from app.schemas import SymbolOut

router = APIRouter()


async def get_session():
    async with SessionLocal() as s:
        yield s


@router.get("", response_model=list[SymbolOut])
async def search_symbols(q: str = "", session=Depends(get_session)):
    stmt = (
        select(Symbol)
        .where(or_(Symbol.ticker.ilike(f"%{q}%"), Symbol.name.ilike(f"%{q}%")))
        .limit(50)
    )
    rows = (await session.execute(stmt)).scalars().all()
    return rows
