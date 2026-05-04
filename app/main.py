from fastapi import FastAPI
from app.database import Base, engine
from app.routes.auth import router as auth_router
from app.models.user import User
Base.metadata.create_all(bind=engine)
app = FastAPI(
 title="App Hotel Popayán API",
 version="1.0.0"
)
app.include_router(auth_router)
@app.get("/")
def root():
 return {"message": "Backend App Hotel Popayán en ejecución"}