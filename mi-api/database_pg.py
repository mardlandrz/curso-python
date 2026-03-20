# database_pg.py
import os
from sqlalchemy import create_engine, text

# Conexión a PostgreSQL
# Lee DATABASE_URL del entorno (configurada en Railway).
# Si no está definida, usa la conexión local como fallback para desarrollo.
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:daniel123@localhost:5432/miapi")

engine = create_engine(DATABASE_URL)

def crear_tabla():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS productos (
                id        SERIAL PRIMARY KEY,
                nombre    TEXT   NOT NULL,
                precio    REAL   NOT NULL,
                categoria TEXT   NOT NULL
            )
        """))
        conn.commit()

def obtener_todos():
    with engine.connect() as conn:
        resultado = conn.execute(text("SELECT * FROM productos"))
        filas = resultado.fetchall()
        return [
            {"id": f[0], "nombre": f[1], "precio": f[2], "categoria": f[3]}
            for f in filas
        ]

def obtener_uno(id: int):
    with engine.connect() as conn:
        resultado = conn.execute(
            text("SELECT * FROM productos WHERE id = :id"),
            {"id": id}
        )
        fila = resultado.fetchone()
        if fila:
            return {"id": fila[0], "nombre": fila[1], "precio": fila[2], "categoria": fila[3]}
        return None

def crear(nombre: str, precio: float, categoria: str):
    with engine.connect() as conn:
        resultado = conn.execute(
            text("INSERT INTO productos (nombre, precio, categoria) VALUES (:nombre, :precio, :categoria) RETURNING id"),
            {"nombre": nombre, "precio": precio, "categoria": categoria}
        )
        conn.commit()
        id_nuevo = resultado.fetchone()[0]
        return obtener_uno(id_nuevo)

def actualizar(id: int, nombre: str, precio: float, categoria: str):
    with engine.connect() as conn:
        conn.execute(
            text("UPDATE productos SET nombre=:nombre, precio=:precio, categoria=:categoria WHERE id=:id"),
            {"nombre": nombre, "precio": precio, "categoria": categoria, "id": id}
        )
        conn.commit()
        return obtener_uno(id)

def eliminar(id: int):
    producto = obtener_uno(id)
    if not producto:
        return None
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM productos WHERE id = :id"), {"id": id})
        conn.commit()
        return producto