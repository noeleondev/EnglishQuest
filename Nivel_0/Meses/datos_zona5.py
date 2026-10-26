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
            ("January",   "llánueri",  "enero"),
            ("February",  "fébrueri",  "febrero"),
            ("March",     "march",     "marzo"),
            ("April",     "éiprol",    "abril"),
            ("May",       "méi",       "mayo"),
            ("June",      "llun",      "junio"),
            ("July",      "llulái",    "julio"),
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

TEORIA = {
    "titulo": "Los Meses del Año (Months of the Year)",
    "explicacion": "Al igual que los días, los meses se escriben con mayúscula inicial.\n\n• Cuando hablas de algo que pasó en un mes específico, usas la preposición 'in'.\n• Ejemplo: 'in May' (en mayo).",
    "tabla": [
        {"en": "January", "pron": "llánueri", "es": "enero"},
        {"en": "February", "pron": "fébrueri", "es": "febrero"},
        {"en": "March", "pron": "march", "es": "marzo"},
        {"en": "April", "pron": "éiprol", "es": "abril"},
        {"en": "May", "pron": "méi", "es": "mayo"},
        {"en": "June", "pron": "llun", "es": "junio"},
        {"en": "July", "pron": "llulái", "es": "julio"},
        {"en": "August", "pron": "ógosta", "es": "agosto"},
        {"en": "September", "pron": "septémber", "es": "septiembre"},
        {"en": "October", "pron": "octóuber", "es": "octubre"},
        {"en": "November", "pron": "novémber", "es": "noviembre"},
        {"en": "December", "pron": "disémber", "es": "diciembre"}
    ]
}