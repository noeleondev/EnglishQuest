ZONA_ID = "zona36"
ZONA_NOMBRE = "A2 — Viajes y Transporte"

SECCIONES = {
    "s1": {
        "nombre": "En el aeropuerto y la ciudad",
        "rango": "15 palabras",
        "palabras": [
            ("airport", "érport", "aeropuerto"),
            ("airplane", "érplein", "avión"),
            ("train", "tréin", "tren"),
            ("bus", "bos", "autobús"),
            ("car", "car", "carro"),
            ("ticket", "tíket", "boleto"),
            ("passport", "pásport", "pasaporte"),
            ("luggage", "lóguich", "equipaje"),
            ("suitcase", "sútkeis", "maleta"),
            ("taxi", "táksi", "taxi"),
            ("subway", "sóbuei", "metro"),
            ("station", "stéishon", "estación"),
            ("road", "róud", "carretera"),
            ("trip", "trip", "viaje"),
            ("vacation", "veikéishon", "vacaciones")
        ]
    }
}
ORDEN_SECCIONES = ["s1"]

def obtener_todas_las_palabras():
    return SECCIONES["s1"]["palabras"]

TEORIA = {
    "titulo": "Viajes y Transporte (A2)",
    "explicacion": "Este vocabulario es esencial para moverte por el mundo.\n\n• Ojo con 'trip' (viaje corto) y 'travel' (viajar en general).\n• 'Luggage' es incontable, nunca digas 'luggages'.\n• En Estados Unidos, el metro se llama 'subway'.",
    "tabla": [
        {"en": "airport", "pron": "érport", "es": "aeropuerto"},
        {"en": "airplane", "pron": "érplein", "es": "avión"},
        {"en": "train", "pron": "tréin", "es": "tren"},
        {"en": "bus", "pron": "bos", "es": "autobús"},
        {"en": "car", "pron": "car", "es": "carro"},
        {"en": "ticket", "pron": "tíket", "es": "boleto"},
        {"en": "passport", "pron": "pásport", "es": "pasaporte"},
        {"en": "luggage", "pron": "lóguich", "es": "equipaje"},
        {"en": "suitcase", "pron": "sútkeis", "es": "maleta"},
        {"en": "taxi", "pron": "táksi", "es": "taxi"},
        {"en": "subway", "pron": "sóbuei", "es": "metro"},
        {"en": "station", "pron": "stéishon", "es": "estación"},
        {"en": "road", "pron": "róud", "es": "carretera"},
        {"en": "trip", "pron": "trip", "es": "viaje"},
        {"en": "vacation", "pron": "veikéishon", "es": "vacaciones"}
    ]
}