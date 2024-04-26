from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import dependencies as deps
from app import models
from app.repositories import users as usr_repo
from app.schemas import users as usr_schema
from core.db import get_session

router = APIRouter()


@router.post("/users")
async def create_user(
    payload: usr_schema.UserIn, db: AsyncSession = Depends(get_session)
):
    """
    Create a new user
    """
    return http_handler(data=await usr_repo.create_user(db, payload), status_code=201)


@router.get("/users/profile")
async def get_user_profile(user: models.User = Depends(deps.get_current_user)):
    """

    Get user profile
    """

    return http_handler(data=usr_repo.get_user_profile(user), status_code=200)
