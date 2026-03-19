# variables.py

# ── TEXTO (strings) ──────────────────────────
# PHP: $nombre = "María";
nombre = "María"
saludo = 'Hola'          # comillas simples o dobles, ambas funcionan

# ── NÚMEROS ENTEROS ──────────────────────────
# PHP: $edad = 25;
edad = 25
tacos_comidos = 3        # 🌮 vivimos en México, ejemplos reales

# ── NÚMEROS DECIMALES ────────────────────────
# PHP: $precio = 99.50;
precio = 99.50
temperatura = 32.5

# ── VERDADERO / FALSO ────────────────────────
# PHP: $activo = true;
activo = True            # ojo: mayúscula. True y False, no true/false
tiene_cuenta = False

# ── VER LOS VALORES ──────────────────────────
print(nombre)
print(edad)
print(precio)
print(activo)
print(type(nombre))     # <class 'str'>    → texto
print(type(edad))       # <class 'int'>    → entero
print(type(precio))     # <class 'float'>  → decimal
print(type(activo))     # <class 'bool'>   → verdadero/falso
# Agrega esto también

# PHP: echo "Hola " . $nombre . ", tienes " . $edad . " años";
# Python, forma moderna con f-strings (la f antes de las comillas es la clave):
print(f"Hola {nombre}, tienes {edad} años")
print(f"El producto cuesta ${precio}")
print(f"¿Usuario activo? {activo}")