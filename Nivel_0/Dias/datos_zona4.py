"""
DATOS DE LA ZONA 4: DÍAS DE LA SEMANA
Fuente: "Inglés desde Cero - Nivel 0 al C2" (Mr. León), páginas 10-11
Estructura: 1 sola sección (zona corta, 7 palabras)
"""

ZONA_ID = "zona4"
ZONA_NOMBRE = "Zona 4 — Días de la semana"

SECCIONES = {
    "s1": {
        "nombre": "Días de la semana",
        "rango": "7 días",
        "palabras": [
            ("Monday",    "móndei",   "lunes"),
            ("Tuesday",   "tiúsdei",  "martes"),
            ("Wednesday", "uénsdei",  "miércoles"),
            ("Thursday",  "zérsdei",  "jueves"),
            ("Friday",    "fráidei",  "viernes"),
            ("Saturday",  "sáturdei", "sábado"),
            ("Sunday",    "sóndei",   "domingo"),
        ],
    },
}

ORDEN_SECCIONES = ["s1"]


def obtener_todas_las_palabras():
    todas = []
    for sid in ORDEN_SECCIONES:
        todas.extend(SECCIONES[sid]["palabras"])
    return todas