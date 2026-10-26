ZONA_ID = "zona30"
ZONA_NOMBRE = "A1 — Presente Simple"

EJERCICIOS = [
    ("I ___ English every day.", ["study", "studies", "studying", "studied"], "study", "Yo estudio inglés todos los días.", "I study English every day."),
    ("She ___ coffee in the morning.", ["drink", "drinks", "drinking", "drank"], "drinks", "Ella bebe café en la mañana.", "She drinks coffee in the morning."),
    ("They ___ not like fish.", ["do", "does", "is", "are"], "do", "A ellos no les gusta el pescado.", "They do not like fish."),
    ("___ he play soccer?", ["Do", "Does", "Is", "Are"], "Does", "¿Él juega fútbol?", "Does he play soccer?"),
    ("We usually ___ dinner at 7.", ["eat", "eats", "eating", "ate"], "eat", "Usualmente cenamos a las 7.", "We usually eat dinner at 7."),
    ("My brother ___ TV every night.", ["watch", "watches", "watching", "watched"], "watches", "Mi hermano ve TV cada noche.", "My brother watches TV every night."),
    ("I ___ from Mexico.", ["am", "is", "are", "be"], "am", "Yo soy de México.", "I am from Mexico.")
]

def obtener_todos_los_ejercicios():
    return EJERCICIOS

TEORIA = {
    "titulo": "El Presente Simple (A1)",
    "explicacion": "Hábitos y rutinas.\n\n• Se usa para acciones que hacemos regularmente.\n• Ojo: con He, She, It, el verbo lleva '-s' o '-es' al final (ej. She drinks).\n• Para negar o preguntar, usamos el auxiliar Do/Does.",
    "tabla": [
        {"en": "I play", "pron": "ái pléi", "es": "Yo juego"},
        {"en": "You play", "pron": "iú pléi", "es": "Tú juegas"},
        {"en": "He plays", "pron": "ji pléis", "es": "Él juega"},
        {"en": "She plays", "pron": "shi pléis", "es": "Ella juega"},
        {"en": "We play", "pron": "uí pléi", "es": "Nosotros jugamos"}
    ]
}