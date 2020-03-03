from sqlalchemy import DECIMAL, TIME, Column, String
from sqlalchemy.dialects.postgresql import UUID

from shopping_hero.models import Base


class Shop(Base):
    __tablename__ = "shop"

    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String)
    latitude = Column(DECIMAL)
    longitude = Column(DECIMAL)
    opens_at = Column(TIME)
    closes_at = Column(TIME)

    def __init__(self, id, name, latitude, longitude, opens_at, closes_at):
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.opens_at = opens_at
        self.closes_at = closes_at
