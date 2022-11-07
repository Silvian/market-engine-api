from httpx import AsyncClient
from pytest_asyncio import fixture

from app.api.server import app
from app.configuration import configuration


@fixture
async def api() -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as api:
        yield api
