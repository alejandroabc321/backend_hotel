from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de la base de datos (se creará un archivo llamado hotel.db)[cite: 1]
DATABASE_URL = "sqlite:///./hotel.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = (
    declarative_base()
)  # Clase base para que nuestros modelos hereden de ella[cite: 1]
