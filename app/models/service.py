from sqlalchemy import Column, Integer, String
from app.database import Base


class ServiceRequest(Base):
    tablename = "services"


id = (Column(Integer, primary_key=True),)

tipo = Column(String)
detalle = Column(String)
estado = Column(String)
