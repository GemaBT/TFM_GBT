from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import User, Role, UserSession
from dependencies import get_db
from auth import hash_password, verify_password, create_token

app = FastAPI()

# =========================
# REGISTRO
# =========================
@app.post("/register")
def register(username: str, email: str, password: str, db: Session = Depends(get_db)):

    user_exists = db.query(User).filter(User.username == username).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Usuario ya existe")

    user = User(
        username=username,
        email=email,
        password_hash=hash_password(password),
        role_id=2  # user normal
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"msg": "Usuario creado"}

# =========================
# LOGIN
# =========================
@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.username == username).first()

    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    token = create_token({"sub": user.username, "role": user.role_id})

    # guardar sesión en DB
    session = UserSession(
        user_id=user.id,
        token=token
    )
    db.add(session)
    db.commit()

    return {"access_token": token}

# =========================
# PROTECCIÓN BÁSICA
# =========================
from fastapi.security import HTTPBearer
from jose import jwt

security = HTTPBearer()

@app.get("/protected")
def protected(token=Depends(security)):

    try:
        payload = jwt.decode(token.credentials, "supersecret", algorithms=["HS256"])
        return {"user": payload}
    except:
        raise HTTPException(status_code=401, detail="Token inválido")

# =========================
# SOLO ADMIN
# =========================
@app.get("/admin")
def admin_only(token=Depends(security)):

    payload = jwt.decode(token.credentials, "supersecret", algorithms=["HS256"])

    if payload["role"] != 1:
        raise HTTPException(status_code=403, detail="No autorizado")

    return {"msg": "Bienvenido admin"}

