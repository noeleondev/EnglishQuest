ZONA_ID = "zona37"
ZONA_NOMBRE = "A2 — Compras y Dinero"

SECCIONES = {
    "s1": {
        "nombre": "En la tienda",
        "rango": "15 palabras",
        "palabras": [
            ("money", "móni", "dinero"),
            ("price", "práis", "precio"),
            ("expensive", "expénsiv", "caro"),
            ("cheap", "chip", "barato"),
            ("store", "stor", "tienda"),
            ("mall", "mol", "centro comercial"),
            ("cash", "cash", "efectivo"),
            ("credit card", "crédit kard", "tarjeta de crédito"),
            ("receipt", "resít", "recibo"),
            ("discount", "díscaunt", "descuento"),
            ("to pay", "tu péi", "pagar"),
            ("to cost", "tu cost", "costar"),
            ("change", "chéinch", "cambio (dinero)"),
            ("cashier", "kashíer", "cajero/a"),
            ("size", "sáis", "talla")
        ]
    }
}
ORDEN_SECCIONES = ["s1"]

def obtener_todas_las_palabras():
    return SECCIONES["s1"]["palabras"]

TEORIA = {
    "titulo": "Compras y Dinero (A2)",
    "explicacion": "Vocabulario clave para sobrevivir en cualquier centro comercial.\n\n• El 'change' no es solo cambio de ropa, también es el vuelto o cambio de dinero.\n• 'Receipt' tiene una 'p' muda (se dice resít).\n• 'Cheap' significa barato (buen precio).",
    "tabla": [
        {"en": "money", "pron": "móni", "es": "dinero"},
        {"en": "price", "pron": "práis", "es": "precio"},
        {"en": "expensive", "pron": "expénsiv", "es": "caro"},
        {"en": "cheap", "pron": "chip", "es": "barato"},
        {"en": "store", "pron": "stor", "es": "tienda"},
        {"en": "mall", "pron": "mol", "es": "centro comercial"},
        {"en": "cash", "pron": "cash", "es": "efectivo"},
        {"en": "credit card", "pron": "crédit kard", "es": "tarjeta de crédito"},
        {"en": "receipt", "pron": "resít", "es": "recibo"},
        {"en": "discount", "pron": "díscaunt", "es": "descuento"},
        {"en": "to pay", "pron": "tu péi", "es": "pagar"},
        {"en": "to cost", "pron": "tu cost", "es": "costar"},
        {"en": "change", "pron": "chéinch", "es": "cambio (dinero)"},
        {"en": "cashier", "pron": "kashíer", "es": "cajero/a"},
        {"en": "size", "pron": "sáis", "es": "talla"}
    ]
}