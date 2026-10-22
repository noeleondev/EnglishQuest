import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import datos_zona34 as datos

def generar_pregunta(fase, num):
    ejercicios = datos.obtener_todos_los_ejercicios().copy()
    random.shuffle(ejercicios)
    ej = ejercicios[num % len(ejercicios)]
    oracion_hueco, opciones, respuesta, traduccion, oracion_completa = ej

    if fase == "f1":
        return {"id": f"z34-{num}", "tipo": "opcion_multiple", "pregunta": f"Completa: {oracion_hueco}", "opciones": opciones, "respuesta_correcta": respuesta, "contexto": traduccion}
    elif fase in ("f2", "f3", "jefe"):
        return {"id": f"z34-{num}", "tipo": "escribir", "pregunta": f"Traduce al inglés: {traduccion}", "respuesta_correcta": oracion_completa, "contexto": f"(Pista: {oracion_hueco})"}

def generar_ronda_completa(fase):
    total = len(datos.obtener_todos_los_ejercicios())
    return [generar_pregunta(fase, i) for i in range(5 if fase == "jefe" else total)]