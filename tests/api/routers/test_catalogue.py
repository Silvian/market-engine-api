import pytest


@pytest.mark.asyncio
class TestCatalogue:
    async def test_empty_list_all_catalogue_items(self, api):
        response = await api.get("api/v1/catalogue/")
        assert response.status_code == 404
        assert response.json() == {"detail": "No catalogue items currently available."}

    async def test_empty_get_catalogue_item_details(self, api):
        response = await api.get("api/v1/catalogue/aeb2c917-eb25-4a5e-b56e-8afdc8061cdb")
        assert response.status_code == 404
        assert response.json() == {"detail": "No item details found."}
