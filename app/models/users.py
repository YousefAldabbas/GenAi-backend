from sqlalchemy import Column, String

from .base import BaseSQLModel


class User(BaseSQLModel):
    __tablename__ = "users"
    full_name = Column(String, index=True)
    date_of_birth = Column(String)
    phone_number = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
