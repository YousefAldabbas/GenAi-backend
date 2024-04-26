from pydantic import BaseModel, ConfigDict, Field, Json


class ProductsBase(BaseModel):
    ...

    model_config = ConfigDict(from_attributese=True, arbitrary_types_allowed=True)


class ProductsIn(ProductsBase):
    name: str = Field(alias="listing_name")
    city: str
    neighborhood: str
    street: str
    land_size: int
    price_per_meter: int
    os_listing_id: int
    description: Json


class ProductsUpdate(ProductsBase): ...


class ProductsOut(BaseModel): ...
