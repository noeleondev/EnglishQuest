ZONA_ID = "zona43"
ZONA_NOMBRE = "A2 — Verbos Irregulares"

SECCIONES = {
    "s1": {
        "nombre": "Pasado Simple (Irregulares)",
        "rango": "15 verbos",
        "palabras": [
            ("go - went", "góu - uént", "ir - fui/fue"),
            ("eat - ate", "it - éit", "comer - comí/comió"),
            ("have - had", "jav - jad", "tener - tuve/tuvo"),
            ("do - did", "du - did", "hacer - hice/hizo"),
            ("see - saw", "si - so", "ver - vi/vio"),
            ("say - said", "séi - sed", "decir - dije/dijo"),
            ("make - made", "méik - méid", "hacer/fabricar - hice/hizo"),
            ("take - took", "téik - tuk", "tomar - tomé/tomó"),
            ("come - came", "com - kéim", "venir - vine/vino"),
            ("get - got", "get - got", "obtener - obtuve/obtuvo"),
            ("give - gave", "giv - géiv", "dar - di/dio"),
            ("know - knew", "nóu - niú", "saber/conocer - supe/supo"),
            ("think - thought", "zink - zot", "pensar - pensé/pensó"),
            ("find - found", "fáind - fáund", "encontrar - encontré/encontró"),
            ("tell - told", "tel - tóuld", "decir/contar - dije/dijo")
        ]
    }
}
ORDEN_SECCIONES = ["s1"]

def obtener_todas_las_palabras():
    return SECCIONES["s1"]["palabras"]

TEORIA = {
    "titulo": "Verbos Irregulares en Pasado (A2)",
    "explicacion": "Estos verbos no siguen la regla de agregar '-ed' en pasado. Tienen su propia forma y debes memorizarlos.\n\n• En la Fase 2, el juego te pedirá escribir la forma base y el pasado (ej. 'go - went').\n• Presta atención a la pronunciación del pasado: 'said' se dice 'sed', no 'séid'.",
    "tabla": [
        {"en": "go - went", "pron": "góu - uént", "es": "ir - fui/fue"},
        {"en": "eat - ate", "pron": "it - éit", "es": "comer - comí/comió"},
        {"en": "have - had", "pron": "jav - jad", "es": "tener - tuve/tuvo"},
        {"en": "do - did", "pron": "du - did", "es": "hacer - hice/hizo"},
        {"en": "see - saw", "pron": "si - so", "es": "ver - vi/vio"},
        {"en": "say - said", "pron": "séi - sed", "es": "decir - dije/dijo"},
        {"en": "make - made", "pron": "méik - méid", "es": "hacer/fabricar - hice/hizo"},
        {"en": "take - took", "pron": "téik - tuk", "es": "tomar - tomé/tomó"},
        {"en": "come - came", "pron": "com - kéim", "es": "venir - vine/vino"},
        {"en": "get - got", "pron": "get - got", "es": "obtener - obtuve/obtuvo"},
        {"en": "give - gave", "pron": "giv - géiv", "es": "dar - di/dio"},
        {"en": "know - knew", "pron": "nóu - niú", "es": "saber/conocer - supe/supo"},
        {"en": "think - thought", "pron": "zink - zot", "es": "pensar - pensé/pensó"},
        {"en": "find - found", "pron": "fáind - fáund", "es": "encontrar - encontré/encontró"},
        {"en": "tell - told", "pron": "tel - tóuld", "es": "decir/contar - dije/dijo"}
    ]
}