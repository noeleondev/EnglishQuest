ZONA_ID = "zona42"
ZONA_NOMBRE = "A2 — Adjetivos Comparativos"

SECCIONES = {
    "s1": {
        "nombre": "Comparando cosas",
        "rango": "12 adjetivos",
        "palabras": [
            ("tall / taller", "tol / tóler", "alto / más alto"),
            ("short / shorter", "short / shórter", "corto o bajo / más corto"),
            ("fast / faster", "fast / fáster", "rápido / más rápido"),
            ("slow / slower", "slóu / slóuer", "lento / más lento"),
            ("big / bigger", "big / bígüer", "grande / más grande"),
            ("small / smaller", "smol / smóler", "pequeño / más pequeño"),
            ("good / better", "gud / béter", "bueno / mejor"),
            ("bad / worse", "bad / uérs", "malo / peor"),
            ("cheap / cheaper", "chip / chíper", "barato / más barato"),
            ("expensive / more expensive", "expénsiv / mor expénsiv", "caro / más caro"),
            ("easy / easier", "ísi / ísi-er", "fácil / más fácil"),
            ("far / farther", "far / fárder", "lejos / más lejos")
        ]
    }
}
ORDEN_SECCIONES = ["s1"]

def obtener_todas_las_palabras():
    return SECCIONES["s1"]["palabras"]

TEORIA = {
    "titulo": "Adjetivos Comparativos (A2)",
    "explicacion": "Se usan para comparar dos cosas o personas.\n\n• Adjetivos cortos: agregan <span style='color:#00d4ff;'><b>-er</b></span> (se pronuncia como un 'er' suave, ej. tóler).\n• Adjetivos largos: usan 'more' (more expensive).\n• Irregulares: good -> better, bad -> worse.\n• Estructura: She is taller than me.",
    "tabla": [
        {"en": "tall / taller", "pron": "tol / tóler", "es": "alto / más alto"},
        {"en": "short / shorter", "pron": "short / shórter", "es": "corto o bajo / más corto"},
        {"en": "fast / faster", "pron": "fast / fáster", "es": "rápido / más rápido"},
        {"en": "slow / slower", "pron": "slóu / slóuer", "es": "lento / más lento"},
        {"en": "big / bigger", "pron": "big / bígüer", "es": "grande / más grande"},
        {"en": "small / smaller", "pron": "smol / smóler", "es": "pequeño / más pequeño"},
        {"en": "good / better", "pron": "gud / béter", "es": "bueno / mejor"},
        {"en": "bad / worse", "pron": "bad / uérs", "es": "malo / peor"},
        {"en": "cheap / cheaper", "pron": "chip / chíper", "es": "barato / más barato"},
        {"en": "expensive / more expensive", "pron": "expénsiv / mor expénsiv", "es": "caro / más caro"},
        {"en": "easy / easier", "pron": "ísi / ísi-er", "es": "fácil / más fácil"},
        {"en": "far / farther", "pron": "far / fárder", "es": "lejos / más lejos"}
    ]
}