"""
DATOS DE LA ZONA 6: SALUDOS Y DESPEDIDAS
Fuente: "Inglés desde Cero - Nivel 0 al C2" (Mr. León), páginas 11-12
Estructura: 2 secciones + Jefe de Zona
"""

ZONA_ID = "zona6"
ZONA_NOMBRE = "Zona 6 — Saludos y despedidas"

SECCIONES = {
    "s1": {
        "nombre": "S1 — Saludos básicos",
        "rango": "9 frases",
        "palabras": [
            ("Hello",            "jelóu",       "hola"),
            ("Hi",               "jái",         "hola (informal)"),
            ("Good morning",     "gud mórnin",  "buenos días"),
            ("Good afternoon",   "gud afternún","buenas tardes"),
            ("Good evening",     "gud ívnin",   "buenas noches (al llegar)"),
            ("Good night",       "gud náit",    "buenas noches (al despedirse)"),
            ("Goodbye",          "gudbái",      "adiós"),
            ("See you later",    "si iu léiter", "nos vemos luego"),
            ("How are you?",     "jáu ar iu",   "¿cómo estás?"),
        ],
    },
    "s2": {
        "nombre": "S2 — Cortesía y presentación",
        "rango": "8 frases",
        "palabras": [
            ("I am fine, thank you", "ái am fáin, zenk iu", "estoy bien, gracias"),
            ("Please",               "plis",                "por favor"),
            ("Thank you",            "zenk iu",             "gracias"),
            ("You are welcome",      "iu ar uélcom",        "de nada"),
            ("Excuse me",            "exkiús mi",           "disculpe"),
            ("I am sorry",           "ái am sóri",          "lo siento"),
            ("What is your name?",   "uát is iór néim",     "¿cómo te llamas?"),
            ("My name is...",        "mái néim is",         "mi nombre es..."),
            ("Nice to meet you",     "náis tu mit iu",      "mucho gusto"),
        ],
    },
}

ORDEN_SECCIONES = ["s1", "s2"]


def obtener_todas_las_palabras():
    todas = []
    for sid in ORDEN_SECCIONES:
        todas.extend(SECCIONES[sid]["palabras"])
    return todas

TEORIA = {
    "titulo": "Saludos y Despedidas (Greetings)",
    "explicacion": "En inglés, la hora del día determina el saludo. 'Good morning' se usa antes del mediodía, 'Good afternoon' de mediodía a 6 pm, y 'Good evening' después de 6 pm. Para despedirte por la noche dices 'Good night'. 'How are you?' es la pregunta estándar.",
    "tabla": [
        {"en": "Hello", "pron": "jelóu", "es": "hola"},
        {"en": "Good morning", "pron": "gud mórnin", "es": "buenos días"},
        {"en": "Good afternoon", "pron": "gud afternún", "es": "buenas tardes"},
        {"en": "Good evening", "pron": "gud ívnin", "es": "buenas noches (al llegar)"},
        {"en": "Good night", "pron": "gud náit", "es": "buenas noches (al despedirse)"},
        {"en": "How are you?", "pron": "jáu ar iu", "es": "¿cómo estás?"},
        {"en": "Please", "pron": "plis", "es": "por favor"},
        {"en": "Thank you", "pron": "zenk iu", "es": "gracias"},
        {"en": "Nice to meet you", "pron": "náis tu mit iu", "es": "mucho gusto"}
    ]
}