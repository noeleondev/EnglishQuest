"""
motor_web_zona1.py — API de preguntas para Zona 1: El Alfabeto
Expone generar_pregunta, evaluar_respuesta, generar_ronda_completa.
NO hace print ni input. NO modifica motor_zona1.py.
"""

import sys
from pathlib import Path

# Añadir el directorio raíz (Nivel 0) al path para importar motor_web_base
_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(_ROOT))
from motor_web_base import (
    _cargar_datos, _palabras_de_datos,
    generar_pregunta as _gp,
    evaluar_respuesta,
    generar_ronda_completa as _gr,
)

# ── Cargar datos de la zona ────────────────────────────────────────────────
_datos   = _cargar_datos(Path(__file__).parent / "datos_zona1.py")
_ZONA_ID = _datos.ZONA_ID          # "zona1"
_NOMBRE  = _datos.ZONA_NOMBRE      # "Zona 1 — El Alfabeto"
_PALABRAS = _palabras_de_datos(_datos)


# ── API pública ────────────────────────────────────────────────────────────

def generar_pregunta(fase: str, num_pregunta: int = 0) -> dict:
    """Genera una pregunta para la fase y número dados."""
    return _gp(_ZONA_ID, _NOMBRE, _PALABRAS, fase, num_pregunta)


def generar_ronda_completa(fase: str) -> list[dict]:
    """Devuelve la ronda completa (todas las palabras en orden aleatorio)."""
    return _gr(_ZONA_ID, _NOMBRE, _PALABRAS, fase)


def info() -> dict:
    """Metadatos de la zona."""
    return {"zona_id": _ZONA_ID, "nombre": _NOMBRE, "total_palabras": len(_PALABRAS)}
