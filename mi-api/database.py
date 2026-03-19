# database.py
import sqlite3

DB = "productos.db"  # nombre del archivo de base de datos

def conectar():
    return sqlite3.connect(DB)

def crear_tabla():
    conn = conectar()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre    TEXT    NOT NULL,
            precio    REAL    NOT NULL,
            categoria TEXT    NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def obtener_todos():
    conn = conectar()
    cursor = conn.execute("SELECT * FROM productos")
    filas = cursor.fetchall()
    conn.close()
    # Convierte cada fila en diccionario
    return [
        {"id": f[0], "nombre": f[1], "precio": f[2], "categoria": f[3]}
        for f in filas
    ]

def obtener_uno(id: int):
    conn = conectar()
    cursor = conn.execute("SELECT * FROM productos WHERE id = ?", (id,))
    fila = cursor.fetchone()
    conn.close()
    if fila:
        return {"id": fila[0], "nombre": fila[1], "precio": fila[2], "categoria": fila[3]}
    return None

def crear(nombre: str, precio: float, categoria: str):
    conn = conectar()
    cursor = conn.execute(
        "INSERT INTO productos (nombre, precio, categoria) VALUES (?, ?, ?)",
        (nombre, precio, categoria)
    )
    conn.commit()
    id_nuevo = cursor.lastrowid
    conn.close()
    return obtener_uno(id_nuevo)

def eliminar(id: int):
    producto = obtener_uno(id)
    if not producto:
        return None
    conn = conectar()
    conn.execute("DELETE FROM productos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return producto

def actualizar(id: int, nombre: str, precio: float, categoria: str):
    conn = conectar()
    conn.execute(
        "UPDATE productos SET nombre = ?, precio = ?, categoria = ? WHERE id = ?",
        (nombre, precio, categoria, id)
    )
    conn.commit()
    conn.close()
    return obtener_uno(id)