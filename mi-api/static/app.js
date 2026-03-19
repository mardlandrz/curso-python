// Token guardado en memoria
let token = null;

// ── LOGIN ─────────────────────────────────────────────────
async function login() {
    const email    = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    // fetch() — exactamente como en PHP pero desde JS
    const respuesta = await fetch("/login", {
        method: "POST",
        headers: {"Content-Type": "application/x-www-form-urlencoded"},
        body: `username=${email}&password=${password}`
    });

    const datos = await respuesta.json();

    if (respuesta.ok) {
        token = datos.access_token;          // guarda el token
        mostrarDashboard();
    } else {
        document.getElementById("error-login").textContent = datos.detail;
    }
}

// ── MOSTRAR / OCULTAR PANTALLAS ───────────────────────────
function mostrarDashboard() {
    document.getElementById("pantalla-login").classList.add("oculto");
    document.getElementById("pantalla-dashboard").classList.remove("oculto");
    cargarProductos();
}

function cerrarSesion() {
    token = null;
    document.getElementById("pantalla-login").classList.remove("oculto");
    document.getElementById("pantalla-dashboard").classList.add("oculto");
}

// ── CARGAR PRODUCTOS ──────────────────────────────────────
async function cargarProductos() {
    const respuesta = await fetch("/productos", {
        headers: {"Authorization": `Bearer ${token}`}
    });

    const productos = await respuesta.json();
    const lista     = document.getElementById("lista-productos");

    lista.innerHTML = "";

    productos.forEach(p => {
        lista.innerHTML += `
            <div class="producto-card">
                <div class="producto-info">
                    <strong>${p.nombre}</strong>
                    <p>$${p.precio} — ${p.categoria}</p>
                </div>
                <div class="producto-acciones">
                    <button class="btn-pequeño btn-rojo" onclick="eliminarProducto(${p.id})">
                        Eliminar
                    </button>
                </div>
            </div>
        `;
    });
}

// ── CREAR PRODUCTO ────────────────────────────────────────
async function crearProducto() {
    const nombre    = document.getElementById("nuevo-nombre").value;
    const precio    = document.getElementById("nuevo-precio").value;
    const categoria = document.getElementById("nuevo-categoria").value;

    if (!nombre || !precio || !categoria) {
        alert("Llena todos los campos");
        return;
    }

    await fetch("/productos", {
        method: "POST",
        headers: {
            "Content-Type":  "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({nombre, precio: parseFloat(precio), categoria})
    });

    // Limpia los campos
    document.getElementById("nuevo-nombre").value    = "";
    document.getElementById("nuevo-precio").value    = "";
    document.getElementById("nuevo-categoria").value = "";

    cargarProductos();    // recarga la lista
}

// ── ELIMINAR PRODUCTO ─────────────────────────────────────
async function eliminarProducto(id) {
    if (!confirm("¿Eliminar este producto?")) return;

    await fetch(`/productos/${id}`, {
        method: "DELETE",
        headers: {"Authorization": `Bearer ${token}`}
    });

    cargarProductos();    // recarga la lista
}