"""
motor_web_base.py — Motor de preguntas puro para la API web
─────────────────────────────────────────────────────────────
Funciones compartidas por todos los motor_web_zonaX.py.
No hace print ni input. Devuelve dicts listos para JSON.

Fases:
  f1   — opción múltiple: dado el español, elige el inglés
  f2   — escribir: dado el español, escribe el inglés
  f3   — inverso: dado el inglés, escribe la pronunciación
  jefe — producción aleatoria: dado el español, escribe inglés (orden aleatorio)
"""

import random
import importlib.util
import sys
from pathlib import Path


# ── Carga dinámica de datos ────────────────────────────────────────────────

def _cargar_datos(ruta_datos: Path) -> object:
    """Importa dinámicamente un módulo datos_zonaX.py y lo devuelve."""
    spec = importlib.util.spec_from_file_location("_datos_zona", ruta_datos)
    mod  = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(ruta_datos.parent))
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.path.pop(0)
    return mod


def _palabras_de_datos(mod) -> list[tuple]:
    """
    Extrae una lista plana de (inglés, pronunciación, traducción) del módulo.
    Compatible con datos que usen PALABRAS (lista) o SECCIONES (dict de secciones).
    """
    if hasattr(mod, "PALABRAS"):
        return list(mod.PALABRAS)
    if hasattr(mod, "SECCIONES"):
        resultado = []
        for sec in mod.SECCIONES.values():
            resultado.extend(sec.get("palabras", []))
        return resultado
    raise ValueError(f"El módulo {mod} no tiene PALABRAS ni SECCIONES.")


# ── Generación de preguntas ────────────────────────────────────────────────

def _hacer_id(zona_id: str, fase: str, idx: int) -> str:
    return f"{zona_id}-{fase}-{idx}"


def _opciones_mc(correcta: str, pool: list[tuple], campo: int = 0, n: int = 4) -> list[str]:
    """
    Genera n opciones de opción múltiple incluyendo la correcta.
    campo=0 → inglés, campo=1 → pronunciación, campo=2 → español
    """
    otras = [p[campo] for p in pool if p[campo] != correcta]
    distractores = random.sample(otras, min(n - 1, len(otras)))
    opciones = distractores + [correcta]
    random.shuffle(opciones)
    return opciones


def generar_pregunta(zona_id: str, zona_nombre: str, palabras: list[tuple],
                     fase: str, idx: int) -> dict:
    """
    Genera UNA pregunta para la fase dada.

    Returns dict con al menos:
      id, tipo, pregunta, respuesta_correcta, contexto, zona
    F1 añade: opciones
    """
    ingles, pron, esp = palabras[idx % len(palabras)]
    pid = _hacer_id(zona_id, fase, idx)

    if fase == "f1":
        opciones = _opciones_mc(ingles, palabras, campo=0)
        return {
            "id": pid,
            "tipo": "opcion_multiple",
            "pregunta": f"¿Cómo se dice '{esp}' en inglés?",
            "opciones": opciones,
            "respuesta_correcta": ingles,
            "contexto": "F1-Reconocimiento",
            "zona": zona_nombre,
            "pronunciacion": pron,
        }

    if fase == "f2":
        return {
            "id": pid,
            "tipo": "escribir",
            "pregunta": f"Escribe en inglés: {esp}  (pronunciación: {pron})",
            "respuesta_correcta": ingles,
            "contexto": "F2-Produccion",
            "zona": zona_nombre,
            "pista_pronunciacion": pron,
        }

    if fase == "f3":
        return {
            "id": pid,
            "tipo": "escribir",
            "pregunta": f"¿Cuál es la pronunciación de '{ingles}'?",
            "respuesta_correcta": pron,
            "contexto": "F3-Inverso",
            "zona": zona_nombre,
            "pista_traduccion": esp,
        }

    if fase == "jefe":
        # Producción aleatoria: a veces pregunta inglés, a veces pronunciación
        modo = random.choice(["produccion", "pronunciacion"])
        if modo == "produccion":
            return {
                "id": pid,
                "tipo": "escribir",
                "pregunta": f"[JEFE] Escribe en inglés: {esp}",
                "respuesta_correcta": ingles,
                "contexto": "JEFE-Dictado",
                "zona": zona_nombre,
                "modo_jefe": "produccion",
            }
        else:
            return {
                "id": pid,
                "tipo": "escribir",
                "pregunta": f"[JEFE] Pronunciación de '{ingles}' ({esp})",
                "respuesta_correcta": pron,
                "contexto": "JEFE-Dictado",
                "zona": zona_nombre,
                "modo_jefe": "pronunciacion",
            }

    raise ValueError(f"Fase desconocida: {fase}")


def evaluar_respuesta(pregunta: dict, respuesta_usuario: str) -> dict:
    """
    Evalúa la respuesta del usuario contra la correcta.
    Acepta variaciones de mayúsculas/minúsculas y espacios extras.

    Returns:
      {"correcto": bool, "feedback": str, "respuesta_correcta": str}
    """
    correcta   = pregunta["respuesta_correcta"].strip().lower()
    dada       = respuesta_usuario.strip().lower()
    es_correcto = (dada == correcta)

    if es_correcto:
        feedback = f"✅ ¡Correcto! '{pregunta['respuesta_correcta']}'"
    else:
        feedback = (
            f"❌ Incorrecto. "
            f"Tu respuesta: '{respuesta_usuario.strip()}' · "
            f"Correcta: '{pregunta['respuesta_correcta']}'"
        )

    return {
        "correcto": es_correcto,
        "feedback": feedback,
        "respuesta_correcta": pregunta["respuesta_correcta"],
        "tu_respuesta": respuesta_usuario.strip(),
    }


def generar_ronda_completa(zona_id: str, zona_nombre: str,
                           palabras: list[tuple], fase: str) -> list[dict]:
    """
    Genera la lista completa de preguntas para una ronda de la fase dada.
    El orden es aleatorio para no repetir siempre el mismo patrón.
    """
    indices = list(range(len(palabras)))
    random.shuffle(indices)
    return [
        generar_pregunta(zona_id, zona_nombre, palabras, fase, i)
        for i in indices
    ]
