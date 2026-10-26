ZONA_ID = "zona33"
ZONA_NOMBRE = "A1 — Can / Can't"

EJERCICIOS = [
    ("I ___ speak English.", ["can", "can't", "cans", "canned"], "can", "Yo puedo hablar inglés.", "I can speak English."),
    ("She ___ swim. (negativo)", ["can", "can't", "not can", "don't can"], "can't", "Ella no sabe nadar.", "She can't swim."),
    ("___ you cook Italian food?", ["Can", "Do", "Are", "Is"], "Can", "¿Puedes cocinar comida italiana?", "Can you cook Italian food?"),
    ("They ___ drive a car; they are too young. (negativo)", ["can", "can't", "don't", "aren't"], "can't", "Ellos no pueden conducir un carro; son muy jóvenes.", "They can't drive a car; they are too young."),
    ("He ___ play the guitar very well.", ["can", "can't", "cans", "is can"], "can", "Él sabe tocar la guitarra muy bien.", "He can play the guitar very well."),
    ("___ I go to the bathroom?", ["Can", "Do", "Am", "Is"], "Can", "¿Puedo ir al baño? (permiso)", "Can I go to the bathroom?")
]

def obtener_todos_los_ejercicios():
    return EJERCICIOS

TEORIA = {
    "titulo": "Can / Can't (A1)",
    "explicacion": "Habilidad o permiso.\n\n• Se usa para expresar habilidad (saber hacer algo) o pedir permiso.\n• Es un verbo modal, por lo que el verbo que lo acompaña siempre va en forma base (sin 'to').\n• Su negativo es 'cannot' o su contracción 'can't'.",
    "tabla": [
        {"en": "I can", "pron": "ái can", "es": "Yo puedo"},
        {"en": "You can", "pron": "iú can", "es": "Tú puedes"},
        {"en": "He can", "pron": "ji can", "es": "Él puede"},
        {"en": "I can't", "pron": "ái cant", "es": "Yo no puedo"},
        {"en": "Can you?", "pron": "can iú?", "es": "¿Puedes tú?"}
    ]
}