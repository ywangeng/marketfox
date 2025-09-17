from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from app.config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    pool_size=10, max_overflow=20, pool_pre_ping=True, pool_recycle=1800
)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)
Base = declarative_base()
