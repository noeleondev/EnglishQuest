ZONA_ID = "zona47"
ZONA_NOMBRE = "A2 — Modales (Should / Must / Have to)"

EJERCICIOS = [
    ("You ___ see a doctor; you look very sick. (consejo)", ["should", "must", "have to", "can"], "should", "Deberías ver a un doctor; te ves muy enfermo.", "You should see a doctor; you look very sick."),
    ("Drivers ___ stop at a red light. (regla/obligación)", ["should", "must", "might", "could"], "must", "Los conductores deben parar en un semáforo rojo.", "Drivers must stop at a red light."),
    ("I ___ finish this report today. (necesidad)", ["should", "must", "have to", "can"], "have to", "Tengo que terminar este informe hoy.", "I have to finish this report today."),
    ("You ___ smoke here; it is forbidden. (prohibición)", ["shouldn't", "don't have to", "must not", "can't"], "must not", "No debes fumar aquí; está prohibido.", "You must not smoke here; it is forbidden."),
    ("You ___ come to the party if you don't want to. (no es necesario)", ["must not", "shouldn't", "don't have to", "can't"], "don't have to", "No tienes que venir a la fiesta si no quieres.", "You don't have to come to the party if you don't want to."),
    ("You ___ drink more water. (consejo)", ["should", "must", "have to", "can"], "should", "Deberías tomar más agua.", "You should drink more water.")
]

def obtener_todos_los_ejercicios():
    return EJERCICIOS

TEORIA = {
    "titulo": "Modales: Should, Must, Have to (A2)",
    "explicacion": "Se usan para expresar obligación, prohibición o consejo.\n\n• Should: Consejo (deberías).\n• Must: Obligación fuerte o regla (debes).\n• Have to: Obligación externa o necesidad (tener que).\n• Must not: Prohibición (no debes).\n• Don't have to: No es necesario (no tienes que).",
    "tabla": [
        {"en": "Should", "pron": "shud", "es": "Deberías (consejo)"},
        {"en": "Must", "pron": "most", "es": "Debes (regla)"},
        {"en": "Have to", "pron": "jav tu", "es": "Tener que (necesidad)"},
        {"en": "Must not", "pron": "most not", "es": "Prohibido"},
        {"en": "Don't have to", "pron": "dount jav tu", "es": "No es necesario"}
    ]
}