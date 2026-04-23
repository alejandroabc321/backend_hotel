class ServiceRequest(Base):
 tablename = "services"
id = Column(Integer,
primary_key=True) tipo =
Column(String)
detalle =
Column(String)
estado =
Column(String)