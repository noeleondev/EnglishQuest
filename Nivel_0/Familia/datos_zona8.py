"""
DATOS DE LA ZONA 8: LA FAMILIA
Fuente: "Inglés desde Cero - Nivel 0 al C2" (Mr. León), páginas 12-13
Estructura: 2 secciones + Jefe de Zona
"""

ZONA_ID = "zona8"
ZONA_NOMBRE = "Zona 8 — La familia"

SECCIONES = {
    "s1": {
        "nombre": "S1 — Padres y hermanos",
        "rango": "8 palabras",
        "palabras": [
            ("mother / mom",  "móder / mom",  "madre / mamá"),
            ("father / dad",  "fáder / dad",  "padre / papá"),
            ("parents",       "pérents",      "padres"),
            ("son",           "son",          "hijo"),
            ("daughter",      "dóter",        "hija"),
            ("brother",       "bróder",       "hermano"),
            ("sister",        "síster",       "hermana"),
            ("baby",          "béibi",        "bebé"),
        ],
    },
    "s2": {
        "nombre": "S2 — Abuelos y otros parientes",
        "rango": "9 palabras",
        "palabras": [
            ("grandmother",  "granmóder",    "abuela"),
            ("grandfather",  "granfáder",    "abuelo"),
            ("grandparents", "granpérents",  "abuelos"),
            ("aunt",         "ant",          "tía"),
            ("uncle",        "óncol",        "tío"),
            ("cousin",       "cósin",        "primo / prima"),
            ("husband",      "jósband",      "esposo"),
            ("wife",         "uáif",         "esposa"),
            ("family",       "fámili",       "familia"),
        ],
    },
}

ORDEN_SECCIONES = ["s1", "s2"]

def obtener_todas_las_palabras():
    todas = []
    for sid in ORDEN_SECCIONES:
        todas.extend(SECCIONES[sid]["palabras"])
    return todas

TEORIA = {
    "titulo": "La Familia (Family)",
    "explicacion": "El inglés es más específico que el español aquí.\n\n• En lugar de decir 'mi tío' (que puede ser hermano de papá o mamá), se usa 'uncle' para ambos.\n• Hay palabras exactas para 'sobrino' (nephew) o 'primo' (cousin).\n• Ojo: 'Parents' significa 'padres' (papá y mamá), NO 'parientes' (esos son 'relatives').",
    "tabla": [
        {"en": "Mother / Mom", "pron": "móder / mom", "es": "madre / mamá"},
        {"en": "Father / Dad", "pron": "fáder / dad", "es": "padre / papá"},
        {"en": "Parents", "pron": "pérents", "es": "padres"},
        {"en": "Brother", "pron": "bróder", "es": "hermano"},
        {"en": "Sister", "pron": "síster", "es": "hermana"},
        {"en": "Grandmother", "pron": "granmóder", "es": "abuela"},
        {"en": "Grandfather", "pron": "granfáder", "es": "abuelo"},
        {"en": "Aunt", "pron": "ant", "es": "tía"},
        {"en": "Uncle", "pron": "óncol", "es": "tío"},
        {"en": "Cousin", "pron": "cósin", "es": "primo / prima"}
    ]
}