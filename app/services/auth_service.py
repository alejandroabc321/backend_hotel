from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash, verify_password, create_access_token

def get_user_by_email(db: Session, email: str):
    """Busca un usuario en la base de datos de PostgreSQL por su correo electrónico."""
    return db.query(User).filter(User.email == email).first()

def register_user(db: Session, user_data: UserCreate):
    """Lógica para registrar un nuevo usuario con contraseña encriptada."""
    existing_user = get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo ya se encuentra registrado"
        )
    
    new_user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        hashed_password=get_password_hash(user_data.password), # Encriptación antes de guardar
        is_active=True,
        is_admin=False
    )
    
    db.add(new_user)
    db.commit() # Guarda físicamente en PostgreSQL
    db.refresh(new_user)
    return new_user

def authenticate_user(db: Session, email: str, password: str):
    """Valida si las credenciales son correctas pero no genera el token aún."""
    user = get_user_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    if not user.is_active:
        return None
    return user

def login_user(db: Session, email: str, password: str):
    """Lógica final de login que genera el token JWT para el usuario."""
    user = authenticate_user(db, email, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Genera el token que la App de Android usará para sesiones futuras
    token = create_access_token(data={"sub": user.email})
    return {
        "access_token": token,
        "token_type": "bearer"
    }