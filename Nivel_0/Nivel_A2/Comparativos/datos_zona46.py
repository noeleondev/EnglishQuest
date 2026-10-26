ZONA_ID = "zona46"
ZONA_NOMBRE = "A2 — Comparativos y Superlativos"

EJERCICIOS = [
    ("This bag is ___ (cheap) than that one.", ["cheap", "cheaper", "the cheapest", "more cheap"], "cheaper", "Esta bolsa es más barata que esa.", "This bag is cheaper than that one."),
    ("She is the ___ (tall) student in the class.", ["tall", "taller", "tallest", "most tall"], "tallest", "Ella es la estudiante más alta de la clase.", "She is the tallest student in the class."),
    ("My cooking is ___ (bad) than my mother's.", ["bad", "worse", "the worst", "badder"], "worse", "Mi cocina es peor que la de mi madre.", "My cooking is worse than my mother's."),
    ("This is the ___ (good) restaurant in town.", ["good", "better", "best", "goodest"], "best", "Este es el mejor restaurante de la ciudad.", "This is the best restaurant in town."),
    ("The train is ___ (fast) than the bus.", ["fast", "faster", "fastest", "more fast"], "faster", "El tren es más rápido que el autobús.", "The train is faster than the bus."),
    ("This is the most ___ (expensive) hotel in the city.", ["expensive", "expensiver", "expensivest", "more expensive"], "expensive", "Este es el hotel más caro de la ciudad.", "This is the most expensive hotel in the city.")
]

def obtener_todos_los_ejercicios():
    return EJERCICIOS

TEORIA = {
    "titulo": "Comparativos y Superlativos (A2)",
    "explicacion": "Se usan para comparar dos o más cosas.\n\n• Comparativo (más... que): Adjetivos cortos agregan <span style='color:#00d4ff;'><b>-er</b></span> (taller). Adjetivos largos usan 'more' (more expensive).\n• Superlativo (el más...): Adjetivos cortos agregan <span style='color:#00d4ff;'><b>-est</b></span> (the tallest). Adjetivos largos usan 'the most' (the most expensive).\n• Irregulares: good -> better -> the best. bad -> worse -> the worst.",
    "tabla": [
        {"en": "Taller than", "pron": "tóler dan", "es": "Más alto que"},
        {"en": "The tallest", "pron": "de tólest", "es": "El más alto"},
        {"en": "Better", "pron": "béter", "es": "Mejor"},
        {"en": "The best", "pron": "de best", "es": "El mejor"}
    ]
}