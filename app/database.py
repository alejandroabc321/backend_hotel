from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# echo=False evita que la consola se llene con cada comando SQL (puedes ponerlo en True para debuggear)
engine = create_engine(settings.DATABASE_URL, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """Inyección de dependencia para obtener la sesión de la base de datos."""[cite: 2]
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()