"""
DATOS DE LA ZONA 18: FRUTAS (NIVEL A1)
"""

ZONA_ID = "zona18"
ZONA_NOMBRE = "A1 — Frutas"

SECCIONES = {
    "s1": {
        "nombre": "Frutas básicas",
        "rango": "15 palabras",
        "palabras": [
            ("apple", "ápol", "manzana"),
            ("banana", "banána", "plátano"),
            ("orange", "óranch", "naranja"),
            ("grape", "gréip", "uva"),
            ("strawberry", "stróberi", "fresa"),
            ("watermelon", "uótermelon", "sandía"),
            ("pineapple", "páinapol", "piña"),
            ("mango", "mángou", "mango"),
            ("lemon", "lémon", "limón"),
            ("peach", "pich", "durazno"),
            ("pear", "per", "pera"),
            ("cherry", "chéri", "cereza"),
            ("melon", "mélon", "melón"),
            ("kiwi", "kíui", "kiwi"),
            ("coconut", "cóukonat", "coco")
        ]
    }
}
ORDEN_SECCIONES = ["s1"]

def obtener_todas_las_palabras():
    todas = []
    for sid in ORDEN_SECCIONES:
        todas.extend(SECCIONES[sid]["palabras"])
    return todas

TEORIA = {
    "titulo": "Las Frutas en Inglés (A1)",
    "explicacion": "Las frutas son vocabulario esencial.\n\n• Fíjate en la pronunciación: en inglés americano, la 'r' al final de palabras como 'pear' o 'cherry' suena suave.\n• Recuerda que 'orange' empieza con sonido de vocal, por lo que diríamos 'an orange'.",
    "tabla": [
        {"en": "apple", "pron": "ápol", "es": "manzana"},
        {"en": "banana", "pron": "banána", "es": "plátano"},
        {"en": "orange", "pron": "óranch", "es": "naranja"},
        {"en": "grape", "pron": "gréip", "es": "uva"},
        {"en": "strawberry", "pron": "stróberi", "es": "fresa"},
        {"en": "watermelon", "pron": "uótermelon", "es": "sandía"},
        {"en": "pineapple", "pron": "páinapol", "es": "piña"},
        {"en": "mango", "pron": "mángou", "es": "mango"},
        {"en": "lemon", "pron": "lémon", "es": "limón"},
        {"en": "peach", "pron": "pich", "es": "durazno"},
        {"en": "pear", "pron": "per", "es": "pera"},
        {"en": "cherry", "pron": "chéri", "es": "cereza"},
        {"en": "melon", "pron": "mélon", "es": "melón"},
        {"en": "kiwi", "pron": "kíui", "es": "kiwi"},
        {"en": "coconut", "pron": "cóukonat", "es": "coco"}
    ]
}