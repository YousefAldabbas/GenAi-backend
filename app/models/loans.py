from sqlalchemy import Boolean, Column, Integer, String, JSON, Text
from .base import BaseSQLModel


class LoanProviders(BaseSQLModel):
    __tablename__ = "loan_providers"

    name = Column(String, index=True)
    is_bank = Column(Boolean)
    phone_number = Column(String)
    email = Column(String)
    address = Column(String)
    description = Column(Text)


class Loans(BaseSQLModel):
    __tablename__ = "loans"

    intrest_rate = Column(Integer)
    loan_amount = Column(Integer)
    loan_provider_id = Column(Integer)
    description = Column(Text)
    sharia_compliant = Column(Boolean)
