from pydantic import BaseModel, ConfigDict


class ProductsBase(BaseModel):
    ...

    model_config = ConfigDict(orm_mode=True, arbitrary_types_allowed=True)


class ProductsIn(ProductsBase):
    ...


class ProductsUpdate(ProductsBase):
    ...


class ProductsOut(BaseModel):
    ...
