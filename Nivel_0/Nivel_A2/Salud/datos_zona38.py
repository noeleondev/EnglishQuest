ZONA_ID = "zona38"
ZONA_NOMBRE = "A2 — Salud y Enfermedades"

SECCIONES = {
    "s1": {
        "nombre": "Síntomas y doctores",
        "rango": "15 palabras",
        "palabras": [
            ("sick / ill", "sik / il", "enfermo"),
            ("headache", "jédeik", "dolor de cabeza"),
            ("stomachache", "stómak-eik", "dolor de estómago"),
            ("fever", "fíver", "fiebre"),
            ("cough", "cof", "tos"),
            ("cold (illness)", "cóuld", "resfriado"),
            ("pain", "péin", "dolor"),
            ("hospital", "jóspital", "hospital"),
            ("medicine", "médisin", "medicina"),
            ("pharmacy", "fármasi", "farmacia"),
            ("appointment", "apóintment", "cita médica"),
            ("injury", "ínyuri", "herida/lesión"),
            ("healthy", "jélzi", "saludable"),
            ("to feel bad", "tu fil bad", "sentirse mal"),
            ("to rest", "tu rest", "descansar")
        ]
    }
}
ORDEN_SECCIONES = ["s1"]

def obtener_todas_las_palabras():
    return SECCIONES["s1"]["palabras"]

TEORIA = {
    "titulo": "Salud y Enfermedades (A2)",
    "explicacion": "Aprende a describir cómo te sientes y a pedir ayuda médica.\n\n• Para decir que te duele algo, usamos 'I have a...' (I have a headache).\n• 'Sick' es enfermo en general, 'cold' es específicamente resfriado.\n• 'Healthy' significa saludable.",
    "tabla": [
        {"en": "sick / ill", "pron": "sik / il", "es": "enfermo"},
        {"en": "headache", "pron": "jédeik", "es": "dolor de cabeza"},
        {"en": "stomachache", "pron": "stómak-eik", "es": "dolor de estómago"},
        {"en": "fever", "pron": "fíver", "es": "fiebre"},
        {"en": "cough", "pron": "cof", "es": "tos"},
        {"en": "cold (illness)", "pron": "cóuld", "es": "resfriado"},
        {"en": "pain", "pron": "péin", "es": "dolor"},
        {"en": "hospital", "pron": "jóspital", "es": "hospital"},
        {"en": "medicine", "pron": "médisin", "es": "medicina"},
        {"en": "pharmacy", "pron": "fármasi", "es": "farmacia"},
        {"en": "appointment", "pron": "apóintment", "es": "cita médica"},
        {"en": "injury", "pron": "ínyuri", "es": "herida/lesión"},
        {"en": "healthy", "pron": "jélzi", "es": "saludable"},
        {"en": "to feel bad", "pron": "tu fil bad", "es": "sentirse mal"},
        {"en": "to rest", "pron": "tu rest", "es": "descansar"}
    ]
}