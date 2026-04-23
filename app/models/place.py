class Place(Base):
 tablename = "places"
id = Column(Integer,
primary_key=True) nombre =
Column(String)
descripcion =
Column(String) lat =
Column(String)
lon = Column(String)