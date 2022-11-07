import pytest


@pytest.mark.asyncio
async def test_check_health(api):
    response = await api.get("/health")
    assert response.status_code == 200
    assert response.json() == {}
