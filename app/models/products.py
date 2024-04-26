from sqlalchemy import Column, Integer, String, JSON
from .base import BaseSQLModel


class Product(BaseSQLModel):
    __tablename__ = "products"

    name = Column(String, index=True)
    description = Column(JSON)
    city = Column(String)
    street = Column(String)
    land_size = Column(Integer)
    price_per_meter = Column(Integer)

    @property
    def price(self):
        return self.land_size * self.price_per_meter
