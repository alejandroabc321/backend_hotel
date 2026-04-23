from fastapi import FastAPI
from app.routes import rooms app = FastAPI()
app.include_router(rooms.router)