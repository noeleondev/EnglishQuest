ZONA_ID = "zona22"
ZONA_NOMBRE = "A1 — Partes del Cuerpo"

SECCIONES = {
    "s1": {
        "nombre": "El cuerpo humano",
        "rango": "15 palabras",
        "palabras": [
            ("head", "jed", "cabeza"),
            ("hair", "jer", "cabello"),
            ("eyes", "áis", "ojos"),
            ("nose", "nóus", "nariz"),
            ("mouth", "máuz", "boca"),
            ("ear", "ir", "oreja"),
            ("face", "féis", "cara"),
            ("neck", "nek", "cuello"),
            ("arm", "arm", "brazo"),
            ("hand", "jand", "mano"),
            ("finger", "fínguer", "dedo (de la mano)"),
            ("leg", "leg", "pierna"),
            ("foot", "fut", "pie"),
            ("knee", "ni", "rodilla"),
            ("stomach", "stómak", "estómago")
        ]
    }
}
ORDEN_SECCIONES = ["s1"]

def obtener_todas_las_palabras():
    return SECCIONES["s1"]["palabras"]

TEORIA = {
    "titulo": "El Cuerpo Humano (A1)",
    "explicacion": "La 'h' en 'head', 'hair' y 'hand' se pronuncia como una 'j' suave (aspirada). El plural de 'foot' (pie) es irregular: se dice 'feet'.",
    "tabla": [
        {"en": "head", "pron": "jed", "es": "cabeza"},
        {"en": "hair", "pron": "jer", "es": "cabello"},
        {"en": "eyes", "pron": "áis", "es": "ojos"},
        {"en": "nose", "pron": "nóus", "es": "nariz"},
        {"en": "mouth", "pron": "máuz", "es": "boca"},
        {"en": "ear", "pron": "ir", "es": "oreja"},
        {"en": "face", "pron": "féis", "es": "cara"},
        {"en": "neck", "pron": "nek", "es": "cuello"},
        {"en": "arm", "pron": "arm", "es": "brazo"},
        {"en": "hand", "pron": "jand", "es": "mano"},
        {"en": "finger", "pron": "fínguer", "es": "dedo (de la mano)"},
        {"en": "leg", "pron": "leg", "es": "pierna"},
        {"en": "foot", "pron": "fut", "es": "pie"},
        {"en": "knee", "pron": "ni", "es": "rodilla"},
        {"en": "stomach", "pron": "stómak", "es": "estómago"}
    ]
}