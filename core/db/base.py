from sqlalchemy.orm import sessionmaker
from app.models.base import Base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from core.settings.base import settings


engine = create_async_engine(
    settings.get("DATABASE_URL"),
    echo=True,
    pool_size=20,
    max_overflow=0,
    pool_timeout=5,
    pool_recycle=3600,
)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
