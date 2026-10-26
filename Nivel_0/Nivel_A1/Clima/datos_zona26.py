ZONA_ID = "zona26"
ZONA_NOMBRE = "A1 — El Clima"

SECCIONES = {
    "s1": {
        "nombre": "El tiempo atmosférico",
        "rango": "10 palabras",
        "palabras": [
            ("sunny", "sóni", "soleado"),
            ("rainy", "réini", "lluvioso"),
            ("cloudy", "cláudi", "nublado"),
            ("windy", "uíndi", "ventoso"),
            ("snowy", "snóui", "nevado"),
            ("hot", "jot", "caluroso"),
            ("cold", "cóuld", "frío"),
            ("storm", "storm", "tormenta"),
            ("rainbow", "réinbou", "arcoíris"),
            ("temperature", "témperachur", "temperatura")
        ]
    }
}
ORDEN_SECCIONES = ["s1"]

def obtener_todas_las_palabras():
    return SECCIONES["s1"]["palabras"]

TEORIA = {
    "titulo": "El Clima en Inglés (A1)",
    "explicacion": "Sufijos y sonidos suaves.\n\n• Para describir el clima, casi siempre usamos la terminación '-y' (sunny, rainy).\n• La palabra 'weather' (clima) suena como 'uérder', con la 'th' suave.",
    "tabla": [
        {"en": "sunny", "pron": "sóni", "es": "soleado"},
        {"en": "rainy", "pron": "réini", "es": "lluvioso"},
        {"en": "cloudy", "pron": "cláudi", "es": "nublado"},
        {"en": "windy", "pron": "uíndi", "es": "ventoso"},
        {"en": "snowy", "pron": "snóui", "es": "nevado"},
        {"en": "hot", "pron": "jot", "es": "caluroso"},
        {"en": "cold", "pron": "cóuld", "es": "frío"},
        {"en": "storm", "pron": "storm", "es": "tormenta"},
        {"en": "rainbow", "pron": "réinbou", "es": "arcoíris"},
        {"en": "temperature", "pron": "témperachur", "es": "temperatura"}
    ]
}