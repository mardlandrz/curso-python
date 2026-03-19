# main.py
from fastapi import FastAPI

# Crear la app — como iniciar tu servidor PHP
app = FastAPI()

# GET /  — la página de inicio
# PHP: if ($_SERVER['REQUEST_URI'] == '/') { echo "Hola"; }
# FastAPI:
@app.get("/")
def inicio():
    return {"mensaje": "Hola mundo desde FastAPI!"}

# GET /saludo/Maria — URL con parámetro
@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"mensaje": f"Hola {nombre}!"}

# GET /productos — devuelve una lista
@app.get("/productos")
def obtener_productos():
    productos = [
        {"id": 1, "nombre": "Taco",      "precio": 25},
        {"id": 2, "nombre": "Agua",      "precio": 15},
        {"id": 3, "nombre": "Quesadilla","precio": 40},
    ]
    return productos


# POST /productos — recibir datos nuevos
# En PHP: $_POST['nombre']
# En FastAPI usamos Pydantic para validar los datos

from pydantic import BaseModel

# Modelo — define qué datos esperamos recibir
class Producto(BaseModel):
    nombre: str
    precio: float
    categoria: str

# Lista que simula una base de datos por ahora
db_productos = [
    {"id": 1, "nombre": "Taco",       "precio": 25,  "categoria": "comida"},
    {"id": 2, "nombre": "Agua",       "precio": 15,  "categoria": "bebida"},
    {"id": 3, "nombre": "Quesadilla", "precio": 40,  "categoria": "comida"},
]

# GET /productos — obtener todos
@app.get("/productos")
def obtener_productos():
    return db_productos

# GET /productos/1 — obtener uno por id
@app.get("/productos/{id}")
def obtener_producto(id: int):
    for producto in db_productos:
        if producto["id"] == id:
            return producto
    return {"error": "Producto no encontrado"}

# POST /productos — crear uno nuevo
@app.post("/productos")
def crear_producto(producto: Producto):
    nuevo = {
        "id":        len(db_productos) + 1,
        "nombre":    producto.nombre,
        "precio":    producto.precio,
        "categoria": producto.categoria,
    }
    db_productos.append(nuevo)
    return {"mensaje": "Producto creado", "producto": nuevo}

# DELETE /productos/1 — eliminar por id
@app.delete("/productos/{id}")
def eliminar_producto(id: int):
    for i, producto in enumerate(db_productos):
        if producto["id"] == id:
            eliminado = db_productos.pop(i)
            return {"mensaje": "Producto eliminado", "producto": eliminado}
    return {"error": "Producto no encontrado"}