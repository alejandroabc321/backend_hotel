# app/models/room.py
from sqlalchemy import Column, Integer, String, Float
from app.database import Base  # Importamos la base que configuramos antes


class Room(Base):
    __tablename__ = "rooms"  # Nombre de la tabla en la DB[cite: 1]

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    tipo = Column(String)  # Ej: "Suite", "Sencilla"[cite: 1]
    precio = Column(Float)
    descripcion = Column(String)
