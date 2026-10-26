ZONA_ID = "zona48"
ZONA_NOMBRE = "A2 — Adverbios de Modo (-ly)"

EJERCICIOS = [
    ("She sings ___ (beautiful).", ["beautiful", "beautifully", "beautifuly", "more beautiful"], "beautifully", "Ella canta bellamente.", "She sings beautifully."),
    ("He runs very ___ (fast).", ["fast", "fastly", "faster", "fastest"], "fast", "Él corre muy rápido.", "He runs very fast."),
    ("They worked ___ on the project. (hard)", ["hard", "hardly", "harder", "hardest"], "hard", "Ellos trabajaron duro en el proyecto.", "They worked hard on the project."),
    ("She answered the question ___ (easy).", ["easy", "easily", "easyly", "more easy"], "easily", "Ella respondió la pregunta fácilmente.", "She answered the question easily."),
    ("He speaks very ___ (quiet).", ["quiet", "quietly", "quieter", "quietest"], "quietly", "Él habla muy tranquilamente.", "He speaks very quietly."),
    ("She drives very ___ (careful).", ["careful", "carefully", "carefuly", "more careful"], "carefully", "Ella conduce con mucho cuidado.", "She drives very carefully.")
]

def obtener_todos_los_ejercicios():
    return EJERCICIOS

TEORIA = {
    "titulo": "Adverbios de Modo (A2)",
    "explicacion": "Describen cómo se realiza una acción. Generalmente se forman agregando <span style='color:#00d4ff;'><b>-ly</b></span> al adjetivo (slow -> slowly).\n\n• Si el adjetivo termina en '-y', cambia a '-ily' (easy -> easily).\n• Si termina en '-le', se cambia a '-ly' (terrible -> terribly).\n• Irregulares: good -> well, fast -> fast, hard -> hard.",
    "tabla": [
        {"en": "Slowly", "pron": "slóuli", "es": "Lentamente"},
        {"en": "Easily", "pron": "ísili", "es": "Fácilmente"},
        {"en": "Well", "pron": "uel", "es": "Bien (de good)"},
        {"en": "Fast", "pron": "fast", "es": "Rápidamente (no cambia)"},
        {"en": "Hard", "pron": "jard", "es": "Duro (no cambia)"}
    ]
}