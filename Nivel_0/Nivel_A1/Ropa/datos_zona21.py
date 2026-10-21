ZONA_ID = "zona21"
ZONA_NOMBRE = "A1 — Ropa"

SECCIONES = {
    "s1": {
        "nombre": "Prendas de vestir",
        "rango": "14 palabras",
        "palabras": [
            ("shirt", "shert", "camisa"),
            ("t-shirt", "tí-shert", "camiseta"),
            ("pants", "pants", "pantalones"),
            ("shorts", "shorts", "pantalones cortos"),
            ("dress", "dres", "vestido"),
            ("skirt", "skert", "falda"),
            ("shoes", "shus", "zapatos"),
            ("socks", "soks", "calcetines"),
            ("jacket", "yáket", "chaqueta"),
            ("coat", "cóut", "abrigo"),
            ("hat", "jat", "sombrero / gorra"),
            ("gloves", "glovs", "guantes"),
            ("belt", "belt", "cinturón"),
            ("sweater", "suéter", "suéter")
        ]
    }
}
ORDEN_SECCIONES = ["s1"]

def obtener_todas_las_palabras():
    return SECCIONES["s1"]["palabras"]

TEORIA = {
    "titulo": "La Ropa en Inglés (A1)",
    "explicacion": "Cuidado con 'pants' (pantalones) y 'shorts' (pantalones cortos), siempre van en plural en inglés. 'Jacket' tiene un sonido de 'y' al inicio (yáket), no de 'j' fuerte.",
    "tabla": [
        {"en": "shirt", "pron": "shert", "es": "camisa"},
        {"en": "t-shirt", "pron": "tí-shert", "es": "camiseta"},
        {"en": "pants", "pron": "pants", "es": "pantalones"},
        {"en": "shorts", "pron": "shorts", "es": "pantalones cortos"},
        {"en": "dress", "pron": "dres", "es": "vestido"},
        {"en": "skirt", "pron": "skert", "es": "falda"},
        {"en": "shoes", "pron": "shus", "es": "zapatos"},
        {"en": "socks", "pron": "soks", "es": "calcetines"},
        {"en": "jacket", "pron": "yáket", "es": "chaqueta"},
        {"en": "coat", "pron": "cóut", "es": "abrigo"},
        {"en": "hat", "pron": "jat", "es": "sombrero / gorra"},
        {"en": "gloves", "pron": "glovs", "es": "guantes"},
        {"en": "belt", "pron": "belt", "es": "cinturón"},
        {"en": "sweater", "pron": "suéter", "es": "suéter"}
    ]
}