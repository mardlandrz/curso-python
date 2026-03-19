# test_api.py
import time
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Emails únicos con timestamp para evitar duplicados
TS = str(int(time.time()))

def registrar_usuario(email, password="123456"):
    time.sleep(0.1)
    client.post("/registro", json={
        "nombre":   "Usuario Test",
        "email":    email,
        "password": password
    })

def obtener_token(email, password="123456"):
    respuesta = client.post("/login", data={
        "username": email,
        "password": password
    })
    return respuesta.json().get("access_token")

def headers_auth(token):
    return {"Authorization": f"Bearer {token}"}

# ── TESTS DE REGISTRO ─────────────────────────────────────
def test_registro_exitoso():
    respuesta = client.post("/registro", json={
        "nombre":   "María Test",
        "email":    f"maria_{TS}@test.com",
        "password": "123456"
    })
    assert respuesta.status_code == 200
    assert "creado" in respuesta.json()["mensaje"]

def test_registro_email_duplicado():
    email = f"duplicado_{TS}@test.com"
    client.post("/registro", json={
        "nombre": "Test", "email": email, "password": "123456"
    })
    time.sleep(0.1)
    respuesta = client.post("/registro", json={
        "nombre": "Test", "email": email, "password": "123456"
    })
    assert respuesta.status_code == 400

# ── TESTS DE LOGIN ────────────────────────────────────────
def test_login_exitoso():
    email = f"login_{TS}@test.com"
    registrar_usuario(email)
    respuesta = client.post("/login", data={
        "username": email,
        "password": "123456"
    })
    assert respuesta.status_code == 200
    assert "access_token" in respuesta.json()

def test_login_password_incorrecta():
    email = f"wrong_{TS}@test.com"
    registrar_usuario(email)
    respuesta = client.post("/login", data={
        "username": email,
        "password": "password_malo"
    })
    assert respuesta.status_code == 401

def test_login_email_no_existe():
    respuesta = client.post("/login", data={
        "username": "noexiste@test.com",
        "password": "123456"
    })
    assert respuesta.status_code == 401

# ── TESTS DE PRODUCTOS ────────────────────────────────────
def test_productos_sin_token():
    respuesta = client.get("/productos")
    assert respuesta.status_code == 401

def test_crear_producto():
    email = f"prod_{TS}@test.com"
    registrar_usuario(email)
    token = obtener_token(email)

    respuesta = client.post("/productos",
        json={"nombre": "Taco test", "precio": 25, "categoria": "comida"},
        headers=headers_auth(token)
    )
    assert respuesta.status_code == 200
    assert respuesta.json()["producto"]["nombre"] == "Taco test"

def test_obtener_productos():
    email = f"get_{TS}@test.com"
    registrar_usuario(email)
    token = obtener_token(email)

    respuesta = client.get("/productos", headers=headers_auth(token))
    assert respuesta.status_code == 200
    assert isinstance(respuesta.json(), list)

def test_eliminar_producto():
    email = f"del_{TS}@test.com"
    registrar_usuario(email)
    token = obtener_token(email)

    creado = client.post("/productos",
        json={"nombre": "Para eliminar", "precio": 10, "categoria": "test"},
        headers=headers_auth(token)
    )
    id_producto = creado.json()["producto"]["id"]

    respuesta = client.delete(f"/productos/{id_producto}",
        headers=headers_auth(token)
    )
    assert respuesta.status_code == 200
    assert respuesta.json()["mensaje"] == "Producto eliminado"

def test_eliminar_producto_no_existe():
    email = f"nodel_{TS}@test.com"
    registrar_usuario(email)
    token = obtener_token(email)

    respuesta = client.delete("/productos/99999",
        headers=headers_auth(token)
    )
    assert respuesta.status_code == 404