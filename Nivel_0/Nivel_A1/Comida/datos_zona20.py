ZONA_ID = "zona20"
ZONA_NOMBRE = "A1 — Comida y Bebidas"

SECCIONES = {
    "s1": {
        "nombre": "Alimentos y bebidas",
        "rango": "15 palabras",
        "palabras": [
            ("bread", "bred", "pan"),
            ("rice", "ráis", "arroz"),
            ("meat", "mit", "carne"),
            ("chicken", "chíken", "pollo"),
            ("fish", "fish", "pescado"),
            ("egg", "eg", "huevo"),
            ("cheese", "chiz", "queso"),
            ("milk", "milk", "leche"),
            ("butter", "bóter", "mantequilla"),
            ("sugar", "shúgar", "azúcar"),
            ("salt", "solt", "sal"),
            ("water", "uóter", "agua"),
            ("juice", "llus", "jugo"),
            ("coffee", "cófi", "café"),
            ("tea", "ti", "té")
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
    "titulo": "Comida y Bebidas (A1)",
    "explicacion": "Ojo con los falsos amigos y la pronunciación.\n\n• 'Chicken' es pollo y 'fish' es pescado.\n• 'Juice' se pronuncia como 'llus' (aplicando nuestra regla de la 'll').\n• 'Sugar' tiene un sonido 'sh' al inicio.",
    "tabla": [
        {"en": "bread", "pron": "bred", "es": "pan"},
        {"en": "rice", "pron": "ráis", "es": "arroz"},
        {"en": "meat", "pron": "mit", "es": "carne"},
        {"en": "chicken", "pron": "chíken", "es": "pollo"},
        {"en": "fish", "pron": "fish", "es": "pescado"},
        {"en": "egg", "pron": "eg", "es": "huevo"},
        {"en": "cheese", "pron": "chiz", "es": "queso"},
        {"en": "milk", "pron": "milk", "es": "leche"},
        {"en": "butter", "pron": "bóter", "es": "mantequilla"},
        {"en": "sugar", "pron": "shúgar", "es": "azúcar"},
        {"en": "salt", "pron": "solt", "es": "sal"},
        {"en": "water", "pron": "uóter", "es": "agua"},
        {"en": "juice", "pron": "llus", "es": "jugo"},
        {"en": "coffee", "pron": "cófi", "es": "café"},
        {"en": "tea", "pron": "ti", "es": "té"}
    ]
}