from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import models
from app.schemas import users as usr_schemas


async def create_user(
    payload: usr_schemas.UserIn, db: AsyncSession
) -> usr_schemas.UserOut:
    """
    @param payload: UserIn schema object
    @param db: SQLAlchemy AsyncSession object
    """
    user = models.User(**payload.model_dump(exclude_unset=True, exclude_none=True))
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return usr_schemas.UserOut(**user.to_dict())


async def get_user_profile(user: models.User, db: AsyncSession) -> usr_schemas.UserOut:
    """
    @param user: User model object
    """

    #  get financial details
    q = await db.execute(
        select(models.FinancialInfo).filter(models.FinancialInfo.user_id == user.id)
    )
    financial_details = q.scalar_one_or_none()

    return usr_schemas.UserOut(**user.to_dict(), done_ekyc=bool(financial_details))


async def update_user_profile(
    user: models.User, payload: usr_schemas.UserUpdate, db: AsyncSession
) -> usr_schemas.UserOut:
    """
    @param user: User model object
    @param payload: UserUpdate schema object
    @param db: SQLAlchemy Session object
    """

    data = payload.model_dump(exclude_unset=True, exclude_none=True)

    for key, value in data.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return usr_schemas.UserOut(**user.to_dict())
