import logging
from typing import List

from fastapi import APIRouter, HTTPException, status

from ..models.items import CatalogueItem

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get(
    "/",
    response_model=List[CatalogueItem],
    response_model_exclude_none=True,
    tags=["Catalogue"],
)
async def list_all_catalogue_items() -> List[CatalogueItem]:
    """Returns a list of all the available catalogue items."""
    items = []
    if not items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No catalogue items currently available."
        )

    return items
