# condicionales.py

# PHP usaba llaves {}  →  Python usa dos puntos : y sangría (indentación)
#
# PHP:                          Python:
# if ($edad >= 18) {            if edad >= 18:
#     echo "Mayor";                 print("Mayor")
# }                             

edad = 10
precio = 0
dia = "viernes"

# ── IF / ELIF / ELSE ─────────────────────────────────────
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres niño")

# ── OPERADORES DE COMPARACIÓN ────────────────────────────
# ==  igual que         (mismo que PHP)
# !=  diferente que     (mismo que PHP)
# >   mayor que         (mismo que PHP)
# <   menor que         (mismo que PHP)
# >=  mayor o igual     (mismo que PHP)
# <=  menor o igual     (mismo que PHP)

if precio > 100:
    print(f"Precio alto: ${precio}")
else:
    print(f"Precio accesible: ${precio}")

# ── AND / OR / NOT ───────────────────────────────────────
# PHP usaba &&  ||  !
# Python usa  and  or  not  (palabras reales, más legible)

tiene_dinero = False        
hay_stock = True

if tiene_dinero and hay_stock:
    print("Puedes comprar")

if not tiene_dinero:
    print("Sin fondos")

# ── COMPARAR TEXTO ───────────────────────────────────────
if dia == "lunes":
    print("Inicio de semana")
elif dia == "viernes":
    print("Ya casi fin de semana!")
else:
    print(f"Hoy es {dia}")