from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database import SessionLocal
from api.models import Permission
from api.schemas import PermissionCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/permisos")
def get_permissions(db: Session = Depends(get_db)):
    return db.query(Permission).all()

@router.post("/permisos")
def create_permission(permission: PermissionCreate, db: Session = Depends(get_db)):
    new_permission = Permission(name=permission.name, description=permission.description)
    db.add(new_permission)
    db.commit()
    db.refresh(new_permission)
    return new_permission

@router.delete("/permisos/{permission_id}")
def delete_permission(permission_id: int, db: Session = Depends(get_db)):
    perm = db.query(Permission).filter(Permission.id == permission_id).first()
    if not perm:
        raise HTTPException(404, "Permiso no encontrado")
    db.delete(perm)
    db.commit()
    return {"message": "Permiso eliminado"}