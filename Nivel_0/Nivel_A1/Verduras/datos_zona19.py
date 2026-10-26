ZONA_ID = "zona19"
ZONA_NOMBRE = "A1 — Verduras"

SECCIONES = {
    "s1": {
        "nombre": "Vegetales",
        "rango": "15 palabras",
        "palabras": [
            ("potato", "potétou", "papa"),
            ("tomato", "tométou", "tomate"),
            ("onion", "ónion", "cebolla"),
            ("carrot", "károt", "zanahoria"),
            ("lettuce", "létis", "lechuga"),
            ("cucumber", "kiúkomber", "pepino"),
            ("garlic", "gárlic", "ajo"),
            ("pepper", "péper", "pimiento/chile"),
            ("corn", "corn", "maíz"),
            ("broccoli", "brócoli", "brócoli"),
            ("spinach", "spínach", "espinaca"),
            ("mushroom", "móshrum", "hongo/champiñón"),
            ("pumpkin", "pómpkin", "calabaza"),
            ("cabbage", "cábich", "repollo"),
            ("beans", "bins", "frijoles")
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
    "titulo": "Las Verduras en Inglés (A1)",
    "explicacion": "Cuidado con las traducciones directas.\n\n• 'Lettuce' es lechuga y 'cabbage' es repollo, son palabras distintas.\n• 'Pepper' se usa tanto para pimiento como para chile.\n• La pronunciación de 'mushroom' tiene el sonido 'sh' suave.",
    "tabla": [
        {"en": "potato", "pron": "potétou", "es": "papa"},
        {"en": "tomato", "pron": "tométou", "es": "tomate"},
        {"en": "onion", "pron": "ónion", "es": "cebolla"},
        {"en": "carrot", "pron": "károt", "es": "zanahoria"},
        {"en": "lettuce", "pron": "létis", "es": "lechuga"},
        {"en": "cucumber", "pron": "kiúkomber", "es": "pepino"},
        {"en": "garlic", "pron": "gárlic", "es": "ajo"},
        {"en": "pepper", "pron": "péper", "es": "pimiento/chile"},
        {"en": "corn", "pron": "corn", "es": "maíz"},
        {"en": "broccoli", "pron": "brócoli", "es": "brócoli"},
        {"en": "spinach", "pron": "spínach", "es": "espinaca"},
        {"en": "mushroom", "pron": "móshrum", "es": "hongo/champiñón"},
        {"en": "pumpkin", "pron": "pómpkin", "es": "calabaza"},
        {"en": "cabbage", "pron": "cábich", "es": "repollo"},
        {"en": "beans", "pron": "bins", "es": "frijoles"}
    ]
}