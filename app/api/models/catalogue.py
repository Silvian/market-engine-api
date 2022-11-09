from typing import List

from pydantic import BaseModel, Field


class Item(BaseModel):
    """Catalogue item data model definition."""

    id: str = Field(
        ...,
        description="Catalogue item unique id.",
        example="aeb2c917-eb25-4a5e-b56e-8afdc8061cdb",
    )
    name: str = Field(
        ...,
        description="Item name.",
        example="Watch",
    )
    image: str = Field(
        None,
        description="Item image url.",
        example="https://example.com/image.jpg",
    )
    rating: float = Field(
        None,
        description="Item rating from 1 to 5.",
        example=4.8,
    )

    def __str__(self):
        return f"Catalogue item name: {self.name} and rating: {self.rating}"


class Review(BaseModel):
    """Catalogue item review data model definition."""

    id: str = Field(
        ...,
        description="Review unique id.",
        example="00853b3f-029b-4450-a829-321ce16c881c",
    )
    item_id: str = Field(
        ...,
        description="Catalogue item unique id reference.",
        example="aeb2c917-eb25-4a5e-b56e-8afdc8061cdb",
    )
    rating: float = Field(
        ...,
        description="Review rating from 1 to 5.",
        example=3,
    )
    comment: str = Field(
        None,
        description="Review comment left by reviewer.",
    )

    def __str__(self):
        return f"Review rating: {self.rating} and comment: {self.comment}"


class ItemDetails(Item):
    """Catalogue item details data model definition."""

    description: str = Field(
        ...,
        description="Item description.",
        example="This is a very nice watch.",
    )
    reviews: List[Review] = Field(
        ...,
        description="Catalogue item reviews",
    )

    def __str__(self):
        return f"Catalogue item name: {self.name} and rating: {self.description}"
