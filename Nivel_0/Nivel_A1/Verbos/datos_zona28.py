ZONA_ID = "zona28"
ZONA_NOMBRE = "A1 — Verbos Comunes"

SECCIONES = {
    "s1": {
        "nombre": "Acciones básicas",
        "rango": "15 verbos",
        "palabras": [
            ("to be", "tu bi", "ser/estar"),
            ("to have", "tu jav", "tener"),
            ("to do", "tu du", "hacer"),
            ("to go", "tu góu", "ir"),
            ("to eat", "tu it", "comer"),
            ("to drink", "tu drink", "beber"),
            ("to sleep", "tu slip", "dormir"),
            ("to work", "tu uérk", "trabajar"),
            ("to study", "tu stódi", "estudiar"),
            ("to play", "tu pléi", "jugar"),
            ("to read", "tu rid", "leer"),
            ("to write", "tu ráit", "escribir"),
            ("to speak", "tu spik", "hablar"),
            ("to listen", "tu lísen", "escuchar"),
            ("to watch", "tu uátch", "ver/mirar")
        ]
    }
}
ORDEN_SECCIONES = ["s1"]

def obtener_todas_las_palabras():
    return SECCIONES["s1"]["palabras"]

TEORIA = {
    "titulo": "Los Verbos Comunes (A1)",
    "explicacion": "En inglés, los verbos en infinitivo siempre llevan la partícula 'to' adelante (ej. 'to eat'). Es la base para empezar a formar oraciones. La 'o' en 'to go' suena como 'ou'.",
    "tabla": [
        {"en": "to be", "pron": "tu bi", "es": "ser/estar"},
        {"en": "to have", "pron": "tu jav", "es": "tener"},
        {"en": "to do", "pron": "tu du", "es": "hacer"},
        {"en": "to go", "pron": "tu góu", "es": "ir"},
        {"en": "to eat", "pron": "tu it", "es": "comer"},
        {"en": "to drink", "pron": "tu drink", "es": "beber"},
        {"en": "to sleep", "pron": "tu slip", "es": "dormir"},
        {"en": "to work", "pron": "tu uérk", "es": "trabajar"},
        {"en": "to study", "pron": "tu stódi", "es": "estudiar"},
        {"en": "to play", "pron": "tu pléi", "es": "jugar"},
        {"en": "to read", "pron": "tu rid", "es": "leer"},
        {"en": "to write", "pron": "tu ráit", "es": "escribir"},
        {"en": "to speak", "pron": "tu spik", "es": "hablar"},
        {"en": "to listen", "pron": "tu lísen", "es": "escuchar"},
        {"en": "to watch", "pron": "tu uátch", "es": "ver/mirar"}
    ]
}