ZONA_ID = "zona25"
ZONA_NOMBRE = "A1 — Animales"

SECCIONES = {
    "s1": {
        "nombre": "Animales comunes",
        "rango": "15 palabras",
        "palabras": [
            ("dog", "dog", "perro"),
            ("cat", "kat", "gato"),
            ("bird", "berd", "pájaro"),
            ("fish", "fish", "pez"),
            ("horse", "jors", "caballo"),
            ("cow", "káu", "vaca"),
            ("pig", "pig", "cerdo"),
            ("chicken", "chíken", "gallina"),
            ("lion", "láion", "león"),
            ("tiger", "táiguer", "tigre"),
            ("elephant", "élefant", "elefante"),
            ("monkey", "mónki", "mono"),
            ("bear", "ber", "oso"),
            ("rabbit", "rábit", "conejo"),
            ("snake", "snéik", "serpiente")
        ]
    }
}
ORDEN_SECCIONES = ["s1"]

def obtener_todas_las_palabras():
    return SECCIONES["s1"]["palabras"]

TEORIA = {
    "titulo": "Los Animales en Inglés (A1)",
    "explicacion": "La 'ch' en 'chicken' suena como en español. La 'i' en 'lion' y 'tiger' es un diptongo (lái-on, tái-guer). 'Bear' (oso) y 'bird' (pájaro) suenan parecido, presta atención a la vocal.",
    "tabla": [
        {"en": "dog", "pron": "dog", "es": "perro"},
        {"en": "cat", "pron": "kat", "es": "gato"},
        {"en": "bird", "pron": "berd", "es": "pájaro"},
        {"en": "fish", "pron": "fish", "es": "pez"},
        {"en": "horse", "pron": "jors", "es": "caballo"},
        {"en": "cow", "pron": "káu", "es": "vaca"},
        {"en": "pig", "pron": "pig", "es": "cerdo"},
        {"en": "chicken", "pron": "chíken", "es": "gallina"},
        {"en": "lion", "pron": "láion", "es": "león"},
        {"en": "tiger", "pron": "táiguer", "es": "tigre"},
        {"en": "elephant", "pron": "élefant", "es": "elefante"},
        {"en": "monkey", "pron": "mónki", "es": "mono"},
        {"en": "bear", "pron": "ber", "es": "oso"},
        {"en": "rabbit", "pron": "rábit", "es": "conejo"},
        {"en": "snake", "pron": "snéik", "es": "serpiente"}
    ]
}