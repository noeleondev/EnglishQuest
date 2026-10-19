ZONA_ID = "gramatica6"
ZONA_NOMBRE = "Gramática — Preguntas con To Be"

EJERCICIOS = [
    ("___ is your name? (qué)", ["What", "Who", "Where", "When"], "What", "¿Cuál es tu nombre?", "What is your name?"),
    ("___ are you from? (dónde)", ["What", "Who", "Where", "When"], "Where", "¿De dónde eres?", "Where are you from?"),
    ("___ is that woman? (quién)", ["What", "Who", "Where", "When"], "Who", "¿Quién es esa mujer?", "Who is that woman?"),
    ("___ is your birthday? (cuándo)", ["What", "Who", "Where", "When"], "When", "¿Cuándo es tu cumpleaños?", "When is your birthday?"),
    ("___ are you sad? (por qué)", ["Why", "How", "Which", "Who"], "Why", "¿Por qué estás triste?", "Why are you sad?"),
    ("___ is your mother? (cómo)", ["Why", "How", "Which", "Who"], "How", "¿Cómo está tu madre?", "How is your mother?")
]

TEORIA = {
    "titulo": "Preguntas con el Verbo To Be",
    "explicacion": "🌟 Para hacer preguntas en inglés, primero va la palabra interrogativa (Wh-) y luego el verbo To Be.\n\n⚙️ Fórmula: **Wh- + To Be + Sujeto + ?**\n\n• What is this? (¿Qué es esto?)\n• Where are you? (¿Dónde estás?)\n• Who is she? (¿Quién es ella?)\n• When is the party? (¿Cuándo es la fiesta?)\n• Why is he crying? (¿Por qué está llorando?)\n• How are you? (¿Cómo estás?)\n\n💡 Fíjate que 'What is your name?' se traduce como '¿Cómo te llamas?', pero literalmente es '¿Qué es tu nombre?'. Es la forma correcta en inglés.",
    "tabla": [
        {"en": "What", "pron": "uát", "es": "Qué"},
        {"en": "Who", "pron": "ju", "es": "Quién"},
        {"en": "Where", "pron": "uérd", "es": "Dónde"},
        {"en": "When", "pron": "uén", "es": "Cuándo"},
        {"en": "Why", "pron": "uái", "es": "Por qué"},
        {"en": "How", "pron": "jáu", "es": "Cómo"}
    ]
}

def obtener_todos_los_ejercicios():
    return EJERCICIOS