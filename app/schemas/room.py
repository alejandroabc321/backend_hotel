from pydantic import BaseModel


class RoomBase(BaseModel):
    precio: float
    descripcion: str


class RoomCreate(RoomBase):
    pass


class RoomResponse(RoomBase):
    id: int

    model_config = {
        "from_attributes": True
    }