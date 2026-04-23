class Booking(Base):
 tablename = "bookings"
id = Column(Integer,
primary_key=True) fecha_inicio =
Column(String)
fecha_fin =
Column(String)
adultos =
Column(Integer)
ninos =
Column(Integer)
estado = Column(String)
room_id = Column(Integer)