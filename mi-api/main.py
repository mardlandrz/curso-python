# main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import database
import usuarios
import seguridad

app = FastAPI()

# Crea las tablas al iniciar
database.crear_tabla()
usuarios.crear_tabla()

# Define dónde está el endpoint de login
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# ── MODELOS ───────────────────────────────────────────────
class Producto(BaseModel):
    nombre:    str
    precio:    float
    categoria: str

class UsuarioRegistro(BaseModel):
    nombre:   str
    email:    str
    password: str

# ── FUNCIÓN: obtener usuario del token ────────────────────
def obtener_usuario_actual(token: str = Depends(oauth2)):
    email = seguridad.verificar_token(token)
    if not email:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    usuario = usuarios.obtener_por_email(email)
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    return usuario

# ── RUTAS PÚBLICAS (sin login) ────────────────────────────
@app.get("/")
def inicio():
    return {"mensaje": "API con seguridad funcionando!"}

@app.post("/registro")
def registrar(usuario: UsuarioRegistro):
    resultado = usuarios.crear_usuario(
        usuario.nombre,
        usuario.email,
        usuario.password
    )
    if not resultado:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    return resultado

@app.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    usuario = usuarios.obtener_por_email(form.username)
    if not usuario:
        raise HTTPException(status_code=401, detail="Email no encontrado")
    if not seguridad.verificar_password(form.password, usuario["password"]):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")
    token = seguridad.crear_token({"sub": usuario["email"]})
    return {"access_token": token, "token_type": "bearer"}

# ── RUTAS PROTEGIDAS (requieren login) ────────────────────
@app.get("/productos")
def obtener_productos(usuario = Depends(obtener_usuario_actual)):
    return database.obtener_todos()

@app.get("/productos/{id}")
def obtener_producto(id: int, usuario = Depends(obtener_usuario_actual)):
    producto = database.obtener_uno(id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.post("/productos")
def crear_producto(producto: Producto, usuario = Depends(obtener_usuario_actual)):
    nuevo = database.crear(producto.nombre, producto.precio, producto.categoria)
    return {"mensaje": "Producto creado", "producto": nuevo}

@app.put("/productos/{id}")
def actualizar_producto(id: int, producto: Producto, usuario = Depends(obtener_usuario_actual)):
    existente = database.obtener_uno(id)
    if not existente:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    actualizado = database.actualizar(id, producto.nombre, producto.precio, producto.categoria)
    return {"mensaje": "Producto actualizado", "producto": actualizado}

@app.delete("/productos/{id}")
def eliminar_producto(id: int, usuario = Depends(obtener_usuario_actual)):
    eliminado = database.eliminar(id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje": "Producto eliminado", "producto": eliminado}

@app.get("/mi-perfil")
def mi_perfil(usuario = Depends(obtener_usuario_actual)):
    return {
        "id":     usuario["id"],
        "nombre": usuario["nombre"],
        "email":  usuario["email"]
    }