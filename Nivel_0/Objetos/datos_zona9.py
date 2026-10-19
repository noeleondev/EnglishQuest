"""
DATOS DE LA ZONA 9: OBJETOS COMUNES
Fuente: "Inglés desde Cero - Nivel 0 al C2" (Mr. León), páginas 13-14
Estructura: 1 sola sección (zona corta, 14 palabras)
Nota: el libro separa "house/key" en una tabla rara, los integro aquí.
"""

ZONA_ID = "zona9"
ZONA_NOMBRE = "Zona 9 — Objetos comunes"

SECCIONES = {
    "s1": {
        "nombre": "Objetos cotidianos",
        "rango": "14 palabras",
        "palabras": [
            ("table",    "téibol",     "mesa"),
            ("chair",    "cher",       "silla"),
            ("book",     "buk",        "libro"),
            ("pen",      "pen",        "bolígrafo"),
            ("pencil",   "pénsol",     "lápiz"),
            ("door",     "dor",        "puerta"),
            ("window",   "uíndou",     "ventana"),
            ("bag",      "bag",        "bolsa / mochila"),
            ("phone",    "fóun",       "teléfono"),
            ("computer", "compúiter",  "computadora"),
            ("bed",      "bed",        "cama"),
            ("clock",    "clok",       "reloj"),
            ("car",      "car",        "carro"),
            ("house",    "jáus",       "casa"),
            ("key",      "ki",         "llave"),
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
    "titulo": "Objetos Comunes (Common Objects)",
    "explicacion": "Este es vocabulario fundamental para el salón de clases y la oficina. Ojo con el falso amigo 'Carpet', que significa 'alfombra' (no carpeta, que es 'folder'). Y 'Phone' es el teléfono (viene de telephone).",
    "tabla": [
        {"en": "Table", "pron": "téibol", "es": "mesa"},
        {"en": "Chair", "pron": "cher", "es": "silla"},
        {"en": "Book", "pron": "buk", "es": "libro"},
        {"en": "Pen", "pron": "pen", "es": "bolígrafo / pluma"},
        {"en": "Pencil", "pron": "pénsol", "es": "lápiz"},
        {"en": "Door", "pron": "dor", "es": "puerta"},
        {"en": "Window", "pron": "uíndou", "es": "ventana"},
        {"en": "Phone", "pron": "fóun", "es": "teléfono"},
        {"en": "Computer", "pron": "compúiter", "es": "computadora"},
        {"en": "Bed", "pron": "bed", "es": "cama"},
        {"en": "House", "pron": "jáus", "es": "casa"},
        {"en": "Key", "pron": "ki", "es": "llave"}
    ]
}