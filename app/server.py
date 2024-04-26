from fastapi import APIRouter

from .views import products_router, users_router

main_router = APIRouter()

main_router.include_router(users_router, prefix="/users", tags=["users"])
main_router.include_router(products_router, prefix="/products", tags=["products"])