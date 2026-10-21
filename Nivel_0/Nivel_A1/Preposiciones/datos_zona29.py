ZONA_ID = "zona29"
ZONA_NOMBRE = "A1 — Preposiciones y Adverbios"

SECCIONES = {
    "s1": {
        "nombre": "Lugar y Frecuencia",
        "rango": "15 palabras",
        "palabras": [
            ("in", "in", "dentro de / en"),
            ("on", "on", "sobre / encima de"),
            ("under", "ónder", "debajo de"),
            ("next to", "nekst tu", "al lado de"),
            ("between", "bituín", "entre"),
            ("behind", "bijáind", "detrás de"),
            ("in front of", "in front of", "delante de"),
            ("always", "ólueis", "siempre"),
            ("usually", "iúshuali", "usualmente"),
            ("often", "ófen", "frecuentemente"),
            ("sometimes", "sómtaims", "a veces"),
            ("never", "néver", "nunca"),
            ("here", "jir", "aquí"),
            ("there", "der", "allí"),
            ("everywhere", "évriuer", "en todas partes")
        ]
    }
}
ORDEN_SECCIONES = ["s1"]

def obtener_todas_las_palabras():
    return SECCIONES["s1"]["palabras"]

TEORIA = {
    "titulo": "Preposiciones y Adverbios (A1)",
    "explicacion": "Las preposiciones de lugar indican dónde está algo (in, on, under). Los adverbios de frecuencia indican cada cuánto ocurre algo (always, never). 'In front of' es una frase de tres palabras.",
    "tabla": [
        {"en": "in", "pron": "in", "es": "dentro de / en"},
        {"en": "on", "pron": "on", "es": "sobre / encima de"},
        {"en": "under", "pron": "ónder", "es": "debajo de"},
        {"en": "next to", "pron": "nekst tu", "es": "al lado de"},
        {"en": "between", "pron": "bituín", "es": "entre"},
        {"en": "behind", "pron": "bijáind", "es": "detrás de"},
        {"en": "in front of", "pron": "in front of", "es": "delante de"},
        {"en": "always", "pron": "ólueis", "es": "siempre"},
        {"en": "usually", "pron": "iúshuali", "es": "usualmente"},
        {"en": "often", "pron": "ófen", "es": "frecuentemente"},
        {"en": "sometimes", "pron": "sómtaims", "es": "a veces"},
        {"en": "never", "pron": "néver", "es": "nunca"},
        {"en": "here", "pron": "jir", "es": "aquí"},
        {"en": "there", "pron": "der", "es": "allí"},
        {"en": "everywhere", "pron": "évriuer", "es": "en todas partes"}
    ]
}