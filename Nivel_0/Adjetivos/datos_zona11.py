"""
DATOS DE LA ZONA 11: ADJETIVOS BÁSICOS
Fuente: "Inglés desde Cero - Nivel 0 al C2" (Mr. León), páginas 14-15
Estructura: 2 secciones + Jefe de Zona
Nota: dividí en dos secciones agrupando por tipo (tamaño/cualidad y estados/opuestos)
"""

ZONA_ID = "zona11"
ZONA_NOMBRE = "Zona 11 — Adjetivos básicos"

SECCIONES = {
    "s1": {
        "nombre": "S1 — Tamaño y cualidad",
        "rango": "10 adjetivos",
        "palabras": [
            ("big",        "big",       "grande"),
            ("small",      "smol",      "pequeño"),
            ("good",       "gud",       "bueno"),
            ("bad",        "bad",       "malo"),
            ("new",        "niu",       "nuevo"),
            ("old",        "óuld",      "viejo"),
            ("long",       "long",      "largo"),
            ("short",      "short",     "corto / bajo"),
            ("tall",       "tol",       "alto"),
            ("beautiful",  "biútiful",  "bonito / hermoso"),
        ],
    },
    "s2": {
        "nombre": "S2 — Estados y velocidad",
        "rango": "10 adjetivos",
        "palabras": [
            ("hot",        "jot",       "caliente"),
            ("cold",       "cóuld",     "frío"),
            ("happy",      "jápi",      "feliz"),
            ("sad",        "sad",       "triste"),
            ("fast",       "fast",      "rápido"),
            ("slow",       "slóu",      "lento"),
            ("easy",       "ísi",       "fácil"),
            ("difficult",  "dífikolt",  "difícil"),
            ("young",      "llong",     "joven"),
            ("expensive",  "expénsiv",  "caro"),
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
    "titulo": "Adjetivos Básicos (Basic Adjectives)",
    "explicacion": "En inglés, los adjetivos son muy sencillos.\n\n• NO tienen género (no hay 'rojo/roja', solo 'red').\n• NO cambian en plural.\n• Siempre van ANTES del sustantivo. Ejemplo: 'Un carro rápido' es 'A fast car' (no 'a car fast').",
    "tabla": [
        {"en": "Big", "pron": "big", "es": "grande"},
        {"en": "Small", "pron": "smol", "es": "pequeño"},
        {"en": "Good", "pron": "gud", "es": "bueno"},
        {"en": "Bad", "pron": "bad", "es": "malo"},
        {"en": "Hot", "pron": "jot", "es": "caliente"},
        {"en": "Cold", "pron": "cóuld", "es": "frío"},
        {"en": "New", "pron": "niu", "es": "nuevo"},
        {"en": "Old", "pron": "óuld", "es": "viejo"},
        {"en": "Happy", "pron": "jápi", "es": "feliz"},
        {"en": "Sad", "pron": "sad", "es": "triste"},
        {"en": "Fast", "pron": "fast", "es": "rápido"},
        {"en": "Slow", "pron": "slóu", "es": "lento"}
    ]
}