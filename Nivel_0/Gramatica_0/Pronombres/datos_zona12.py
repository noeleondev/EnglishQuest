"""
DATOS DE GRAMÁTICA 1: PRONOMBRES PERSONALES
Nivel 0
"""

ZONA_ID = "gramatica1"
ZONA_NOMBRE = "Gramática — Pronombres Personales"

# Para gramática, en lugar de palabras, guardamos ejercicios
# Formato: (oración_con_hueco, opciones, respuesta_correcta, traducción, oración_completa)
EJERCICIOS = [
    ("___ am from Mexico.", ["I", "You", "He", "They"], "I", "Yo soy de México.", "I am from Mexico."),
    ("___ is my brother.", ["I", "He", "She", "It"], "He", "Él es mi hermano.", "He is my brother."),
    ("___ is a dog.", ["He", "She", "It", "We"], "It", "Eso es un perro.", "It is a dog."),
    ("___ are my parents.", ["He", "She", "It", "They"], "They", "Ellos son mis padres.", "They are my parents."),
    ("___ is my mother.", ["He", "She", "It", "We"], "She", "Ella es mi madre.", "She is my mother."),
    ("___ are students.", ["I", "You", "He", "She"], "You", "Ustedes son estudiantes.", "You are students."),
    ("___ are friends.", ["I", "He", "It", "We"], "We", "Nosotros somos amigos.", "We are friends.")
]

TEORIA = {
    "titulo": "Los Pronombres Personales",
    "explicacion": "🌟 Los pronombres son el sujeto de la oración. En inglés, no existe distinción entre 'tú' y 'usted' (ambos son 'You'). Para cosas, animales o conceptos abstractos se usa 'It'.\n\n⚙️ Reglas básicas:\n• I (yo) siempre va en mayúscula.\n• He (él) y She (ella) solo para personas.\n• It (eso) para objetos o animales.\n• They (ellos) para plural.",
    "tabla": [
        {"en": "I", "pron": "ái", "es": "yo"},
        {"en": "You", "pron": "iu", "es": "tú / usted"},
        {"en": "He", "pron": "ji", "es": "él"},
        {"en": "She", "pron": "shi", "es": "ella"},
        {"en": "It", "pron": "it", "es": "eso (cosas/animales)"},
        {"en": "We", "pron": "ui", "es": "nosotros"},
        {"en": "They", "pron": "déi", "es": "ellos / ellas"}
    ]
}
