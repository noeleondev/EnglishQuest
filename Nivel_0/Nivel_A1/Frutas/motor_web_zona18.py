"""
MOTOR WEB DE LA ZONA 18: FRUTAS
"""

import random
import sys
from pathlib import Path

# Importar datos (según manual)
sys.path.insert(0, str(Path(__file__).parent))
import datos_zona18 as datos

def generar_pregunta(fase, num):
    palabras = datos.obtener_todas_las_palabras().copy()
    random.shuffle(palabras)
    palabra = palabras[num % len(palabras)]
    ingles, pronun, traduccion = palabra

    if fase == "f1":
        # F1: Opción múltiple (Español -> Inglés)
        opciones = [ingles]
        otras = [p[0] for p in palabras if p[0] != ingles]
        if len(otras) < 3:
            otras = [p[0] for p in datos.obtener_todas_las_palabras() if p[0] != ingles]
        opciones += random.sample(otras, 3)
        random.shuffle(opciones)
        
        return {
            "id": f"a1frutas-{fase}-{num}",
            "tipo": "opcion_multiple",
            "pregunta": f"¿Cuál es '{traduccion}' en inglés?",
            "opciones": opciones,
            "respuesta_correcta": ingles,
            "contexto": "Fase 1 — Reconocimiento"
        }
    elif fase == "f2":
        # F2: Escribir (Pronunciación -> Inglés)
        return {
            "id": f"a1frutas-{fase}-{num}",
            "tipo": "escribir",
            "pregunta": f"¿Cómo se escribe: {pronun}? ({traduccion})",
            "respuesta_correcta": ingles,
            "contexto": "Fase 2 — Producción"
        }
    elif fase == "f3":
        # F3: Inverso (Inglés -> Pronunciación + Traducción)
        return {
            "id": f"a1frutas-{fase}-{num}",
            "tipo": "inverso",
            "pregunta": f"Escribe pronunciación y traducción de: {ingles}",
            "respuesta_correcta": f"{pronun}, {traduccion}",
            "contexto": "Fase 3 — Inverso"
        }
    else: # jefe
        # Jefe: Alterna entre dictado y traducción
        if random.random() < 0.5:
            return {
                "id": f"a1frutas-{fase}-{num}",
                "tipo": "escribir",
                "pregunta": f"👹 DICTADO: ¿qué fruta suena como {pronun}?",
                "respuesta_correcta": ingles,
                "contexto": "JEFE — Dictado"
            }
        else:
            return {
                "id": f"a1frutas-{fase}-{num}",
                "tipo": "escribir",
                "pregunta": f"👹 PRODUCE: ¿cómo se escribe '{traduccion}'?",
                "respuesta_correcta": ingles,
                "contexto": "JEFE — Producción"
            }

def generar_ronda_completa(fase):
    total = len(datos.obtener_todas_las_palabras())
    num_preguntas = 5 if fase == "jefe" else total
    return [generar_pregunta(fase, i) for i in range(num_preguntas)]