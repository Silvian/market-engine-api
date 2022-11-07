import pytest


@pytest.mark.asyncio
class TestCatalogue:

    async def test_empty_list_all_catalogue_items(self, api):
        response = await api.get("api/v1/catalogue/")
        assert response.status_code == 404
        assert response.json() == {
            "detail": "No catalogue items currently available."
        }
