from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError
from app.database import get_db
from app.schemas.user import UserCreate, UserResponse
from app.schemas.auth import Token
from app.services.auth_service import register_user, login_user, get_user_by_email
from app.core.security import oauth2_scheme, decode_access_token

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """Ruta para registrar nuevos usuarios en el sistema."""[cite: 2]
    return register_user(db, user)

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Ruta de inicio de sesión que devuelve el token JWT."""[cite: 2]
    # OAuth2PasswordRequestForm usa "username", aquí lo interpretamos como email
    return login_user(db, form_data.username, form_data.password)

@router.get("/me", response_model=UserResponse)
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """Ruta protegida que devuelve la información del usuario actual autenticado."""[cite: 2]
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar el token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decodifica el token para obtener la identidad del usuario
        payload = decode_access_token(token)
        email: str | None = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    # Busca al usuario en la base de datos basándose en el token
    user = get_user_by_email(db, email)
    if user is None:
        raise credentials_exception
    return user