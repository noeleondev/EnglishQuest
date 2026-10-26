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

TEORIA = {
    "titulo": "Los Pronombres Personales (Subject Pronouns)",
    "explicacion": "Los pronombres son el sujeto de la oración.\n\n• En inglés, 'I' (yo) SIEMPRE se escribe con mayúscula.\n• No existe distinción entre 'tú' y 'usted' (ambos son 'You').\n• Para cosas, animales o conceptos abstractos se usa 'It'.",
    "tabla": [
        {"en": "I", "pron": "ái", "es": "yo"},
        {"en": "You", "pron": "iu", "es": "tú / usted / ustedes"},
        {"en": "He", "pron": "ji", "es": "él"},
        {"en": "She", "pron": "shi", "es": "ella"},
        {"en": "It", "pron": "it", "es": "eso / ello (cosas y animales)"},
        {"en": "We", "pron": "ui", "es": "nosotros"},
        {"en": "They", "pron": "déi", "es": "ellos / ellas"}
    ]
}