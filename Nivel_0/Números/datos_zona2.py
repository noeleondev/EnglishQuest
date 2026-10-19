ZONA_ID = "zona2"
ZONA_NOMBRE = "Zona 2 — Números (0 al 20)"

SECCIONES = {
    "s1": {
        "nombre": "Números Básicos",
        "rango": "0–20",
        "palabras": [
            ("zero", "zírou", "cero"),
            ("one", "uán", "uno"),
            ("two", "tu", "dos"),
            ("three", "zrí", "tres"),
            ("four", "for", "cuatro"),
            ("five", "fáiv", "cinco"),
            ("six", "siks", "seis"),
            ("seven", "séven", "siete"),
            ("eight", "éit", "ocho"),
            ("nine", "náin", "nueve"),
            ("ten", "ten", "diez"),
            ("eleven", "iléven", "once"),
            ("twelve", "tuélv", "doce"),
            ("thirteen", "zértin", "trece"),
            ("fourteen", "fórtin", "catorce"),
            ("fifteen", "fíftin", "quince"),
            ("sixteen", "síkstin", "dieciséis"),
            ("seventeen", "séventin", "diecisiete"),
            ("eighteen", "éitin", "dieciocho"),
            ("nineteen", "náintin", "diecinueve"),
            ("twenty", "tuénti", "veinte"),
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
    "titulo": "Los Números Básicos (0 al 20)",
    "explicacion": "Para empezar, debes dominar los números del 0 al 20. Del 13 al 19 terminan con '-teen' (como sixteen). En el siguiente nivel (A1) aprenderás las decenas y los números del 20 al 100.",
    "tabla": [
        {"en": "one", "pron": "uán", "es": "1"},
        {"en": "two", "pron": "tu", "es": "2"},
        {"en": "three", "pron": "zrí", "es": "3"},
        {"en": "four", "pron": "for", "es": "4"},
        {"en": "five", "pron": "fáiv", "es": "5"},
        {"en": "six", "pron": "siks", "es": "6"},
        {"en": "seven", "pron": "séven", "es": "7"},
        {"en": "eight", "pron": "éit", "es": "8"},
        {"en": "nine", "pron": "náin", "es": "9"},
        {"en": "ten", "pron": "ten", "es": "10"},
        {"en": "eleven", "pron": "iléven", "es": "11"},
        {"en": "twelve", "pron": "tuélv", "es": "12"},
        {"en": "thirteen", "pron": "zértin", "es": "13"},
        {"en": "fourteen", "pron": "fórtin", "es": "14"},
        {"en": "fifteen", "pron": "fíftin", "es": "15"},
        {"en": "sixteen", "pron": "síkstin", "es": "16"},
        {"en": "seventeen", "pron": "séventin", "es": "17"},
        {"en": "eighteen", "pron": "éitin", "es": "18"},
        {"en": "nineteen", "pron": "náintin", "es": "19"},
        {"en": "twenty", "pron": "tuénti", "es": "20"}
    ]
}