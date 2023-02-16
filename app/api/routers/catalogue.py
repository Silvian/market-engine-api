import grpc
import logging
from typing import List

from fastapi import APIRouter, HTTPException, status

from ..models.catalogue import Item, ItemDetails
from ..pb2 import catalogue_pb2 as catalogue
from ..pb2 import catalogue_pb2_grpc as catalogue_grpc

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    "/",
    response_model=List[Item],
    response_model_exclude_none=True,
    tags=["Catalogue"],
)
async def list_all_catalogue_items() -> List[Item]:
    """Returns a list of all the available catalogue items."""
    items = []
    with grpc.insecure_channel('10.0.8.146:50051') as channel:
        stub = catalogue_grpc.CatalogueStub(channel)
        response = stub.listCatalogueItems(catalogue.ItemsRequest(itemsLimit=1))
        print(f"Response: {response.items}")
        items = response.items
    if not items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No catalogue items currently available."
        )

    return items


@router.get(
    "/{id}",
    response_model=ItemDetails,
    response_model_exclude_none=True,
    tags=["Catalogue"],
)
async def get_catalogue_item_details(id: str) -> ItemDetails:
    """Returns catalogue item details and reviews."""
    item = None
    with grpc.insecure_channel('10.0.8.146:50051') as channel:
        stub = catalogue_grpc.CatalogueStub(channel)
        response = stub.getItemDetails(catalogue.ItemDetailsRequest(itemId=id, reviewsLimit=10))
        print(f"Response: {response}")
        item = ItemDetails(
            id=response.id,
            name=response.name,
            image=response.image,
            rating=response.rating,
            description=response.description,
            reviews=[],
        )
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No item details found.",
        )

    return item
