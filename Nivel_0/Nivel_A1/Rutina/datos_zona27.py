ZONA_ID = "zona27"
ZONA_NOMBRE = "A1 — Rutina Diaria"

SECCIONES = {
    "s1": {
        "nombre": "Acciones y momentos del día",
        "rango": "15 palabras/frases",
        "palabras": [
            ("morning", "mórnin", "mañana"),
            ("afternoon", "afternún", "tarde"),
            ("evening", "ívnin", "noche (temprano)"),
            ("night", "náit", "noche"),
            ("today", "tudéi", "hoy"),
            ("tomorrow", "tumórou", "mañana (día siguiente)"),
            ("yesterday", "iésterdei", "ayer"),
            ("wake up", "uéik op", "despertarse"),
            ("get up", "get op", "levantarse"),
            ("take a shower", "téik a sháuer", "ducharse"),
            ("get dressed", "get drest", "vestirse"),
            ("go to work", "góu tu uérk", "ir al trabajo"),
            ("go to school", "góu tu skul", "ir a la escuela"),
            ("go to bed", "góu tu bed", "irse a dormir"),
            ("have breakfast", "jav brékfast", "desayunar")
        ]
    }
}
ORDEN_SECCIONES = ["s1"]

def obtener_todas_las_palabras():
    return SECCIONES["s1"]["palabras"]

TEORIA = {
    "titulo": "La Rutina Diaria (A1)",
    "explicacion": "Aquí usamos verbos compuestos (phrasal verbs) muy comunes. Fíjate que 'wake up' (despertarse) es diferente de 'get up' (levantarse de la cama). La 'h' en 'have breakfast' se pronuncia como 'j' suave.",
    "tabla": [
        {"en": "morning", "pron": "mórnin", "es": "mañana"},
        {"en": "afternoon", "pron": "afternún", "es": "tarde"},
        {"en": "evening", "pron": "ívnin", "es": "noche (temprano)"},
        {"en": "night", "pron": "náit", "es": "noche"},
        {"en": "today", "pron": "tudéi", "es": "hoy"},
        {"en": "tomorrow", "pron": "tumórou", "es": "mañana (día siguiente)"},
        {"en": "yesterday", "pron": "iésterdei", "es": "ayer"},
        {"en": "wake up", "pron": "uéik op", "es": "despertarse"},
        {"en": "get up", "pron": "get op", "es": "levantarse"},
        {"en": "take a shower", "pron": "téik a sháuer", "es": "ducharse"},
        {"en": "get dressed", "pron": "get drest", "es": "vestirse"},
        {"en": "go to work", "pron": "góu tu uérk", "es": "ir al trabajo"},
        {"en": "go to school", "pron": "góu tu skul", "es": "ir a la escuela"},
        {"en": "go to bed", "pron": "góu tu bed", "es": "irse a dormir"},
        {"en": "have breakfast", "pron": "jav brékfast", "es": "desayunar"}
    ]
}