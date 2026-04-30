from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    fecha_inicio = Column(String)  # Fecha de entrada
    fecha_fin = Column(String)  # Fecha de salida
    adultos = Column(Integer)
    ninos = Column(Integer)
    estado = Column(String)  # Ej: "Confirmada", "Pendiente"
    room_id = Column(Integer)  # ID de la habitación reservada
