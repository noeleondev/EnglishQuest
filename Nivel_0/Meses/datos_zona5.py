"""
DATOS DE LA ZONA 5: MESES DEL AÑO
Fuente: "Inglés desde Cero - Nivel 0 al C2" (Mr. León), página 11
Estructura: 1 sola sección (zona corta, 12 palabras)
"""

ZONA_ID = "zona5"
ZONA_NOMBRE = "Zona 5 — Meses del año"

SECCIONES = {
    "s1": {
        "nombre": "Meses del año",
        "rango": "12 meses",
        "palabras": [
            ("January",   "yánueri",   "enero"),
            ("February",  "fébrueri",  "febrero"),
            ("March",     "march",     "marzo"),
            ("April",     "éiprol",    "abril"),
            ("May",       "méi",       "mayo"),
            ("June",      "yun",       "junio"),
            ("July",      "yulái",     "julio"),
            ("August",    "ógosta",    "agosto"),
            ("September", "septémber", "septiembre"),
            ("October",   "octóuber",  "octubre"),
            ("November",  "novémber",  "noviembre"),
            ("December",  "disémber",  "diciembre"),
        ],
    },
}

ORDEN_SECCIONES = ["s1"]


def obtener_todas_las_palabras():
    todas = []
    for sid in ORDEN_SECCIONES:
        todas.extend(SECCIONES[sid]["palabras"])
    return todas