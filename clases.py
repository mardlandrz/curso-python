#python# clases.py

# ── QUÉ ES UNA CLASE ─────────────────────────────────────
# Una clase es un molde para crear objetos.
# Ejemplo real: el molde es "Producto", 
# los objetos son "Taco", "Agua", "Quesadilla"

# PHP:                          Python:
# class Producto {              class Producto:
#   public $nombre;                 def __init__(self, nombre, precio):
#   public function __construct()       self.nombre = nombre
# }                                     self.precio = precio

class Producto:
    # __init__ es el constructor — se ejecuta al crear el objeto
    # self es el objeto mismo (como $this en PHP)
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    # Método — una función dentro de la clase
    def describir(self):
        return f"{self.nombre} cuesta ${self.precio}"

    def aplicar_descuento(self, porcentaje):
        descuento    = self.precio * (porcentaje / 100)
        self.precio  = self.precio - descuento
        return f"Nuevo precio: ${self.precio}"


# ── CREAR OBJETOS (instanciar) ────────────────────────────
taco      = Producto("Taco de canasta", 25)
agua      = Producto("Agua mineral", 15)
quesadilla = Producto("Quesadilla", 40)

# Acceder a sus datos
print(taco.nombre)           # Taco de canasta
print(agua.precio)           # 15

# Llamar sus métodos
print(taco.describir())
print(quesadilla.describir())

print("---")

# Aplicar descuento
print(taco.aplicar_descuento(10))    # 10% de descuento

print("---")

# ── LISTA DE OBJETOS ─────────────────────────────────────
# Así es como trabajarás en proyectos reales
productos = [
    Producto("Taco",      25),
    Producto("Agua",      15),
    Producto("Torta",     45),
]

for p in productos:
    print(p.describir())

print("---")

# ── CLASE CON VALIDACIÓN ──────────────────────────────────
# Aquí combinamos todo lo aprendido:
# clases + condicionales + errores

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo   = saldo_inicial

    def depositar(self, cantidad):
        if cantidad <= 0:
            return "Error: la cantidad debe ser mayor a cero"
        self.saldo += cantidad
        return f"Depósito exitoso. Saldo: ${self.saldo}"

    def retirar(self, cantidad):
        try:
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor a cero")
            if cantidad > self.saldo:
                raise ValueError("Saldo insuficiente")
            self.saldo -= cantidad
            return f"Retiro exitoso. Saldo: ${self.saldo}"
        except ValueError as e:
            return f"Error: {e}"

    def ver_saldo(self):
        return f"{self.titular} tiene ${self.saldo}"


# Crear cuenta y operar
cuenta = CuentaBancaria("María", 1000)

print(cuenta.ver_saldo())
print(cuenta.depositar(500))
print(cuenta.retirar(200))
print(cuenta.retirar(5000))    # intenta retirar más de lo que hay
print(cuenta.depositar(-100))  # intenta depositar negativo
print(cuenta.ver_saldo())