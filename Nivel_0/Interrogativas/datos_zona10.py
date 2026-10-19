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

TEORIA = {
    "titulo": "Palabras Interrogativas (Question Words)",
    "explicacion": "Todas estas palabras empiezan con 'Wh' (excepto 'How'). 'Who' se usa para personas, 'Where' para lugares, 'When' para tiempo y 'Why' para razones. La diferencia entre 'How much' y 'How many' es si el sustantivo se puede contar o no (dinero/tiempo vs. manzanas/personas).",
    "tabla": [
        {"en": "What", "pron": "uát", "es": "qué"},
        {"en": "Who", "pron": "ju", "es": "quién"},
        {"en": "Where", "pron": "uérd", "es": "dónde"},
        {"en": "When", "pron": "uén", "es": "cuándo"},
        {"en": "Why", "pron": "uái", "es": "por qué"},
        {"en": "How", "pron": "jáu", "es": "cómo"},
        {"en": "Which", "pron": "uích", "es": "cuál"},
        {"en": "How much", "pron": "jáu moch", "es": "cuánto (incontable)"},
        {"en": "How many", "pron": "jáu méni", "es": "cuántos (contable)"}
    ]
}