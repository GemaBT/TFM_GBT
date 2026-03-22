
from sqlalchemy.orm import Session
from api.database import SessionLocal
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/ping")
def ping():
    return {"message": "¡API funcionando!"}


@router.get("/usuarios")
def read_users(db: Session = Depends(get_db)):
    # Ejecutamos la consulta usando text()
    users = db.execute(text("SELECT * FROM users")).mappings().all()
    # Retornamos la lista de diccionarios
    return {"usuarios": [dict(u) for u in users]}


@router.get("/test")
def read_users(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1")).scalar()
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
    
# 📥 Obtener usuario por ID
@router.get("/usuarios/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.execute(
        text("SELECT * FROM users WHERE id = :id"),
        {"id": user_id}
    ).mappings().first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return dict(user)

# ➕ Crear usuario
@router.post("/usuarios")
def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    try:
        db.execute(
            text("""
                INSERT INTO users (username, email, password_hash, role_id, is_active)
                VALUES (:username, :email, :password, 1, 1)
            """),
            {
                "username": username,
                "email": email,
                "password": password
            }
        )
        db.commit()

        return {"message": "Usuario creado correctamente"}

    except Exception as e:
        db.rollback()
        return {"error": str(e)}

# ✏️ Actualizar usuario
@router.put("/usuarios/{user_id}")
def update_user(user_id: int, username: str, email: str, db: Session = Depends(get_db)):
    result = db.execute(
        text("""
            UPDATE users 
            SET username = :username, email = :email
            WHERE id = :id
        """),
        {
            "id": user_id,
            "username": username,
            "email": email
        }
    )

    db.commit()

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return {"message": "Usuario actualizado"}

# ❌ Eliminar usuario
@router.delete("/usuarios/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    result = db.execute(
        text("DELETE FROM users WHERE id = :id"),
        {"id": user_id}
    )

    db.commit()

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return {"message": "Usuario eliminado"}

"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database import SessionLocal
from api.models import User
from api.schemas import UserCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/usuarios")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("/usuarios")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=user.password,
        role_id=1
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.delete("/usuarios/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, "Usuario no encontrado")
    db.delete(user)
    db.commit()
    return {"message": "Usuario eliminado"}
"""