from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# engine se encarga de la conexión física a PostgreSQL
engine = create_engine(settings.DATABASE_URL, echo=False)

# SessionLocal es la fábrica de sesiones para interactuar con los datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """Inyección de dependencia para obtener la sesión de la base de datos."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()