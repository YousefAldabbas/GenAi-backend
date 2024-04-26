from typing import Optional

from pydantic import BaseModel, ConfigDict


class FinancialDetailsBase(BaseModel):
    total_monthly_income: int
    employment_status: str
    have_loan: bool
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class FinancialDetailsIn(FinancialDetailsBase): ...


class FinancialDetailsUpdate(FinancialDetailsBase):
    total_monthly_income: Optional[int] = None
    employment_status: Optional[str] = None
    have_loan: Optional[bool] = None


class FinancialDetailsOut(FinancialDetailsBase): ...
