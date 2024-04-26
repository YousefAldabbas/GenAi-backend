from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import dependencies as deps
from app import models
from app.repositories import users as usr_repo
from app.schemas import users as usr_schema
from core.db import get_session
from utils import http_handler

router = APIRouter()


@router.post("", response_model=usr_schema.UserOut)
async def create_user(
    payload: usr_schema.UserIn, db: AsyncSession = Depends(get_session)
):
    """
    Create a new user
    """
    return http_handler(data=await usr_repo.create_user(payload, db), status_code=201)


@router.patch("/profile", response_model=usr_schema.UserOut)
async def update_user_profile(
    payload: usr_schema.UserUpdate,
    user: models.User = Depends(deps.get_current_user),
    db: AsyncSession = Depends(get_session),
):
    """
    Update user profile
    """

    return http_handler(
        data=await usr_repo.update_user_profile(user, payload, db), status_code=200
    )


@router.get("/profile", response_model=usr_schema.UserOut)
async def get_user_profile(
    user: models.User = Depends(deps.get_current_user),
    db: AsyncSession = Depends(get_session),
):
    """
    Get user profile
    """

    return http_handler(data=await usr_repo.get_user_profile(user, db), status_code=200)
