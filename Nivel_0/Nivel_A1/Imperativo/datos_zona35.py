ZONA_ID = "zona35"
ZONA_NOMBRE = "A1 — El Imperativo"

EJERCICIOS = [
    ("___ the door, please. (cerrar)", ["Close", "Closes", "Closing", "To close"], "Close", "Cierra la puerta, por favor.", "Close the door, please."),
    ("___ touch that! (negativo)", ["No", "Don't", "Not", "Doesn't"], "Don't", "¡No toques eso!", "Don't touch that!"),
    ("___ down, please. (sentarse)", ["Sit", "Sits", "Sitting", "To sit"], "Sit", "Siéntate, por favor.", "Sit down, please."),
    ("___ be late for class. (negativo)", ["No", "Don't", "Not", "Doesn't"], "Don't", "No llegues tarde a clase.", "Don't be late for class."),
    ("___ your homework now. (hacer)", ["Do", "Does", "Doing", "To do"], "Do", "Haz tu tarea ahora.", "Do your homework now."),
    ("___ noise in the library. (negativo)", ["No make", "Don't make", "Not make", "Doesn't make"], "Don't make", "No hagas ruido en la biblioteca.", "Don't make noise in the library.")
]

def obtener_todos_los_ejercicios():
    return EJERCICIOS

TEORIA = {
    "titulo": "El Imperativo (A1)",
    "explicacion": "Órdenes, instrucciones y consejos.\n\n• Se forma usando el verbo en su forma base SIN el 'to' y sin sujeto (ej. 'Open the door').\n• Para negar, solo agregamos 'Don't' al principio (ej. 'Don't open').\n• Es muy útil para dar direcciones o instrucciones en clase.",
    "tabla": [
        {"en": "Open", "pron": "óupen", "es": "Abre"},
        {"en": "Close", "pron": "clóus", "es": "Cierra"},
        {"en": "Sit down", "pron": "sit dáun", "es": "Siéntate"},
        {"en": "Don't touch", "pron": "dount tách", "es": "No toques"},
        {"en": "Please, wait", "pron": "plis, uéit", "es": "Por favor, espera"}
    ]
}