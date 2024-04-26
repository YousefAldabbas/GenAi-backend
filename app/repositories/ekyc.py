from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import models
from app.schemas import ekyc as ekyc_schemas


async def get_financial_details(
    user: models.User,
    session: AsyncSession,
) -> ekyc_schemas.FinancialDetailsOut:
    q = await session.execute(
        select(models.FinancialInfo).filter(models.FinancialInfo.user_id == user.id)
    )
    financial_details = q.scalar_one_or_none()

    if not financial_details:
        raise HTTPException(status_code=404, detail="Financial details not found")

    return ekyc_schemas.FinancialDetailsOut(**financial_details.to_dict())


async def insert_financial_details(
    user: models.User, payload: ekyc_schemas.FinancialDetailsIn, db: AsyncSession
) -> ekyc_schemas.FinancialDetailsOut:
    financial_details = models.FinancialInfo(**payload.model_dump(), user_id=user.id)
    db.add(financial_details)
    await db.commit()
    await db.refresh(financial_details)
    return ekyc_schemas.FinancialDetailsOut(**financial_details.to_dict())


async def update_financial_details(
    user: models.User, payload: ekyc_schemas.FinancialDetailsUpdate, db: AsyncSession
) -> ekyc_schemas.FinancialDetailsOut:
    q = await db.execute(
        select(models.FinancialInfo).filter(models.FinancialInfo.user_id == user.id)
    )
    financial_details = q.scalar_one_or_none()

    data = payload.model_dump(exclude_unset=True, exclude_none=True)

    for key, value in data.items():
        setattr(financial_details, key, value)

    await db.commit()
    await db.refresh(financial_details)
    return ekyc_schemas.FinancialDetailsOut(**financial_details.to_dict())
