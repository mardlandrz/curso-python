# errores.py

# ── EL PROBLEMA SIN MANEJO DE ERRORES ────────────────────
# Si no manejas errores, tu programa muere completamente

# Esto crashea el programa:
# numero = int("hola")   # ValueError: no puedes convertir "hola" a número
# print(numero)          # esta línea nunca se ejecuta

# ── TRY / EXCEPT ─────────────────────────────────────────
# PHP: try { } catch (Exception $e) { }
# Python:

try:
    numero = int("hola")      # intenta esto
    print(numero)
except:
    print("Eso no es un número")   # si falla, hace esto

# El programa NO muere, continúa normalmente
print("El programa sigue funcionando")

print("---")

# ── CAPTURAR EL ERROR ESPECÍFICO ─────────────────────────
try:
    resultado = 10 / 0        # división entre cero
except ZeroDivisionError:
    print("Error: no puedes dividir entre cero")

print("---")

# ── VER EL MENSAJE DEL ERROR ─────────────────────────────
try:
    numero = int("abc")
except ValueError as error:
    print(f"Ocurrió un error: {error}")

print("---")

# ── VARIOS EXCEPT ────────────────────────────────────────
def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Error: no puedes dividir entre cero"
    except TypeError:
        return "Error: solo puedes dividir números"

print(dividir(10, 2))       # 5.0
print(dividir(10, 0))       # Error: no puedes dividir entre cero
print(dividir(10, "hola"))  # Error: solo puedes dividir números

print("---")

# ── FINALLY ──────────────────────────────────────────────
# Se ejecuta SIEMPRE, haya error o no
# Útil para cerrar archivos, conexiones a base de datos, etc.

def conectar_bd():
    try:
        print("Conectando a la base de datos...")
        # simulamos un error
        raise Exception("Sin conexión")
        print("Conectado!")          # esta línea nunca se ejecuta
    except Exception as error:
        print(f"Error de conexión: {error}")
    finally:
        print("Esto se ejecuta siempre — cerrando conexión")

conectar_bd()

# Con try — el programa sobrevive
try:
    edad = int(input("Escribe tu edad: "))
    print(f"Tienes {edad} años")
except ValueError:
    print("Eso no es una edad válida!")

