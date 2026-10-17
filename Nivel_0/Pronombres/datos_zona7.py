"""
DATOS DE LA ZONA 7: PRONOMBRES PERSONALES
Fuente: "Inglés desde Cero - Nivel 0 al C2" (Mr. León), página 12
Estructura: 1 sola sección (zona corta, 7 palabras)
"""

ZONA_ID = "zona7"
ZONA_NOMBRE = "Zona 7 — Pronombres personales"

SECCIONES = {
    "s1": {
        "nombre": "Subject Pronouns",
        "rango": "7 pronombres",
        "palabras": [
            ("I",    "ái",   "yo"),
            ("You",  "iu",   "tú / usted"),
            ("He",   "ji",   "él"),
            ("She",  "shi",  "ella"),
            ("It",   "it",   "eso / ello (cosas y animales)"),
            ("We",   "ui",   "nosotros"),
            ("They", "déi",  "ellos / ellas"),
        ],
    },
}

ORDEN_SECCIONES = ["s1"]


def obtener_todas_las_palabras():
    todas = []
    for sid in ORDEN_SECCIONES:
        todas.extend(SECCIONES[sid]["palabras"])
    return todas