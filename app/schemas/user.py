from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    """Esquema para la creación de un nuevo usuario."""
    full_name: str = Field(..., min_length=3, max_length=120)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=100)

class UserResponse(BaseModel):
    """Esquema para devolver datos del usuario (sin la contraseña)."""
    id: int
    full_name: str
    email: EmailStr
    is_active: bool
    is_admin: bool

    class Config:
        from_attributes = True # Permite que Pydantic lea modelos de SQLAlchemy

class UserLogin(BaseModel):
    """Esquema para la validación de login."""
    email: EmailStr
    password: str