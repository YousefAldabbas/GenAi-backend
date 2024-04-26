from fastapi import HTTPException, Query
from app import models


# TODO get user from auth token after implementing authentication
def get_current_user(user_id: int = Query(..., description="User ID")) -> models.User:
    """
    Get current user
    """

    if user := models.User.get(user_id):
        return user
    raise HTTPException(status_code=404, detail="User not found")



