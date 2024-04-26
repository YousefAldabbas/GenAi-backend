from sqlalchemy.ext.asyncio import AsyncSession

from app import models
from app.schemas import users as usr_schemas


async def create_user(
    user: usr_schemas.UserIn, db: AsyncSession
) -> usr_schemas.UserOut:
    """
    @param user: UserIn schema object
    @param db: SQLAlchemy AsyncSession object
    """
    db_user = models.User(
        username=user.username, email=user.email, password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def get_user_profile(user: models.User) -> usr_schemas.UserOut:
    """
    @param user: User model object
    """
    return usr_schemas.UserOut.model_validate_json(user)


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
    return usr_schemas.UserOut.model_validate_json(user)
