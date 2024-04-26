from fastapi import Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import models
from core.db import get_session


# TODO get user from auth token after implementing authentication
async def get_current_user(
    user_id: int = Query(..., description="User ID"),
    db: AsyncSession = Depends(get_session),
):
    """
    Get current user
    """

    q = await db.execute(select(models.User).where(models.User.id == user_id))
    user = q.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
