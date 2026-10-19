ZONA_ID = "gramatica3"
ZONA_NOMBRE = "Gramática — Artículos A / An"

EJERCICIOS = [
    ("___ apple", ["a", "an", "the", "-"], "an", "una manzana", "an apple"),
    ("___ book", ["a", "an", "the", "-"], "a", "un libro", "a book"),
    ("___ elephant", ["a", "an", "the", "-"], "an", "un elefante", "an elephant"),
    ("___ car", ["a", "an", "the", "-"], "a", "un carro", "a car"),
    ("___ hour", ["a", "an", "the", "-"], "an", "una hora", "an hour"),
    ("___ university", ["a", "an", "the", "-"], "a", "una universidad", "a university"),
    ("___ orange", ["a", "an", "the", "-"], "an", "una naranja", "an orange")
]

TEORIA = {
    "titulo": "Los Artículos A / An",
    "explicacion": "🌟 En inglés, 'A' y 'An' significan 'un' o 'una'.\n\n⚙️ La regla NO depende de cómo se escribe la palabra, sino de **cómo suena**:\n• Usa **A** antes de sonido de consonante: a book, a car, a university (suena 'yu').\n• Usa **AN** antes de sonido de vocal: an apple, an hour (la 'h' es muda, suena 'au-er').\n\n💡 Tip: Si la palabra suena como si empezara con A, E, I, O, U, usa AN.",
    "tabla": [
        {"en": "A book", "pron": "a buk", "es": "un libro"},
        {"en": "An apple", "pron": "an ápol", "es": "una manzana"},
        {"en": "A car", "pron": "a car", "es": "un carro"},
        {"en": "An orange", "pron": "an óranch", "es": "una naranja"},
        {"en": "A university", "pron": "a iunivérsiti", "es": "una universidad"},
        {"en": "An hour", "pron": "an áuer", "es": "una hora (h muda)"}
    ]
}

def obtener_todos_los_ejercicios():
    return EJERCICIOS