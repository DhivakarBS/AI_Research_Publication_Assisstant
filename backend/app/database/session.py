from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config.settings import get_settings
from app.database.base import Base

settings = get_settings()

engine = create_engine(settings.database_url, future=True)
async_engine = create_async_engine(
    settings.database_url.replace("postgresql+psycopg", "postgresql+asyncpg"),
    future=True,
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)
