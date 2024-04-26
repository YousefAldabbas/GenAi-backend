from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

beat_router = APIRouter()


@beat_router.get("")
async def beat():
    return JSONResponse(status_code=status.HTTP_200_OK, content={})
