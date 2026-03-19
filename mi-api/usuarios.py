# usuarios.py
import sqlite3
import seguridad

DB = "usuarios.db"

def conectar():
    return sqlite3.connect(DB)

def crear_tabla():
    conn = conectar()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre   TEXT    NOT NULL,
            email    TEXT    UNIQUE NOT NULL,
            password TEXT    NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def crear_usuario(nombre: str, email: str, password: str):
    try:
        conn = conectar()
        password_encriptado = seguridad.encriptar_password(password)
        conn.execute(
            "INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)",
            (nombre, email, password_encriptado)
        )
        conn.commit()
        conn.close()
        return {"mensaje": f"Usuario {nombre} creado exitosamente"}
    except sqlite3.IntegrityError:
        return None  # email ya existe

def obtener_por_email(email: str):
    conn = conectar()
    cursor = conn.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    fila = cursor.fetchone()
    conn.close()
    if fila:
        return {"id": fila[0], "nombre": fila[1], "email": fila[2], "password": fila[3]}
    return None