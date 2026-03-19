# funciones.py

# ── FUNCIÓN BÁSICA ───────────────────────────────────────
# PHP: function saludar($nombre) { return "Hola " . $nombre; }
# Python:

def saludar(nombre):
    return f"Hola {nombre}!"

resultado = saludar("María")
print(resultado)

print("---")

# ── FUNCIÓN CON VARIOS PARÁMETROS ────────────────────────
def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total

print(calcular_total(25, 3))     # 75
print(calcular_total(99, 2))     # 198

print("---")

# ── PARÁMETROS CON VALOR POR DEFECTO ─────────────────────
# Si no pasas el argumento, usa el valor default
def saludar_formal(nombre, saludo="Hola"):
    return f"{saludo} {nombre}!"

print(saludar_formal("María"))              # usa "Hola" por defecto
print(saludar_formal("María", "Buenos días"))  # usa el que mandas

print("---")

# ── FUNCIÓN QUE RETORNA VARIOS VALORES ───────────────────
# Esto NO existe en PHP — es una ventaja de Python
def precio_con_iva(precio):
    iva = precio * 0.16
    total = precio + iva
    return precio, iva, total       # retorna 3 valores a la vez

base, impuesto, final = precio_con_iva(100)
print(f"Base: ${base}")
print(f"IVA:  ${impuesto}")
print(f"Total: ${final}")

print("---")

# ── FUNCIÓN DENTRO DE FUNCIÓN ────────────────────────────
def procesar_orden(producto, cantidad, precio_unitario):
    def calcular_descuento(total):
        if total > 200:
            return total * 0.10    # 10% descuento
        return 0

    subtotal  = cantidad * precio_unitario
    descuento = calcular_descuento(subtotal)
    total     = subtotal - descuento

    print(f"Producto:  {producto}")
    print(f"Subtotal:  ${subtotal}")
    print(f"Descuento: ${descuento}")
    print(f"Total:     ${total}")

procesar_orden("Teclado", 3, 80)

def calcular_envio(peso):
    if peso <= 5:
        return f"envio gratis"
    elif peso >= 5:
        return f"envio de $50"
print(calcular_envio(20))