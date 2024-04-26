from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# an Engine, which the Session will use for connection
# resources
engine = create_engine("postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/hack")

SessionLocal = sessionmaker(engine)


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
