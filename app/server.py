from fastapi import FastAPI
from .views import users_router, products_router

app = FastAPI()

[app.include_router(router) for router in (users_router, products_router)]
