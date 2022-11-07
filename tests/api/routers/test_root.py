import pytest


@pytest.mark.asyncio
async def test_root(api):
    response = await api.get("/")
    assert response.status_code == 307
    assert response.headers["Location"] == "/docs"
