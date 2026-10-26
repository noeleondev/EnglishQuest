ZONA_ID = "zona23"
ZONA_NOMBRE = "A1 — La Casa"

SECCIONES = {
    "s1": {
        "nombre": "Habitaciones y partes",
        "rango": "15 palabras",
        "palabras": [
            ("house", "jáus", "casa"),
            ("kitchen", "kíchen", "cocina"),
            ("bedroom", "bédrum", "dormitorio"),
            ("bathroom", "bázrum", "baño"),
            ("living room", "líving rum", "sala"),
            ("dining room", "dáining rum", "comedor"),
            ("garden", "gárden", "jardín"),
            ("garage", "garách", "garaje"),
            ("roof", "ruf", "techo"),
            ("wall", "uól", "pared"),
            ("floor", "flor", "piso"),
            ("stairs", "stérs", "escaleras"),
            ("yard", "yard", "patio"),
            ("basement", "béismant", "sótano"),
            ("closet", "clóset", "clóset / armario")
        ]
    }
}
ORDEN_SECCIONES = ["s1"]

def obtener_todas_las_palabras():
    return SECCIONES["s1"]["palabras"]

TEORIA = {
    "titulo": "La Casa y sus Habitaciones (A1)",
    "explicacion": "Diferencias importantes de concepto.\n\n• 'House' es la construcción física, mientras que 'home' es el hogar (el concepto emocional).\n• Fíjate en 'living room' (sala), que literalmente significa 'cuarto para vivir'.",
    "tabla": [
        {"en": "house", "pron": "jáus", "es": "casa"},
        {"en": "kitchen", "pron": "kíchen", "es": "cocina"},
        {"en": "bedroom", "pron": "bédrum", "es": "dormitorio"},
        {"en": "bathroom", "pron": "bázrum", "es": "baño"},
        {"en": "living room", "pron": "líving rum", "es": "sala"},
        {"en": "dining room", "pron": "dáining rum", "es": "comedor"},
        {"en": "garden", "pron": "gárden", "es": "jardín"},
        {"en": "garage", "pron": "garách", "es": "garaje"},
        {"en": "roof", "pron": "ruf", "es": "techo"},
        {"en": "wall", "pron": "uól", "es": "pared"},
        {"en": "floor", "pron": "flor", "es": "piso"},
        {"en": "stairs", "pron": "stérs", "es": "escaleras"},
        {"en": "yard", "pron": "yard", "es": "patio"},
        {"en": "basement", "pron": "béismant", "es": "sótano"},
        {"en": "closet", "pron": "clóset", "es": "clóset / armario"}
    ]
}