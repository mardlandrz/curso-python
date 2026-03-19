# listas_dicts.py

# ── LISTAS ───────────────────────────────────────────────
# PHP: $frutas = ["mango", "guayaba", "tamarindo"];
# Python es igual pero sin el $

frutas = ["mango", "guayaba", "tamarindo"]

print(frutas[0])          # mango  (inicia en 0, igual que PHP)
print(frutas[-1])         # tamarindo  (índice negativo = desde el final)
print(len(frutas))        # 3  (len() es como count() en PHP)

print("---")

# ── MÉTODOS DE LISTA ─────────────────────────────────────
frutas.append("mango")        # agrega al final
frutas.remove("guayaba")      # elimina por valor
print(frutas)                 # ['mango', 'tamarindo', 'mango']

print(frutas.count("mango"))  # 2 — cuántas veces aparece
frutas.sort()                 # ordena alfabéticamente
print(frutas)                 # ['mango', 'mango', 'tamarindo']

print("---")

# ── DICCIONARIOS ─────────────────────────────────────────
# PHP: array asociativo  →  $producto = ["nombre" => "Taco", "precio" => 25];
# Python:

producto = {
    "nombre":    "Taco de canasta",
    "precio":    25,
    "categoria": "comida",
    "activo":    True
}

print(producto["nombre"])     # Taco de canasta
print(producto["precio"])     # 25

print("---")

# ── MODIFICAR Y AGREGAR ──────────────────────────────────
producto["precio"] = 30                  # modifica
producto["descripcion"] = "Rico taco"   # agrega nueva clave

print(producto)

print("---")

# ── RECORRER UN DICCIONARIO ──────────────────────────────
for clave, valor in producto.items():
    print(f"{clave}: {valor}")

print("---")

# ── LISTA DE DICCIONARIOS ────────────────────────────────
# Esto es lo que más usarás — datos de una base de datos,
# respuesta de una API, etc.

carrito = [
    {"producto": "Taco",     "precio": 25, "cantidad": 3},
    {"producto": "Agua",     "precio": 15, "cantidad": 2},
    {"producto": "Quesadilla","precio": 40, "cantidad": 1},
]

total = 0

for item in carrito:
    subtotal = item["precio"] * item["cantidad"]
    total += subtotal
    print(f'{item["producto"]}: ${subtotal}')

print(f"Total: ${total}")