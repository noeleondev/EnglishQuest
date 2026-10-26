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

TEORIA = {
    "titulo": "Los Días de la Semana (Days of the Week)",
    "explicacion": "En inglés, los días de la semana SIEMPRE se escriben con mayúscula inicial.\n\n• La semana en inglés (especialmente en EE.UU.) empieza en domingo, aunque el lunes es el primer día laboral.\n• Cuando dices 'el lunes', usas la preposición 'on': 'on Monday'.",
    "tabla": [
        {"en": "Monday", "pron": "móndei", "es": "lunes"},
        {"en": "Tuesday", "pron": "tiúsdei", "es": "martes"},
        {"en": "Wednesday", "pron": "uénsdei", "es": "miércoles"},
        {"en": "Thursday", "pron": "zérsdei", "es": "jueves"},
        {"en": "Friday", "pron": "fráidei", "es": "viernes"},
        {"en": "Saturday", "pron": "sáturdei", "es": "sábado"},
        {"en": "Sunday", "pron": "sóndei", "es": "domingo"}
    ]
}