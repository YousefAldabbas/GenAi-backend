from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.products import add_land_product
from app.schemas.products import ProductsIn
from core.db import get_session

router = APIRouter()


@router.post("")
async def add_product(req_payload: ProductsIn, db: AsyncSession = Depends(get_session)):
    data = await add_land_product(req_payload, db)
    return JSONResponse(status_code=status.HTTP_200_OK, content=data)
