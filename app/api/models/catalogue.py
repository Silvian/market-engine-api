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
        example="watch",
    )
    description: str = Field(
        None,
        description="Item description.",
        example="This is a very nice watch."
    )

    def __str__(self):
        return f"Catalogue item name: {self.name} and description: {self.description}"
