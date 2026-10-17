"""
DATOS DE LA ZONA 10: PALABRAS INTERROGATIVAS
Fuente: "Inglés desde Cero - Nivel 0 al C2" (Mr. León), página 14
Estructura: 1 sola sección (zona corta, 9 palabras)
"""

ZONA_ID = "zona10"
ZONA_NOMBRE = "Zona 10 — Palabras interrogativas"

SECCIONES = {
    "s1": {
        "nombre": "Question Words",
        "rango": "9 palabras",
        "palabras": [
            ("What",     "uát",       "qué"),
            ("Who",      "ju",        "quién"),
            ("Where",    "uérd",      "dónde"),
            ("When",     "uén",       "cuándo"),
            ("Why",      "uái",       "por qué"),
            ("How",      "jáu",       "cómo"),
            ("How much", "jáu moch",  "cuánto (no contable)"),
            ("How many", "jáu méni",  "cuántos (contable)"),
            ("Which",    "uích",      "cuál"),
        ],
    },
}

ORDEN_SECCIONES = ["s1"]


def obtener_todas_las_palabras():
    todas = []
    for sid in ORDEN_SECCIONES:
        todas.extend(SECCIONES[sid]["palabras"])
    return todas