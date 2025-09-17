from sqlalchemy import String, Integer, Date, Float, ForeignKey, UniqueConstraint, Numeric, DateTime, text
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base


class Symbol(Base):
    __tablename__ = "symbols"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ticker: Mapped[str] = mapped_column(String(32), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(128))
    exchange: Mapped[str] = mapped_column(String(16), default="LSE")
    currency: Mapped[str] = mapped_column(String(8), default="GBP")


class DailyBar(Base):
    __tablename__ = "daily_bars"
    symbol_id: Mapped[int] = mapped_column(ForeignKey("symbols.id"), primary_key=True)
    date: Mapped[Date] = mapped_column(Date, primary_key=True)
    open: Mapped[float] = mapped_column(Float)
    high: Mapped[float] = mapped_column(Float)
    low: Mapped[float] = mapped_column(Float)
    close: Mapped[float] = mapped_column(Float)
    volume: Mapped[float] = mapped_column(Float)
    __table_args__ = (UniqueConstraint("symbol_id", "date", name="uq_symbol_date"),)


class FeaturesDaily(Base):
    __tablename__ = "features_daily"
    symbol: Mapped[str] = mapped_column(String, primary_key=True)
    ts: Mapped[Date] = mapped_column(Date, primary_key=True)
    ma20: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    ma50: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    ma200: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    ema12: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    ema26: Mapped[float | None] = mapped_column(Numeric, nullable=True)
    computed_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=text("now()")
    )
