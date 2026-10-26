import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import datos_zona31 as datos  

_EJERCICIOS = datos.obtener_todos_los_ejercicios().copy()
random.shuffle(_EJERCICIOS)

def generar_pregunta(fase, num):
    ej = _EJERCICIOS[num % len(_EJERCICIOS)]
    oracion_hueco, opciones, respuesta, traduccion, oracion_completa = ej

    if fase == "f1":
        return {"id": f"z31-{num}", "tipo": "opcion_multiple", "pregunta": f"Completa: {oracion_hueco}", "opciones": opciones, "respuesta_correcta": respuesta, "contexto": traduccion}
    elif fase in ("f2", "f3", "jefe"):
        return {"id": f"z31-{num}", "tipo": "escribir", "pregunta": f"Traduce al inglés: {traduccion}", "respuesta_correcta": oracion_completa, "contexto": f"(Pista: {oracion_hueco})"}

def generar_ronda_completa(fase):
    random.shuffle(_EJERCICIOS) 
    total = len(_EJERCICIOS)
    return [generar_pregunta(fase, i) for i in range(5 if fase == "jefe" else total)]