import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware

from ..configuration import configuration
from . import exception_handlers
from .routers import health, root, router_v1

logger = logging.getLogger(__name__)

openapi_tags = [
    {
        "name": "Market Engine API",
        "description": "Market Engine API provides a new fast and scalable e-commerce engine solution.",
    },
]

app = FastAPI(
    title="market-engine-api",
    version="v1.0",
    openapi_tags=openapi_tags,
    docs_url="/docs/",
    redoc_url="/redocs/",
)

app.add_middleware(GZipMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=configuration.cors.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


exception_handlers.register(app)

app.include_router(router_v1, prefix="/api/v1")
app.include_router(health.router, prefix="/health")
app.include_router(root.router, prefix="")
