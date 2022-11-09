import logging
from typing import List

from fastapi import APIRouter, HTTPException, status

from ..models.catalogue import Item, ItemDetails

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
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No item details found.",
        )

    return item
