from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database import SessionLocal
from api.models import Role, Permission

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/roles/{role_id}/permisos/{permiso_id}")
def add_permission(role_id: int, permiso_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).get(role_id)
    permiso = db.query(Permission).get(permiso_id)
    if not role or not permiso:
        raise HTTPException(404, "No encontrado")
    role.permissions.append(permiso)
    db.commit()
    return {"message": "Permiso añadido"}

@router.delete("/roles/{role_id}/permisos/{permiso_id}")
def remove_permission(role_id: int, permiso_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).get(role_id)
    permiso = db.query(Permission).get(permiso_id)
    if not role or not permiso:
        raise HTTPException(404, "No encontrado")
    role.permissions.remove(permiso)
    db.commit()
    return {"message": "Permiso eliminado"}