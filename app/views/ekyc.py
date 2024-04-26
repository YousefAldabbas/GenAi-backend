from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import dependencies as deps
from app import models
from app.repositories import ekyc as ekyc_repo
from app.schemas import ekyc as ekyc_schema
from core.db import get_session
from utils import http_handler

router = APIRouter()


@router.get("/financial", response_model=ekyc_schema.FinancialDetailsOut)
async def get_financial_details(
    user: models.User = Depends(deps.get_current_user),
    db: AsyncSession = Depends(get_session),
):
    """
    Get user financial eKYC
    """
    return http_handler(data=await ekyc_repo.get_financial_details(user, db), status_code=200)


@router.post("/financial", response_model=ekyc_schema.FinancialDetailsOut)
async def insert_financial_details(
    payload: ekyc_schema.FinancialDetailsIn,
    user: models.User = Depends(deps.get_current_user),
    db: AsyncSession = Depends(get_session),
):
    """
    Insert user financial eKYC
    """

    return http_handler(
        data=await ekyc_repo.insert_financial_details(user, payload, db),
        status_code=201,
    )


@router.patch("/financial", response_model=ekyc_schema.FinancialDetailsOut)
async def update_financial_details(
    payload: ekyc_schema.FinancialDetailsUpdate,
    user: models.User = Depends(deps.get_current_user),
    db: AsyncSession = Depends(get_session),
):
    """
    Update user financial eKYC
    """

    return http_handler(
        data=await ekyc_repo.update_financial_details(user, payload, db),
        status_code=200,
    )
