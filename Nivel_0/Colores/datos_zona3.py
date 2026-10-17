"""
DATOS DE LA ZONA 3: COLORES
Fuente: "Inglés desde Cero - Nivel 0 al C2" (Mr. León), página 10
Estructura: 1 sola sección (zona corta, 12 palabras)
"""

ZONA_ID = "zona3"
ZONA_NOMBRE = "Zona 3 — Colores"

# ─────────────────────────────────────────────
# SECCIÓN ÚNICA
# Zona corta: 12 palabras, 4 fases sin sub-secciones.
# ─────────────────────────────────────────────
SECCIONES = {
    "s1": {
        "nombre": "Colores básicos",
        "rango": "12 colores",
        "palabras": [
            ("red",    "red",     "rojo"),
            ("blue",   "blu",     "azul"),
            ("green",  "grin",    "verde"),
            ("yellow", "iélou",   "amarillo"),
            ("orange", "óranchn", "naranja"),
            ("purple", "pérpol",  "morado"),
            ("pink",   "pink",    "rosa"),
            ("black",  "blak",    "negro"),
            ("white",  "uáit",    "blanco"),
            ("brown",  "bráun",   "café/marrón"),
            ("gray",   "gréi",    "gris"),
            ("gold",   "gold",    "dorado"),
        ],
    },
}

ORDEN_SECCIONES = ["s1"]


def obtener_todas_las_palabras():
    """Devuelve la lista completa de las 12 palabras."""
    todas = []
    for sid in ORDEN_SECCIONES:
        todas.extend(SECCIONES[sid]["palabras"])
    return todas