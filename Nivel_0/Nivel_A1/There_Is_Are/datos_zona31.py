ZONA_ID = "zona31"
ZONA_NOMBRE = "A1 — There is / There are"

EJERCICIOS = [
    ("___ a book on the table.", ["There is", "There are", "It is", "They are"], "There is", "Hay un libro en la mesa.", "There is a book on the table."),
    ("___ five rooms in the house.", ["There is", "There are", "It is", "They are"], "There are", "Hay cinco habitaciones en la casa.", "There are five rooms in the house."),
    ("___ there any eggs in the fridge?", ["Is", "Are", "Do", "Does"], "Are", "¿Hay huevos en el refrigerador?", "Are there any eggs in the fridge?"),
    ("There ___ any milk.", ["is not", "are not", "do not", "does not"], "is not", "No hay leche.", "There is not any milk."),
    ("There ___ a cat in the garden.", ["is", "are", "am", "be"], "is", "Hay un gato en el jardín.", "There is a cat in the garden.")
]

def obtener_todos_los_ejercicios():
    return EJERCICIOS

TEORIA = {
    "titulo": "There is / There are (A1)",
    "explicacion": "El equivalente a 'Hay'.\n\n• Usamos 'There is' para singular (una cosa).\n• Usamos 'There are' para plural (varias cosas).\n• Es muy común usarlo para describir lugares.",
    "tabla": [
        {"en": "There is a book", "pron": "der is a buk", "es": "Hay un libro"},
        {"en": "There are books", "pron": "der ar buks", "es": "Hay libros"},
        {"en": "Is there...?", "pron": "is der...?", "es": "¿Hay...? (singular)"},
        {"en": "Are there...?", "pron": "ar der...?", "es": "¿Hay...? (plural)"}
    ]
}