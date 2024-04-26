from sqlalchemy import Boolean, Column, Integer, String

from .base import BaseSQLModel


class FinancialInfo(BaseSQLModel):
    __tablename__ = "financial_info"

    user_id = Column(Integer, index=True)
    total_monthly_income = Column(Integer)
    employment_status = Column(String)
    have_loan = Column(Boolean)
