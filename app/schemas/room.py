from pydantic import BaseModel
precio: float
descripcion: str
class RoomCreate(RoomBase): pass
class RoomResponse(RoomBase):
id: int
class Config:
orm_mode = True