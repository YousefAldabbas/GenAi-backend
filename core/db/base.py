from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.base import Base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

# an Engine, which the Session will use for connection
# resources
engine = create_async_engine(
    "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/hack"
)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
