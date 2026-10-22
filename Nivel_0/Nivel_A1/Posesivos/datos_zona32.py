ZONA_ID = "zona32"
ZONA_NOMBRE = "A1 — Adjetivos Posesivos"

EJERCICIOS = [
    ("This is ___ house. (yo)", ["my", "your", "his", "her"], "my", "Esta es mi casa.", "This is my house."),
    ("Is this ___ book? (tú)", ["my", "your", "his", "her"], "your", "¿Es este tu libro?", "Is this your book?"),
    ("Peter loves ___ dog. (él)", ["my", "your", "his", "her"], "his", "Peter ama a su perro.", "Peter loves his dog."),
    ("Maria is with ___ mother. (ella)", ["my", "your", "his", "her"], "her", "María está con su madre.", "Maria is with her mother."),
    ("We love ___ school. (nosotros)", ["our", "their", "your", "its"], "our", "Nosotros amamos nuestra escuela.", "We love our school."),
    ("They play with ___ toys. (ellos)", ["our", "their", "your", "its"], "their", "Ellos juegan con sus juguetes.", "They play with their toys."),
    ("The dog wags ___ tail. (eso/animal)", ["my", "your", "their", "its"], "its", "El perro mueve su cola.", "The dog wags its tail."),
    ("This is Peter's car. It is ___ car. (de él)", ["his", "her", "my", "our"], "his", "Este es el carro de Peter. Es su carro.", "This is Peter's car. It is his car.")
]

def obtener_todos_los_ejercicios():
    return EJERCICIOS

TEORIA = {
    "titulo": "Adjetivos Posesivos (A1)",
    "explicacion": "Indican pertenencia (mi, tu, su, nuestro). A diferencia del español, en inglés el adjetivo posesivo concuerda con el dueño, no con la cosa poseída. 'His' es de él, 'Her' es de ella, 'Its' es de una cosa o animal.",
    "tabla": [
        {"en": "My", "pron": "mái", "es": "Mi"},
        {"en": "Your", "pron": "iór", "es": "Tu"},
        {"en": "His", "pron": "jis", "es": "Su (de él)"},
        {"en": "Her", "pron": "jer", "es": "Su (de ella)"},
        {"en": "Its", "pron": "its", "es": "Su (de cosa/animal)"},
        {"en": "Our", "pron": "áuer", "es": "Nuestro/a"},
        {"en": "Their", "pron": "dér", "es": "Su (de ellos)"}
    ]
}