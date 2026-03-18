from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "Hola esta es mi API"}

@app.get("/usuarios")
def usuarios():
    return [
        {"id": 1, "nombre": "Ana"},
        {"id": 2, "nombre": "Carlos"}
    ]