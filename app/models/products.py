from sqlalchemy import JSON, Column, Integer, String

from .base import BaseSQLModel


class Product(BaseSQLModel):
    __tablename__ = "products"

    name = Column(String, index=True)
    description = Column(JSON)
    city = Column(String)
    neighborhood = Column(String)
    street = Column(String)
    land_size = Column(Integer)
    price_per_meter = Column(Integer)
    os_listing_id = Column(Integer)

    @property
    def price(self):
        return self.land_size * self.price_per_meter
