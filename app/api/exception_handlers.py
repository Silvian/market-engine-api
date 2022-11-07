from fastapi import FastAPI, Request, status
from fastapi.exception_handlers import http_exception_handler
from fastapi.exceptions import HTTPException

from ..exceptions import AppError


async def app_error_handler(request: Request, exc: AppError):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return await http_exception_handler(request, HTTPException(status_code, {"message": str(exc)}))


def register(app: FastAPI):
    app.add_exception_handler(AppError, app_error_handler)
