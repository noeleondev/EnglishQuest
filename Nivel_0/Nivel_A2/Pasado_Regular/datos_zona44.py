ZONA_ID = "zona44"
ZONA_NOMBRE = "A2 — Pasado Simple (Regulares)"

EJERCICIOS = [
    ("I ___ (work) at a restaurant last summer.", ["work", "worked", "working", "works"], "worked", "Yo trabajé en un restaurante el verano pasado.", "I worked at a restaurant last summer."),
    ("She ___ (study) for the exam yesterday.", ["study", "studied", "studying", "studies"], "studied", "Ella estudió para el examen ayer.", "She studied for the exam yesterday."),
    ("They ___ (not/watch) the movie last night.", ["don't watch", "didn't watch", "not watched", "didn't watched"], "didn't watch", "Ellos no vieron la película anoche.", "They didn't watch the movie last night."),
    ("___ you ___ (clean) the house yesterday?", ["Do / clean", "Did / clean", "Did / cleaned", "Are / cleaning"], "Did / clean", "¿Limpiaste la casa ayer?", "Did you clean the house yesterday?"),
    ("He ___ (stop) at the red light.", ["stop", "stoped", "stopped", "stopping"], "stopped", "Él se detuvo en el semáforo rojo.", "He stopped at the red light."),
    ("We ___ (play) soccer last weekend.", ["play", "played", "playing", "plays"], "played", "Nosotros jugamos fútbol el fin de semana pasado.", "We played soccer last weekend.")
]

def obtener_todos_los_ejercicios():
    return EJERCICIOS

TEORIA = {
    "titulo": "Pasado Simple - Verbos Regulares (A2)",
    "explicacion": "Se usa para acciones terminadas en el pasado.\n\n• La regla general es agregar <span style='color:#00d4ff;'><b>-ed</b></span> al verbo (work -> worked).\n• Si termina en 'e', solo se agrega '-d' (live -> lived).\n• Si termina en consonante + 'y', la 'y' cambia a 'i' + 'ed' (study -> studied).\n• El sufijo -ed suena como 't' (uérkt), 'd' (pléid) o 'id' (stódid) dependiendo del verbo.",
    "tabla": [
        {"en": "I worked", "pron": "ái uérkt", "es": "Yo trabajé"},
        {"en": "You played", "pron": "iú pléid", "es": "Tú jugaste"},
        {"en": "He studied", "pron": "ji stódid", "es": "Él estudió"},
        {"en": "Did you work?", "pron": "did iú uérk?", "es": "¿Trabajaste?"}
    ]
}