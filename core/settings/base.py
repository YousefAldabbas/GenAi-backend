from typing import Any
from dotenv import load_dotenv
from pydantic import (
    Field,
)

from pydantic_settings import BaseSettings

load_dotenv(".env")


class Settings(BaseSettings):

    DATABASE_URL: str = Field(alias="DATABASE_URL")


settings: dict[str, Any] = Settings().model_dump()
