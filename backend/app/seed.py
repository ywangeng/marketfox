import os, csv, random, asyncio
from datetime import date, timedelta
from sqlalchemy import select
from app.db import SessionLocal
from app.models import Symbol, DailyBar


async def seed_symbols(session):
    path = os.path.join(os.path.dirname(__file__), "seed_ftse.csv")
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            exists = (await session.execute(select(Symbol).where(Symbol.ticker == row["ticker"]))).scalar_one_or_none()
            if not exists:
                session.add(Symbol(ticker=row["ticker"], name=row["name"], exchange="LSE", currency="GBP"))
    await session.commit()


async def seed_prices(session, days: int = 90):
    symbols = (await session.execute(select(Symbol))).scalars().all()
    start = date.today() - timedelta(days=days)
    for s in symbols:
        price = random.uniform(80, 400)
        for i in range(days):
            d = start + timedelta(days=i)
            if d.weekday() >= 5:
                continue
            delta = random.uniform(-2.0, 2.0)
            o = price
            c = max(1.0, price + delta)
            h = max(o, c) + random.uniform(0, 1.5)
            l = min(o, c) - random.uniform(0, 1.5)
            v = random.uniform(1e6, 10e6)
            session.add(DailyBar(symbol_id=s.id, date=d, open=o, high=h, low=l, close=c, volume=v))
            price = c
    await session.commit()


async def main():
    async with SessionLocal() as session:
        await seed_symbols(session)
        await seed_prices(session)
    print("Seed complete.")


if __name__ == "__main__":
    asyncio.run(main())
