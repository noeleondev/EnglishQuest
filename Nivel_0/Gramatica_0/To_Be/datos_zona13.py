ZONA_ID = "gramatica2"
ZONA_NOMBRE = "Gramática — Verbo To Be"

# (oración_con_hueco, opciones, respuesta_correcta, traducción, oración_completa)
EJERCICIOS = [
    ("I ___ a student.", ["am", "is", "are", "be"], "am", "Yo soy un estudiante.", "I am a student."),
    ("She ___ my sister.", ["am", "is", "are", "be"], "is", "Ella es mi hermana.", "She is my sister."),
    ("They ___ my parents.", ["am", "is", "are", "be"], "are", "Ellos son mis padres.", "They are my parents."),
    ("He ___ not at home.", ["am", "is", "are", "be"], "is", "Él no está en casa.", "He is not at home."),
    ("___ you ready?", ["Am", "Is", "Are", "Be"], "Are", "¿Estás listo?", "Are you ready?"),
    ("It ___ a dog.", ["am", "is", "are", "be"], "is", "Eso es un perro.", "It is a dog."),
    ("We ___ happy.", ["am", "is", "are", "be"], "are", "Nosotros estamos felices.", "We are happy.")
]

TEORIA = {
    "titulo": "El Verbo 'To Be' (Ser o Estar)",
    "explicacion": "🌟 ¡El verbo más importante del inglés!\n\nEn español tenemos dos verbos: SER y ESTAR. En inglés, ambos se convierten en un solo verbo: 'To Be'. El significado depende del contexto.\n\n⚙️ Reglas rápidas:\n• I (yo) → **am** (I am happy = estoy feliz)\n• He/She/It → **is** (She is smart = ella es lista)\n• You/We/They → **are** (They are students = ellos son estudiantes)\n\n❌ Negativo: Solo agrega 'not' (I am not, She is not).\n❓ Pregunta: Invierte el orden (Are you...? Is he...?).",
    "tabla": [
        {"en": "I am", "pron": "ái am", "es": "Yo soy / estoy"},
        {"en": "You are", "pron": "iu ar", "es": "Tú eres / estás"},
        {"en": "He is", "pron": "ji is", "es": "Él es / está"},
        {"en": "She is", "pron": "shi is", "es": "Ella es / está"},
        {"en": "It is", "pron": "it is", "es": "Eso es / está"},
        {"en": "We are", "pron": "ui ar", "es": "Nosotros somos / estamos"},
        {"en": "They are", "pron": "déi ar", "es": "Ellos son / están"}
    ]
}