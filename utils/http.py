
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


def http_handler(
    data: dict = None, status_code: int = 200, message: str = None
) -> JSONResponse:
    """
    Handle HTTP responses
    """

    response = {"data": jsonable_encoder(data), "message": message}
    return JSONResponse(content=response, status_code=status_code)
