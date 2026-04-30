from sqlalchemy import Column, Integer, String
from app.database import Base


class Place(Base):
    tablename = "places"


id = Column(Integer, primary_key=True)

nombre = Column(String)
descripcion = Column(String)
lat = Column(String)
lon = Column(String)
