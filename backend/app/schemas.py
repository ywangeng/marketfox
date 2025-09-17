from typing import List, Dict, Optional
from pydantic import BaseModel
from datetime import date


class SymbolOut(BaseModel):
    id: int
    ticker: str
    name: str

    class Config:
        from_attributes = True


class PricePoint(BaseModel):
    date: str
    o: float
    h: float
    l: float
    c: float
    v: float


class OHLCV(BaseModel):
    ts: date
    open: float
    high: float
    low: float
    close: float
    volume: Optional[float] = None
