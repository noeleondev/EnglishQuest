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