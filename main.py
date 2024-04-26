from fastapi import FastAPI

from app.server import main_router
from core.middlewares.exception import ExceptionHandlerMiddleware

app = FastAPI()

app.include_router(main_router)
app.add_middleware(ExceptionHandlerMiddleware)