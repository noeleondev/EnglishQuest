ZONA_ID = "zona41"
ZONA_NOMBRE = "A2 — Pasatiempos y Deportes"

SECCIONES = {
    "s1": {
        "nombre": "Tiempo libre y actividades",
        "rango": "15 palabras",
        "palabras": [
            ("soccer", "sóker", "fútbol"),
            ("basketball", "básketbol", "baloncesto"),
            ("swimming", "suíming", "natación"),
            ("running", "róning", "correr (actividad)"),
            ("dancing", "dánsing", "bailar (actividad)"),
            ("painting", "péinting", "pintar (actividad)"),
            ("singing", "sínguing", "cantar (actividad)"),
            ("reading", "ríding", "leer (actividad)"),
            ("cooking", "kúking", "cocinar (actividad)"),
            ("fishing", "fishing", "pescar (actividad)"),
            ("hiking", "jáiking", "senderismo"),
            ("cycling", "sáikling", "ciclismo"),
            ("photography", "fotógrafi", "fotografía"),
            ("gardening", "gárdening", "jardinería"),
            ("video games", "vídeo guéims", "videojuegos")
        ]
    }
}
ORDEN_SECCIONES = ["s1"]

def obtener_todas_las_palabras():
    return SECCIONES["s1"]["palabras"]

TEORIA = {
    "titulo": "Pasatiempos y Deportes (A2)",
    "explicacion": "Para hablar de lo que te gusta hacer en tu tiempo libre.\n\n• Fíjate que muchas actividades terminan en <span style='color:#00d4ff;'><b>-ing</b></span> cuando se usan como sustantivos (Swimming = la natación).\n• 'Soccer' es fútbol en inglés americano, mientras que en británico se dice 'football'.",
    "tabla": [
        {"en": "soccer", "pron": "sóker", "es": "fútbol"},
        {"en": "basketball", "pron": "básketbol", "es": "baloncesto"},
        {"en": "swimming", "pron": "suíming", "es": "natación"},
        {"en": "running", "pron": "róning", "es": "correr (actividad)"},
        {"en": "dancing", "pron": "dánsing", "es": "bailar (actividad)"},
        {"en": "painting", "pron": "péinting", "es": "pintar (actividad)"},
        {"en": "singing", "pron": "sínguing", "es": "cantar (actividad)"},
        {"en": "reading", "pron": "ríding", "es": "leer (actividad)"},
        {"en": "cooking", "pron": "kúking", "es": "cocinar (actividad)"},
        {"en": "fishing", "pron": "fishing", "es": "pescar (actividad)"},
        {"en": "hiking", "pron": "jáiking", "es": "senderismo"},
        {"en": "cycling", "pron": "sáikling", "es": "ciclismo"},
        {"en": "photography", "pron": "fotógrafi", "es": "fotografía"},
        {"en": "gardening", "pron": "gárdening", "es": "jardinería"},
        {"en": "video games", "pron": "vídeo guéims", "es": "videojuegos"}
    ]
}