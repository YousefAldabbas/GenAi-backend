from fastapi import HTTPException
from app.schemas import users as usr_schemas
from app import models
from sqlalchemy.orm import Session


async def create_user(user: usr_schemas.UserIn, db: Session) -> usr_schemas.UserOut:
    db_user = models.User(
        username=user.username, email=user.email, password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def get_user_profile(user_id: int, db: Session) -> usr_schemas.UserOut:
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return usr_schemas.UserOut.model_validate_json(user)


async def update_user_profile(
    user: models.User, payload: usr_schemas.UserUpdate, db: Session
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
