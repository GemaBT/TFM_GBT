from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database import SessionLocal
from api.models import Role
from api.schemas import RoleCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/roles")
def get_roles(db: Session = Depends(get_db)):
    return db.query(Role).all()

@router.post("/roles")
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    new_role = Role(name=role.name, description=role.description)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

@router.delete("/roles/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(404, "Role no encontrado")
    db.delete(role)
    db.commit()
    return {"message": "Role eliminado"}