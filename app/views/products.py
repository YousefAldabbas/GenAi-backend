from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.schemas.products import ProductsIn
from app.repositories.products import add_land_product

router = APIRouter()


@router.post("")
async def add_product(req_payload: ProductsIn, db):
    data = await add_land_product(req_payload, db)
    return JSONResponse(status_code=status.HTTP_200_OK, content=data)
