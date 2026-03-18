from fastapi import FastAPI
#from routers import users
from api.router import user_routes

app = FastAPI()

#app.include_router(user_routes.router)
app.include_router(user_routes.router, prefix="/api")

"""
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://api_user:api_password@localhost:3307/api_security")
conn = engine.connect()
result = conn.execute("SELECT * FROM users").fetchall()
print(result)
conn.close()
"""