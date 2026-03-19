# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import database

app = FastAPI()

# Crea la tabla al iniciar el servidor
database.crear_tabla()

class Producto(BaseModel):
    nombre:    str
    precio:    float
    categoria: str

@app.get("/")
def inicio():
    return {"mensaje": "API con base de datos funcionando!"}

@app.get("/productos")
def obtener_productos():
    return database.obtener_todos()

@app.get("/productos/{id}")
def obtener_producto(id: int):
    producto = database.obtener_uno(id)
    if not producto:
        return {"error": "Producto no encontrado"}
    return producto

@app.post("/productos")
def crear_producto(producto: Producto):
    nuevo = database.crear(producto.nombre, producto.precio, producto.categoria)
    return {"mensaje": "Producto creado", "producto": nuevo}

@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    eliminado = database.eliminar(id)
    if not eliminado:
        return {"error": "Producto no encontrado"}
    return {"mensaje": "Producto eliminado", "producto": eliminado}