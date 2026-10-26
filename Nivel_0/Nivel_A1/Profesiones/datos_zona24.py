ZONA_ID = "zona24"
ZONA_NOMBRE = "A1 — Profesiones"

SECCIONES = {
    "s1": {
        "nombre": "Trabajos y ocupaciones",
        "rango": "15 palabras",
        "palabras": [
            ("teacher", "tícher", "maestro/a"),
            ("doctor", "dóctor", "doctor/a"),
            ("nurse", "ners", "enfermero/a"),
            ("engineer", "enllinír", "ingeniero/a"),
            ("lawyer", "lóller", "abogado/a"),
            ("police officer", "polís ófiser", "policía"),
            ("firefighter", "fáirfaiter", "bombero/a"),
            ("chef", "chef", "chef / cocinero"),
            ("waiter", "uéiter", "mesero"),
            ("driver", "dráiver", "conductor/a"),
            ("farmer", "fármer", "agricultor/a"),
            ("student", "stúdent", "estudiante"),
            ("dentist", "déntist", "dentista"),
            ("artist", "ártist", "artista"),
            ("singer", "sínguer", "cantante")
        ]
    }
}
ORDEN_SECCIONES = ["s1"]

def obtener_todas_las_palabras():
    return SECCIONES["s1"]["palabras"]

TEORIA = {
    "titulo": "Las Profesiones en Inglés (A1)",
    "explicacion": "Sufijos y pronunciación.\n\n• Muchas profesiones terminan en '-er' o '-or' (teacher, doctor).\n• 'Chef' es una palabra francesa adoptada, por eso se pronuncia igual que en español.\n• 'Police officer' es el término moderno para no especificar género.",
    "tabla": [
        {"en": "teacher", "pron": "tícher", "es": "maestro/a"},
        {"en": "doctor", "pron": "dóctor", "es": "doctor/a"},
        {"en": "nurse", "pron": "ners", "es": "enfermero/a"},
        {"en": "engineer", "pron": "enllinír", "es": "ingeniero/a"},
        {"en": "lawyer", "pron": "lóller", "es": "abogado/a"},
        {"en": "police officer", "pron": "polís ófiser", "es": "policía"},
        {"en": "firefighter", "pron": "fáirfaiter", "es": "bombero/a"},
        {"en": "chef", "pron": "chef", "es": "chef / cocinero"},
        {"en": "waiter", "pron": "uéiter", "es": "mesero"},
        {"en": "driver", "pron": "dráiver", "es": "conductor/a"},
        {"en": "farmer", "pron": "fármer", "es": "agricultor/a"},
        {"en": "student", "pron": "stúdent", "es": "estudiante"},
        {"en": "dentist", "pron": "déntist", "es": "dentista"},
        {"en": "artist", "pron": "ártist", "es": "artista"},
        {"en": "singer", "pron": "sínguer", "es": "cantante"}
    ]
}