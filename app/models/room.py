from sqlalchemy import Column, Integer, String,
Float class Room(Base):
 tablename = "rooms"
id = Column(Integer, primary_key=True,
index=True) nombre = Column(String)
tipo =
Column(String)
precio =
Column(Float)
descripcion = Column(String)