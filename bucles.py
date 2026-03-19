# bucles.py

# ── FOR ──────────────────────────────────────────────────
# En PHP: for ($i = 0; $i < 5; $i++)
# En Python es mucho más simple con range()

for i in range(5):
    print(i)           # imprime 0, 1, 2, 3, 4

print("---")

# range(inicio, fin)  →  fin NO se incluye
for i in range(1, 6):
    print(i)           # imprime 1, 2, 3, 4, 5

print("---")

# ── RECORRER UNA LISTA (como array en PHP) ───────────────
frutas = ["mango", "tamarindo", "guayaba"]

for fruta in frutas:
    print(fruta)

print("---")

# ── FOR CON F-STRING ─────────────────────────────────────
productos = ["taco", "torta", "quesadilla"]
precios   = [25, 40, 35]

for i in range(len(productos)):
    print(f"{productos[i]} cuesta ${precios[i]}")

print("---")

# ── WHILE ────────────────────────────────────────────────
# Igual que PHP, se repite MIENTRAS la condición sea True

contador = 0

while contador < 3:
    print(f"Vuelta número {contador}")
    contador += 1      # += es igual que en PHP

print("---")

# ── BREAK Y CONTINUE ─────────────────────────────────────
# break    → sale del bucle completamente
# continue → salta a la siguiente vuelta

for numero in range(100):
    if numero == 3:
        continue       # salta el 3
    if numero == 7:
        break          # para en el 7
    print(numero)
