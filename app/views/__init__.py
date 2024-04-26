from .ekyc import router as financial_router
from .products import router as products_router
from .users import router as users_router

__all__ = ("users_router", "products_router","financial_router")
