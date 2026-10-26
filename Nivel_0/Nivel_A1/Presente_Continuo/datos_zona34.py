ZONA_ID = "zona34"
ZONA_NOMBRE = "A1 — Presente Continuo"

EJERCICIOS = [
    ("I ___ reading a book.", ["am", "is", "are", "be"], "am", "Estoy leyendo un libro.", "I am reading a book."),
    ("She ___ cooking dinner.", ["am", "is", "are", "be"], "is", "Ella está cocinando la cena.", "She is cooking dinner."),
    ("They ___ not playing soccer.", ["am", "is", "are", "be"], "are", "Ellos no están jugando fútbol.", "They are not playing soccer."),
    ("___ you watching TV?", ["Am", "Is", "Are", "Be"], "Are", "¿Estás viendo la televisión?", "Are you watching TV?"),
    ("He ___ sleeping right now.", ["am", "is", "are", "be"], "is", "Él está durmiendo ahora mismo.", "He is sleeping right now."),
    ("We ___ studying English.", ["am", "is", "are", "be"], "are", "Nosotros estamos estudiando inglés.", "We are studying English.")
]

def obtener_todos_los_ejercicios():
    return EJERCICIOS

TEORIA = {
    "titulo": "El Presente Continuo (A1)",
    "explicacion": "Acciones en este preciso momento.\n\n• Se usa para acciones que están ocurriendo ahora mismo.\n• Se forma con el verbo 'to be' (am/is/are) + el verbo principal con terminación '-ing' (leyendo = reading).\n• Ejemplo: I am eating (Estoy comiendo).",
    "tabla": [
        {"en": "I am eating", "pron": "ái am íting", "es": "Estoy comiendo"},
        {"en": "She is running", "pron": "shi is róning", "es": "Ella está corriendo"},
        {"en": "They are playing", "pron": "déi ar pléiing", "es": "Ellos están jugando"},
        {"en": "Are you working?", "pron": "ar iú uérking?", "es": "¿Estás trabajando?"}
    ]
}