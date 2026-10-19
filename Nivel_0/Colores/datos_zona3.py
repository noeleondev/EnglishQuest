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

TEORIA = {
    "titulo": "Los Colores (Colors)",
    "explicacion": "Los colores en inglés son adjetivos, así que no cambian según el género. Cuando quieras decir 'un carro rojo', dirás 'a red car' (el color va antes del sustantivo).",
    "tabla": [
        {"en": "red", "pron": "red", "es": "rojo"},
        {"en": "blue", "pron": "blu", "es": "azul"},
        {"en": "green", "pron": "grin", "es": "verde"},
        {"en": "yellow", "pron": "iélou", "es": "amarillo"},
        {"en": "orange", "pron": "óranchn", "es": "naranja"},
        {"en": "purple", "pron": "pérpol", "es": "morado"},
        {"en": "pink", "pron": "pink", "es": "rosa"},
        {"en": "black", "pron": "blak", "es": "negro"},
        {"en": "white", "pron": "uáit", "es": "blanco"},
        {"en": "brown", "pron": "bráun", "es": "café / marrón"},
        {"en": "gray", "pron": "gréi", "es": "gris"},
        {"en": "gold", "pron": "gold", "es": "dorado"}
    ]
}