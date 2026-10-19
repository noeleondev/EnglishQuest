import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import datos_zona16 as datos

def generar_pregunta(fase, num):
    ejercicios = datos.EJERCICIOS.copy()
    random.shuffle(ejercicios)
    ej = ejercicios[num % len(ejercicios)]
    oracion_hueco, opciones, respuesta, traduccion, oracion_completa = ej

    if fase == "f1":
        return {"id": f"g5-{fase}-{num}", "tipo": "opcion_multiple", "pregunta": f"Completa: {oracion_hueco}", "opciones": opciones, "respuesta_correcta": respuesta, "contexto": traduccion}
    else:
        return {"id": f"g5-{fase}-{num}", "tipo": "escribir", "pregunta": f"Traduce al inglés: {traduccion}", "respuesta_correcta": oracion_completa, "contexto": f"(Pista: {oracion_hueco})"}

def generar_ronda_completa(fase):
    total = len(datos.EJERCICIOS)
    num_preguntas = 5 if fase == "jefe" else total
    return [generar_pregunta(fase, i) for i in range(num_preguntas)]