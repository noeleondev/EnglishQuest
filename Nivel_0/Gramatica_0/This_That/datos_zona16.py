ZONA_ID = "gramatica5"
ZONA_NOMBRE = "Gramática — This / That / These / Those"

EJERCICIOS = [
    ("___ is my pen. (cerca, singular)", ["This", "That", "These", "Those"], "This", "Este es mi bolígrafo.", "This is my pen."),
    ("___ is your car. (lejos, singular)", ["This", "That", "These", "Those"], "That", "Ese es tu carro.", "That is your car."),
    ("___ are my books. (cerca, plural)", ["This", "That", "These", "Those"], "These", "Estos son mis libros.", "These are my books."),
    ("___ are her shoes. (lejos, plural)", ["This", "That", "These", "Those"], "Those", "Esos son sus zapatos.", "Those are her shoes."),
    ("___ is a good book. (cerca)", ["This", "That", "These", "Those"], "This", "Este es un buen libro.", "This is a good book."),
    ("___ are my friends. (cerca)", ["This", "That", "These", "Those"], "These", "Estos son mis amigos.", "These are my friends.")
]

TEORIA = {
    "titulo": "Demostrativos: This / That / These / Those",
    "explicacion": "🌟 Sirven para señalar cosas dependiendo de dos factores: **Distancia** (cerca o lejos) y **Cantidad** (singular o plural).\n\n⚙️ Las 4 combinaciones:\n\n• **This** (Este/Esta) → Cerca + Singular. Ej: This book (este libro).\n• **That** (Ese/Esa) → Lejos + Singular. Ej: That car (ese carro).\n• **These** (Estos/Estas) → Cerca + Plural. Ej: These books (estos libros).\n• **Those** (Esos/Esas) → Lejos + Plural. Ej: Those cars (esos carros).\n\n💡 Tip: This y These llevan 'T-H-I' (la 'i' es chiquita, como algo cerca). That y Those llevan 'T-H-A' (la 'a' es abierta, como algo lejano).",
    "tabla": [
        {"en": "This", "pron": "dis", "es": "Este / Esta (cerca)"},
        {"en": "That", "pron": "dat", "es": "Ese / Esa (lejos)"},
        {"en": "These", "pron": "diis", "es": "Estos / Estas (cerca)"},
        {"en": "Those", "pron": "dous", "es": "Esos / Esas (lejos)"}
    ]
}

def obtener_todos_los_ejercicios():
    return EJERCICIOS