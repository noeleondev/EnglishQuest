import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import datos_zona18 as datos

# Lista global que se mezcla al iniciar
_PALABRAS = datos.obtener_todas_las_palabras().copy()
random.shuffle(_PALABRAS)

def generar_pregunta(fase, num):
    palabra = _PALABRAS[num % len(_PALABRAS)]
    ingles, pronun, traduccion = palabra

    if fase == "f1":
        opciones = [ingles]
        otras = [p[0] for p in _PALABRAS if p[0] != ingles]
        if len(otras) < 3:
            otras = [p[0] for p in datos.obtener_todas_las_palabras() if p[0] != ingles]
        opciones += random.sample(otras, 3)
        random.shuffle(opciones)
        return {"id": f"a1frutas-{fase}-{num}", "tipo": "opcion_multiple", "pregunta": f"¿Cuál es '{traduccion}' en inglés?", "opciones": opciones, "respuesta_correcta": ingles, "contexto": "Fase 1 — Reconocimiento"}
    elif fase == "f2":
        return {"id": f"a1frutas-{fase}-{num}", "tipo": "escribir", "pregunta": f"¿Cómo se escribe: {pronun}? ({traduccion})", "respuesta_correcta": ingles, "contexto": "Fase 2 — Producción"}
    elif fase == "f3":
        return {"id": f"a1frutas-{fase}-{num}", "tipo": "inverso", "pregunta": f"Escribe pronunciación y traducción de: {ingles}", "respuesta_correcta": f"{pronun}, {traduccion}", "contexto": "Fase 3 — Inverso"}
    else:
        if random.random() < 0.5:
            return {"id": f"a1frutas-{fase}-{num}", "tipo": "escribir", "pregunta": f"👹 DICTADO: ¿qué fruta suena como {pronun}?", "respuesta_correcta": ingles, "contexto": "JEFE — Dictado"}
        else:
            return {"id": f"a1frutas-{fase}-{num}", "tipo": "escribir", "pregunta": f"👹 PRODUCE: ¿cómo se escribe '{traduccion}'?", "respuesta_correcta": ingles, "contexto": "JEFE — Producción"}

def generar_ronda_completa(fase):
    random.shuffle(_PALABRAS) # Nuevo orden para cada ronda
    total = len(_PALABRAS)
    num_preguntas = 5 if fase == "jefe" else total
    return [generar_pregunta(fase, i) for i in range(num_preguntas)]