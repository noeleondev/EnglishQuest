"""
servidor.py — v2 — Servidor web con soporte multi-usuario
Framework : Flask
Puerto    : 5000
Archivos estáticos servidos desde ./web/

Uso:
    python servidor.py

Estructura de datos de jugadores:
    jugadores/<nombre>/perfil.json
    jugadores/<nombre>/progreso/zonaX.json
    jugadores/_registro.json
"""

import os
import sys
import json
import re
import importlib.util
import subprocess
from pathlib import Path
from datetime import datetime, timezone

from flask import Flask, jsonify, send_from_directory, abort, request

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN GENERAL
# ─────────────────────────────────────────────────────────────────────────────

BASE_DIR   = Path(__file__).resolve().parent
WEB_DIR    = BASE_DIR / "web"
JUGADORES  = BASE_DIR / "jugadores"       # raíz de todos los perfiles
REGISTRO   = JUGADORES / "_registro.json"

JUGADORES.mkdir(exist_ok=True)

ZONAS = {
    "Alfabeto":       ("Nivel_0/Alfabeto",       1),
    "Números":        ("Nivel_0/Números",        2),
    "Colores":        ("Nivel_0/Colores",        3),
    "Días":           ("Nivel_0/Dias",           4),
    "Meses":          ("Nivel_0/Meses",          5),
    "Saludos":        ("Nivel_0/Saludos",        6),
    "Pronombres":     ("Nivel_0/Pronombres",     7),
    "Familia":        ("Nivel_0/Familia",        8),
    "Objetos":        ("Nivel_0/Objetos",        9),
    "Interrogativas": ("Nivel_0/Interrogativas", 10),
    "Adjetivos":      ("Nivel_0/Adjetivos",      11),
    "G1 - Pronombres": ("Nivel_0/Gramatica_0/Pronombres", 12),
    "G2 - Verbo To Be": ("Nivel_0/Gramatica_0/To_Be", 13),
    "G3 - Artículos A-An": ("Nivel_0/Gramatica_0/Articulos", 14),
    "G4 - Plurales": ("Nivel_0/Gramatica_0/Plurales", 15),
    "G5 - This-That": ("Nivel_0/Gramatica_0/This_That", 16),
    "G6 - Wh-Questions": ("Nivel_0/Gramatica_0/Wh_Questions", 17),
    "A1 - Frutas":     ("Nivel_0/Nivel_A1/Frutas",  18),
    "A1 - Verduras":     ("Nivel_0/Nivel_A1/Verduras",  19),
    "A1 - Comida":     ("Nivel_0/Nivel_A1/Comida",  20),
    "A1 - Ropa":     ("Nivel_0/Nivel_A1/Ropa",  21),
    "A1 - Cuerpo":     ("Nivel_0/Nivel_A1/Cuerpo",  22),
    "A1 - Casa":     ("Nivel_0/Nivel_A1/Casa",  23),
    "A1 - Profesiones": ("Nivel_0/Nivel_A1/Profesiones", 24), 
    "A1 - Animales":    ("Nivel_0/Nivel_A1/Animales",    25), 
    "A1 - Clima":       ("Nivel_0/Nivel_A1/Clima",       26),
    "A1 - Rutina":       ("Nivel_0/Nivel_A1/Rutina",       27), 
    "A1 - Verbos":       ("Nivel_0/Nivel_A1/Verbos",       28),
    "A1 - Preposiciones":("Nivel_0/Nivel_A1/Preposiciones",29), 
}

app = Flask(__name__, static_folder=None)
@app.after_request
def add_header(response):
    """
    Evita que el navegador guarde en caché las respuestas de la API.
    """
    if response.content_type == 'application/json':
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
    return response

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS DE USUARIOS
# ─────────────────────────────────────────────────────────────────────────────

_RE_NOMBRE = re.compile(r"^[A-Za-z0-9_]{2,20}$")

def _validar_nombre(nombre: str) -> bool:
    return bool(_RE_NOMBRE.match(nombre))

def _leer_registro() -> dict:
    if not REGISTRO.exists():
        return {"usuarios": [], "ultimo_usuario": None}
    try:
        return json.loads(REGISTRO.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {"usuarios": [], "ultimo_usuario": None}

def _guardar_registro(reg: dict) -> None:
    REGISTRO.write_text(json.dumps(reg, ensure_ascii=False, indent=2), encoding="utf-8")

def _usuario_dir(nombre: str) -> Path:
    return JUGADORES / nombre

def _perfil_path(nombre: str) -> Path:
    return _usuario_dir(nombre) / "perfil.json"

def _progreso_dir(nombre: str) -> Path:
    return _usuario_dir(nombre) / "progreso"

def _progreso_path_usuario(nombre: str, num: int) -> Path:
    return _progreso_dir(nombre) / f"zona{num}.json"

def _leer_perfil(nombre: str) -> dict | None:
    p = _perfil_path(nombre)
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None

def _ahora_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")

def _resolver_usuario(fallback_ultimo: bool = True) -> str | None:
    """
    Obtiene el nombre de usuario desde ?usuario= o del último activo.
    Devuelve None si no hay ninguno disponible.
    """
    nombre = request.args.get("usuario") or request.json.get("usuario") \
        if request.is_json else request.args.get("usuario")
    if nombre:
        return nombre
    if fallback_ultimo:
        reg = _leer_registro()
        return reg.get("ultimo_usuario")
    return None

def _actualizar_sesion(nombre: str) -> None:
    """Actualiza ultima_sesion en el perfil y ultimo_usuario en el registro."""
    p = _perfil_path(nombre)
    if p.exists():
        try:
            perfil = json.loads(p.read_text(encoding="utf-8"))
            perfil["ultima_sesion"] = _ahora_iso()
            p.write_text(json.dumps(perfil, ensure_ascii=False, indent=2), encoding="utf-8")
        except (json.JSONDecodeError, OSError):
            pass
    reg = _leer_registro()
    reg["ultimo_usuario"] = nombre
    _guardar_registro(reg)

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS DE PROGRESO (ahora por usuario)
# ─────────────────────────────────────────────────────────────────────────────

def _leer_progreso(usuario: str, num: int) -> dict | None:
    ruta = _progreso_path_usuario(usuario, num)
    if not ruta.exists():
        # Retrocompatibilidad: intentar leer del path legado por zona
        for nombre_zona, (subcarpeta, n) in ZONAS.items():
            if n == num:
                legacy = BASE_DIR / subcarpeta / f"progreso_zona{num}.json"
                if legacy.exists():
                    try:
                        return json.loads(legacy.read_text(encoding="utf-8"))
                    except (json.JSONDecodeError, OSError):
                        pass
        return None
    try:
        return json.loads(ruta.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None

def _resumen_zona(usuario: str, nombre: str, num: int) -> dict:
    datos = _leer_progreso(usuario, num)
    if datos is None:
        return {"nombre": nombre, "completa": False, "progreso_promedio": 0, "xp": 0, "bloqueada": False}

    fases    = datos.get("fases", {})
    puntajes = [f.get("mejor_puntaje", 0) for f in fases.values()]
    aprobadas= [f.get("aprobada", False) for f in fases.values()]
    promedio = round(sum(puntajes) / len(puntajes)) if puntajes else 0
    completa = bool(fases) and all(aprobadas)

    return {"nombre": nombre, "completa": completa, "progreso_promedio": promedio,
            "xp": datos.get("xp_total", 0), "bloqueada": False}

# ─────────────────────────────────────────────────────────────────────────────
# ARCHIVOS ESTÁTICOS
# ─────────────────────────────────────────────────────────────────────────────

@app.route("/", defaults={"ruta": "index.html"})
@app.route("/<path:ruta>")
def estaticos(ruta):
    archivo = WEB_DIR / ruta
    if archivo.exists() and archivo.is_file():
        return send_from_directory(WEB_DIR, ruta)
    index = WEB_DIR / "index.html"
    if index.exists():
        return send_from_directory(WEB_DIR, "index.html")
    return jsonify({"error": "Carpeta web/ no encontrada."}), 404

# ─────────────────────────────────────────────────────────────────────────────
# ENDPOINTS DE USUARIOS
# ─────────────────────────────────────────────────────────────────────────────

@app.route("/api/usuarios", methods=["GET"])
def api_listar_usuarios():
    """GET /api/usuarios — lista todos los usuarios registrados."""
    reg     = _leer_registro()
    nombres = reg.get("usuarios", [])
    lista   = []
    for n in nombres:
        perfil = _leer_perfil(n)
        lista.append(perfil or {"nombre": n, "nombre_mostrar": n})
    return jsonify({"usuarios": lista, "ultimo_usuario": reg.get("ultimo_usuario")})


@app.route("/api/usuarios/crear", methods=["POST"])
def api_crear_usuario():
    """
    POST /api/usuarios/crear
    Body JSON: {"nombre": "Mr_Leon", "nombre_mostrar": "Mr. León", "avatar": "🎮"}
    """
    datos = request.get_json(silent=True) or {}
    nombre        = (datos.get("nombre") or "").strip()
    nombre_mostrar= (datos.get("nombre_mostrar") or nombre).strip()
    avatar        = datos.get("avatar", "🎮")

    if not _validar_nombre(nombre):
        return jsonify({"error": "Nombre inválido. Solo letras, números y _ (2-20 caracteres)."}), 400

    reg = _leer_registro()

    # Resolver conflicto de nombre
    nombre_final = nombre
    sufijo = 2
    while nombre_final in reg.get("usuarios", []):
        nombre_final = f"{nombre}{sufijo}"
        sufijo += 1

    # Crear estructura de directorios
    dir_usuario = _usuario_dir(nombre_final)
    dir_usuario.mkdir(parents=True, exist_ok=True)
    _progreso_dir(nombre_final).mkdir(exist_ok=True)

    # Crear perfil
    perfil = {
        "nombre":         nombre_final,
        "nombre_mostrar": nombre_mostrar,
        "creado":         _ahora_iso(),
        "ultima_sesion":  _ahora_iso(),
        "avatar":         avatar,
    }
    _perfil_path(nombre_final).write_text(
        json.dumps(perfil, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # Actualizar registro
    reg.setdefault("usuarios", []).append(nombre_final)
    reg["ultimo_usuario"] = nombre_final
    _guardar_registro(reg)

    return jsonify({"ok": True, "perfil": perfil}), 201


@app.route("/api/usuarios/<nombre>", methods=["GET"])
def api_obtener_usuario(nombre: str):
    """GET /api/usuarios/<nombre> — perfil de un usuario."""
    perfil = _leer_perfil(nombre)
    if perfil is None:
        abort(404, description=f"Usuario '{nombre}' no existe.")
    _actualizar_sesion(nombre)
    return jsonify(perfil)


@app.route("/api/usuarios/<nombre>", methods=["DELETE"])
def api_eliminar_usuario(nombre: str):
    """DELETE /api/usuarios/<nombre> — elimina usuario y todo su progreso."""
    if _leer_perfil(nombre) is None:
        abort(404, description=f"Usuario '{nombre}' no existe.")

    import shutil
    shutil.rmtree(_usuario_dir(nombre), ignore_errors=True)

    reg = _leer_registro()
    reg["usuarios"] = [u for u in reg.get("usuarios", []) if u != nombre]
    if reg.get("ultimo_usuario") == nombre:
        reg["ultimo_usuario"] = reg["usuarios"][0] if reg["usuarios"] else None
    _guardar_registro(reg)

    return jsonify({"ok": True, "eliminado": nombre})


@app.route("/api/usuarios/<nombre>/reiniciar", methods=["POST"])
def api_reiniciar_usuario(nombre: str):
    """POST /api/usuarios/<nombre>/reiniciar — borra el progreso de todas las zonas."""
    if _leer_perfil(nombre) is None:
        abort(404, description=f"Usuario '{nombre}' no existe.")

    import shutil
    dir_prog = _progreso_dir(nombre)
    if dir_prog.exists():
        shutil.rmtree(dir_prog)
    dir_prog.mkdir(exist_ok=True)

    return jsonify({"ok": True, "reiniciado": nombre})


@app.route("/api/usuarios/<nombre>/progreso", methods=["GET"])
def api_progreso_usuario(nombre: str):
    """GET /api/usuarios/<nombre>/progreso — progreso completo de todas las zonas."""
    if _leer_perfil(nombre) is None:
        abort(404, description=f"Usuario '{nombre}' no existe.")

    resultado = {}
    for zona_nombre, (_, num) in ZONAS.items():
        resultado[zona_nombre] = _leer_progreso(nombre, num)
    return jsonify({"usuario": nombre, "progreso": resultado})

# ─────────────────────────────────────────────────────────────────────────────
# ENDPOINTS DE JUEGO (con soporte ?usuario=)
# ─────────────────────────────────────────────────────────────────────────────

@app.route("/api/zonas", methods=["GET"])
def api_zonas():
    """
    GET /api/zonas?usuario=Mr_Leon
    Devuelve la lista de zonas con el progreso del usuario indicado.
    """
    usuario = request.args.get("usuario") or _leer_registro().get("ultimo_usuario")
    if not usuario:
        usuario = "__anonimo__"

    lista = []
    for nombre, (_, num) in ZONAS.items():
        lista.append(_resumen_zona(usuario, nombre, num))
    return jsonify({"zonas": lista, "usuario": usuario})


@app.route("/api/zona/<nombre>", methods=["GET"])
def api_zona_detalle(nombre: str):
    """
    GET /api/zona/<nombre>?usuario=Mr_Leon
    Detalle completo de una zona para el usuario indicado.
    """
    if nombre not in ZONAS:
        abort(404, description=f"Zona '{nombre}' no existe.")

    usuario = request.args.get("usuario") or _leer_registro().get("ultimo_usuario") or "__anonimo__"
    _, num  = ZONAS[nombre]

    datos_raw = _leer_progreso(usuario, num)
    resumen   = _resumen_zona(usuario, nombre, num)

    return jsonify({"resumen": resumen, "progreso": datos_raw, "usuario": usuario})

@app.route("/api/teoria/<nombre>", methods=["GET"])
def api_teoria(nombre: str):
    """
    GET /api/teoria/<nombre>
    Devuelve el material de estudio (teoría) de una zona.
    """
    if nombre not in ZONAS:
        abort(404, description=f"Zona '{nombre}' no existe.")

    subcarpeta, num = ZONAS[nombre]
    
    # Intentar cargar el archivo de datos para leer la variable TEORIA
    ruta_datos = BASE_DIR / subcarpeta / f"datos_zona{num}.py"
    
    if not ruta_datos.exists():
        # Para las zonas viejas que no tengan TEORIA aún, devolvemos un mensaje por defecto
        return jsonify({
            "titulo": nombre,
            "explicacion": "Material en construcción para esta zona.",
            "tabla": []
        })

    spec = importlib.util.spec_from_file_location(f"datos_zona{num}", ruta_datos)
    modulo = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(BASE_DIR))
    try:
        spec.loader.exec_module(modulo)
        teoria = getattr(modulo, "TEORIA", {
            "titulo": nombre,
            "explicacion": "Material no definido en este archivo.",
            "tabla": []
        })
        return jsonify(teoria)
    finally:
        if str(BASE_DIR) in sys.path:
            sys.path.remove(str(BASE_DIR))
            
@app.route("/api/jugar/<nombre>/<fase>", methods=["POST"])
def api_jugar(nombre: str, fase: str):
    """
    POST /api/jugar/<nombre>/<fase>?usuario=Mr_Leon
    Ejecuta la ronda completa usando el motor web (sin subproceso).
    Devuelve todas las preguntas para que el frontend las juegue.
    """
    if nombre not in ZONAS:
        abort(404, description=f"Zona '{nombre}' no existe.")

    fases_validas = {"f1", "f2", "f3", "jefe"}
    if fase not in fases_validas:
        abort(400, description=f"Fase '{fase}' no válida.")

    usuario = request.args.get("usuario") or _leer_registro().get("ultimo_usuario") or "__anonimo__"
    
    # AQUI ESTABA EL ERROR: Tenías dos líneas buscando lo mismo. 
    # Lo dejamos en una sola, convirtiendo la ruta a Path para que Windows la entienda.
    subcarpeta_str, num = ZONAS[nombre]
    subcarpeta = Path(subcarpeta_str)
    ruta_motor_web = BASE_DIR / subcarpeta / f"motor_web_zona{num}.py"

    if not ruta_motor_web.exists():
        abort(404, description=f"motor_web_zona{num}.py no encontrado en {ruta_motor_web}")

    # Cargar el motor web dinámicamente
    spec = importlib.util.spec_from_file_location(f"motor_web_zona{num}", ruta_motor_web)
    modulo = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(BASE_DIR))
    try:
        spec.loader.exec_module(modulo)
        # Intentar usar generar_ronda_completa si existe
        if hasattr(modulo, "generar_ronda_completa"):
            ronda = modulo.generar_ronda_completa(fase)
            return jsonify({
                "zona": nombre,
                "fase": fase,
                "usuario": usuario,
                "modo": "ronda_completa",
                "total": len(ronda),
                "preguntas": ronda,
                "ejecutado": True,
                "codigo_salida": 0,
                "stdout": f"Ronda de {len(ronda)} preguntas generada.",
                "stderr": "",
                "progreso_actualizado": _leer_progreso(usuario, num),
            })
        else:
            return jsonify({"error": "motor_web no implementa generar_ronda_completa"}), 500
    finally:
        if str(BASE_DIR) in sys.path:
            sys.path.remove(str(BASE_DIR))


@app.route("/api/pregunta/<nombre>/<fase>", methods=["GET"])
def api_pregunta(nombre: str, fase: str):
    """
    GET /api/pregunta/<zona>/<fase>?num=0&usuario=Mr_Leon
    Genera una pregunta usando el nuevo motor_web (sin subproceso, sin input).
    """
    if nombre not in ZONAS:
        abort(404, description=f"Zona '{nombre}' no existe.")

    fases_validas = {"f1", "f2", "f3", "jefe"}
    if fase not in fases_validas:
        abort(400, description=f"Fase '{fase}' no válida.")

    _, num    = ZONAS[nombre]
    num_preg  = int(request.args.get("num", 0))

    subcarpeta, num = ZONAS[nombre]
    ruta_motor_web = BASE_DIR / subcarpeta / f"motor_web_zona{num}.py"
    if not ruta_motor_web.exists():
        abort(404, description=f"motor_web_zona{num}.py no encontrado.")

    spec   = importlib.util.spec_from_file_location(f"motor_web_zona{num}", ruta_motor_web)
    modulo = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(BASE_DIR))
    try:
        spec.loader.exec_module(modulo)
    finally:
        if str(BASE_DIR) in sys.path:
            sys.path.remove(str(BASE_DIR))

    pregunta = modulo.generar_pregunta(fase, num_preg)
    return jsonify(pregunta)


@app.route("/api/ronda/<nombre>/<fase>", methods=["GET"])
def api_ronda(nombre: str, fase: str):
    """
    GET /api/ronda/<zona>/<fase>?usuario=Mr_Leon
    Devuelve la ronda completa (lista de preguntas) para una fase.
    """
    if nombre not in ZONAS:
        abort(404, description=f"Zona '{nombre}' no existe.")

    fases_validas = {"f1", "f2", "f3", "jefe"}
    if fase not in fases_validas:
        abort(400)

    _, num = ZONAS[nombre]
    subcarpeta, num = ZONAS[nombre]
    ruta_motor_web = BASE_DIR / subcarpeta / f"motor_web_zona{num}.py"
    if not ruta_motor_web.exists():
        abort(404)

    spec   = importlib.util.spec_from_file_location(f"motor_web_zona{num}", ruta_motor_web)
    modulo = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(BASE_DIR))
    try:
        spec.loader.exec_module(modulo)
    finally:
        if str(BASE_DIR) in sys.path:
            sys.path.remove(str(BASE_DIR))

    ronda = modulo.generar_ronda_completa(fase)
    return jsonify({"zona": nombre, "fase": fase, "total": len(ronda), "preguntas": ronda})


@app.route("/api/evaluar", methods=["POST"])
def api_evaluar():
    """
    POST /api/evaluar
    Body: {"pregunta": {...}, "respuesta": "green"}
    Evalúa una respuesta del usuario sin persistencia.
    """
    datos    = request.get_json(silent=True) or {}
    pregunta = datos.get("pregunta")
    resp     = datos.get("respuesta", "")

    if not pregunta or "respuesta_correcta" not in pregunta:
        abort(400, description="Falta 'pregunta' con 'respuesta_correcta'.")

    sys.path.insert(0, str(BASE_DIR))
    try:
        from motor_web_base import evaluar_respuesta
    finally:
        if str(BASE_DIR) in sys.path:
            sys.path.remove(str(BASE_DIR))

    resultado = evaluar_respuesta(pregunta, resp)
    return jsonify(resultado)


# ─────────────────────────────────────────────────────────────────────────────
# ENDPOINT: GET /api/stats (con soporte ?usuario=)
# ─────────────────────────────────────────────────────────────────────────────

@app.route("/api/stats", methods=["GET"])
def api_stats():
    """GET /api/stats?usuario=Mr_Leon — estadísticas globales del usuario."""
    usuario = request.args.get("usuario") or _leer_registro().get("ultimo_usuario") or "__anonimo__"

    xp_total = 0
    racha_max_global = 0
    zonas_completadas = 0
    zonas_iniciadas   = 0

    for _, (_, num) in ZONAS.items():
        datos = _leer_progreso(usuario, num)
        if datos is None:
            continue
        zonas_iniciadas += 1
        xp_total += datos.get("xp_total", 0)
        racha = datos.get("racha_max", 0)
        if racha > racha_max_global:
            racha_max_global = racha
        fases = datos.get("fases", {})
        if fases and all(f.get("aprobada", False) for f in fases.values()):
            zonas_completadas += 1

    return jsonify({
        "usuario":           usuario,
        "xp_total":          xp_total,
        "racha_max_global":  racha_max_global,
        "zonas_completadas": zonas_completadas,
        "zonas_iniciadas":   zonas_iniciadas,
        "zonas_totales":     len(ZONAS),
    })


# ─────────────────────────────────────────────────────────────────────────────
# ENDPOINT: POST /api/guardar-progreso
# Persiste el resultado de una ronda jugada desde el frontend interactivo.
# ─────────────────────────────────────────────────────────────────────────────

@app.route("/api/guardar-progreso", methods=["POST"])
def api_guardar_progreso():
    """
    POST /api/guardar-progreso
    Body: {
        "usuario":      "Mr_Leon",
        "zona":         "Alfabeto",
        "num":          1,
        "fase":         "f1",
        "porcentaje":   92,
        "xp_ganada":    850,
        "racha_maxima": 12,
        "errores":      [{"palabra": "green", "tu_respuesta": "grin"}]
    }
    Guarda (o actualiza) el progreso de la fase para el usuario indicado.
    """
    datos         = request.get_json(silent=True) or {}
    usuario       = datos.get("usuario")
    num           = datos.get("num")
    fase          = datos.get("fase")
    porcentaje    = int(datos.get("porcentaje", 0))
    xp_ganada     = int(datos.get("xp_ganada", 0))
    racha_maxima  = int(datos.get("racha_maxima", 0))

    if not usuario or num is None or not fase:
        abort(400, description="Faltan campos: usuario, num, fase.")

    fases_validas = {"f1", "f2", "f3", "jefe"}
    if fase not in fases_validas:
        abort(400, description=f"Fase '{fase}' no válida.")

    # Esquema vacío para un progreso nuevo
    _fases_vacias = {
        k: {"mejor_puntaje": 0, "aprobada": False, "intentos": 0, "xp_ganada": 0}
        for k in fases_validas
    }

    ruta = _progreso_path_usuario(usuario, num)

    if ruta.exists():
        try:
            progreso = json.loads(ruta.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            progreso = {}
    else:
        progreso = {}

    # Garantizar estructura mínima
    progreso.setdefault("zona", datos.get("zona", ""))
    progreso.setdefault("xp_total", 0)
    progreso.setdefault("racha_max", 0)
    progreso.setdefault("fases", _fases_vacias)

    # Actualizar la fase jugada
    f = progreso["fases"].setdefault(
        fase, {"mejor_puntaje": 0, "aprobada": False, "intentos": 0, "xp_ganada": 0}
    )
    f["intentos"]     = f.get("intentos", 0) + 1
    if porcentaje > f.get("mejor_puntaje", 0):
        f["mejor_puntaje"] = porcentaje
    if xp_ganada > f.get("xp_ganada", 0):
        f["xp_ganada"] = xp_ganada
    f["aprobada"] = f["mejor_puntaje"] >= 80

    # Acumular XP global y actualizar racha máxima
    progreso["xp_total"]  = progreso.get("xp_total", 0) + xp_ganada
    progreso["racha_max"] = max(progreso.get("racha_max", 0), racha_maxima)

    # Recalcular si la zona está completa (las 4 fases aprobadas)
    progreso["completa"] = all(
        progreso["fases"].get(k, {}).get("aprobada", False)
        for k in fases_validas
    )

    # Persistir
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(progreso, indent=2, ensure_ascii=False), encoding="utf-8")

    _actualizar_sesion(usuario)

    return jsonify({"ok": True, "progreso": progreso})


# ─────────────────────────────────────────────────────────────────────────────
# PUNTO DE ENTRADA
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("  English Quest — Servidor v2 (multi-usuario)")
    print(f"  Base dir    : {BASE_DIR}")
    print(f"  Jugadores   : {JUGADORES}")
    print(f"  Web dir     : {WEB_DIR}")
    print("  URL         : http://localhost:5000")
    print("=" * 60)
    app.run(host="0.0.0.0", port=5000, debug=True)
