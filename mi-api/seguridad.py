# seguridad.py
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

# Configuración — en producción estos valores van en variables de entorno
SECRET_KEY = "mi-clave-secreta-super-segura-2024"
ALGORITMO = "HS256"
MINUTOS_EXPIRACION = 30

# Motor de encriptación de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def encriptar_password(password: str) -> str:
    # Convierte "123456" en "$2b$12$xyz..." — no se puede revertir
    return pwd_context.hash(password)

def verificar_password(password: str, password_encriptado: str) -> bool:
    # Compara la contraseña con la encriptada
    return pwd_context.verify(password, password_encriptado)

def crear_token(datos: dict) -> str:
    # Crea un token JWT con expiración
    datos_token = datos.copy()
    expiracion = datetime.utcnow() + timedelta(minutes=MINUTOS_EXPIRACION)
    datos_token.update({"exp": expiracion})
    return jwt.encode(datos_token, SECRET_KEY, algorithm=ALGORITMO)

def verificar_token(token: str) -> str | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITMO])
        usuario = payload.get("sub")
        return usuario
    except JWTError:
        return None