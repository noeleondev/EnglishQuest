ZONA_ID = "gramatica4"
ZONA_NOMBRE = "Gramática — El Plural"

EJERCICIOS = [
    ("one book, two ___", ["books", "bookes", "book", "bookies"], "books", "dos libros", "two books"),
    ("one box, two ___", ["boxs", "boxes", "box", "boxies"], "boxes", "dos cajas", "two boxes"),
    ("one city, two ___", ["citys", "cities", "city", "cityes"], "cities", "dos ciudades", "two cities"),
    ("one man, two ___", ["mans", "men", "man", "mens"], "men", "dos hombres", "two men"),
    ("one child, two ___", ["childs", "children", "child", "childrens"], "children", "dos niños", "two children"),
    ("one toy, two ___", ["toys", "toies", "toy", "toyes"], "toys", "dos juguetes", "two toys"),
    ("one woman, two ___", ["womans", "women", "woman", "womens"], "women", "dos mujeres", "two women")
]

TEORIA = {
    "titulo": "El Plural de los Sustantivos",
    "explicacion": "🌟 En español agregamos 's' o 'es'. En inglés es muy similar, pero hay trampas.\n\n⚙️ Reglas principales:\n• Normal: agrega **-s** (book → books).\n• Termina en S, SS, SH, CH, X, Z: agrega **-es** (box → boxes).\n• Termina en Consonante + Y: la Y cambia a I y agrega **-es** (city → cities).\n• Termina en Vocal + Y: solo agrega **-s** (toll → tolls).\n\n🚨 ¡Ojo con los irregulares! No siguen reglas:\n• man → men (hombre → hombres)\n• woman → women (mujer → mujeres)\n• child → children (niño → niños)",
    "tabla": [
        {"en": "Book → Books", "pron": "buk → buks", "es": "libro → libros"},
        {"en": "Box → Boxes", "pron": "boks → bókses", "es": "caja → cajas"},
        {"en": "City → Cities", "pron": "siti → sitis", "es": "ciudad → ciudades"},
        {"en": "Toy → Toys", "pron": "toll → tolls", "es": "juguete → juguetes"},
        {"en": "Man → Men", "pron": "man → men", "es": "hombre → hombres"},
        {"en": "Child → Children", "pron": "chaild → chíldren", "es": "niño → niños"}
    ]
}

def obtener_todos_los_ejercicios():
    return EJERCICIOS