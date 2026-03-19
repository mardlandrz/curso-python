# usuarios.py
from sqlalchemy import create_engine, text
import seguridad

DATABASE_URL = "postgresql://postgres:daniel123@localhost:5432/miapi"
engine = create_engine(DATABASE_URL)

def crear_tabla():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id       SERIAL PRIMARY KEY,
                nombre   TEXT   NOT NULL,
                email    TEXT   UNIQUE NOT NULL,
                password TEXT   NOT NULL
            )
        """))
        conn.commit()

def crear_usuario(nombre: str, email: str, password: str):
    try:
        password_encriptado = seguridad.encriptar_password(password)
        with engine.connect() as conn:
            conn.execute(
                text("INSERT INTO usuarios (nombre, email, password) VALUES (:nombre, :email, :password)"),
                {"nombre": nombre, "email": email, "password": password_encriptado}
            )
            conn.commit()
        return {"mensaje": f"Usuario {nombre} creado exitosamente"}
    except Exception:
        return None

def obtener_por_email(email: str):
    with engine.connect() as conn:
        resultado = conn.execute(
            text("SELECT * FROM usuarios WHERE email = :email"),
            {"email": email}
        )
        fila = resultado.fetchone()
        if fila:
            return {"id": fila[0], "nombre": fila[1], "email": fila[2], "password": fila[3]}
        return None