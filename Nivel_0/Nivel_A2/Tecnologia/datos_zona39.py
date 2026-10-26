ZONA_ID = "zona39"
ZONA_NOMBRE = "A2 — Tecnología"

SECCIONES = {
    "s1": {
        "nombre": "Dispositivos y el mundo digital",
        "rango": "15 palabras",
        "palabras": [
            ("computer", "compúiter", "computadora"),
            ("laptop", "láptop", "computadora portátil"),
            ("phone", "fóun", "teléfono"),
            ("internet", "ínternet", "internet"),
            ("email", "ímeil", "correo electrónico"),
            ("password", "pásuord", "contraseña"),
            ("screen", "skrín", "pantalla"),
            ("application / app", "aplikéishon / ap", "aplicación"),
            ("camera", "kámera", "cámara"),
            ("charger", "chárjer", "cargador"),
            ("battery", "báteri", "batería"),
            ("download", "dáunloud", "descargar"),
            ("to upload", "tu áploud", "subir (archivo)"),
            ("Wi-Fi", "uái-fái", "wifi"),
            ("message", "mésich", "mensaje")
        ]
    }
}
ORDEN_SECCIONES = ["s1"]

def obtener_todas_las_palabras():
    return SECCIONES["s1"]["palabras"]

TEORIA = {
    "titulo": "Tecnología (A2)",
    "explicacion": "Vocabulario indispensable para el mundo moderno.\n\n• 'Download' es bajar un archivo, 'Upload' es subirlo a la nube.\n• Ojo con 'charger' (cargador), que suena parecido a 'chair' (silla), pero se pronuncia chárjer.",
    "tabla": [
        {"en": "computer", "pron": "compúiter", "es": "computadora"},
        {"en": "laptop", "pron": "láptop", "es": "computadora portátil"},
        {"en": "phone", "pron": "fóun", "es": "teléfono"},
        {"en": "internet", "pron": "ínternet", "es": "internet"},
        {"en": "email", "pron": "ímeil", "es": "correo electrónico"},
        {"en": "password", "pron": "pásuord", "es": "contraseña"},
        {"en": "screen", "pron": "skrín", "es": "pantalla"},
        {"en": "application / app", "pron": "aplikéishon / ap", "es": "aplicación"},
        {"en": "camera", "pron": "kámera", "es": "cámara"},
        {"en": "charger", "pron": "chárjer", "es": "cargador"},
        {"en": "battery", "pron": "báteri", "es": "batería"},
        {"en": "download", "pron": "dáunloud", "es": "descargar"},
        {"en": "to upload", "pron": "tu áploud", "es": "subir (archivo)"},
        {"en": "Wi-Fi", "pron": "uái-fái", "es": "wifi"},
        {"en": "message", "pron": "mésich", "es": "mensaje"}
    ]
}