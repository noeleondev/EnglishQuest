ZONA_ID = "zona45"
ZONA_NOMBRE = "A2 — Futuro (Going to / Will)"

EJERCICIOS = [
    ("I ___ (visit) my grandmother this weekend. (plan)", ["will visit", "am going to visit", "visit", "visiting"], "am going to visit", "Voy a visitar a mi abuela este fin de semana.", "I am going to visit my grandmother this weekend."),
    ("She ___ (not/travel) next month. (plan)", ["won't travel", "isn't going to travel", "doesn't travel", "not travel"], "isn't going to travel", "Ella no va a viajar el próximo mes.", "She isn't going to travel next month."),
    ("I ___ (call) you tomorrow. (promesa)", ["am going to call", "will call", "call", "called"], "will call", "Te llamaré mañana.", "I will call you tomorrow."),
    ("It ___ (rain) tonight. (predicción)", ["is going to rain", "will rain", "rains", "raining"], "will rain", "Lloverá esta noche.", "It will rain tonight."),
    ("___ you ___ (help) me with this? (ofrecimiento)", ["Are / going to help", "Will / help", "Do / help", "Did / help"], "Will / help", "¿Me ayudarás con esto?", "Will you help me with this?"),
    ("We ___ (buy) a new house next year. (plan)", ["will buy", "are going to buy", "buy", "bought"], "are going to buy", "Vamos a comprar una casa nueva el próximo año.", "We are going to buy a new house next year.")
]

def obtener_todos_los_ejercicios():
    return EJERCICIOS

TEORIA = {
    "titulo": "El Futuro: Going to vs Will (A2)",
    "explicacion": "Ambos se usan para el futuro, pero tienen matices distintos.\n\n• 'Going to': Se usa para planes e intenciones ya decididas antes de hablar (I am going to travel).\n• 'Will': Se usa para decisiones espontáneas, promesas, ofrecimientos y predicciones (I will help you).",
    "tabla": [
        {"en": "I will call", "pron": "ái uíl col", "es": "Yo llamaré"},
        {"en": "She is going to travel", "pron": "shi is góuing tu trável", "es": "Ella va a viajar"},
        {"en": "Will you help?", "pron": "uíl iú jelp?", "es": "¿Me ayudarás?"}
    ]
}