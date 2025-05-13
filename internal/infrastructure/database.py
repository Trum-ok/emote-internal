from collections.abc import AsyncGenerator
from logging import getLogger

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from config import config
from config.loggers import DB
from internal.infrastructure.models import Base

logger = getLogger(DB)

engine = create_async_engine(config.db.url, echo=True)
async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def init_db() -> None:
    """Инициализация базы данных."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database connection established")


async def get_session() -> AsyncGenerator[AsyncSession]:
    """Предоставление сессии базы данных."""
    async with async_session() as session:
        yield session


async def stop_db() -> None:
    """Закрытие соединения с базой данных."""
    await engine.dispose()
    logger.info("Database connection closed")
