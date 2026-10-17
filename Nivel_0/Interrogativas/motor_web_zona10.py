"""
motor_web_zona10.py — API de preguntas para Zona 10: Interrogativas
NO hace print ni input. NO modifica motor_zona10.py.
"""

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(_ROOT))
from motor_web_base import (
    _cargar_datos, _palabras_de_datos,
    generar_pregunta as _gp,
    evaluar_respuesta,
    generar_ronda_completa as _gr,
)

_datos    = _cargar_datos(Path(__file__).parent / "datos_zona10.py")
_ZONA_ID  = _datos.ZONA_ID
_NOMBRE   = _datos.ZONA_NOMBRE
_PALABRAS = _palabras_de_datos(_datos)


def generar_pregunta(fase: str, num_pregunta: int = 0) -> dict:
    return _gp(_ZONA_ID, _NOMBRE, _PALABRAS, fase, num_pregunta)

def generar_ronda_completa(fase: str) -> list[dict]:
    return _gr(_ZONA_ID, _NOMBRE, _PALABRAS, fase)

def info() -> dict:
    return {"zona_id": _ZONA_ID, "nombre": _NOMBRE, "total_palabras": len(_PALABRAS)}
