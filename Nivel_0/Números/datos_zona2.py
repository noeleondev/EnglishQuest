"""
DATOS DE LA ZONA 2: NÚMEROS 0–100
Fuente: "Inglés desde Cero - Nivel 0 al C2" (Mr. León), páginas 9-10
Estructura: 10 secciones de ~10 números + jefe de zona

Formato de cada entrada: (inglés, pronunciación_español, traducción)
"""

ZONA_ID = "zona2"
ZONA_NOMBRE = "Zona 2 — Números 0–100"

# ─────────────────────────────────────────────
# SECCIONES
# Cada sección es un bloque jugable independiente.
# Bloqueo progresivo: S2 requiere aprobar S1, etc.
# ─────────────────────────────────────────────
SECCIONES = {
    "s1": {
        "nombre": "S1 — Del 0 al 9",
        "rango": "0–9",
        "palabras": [
            ("zero",       "zírou",   "cero"),
            ("one",        "uán",     "uno"),
            ("two",        "tu",      "dos"),
            ("three",      "zrí",     "tres"),
            ("four",       "for",     "cuatro"),
            ("five",       "fáiv",    "cinco"),
            ("six",        "siks",    "seis"),
            ("seven",      "séven",   "siete"),
            ("eight",      "éit",     "ocho"),
            ("nine",       "náin",    "nueve"),
        ],
    },
    "s2": {
        "nombre": "S2 — Del 10 al 19",
        "rango": "10–19",
        "palabras": [
            ("ten",        "ten",     "diez"),
            ("eleven",     "iléven",  "once"),
            ("twelve",     "tuélv",   "doce"),
            ("thirteen",   "zértin",  "trece"),
            ("fourteen",   "fórtin",  "catorce"),
            ("fifteen",    "fíftin",  "quince"),
            ("sixteen",    "síkstin", "dieciséis"),
            ("seventeen",  "séventin","diecisiete"),
            ("eighteen",   "éitin",   "dieciocho"),
            ("nineteen",   "náintin", "diecinueve"),
        ],
    },
    "s3": {
        "nombre": "S3 — Del 20 al 29",
        "rango": "20–29",
        "palabras": [
            ("twenty",       "tuénti",    "veinte"),
            ("twenty-one",   "tuénti-uán","veintiuno"),
            ("twenty-two",   "tuénti-tu", "veintidós"),
            ("twenty-three", "tuénti-zrí","veintitrés"),
            ("twenty-four",  "tuénti-for","veinticuatro"),
            ("twenty-five",  "tuénti-fáiv","veinticinco"),
            ("twenty-six",   "tuénti-siks","veintiséis"),
            ("twenty-seven", "tuénti-séven","veintisiete"),
            ("twenty-eight", "tuénti-éit","veintiocho"),
            ("twenty-nine",  "tuénti-náin","veintinueve"),
        ],
    },
    "s4": {
        "nombre": "S4 — Del 30 al 39",
        "rango": "30–39",
        "palabras": [
            ("thirty",       "zérti",     "treinta"),
            ("thirty-one",   "zérti-uán", "treinta y uno"),
            ("thirty-two",   "zérti-tu",  "treinta y dos"),
            ("thirty-three", "zérti-zrí", "treinta y tres"),
            ("thirty-four",  "zérti-for", "treinta y cuatro"),
            ("thirty-five",  "zérti-fáiv","treinta y cinco"),
            ("thirty-six",   "zérti-siks","treinta y seis"),
            ("thirty-seven", "zérti-séven","treinta y siete"),
            ("thirty-eight", "zérti-éit", "treinta y ocho"),
            ("thirty-nine",  "zérti-náin","treinta y nueve"),
        ],
    },
    "s5": {
        "nombre": "S5 — Del 40 al 49",
        "rango": "40–49",
        "palabras": [
            ("forty",       "fórti",     "cuarenta"),
            ("forty-one",   "fórti-uán", "cuarenta y uno"),
            ("forty-two",   "fórti-tu",  "cuarenta y dos"),
            ("forty-three", "fórti-zrí", "cuarenta y tres"),
            ("forty-four",  "fórti-for", "cuarenta y cuatro"),
            ("forty-five",  "fórti-fáiv","cuarenta y cinco"),
            ("forty-six",   "fórti-siks","cuarenta y seis"),
            ("forty-seven", "fórti-séven","cuarenta y siete"),
            ("forty-eight", "fórti-éit", "cuarenta y ocho"),
            ("forty-nine",  "fórti-náin","cuarenta y nueve"),
        ],
    },
    "s6": {
        "nombre": "S6 — Del 50 al 59",
        "rango": "50–59",
        "palabras": [
            ("fifty",       "fífti",     "cincuenta"),
            ("fifty-one",   "fífti-uán", "cincuenta y uno"),
            ("fifty-two",   "fífti-tu",  "cincuenta y dos"),
            ("fifty-three", "fífti-zrí", "cincuenta y tres"),
            ("fifty-four",  "fífti-for", "cincuenta y cuatro"),
            ("fifty-five",  "fífti-fáiv","cincuenta y cinco"),
            ("fifty-six",   "fífti-siks","cincuenta y seis"),
            ("fifty-seven", "fífti-séven","cincuenta y siete"),
            ("fifty-eight", "fífti-éit", "cincuenta y ocho"),
            ("fifty-nine",  "fífti-náin","cincuenta y nueve"),
        ],
    },
    "s7": {
        "nombre": "S7 — Del 60 al 69",
        "rango": "60–69",
        "palabras": [
            ("sixty",       "síksti",    "sesenta"),
            ("sixty-one",   "síksti-uán","sesenta y uno"),
            ("sixty-two",   "síksti-tu", "sesenta y dos"),
            ("sixty-three", "síksti-zrí","sesenta y tres"),
            ("sixty-four",  "síksti-for","sesenta y cuatro"),
            ("sixty-five",  "síksti-fáiv","sesenta y cinco"),
            ("sixty-six",   "síksti-siks","sesenta y seis"),
            ("sixty-seven", "síksti-séven","sesenta y siete"),
            ("sixty-eight", "síksti-éit","sesenta y ocho"),
            ("sixty-nine",  "síksti-náin","sesenta y nueve"),
        ],
    },
    "s8": {
        "nombre": "S8 — Del 70 al 79",
        "rango": "70–79",
        "palabras": [
            ("seventy",       "séventi",     "setenta"),
            ("seventy-one",   "séventi-uán", "setenta y uno"),
            ("seventy-two",   "séventi-tu",  "setenta y dos"),
            ("seventy-three", "séventi-zrí", "setenta y tres"),
            ("seventy-four",  "séventi-for", "setenta y cuatro"),
            ("seventy-five",  "séventi-fáiv","setenta y cinco"),
            ("seventy-six",   "séventi-siks","setenta y seis"),
            ("seventy-seven", "séventi-séven","setenta y siete"),
            ("seventy-eight", "séventi-éit", "setenta y ocho"),
            ("seventy-nine",  "séventi-náin","setenta y nueve"),
        ],
    },
    "s9": {
        "nombre": "S9 — Del 80 al 89",
        "rango": "80–89",
        "palabras": [
            ("eighty",       "éiti",      "ochenta"),
            ("eighty-one",   "éiti-uán",  "ochenta y uno"),
            ("eighty-two",   "éiti-tu",   "ochenta y dos"),
            ("eighty-three", "éiti-zrí",  "ochenta y tres"),
            ("eighty-four",  "éiti-for",  "ochenta y cuatro"),
            ("eighty-five",  "éiti-fáiv", "ochenta y cinco"),
            ("eighty-six",   "éiti-siks", "ochenta y seis"),
            ("eighty-seven", "éiti-séven","ochenta y siete"),
            ("eighty-eight", "éiti-éit",  "ochenta y ocho"),
            ("eighty-nine",  "éiti-náin", "ochenta y nueve"),
        ],
    },
    "s10": {
        "nombre": "S10 — Del 90 al 100",
        "rango": "90–100",
        "palabras": [
            ("ninety",       "náinti",     "noventa"),
            ("ninety-one",   "náinti-uán", "noventa y uno"),
            ("ninety-two",   "náinti-tu",  "noventa y dos"),
            ("ninety-three", "náinti-zrí", "noventa y tres"),
            ("ninety-four",  "náinti-for", "noventa y cuatro"),
            ("ninety-five",  "náinti-fáiv","noventa y cinco"),
            ("ninety-six",   "náinti-siks","noventa y seis"),
            ("ninety-seven", "náinti-séven","noventa y siete"),
            ("ninety-eight", "náinti-éit", "noventa y ocho"),
            ("ninety-nine",  "náinti-náin","noventa y nueve"),
            ("one hundred",  "uán jándred","cien"),
        ],
    },
}

# Orden de las secciones (para bloqueo progresivo)
ORDEN_SECCIONES = ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10"]

# ─────────────────────────────────────────────
# JEFE DE ZONA: todas las palabras mezcladas
# ─────────────────────────────────────────────
def obtener_todas_las_palabras():
    """Devuelve la lista completa de las 101 palabras."""
    todas = []
    for sid in ORDEN_SECCIONES:
        todas.extend(SECCIONES[sid]["palabras"])
    return todas