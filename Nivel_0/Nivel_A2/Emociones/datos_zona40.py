ZONA_ID = "zona40"
ZONA_NOMBRE = "A2 — Emociones y Sentimientos"

SECCIONES = {
    "s1": {
        "nombre": "Cómo nos sentimos",
        "rango": "15 palabras",
        "palabras": [
            ("happy", "jápi", "feliz"),
            ("sad", "sad", "triste"),
            ("angry", "ángri", "enojado"),
            ("scared", "skerd", "asustado"),
            ("nervous", "nérvos", "nervioso"),
            ("tired", "táierd", "cansado"),
            ("excited", "eksáited", "emocionado"),
            ("bored", "bord", "aburrido"),
            ("surprised", "sorpráisd", "sorprendido"),
            ("worried", "uórid", "preocupado"),
            ("proud", "práud", "orgulloso"),
            ("confused", "confiúsd", "confundido"),
            ("relaxed", "riláksd", "relajado"),
            ("embarrassed", "embárasd", "avergonzado"),
            ("in love", "in lov", "enamorado")
        ]
    }
}
ORDEN_SECCIONES = ["s1"]

def obtener_todas_las_palabras():
    return SECCIONES["s1"]["palabras"]

TEORIA = {
    "titulo": "Emociones y Sentimientos (A2)",
    "explicacion": "Aprende a expresar cómo te sientes en diferentes situaciones.\n\n• 'Excited' significa emocionado de alegría, no es lo mismo que 'excited' en un sentido sexual.\n• Cuidado con 'embarrassed', que significa avergonzado (no embarazada, eso es 'pregnant').",
    "tabla": [
        {"en": "happy", "pron": "jápi", "es": "feliz"},
        {"en": "sad", "pron": "sad", "es": "triste"},
        {"en": "angry", "pron": "ángri", "es": "enojado"},
        {"en": "scared", "pron": "skerd", "es": "asustado"},
        {"en": "nervous", "pron": "nérvos", "es": "nervioso"},
        {"en": "tired", "pron": "táierd", "es": "cansado"},
        {"en": "excited", "pron": "eksáited", "es": "emocionado"},
        {"en": "bored", "pron": "bord", "es": "aburrido"},
        {"en": "surprised", "pron": "sorpráisd", "es": "sorprendido"},
        {"en": "worried", "pron": "uórid", "es": "preocupado"},
        {"en": "proud", "pron": "práud", "es": "orgulloso"},
        {"en": "confused", "pron": "confiúsd", "es": "confundido"},
        {"en": "relaxed", "pron": "riláksd", "es": "relajado"},
        {"en": "embarrassed", "pron": "embárasd", "es": "avergonzado"},
        {"en": "in love", "pron": "in lov", "es": "enamorado"}
    ]
}