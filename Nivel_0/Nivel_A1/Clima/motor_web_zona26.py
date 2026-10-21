import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import datos_zona26 as datos

def generar_pregunta(fase, num):
    palabras = datos.obtener_todas_las_palabras().copy()
    random.shuffle(palabras)
    palabra = palabras[num % len(palabras)]
    ingles, pronun, traduccion = palabra

    if fase == "f1":
        opciones = [ingles]
        otras = [p[0] for p in palabras if p[0] != ingles]
        opciones += random.sample(otras, 3)
        random.shuffle(opciones)
        return {"id": f"z26-{num}", "tipo": "opcion_multiple", "pregunta": f"¿Cuál es '{traduccion}'?", "opciones": opciones, "respuesta_correcta": ingles, "contexto": "F1"}
    elif fase == "f2":
        return {"id": f"z26-{num}", "tipo": "escribir", "pregunta": f"¿Cómo se escribe: {pronun}? ({traduccion})", "respuesta_correcta": ingles, "contexto": "F2"}
    elif fase == "f3":
        return {"id": f"z26-{num}", "tipo": "inverso", "pregunta": f"Escribe pronun. y traducción: {ingles}", "respuesta_correcta": f"{pronun}, {traduccion}", "contexto": "F3"}
    else:
        if random.random() < 0.5:
            return {"id": f"z26-{num}", "tipo": "escribir", "pregunta": f"👹 DICTADO: {pronun}", "respuesta_correcta": ingles, "contexto": "JEFE"}
        else:
            return {"id": f"z26-{num}", "tipo": "escribir", "pregunta": f"👹 PRODUCE: {traduccion}", "respuesta_correcta": ingles, "contexto": "JEFE"}

def generar_ronda_completa(fase):
    total = len(datos.obtener_todas_las_palabras())
    return [generar_pregunta(fase, i) for i in range(5 if fase == "jefe" else total)]