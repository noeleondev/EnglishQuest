/**
 * app.js — v3
 * ─────────────────────────────────────────────────────────────
 * Novedades v3:
 *   - Soporte multi-usuario: todas las llamadas API incluyen
 *     ?usuario=<nombre> vía UserManager.apiParam().
 *   - Escucha evento 'eq:usuario-cambiado' para recargar datos
 *     cuando el usuario activo cambia desde UserManager.
 *   - Inicialización diferida: espera a que UserManager resuelva
 *     el usuario antes de cargar zonas y stats.
 * ─────────────────────────────────────────────────────────────
 */

// ── Estado global ──────────────────────────────────────────────────────────
const State = {
  zonas:          [],
  zonaActiva:     null,
  faseActiva:     null,
  jugando:        false,
  xpAnterior:     0,      // XP total antes de la última partida (para delta)
  rachaActual:    0,      // racha máxima global actual (para la barra)
};

// ── Metadata de iconos y nombres ──────────────────────────────────────────
const ZONA_META = {
  'Alfabeto':       { icon: '🔤', orden: 1 },
  'Números':        { icon: '🔢', orden: 2 },
  'Colores':        { icon: '🎨', orden: 3 },
  'Días':           { icon: '📅', orden: 4 },
  'Meses':          { icon: '🗓️', orden: 5 },
  'Saludos':        { icon: '👋', orden: 6 },
  'Pronombres':     { icon: '👤', orden: 7 },
  'Familia':        { icon: '👨‍👩‍👧', orden: 8 },
  'Objetos':        { icon: '🪑', orden: 9 },
  'Interrogativas': { icon: '❓', orden: 10 },
  'Adjetivos':      { icon: '✨', orden: 11 },
  'G1 - Pronombres': { icon: '👤', orden: 12 },
  'G2 - Verbo To Be': { icon: '🧬', orden: 13 },
  'G3 - Artículos A-An': { icon: '📝', orden: 14 },
  'G4 - Plurales': { icon: '📚', orden: 15 },
  'G5 - This-That': { icon: '👉', orden: 16 },
  'G6 - Wh-Questions': { icon: '❓', orden: 17 },
};

const FASE_META = {
  f1:   { icon: '📖', nombre: 'Fase 1 — Reconocimiento' },
  f2:   { icon: '⏱️', nombre: 'Fase 2 — Producción' },
  f3:   { icon: '🔄', nombre: 'Fase 3 — Inverso' },
  jefe: { icon: '👾', nombre: 'JEFE — Dictado' },
};

// Símbolos del confeti (mezcla de ASCII y emoji simples)
const CONFETTI_SYMBOLS = ['★', '✦', '◆', '▲', '●', '✱', '❋', '⬟', '✿', '❂'];

// ── Helpers ────────────────────────────────────────────────────────────────

async function apiGet(url) {
  // Añade el parámetro de usuario activo si UserManager está disponible
  const sep = url.includes('?') ? '&' : '?';
  const param = (typeof UserManager !== 'undefined') ? UserManager.apiParam().replace('?', sep) : '';
  const full = url + param;
  const res = await fetch(full);
  if (!res.ok) throw new Error(`GET ${full} → ${res.status} ${res.statusText}`);
  return res.json();
}

async function apiPost(url) {
  const sep = url.includes('?') ? '&' : '?';
  const param = (typeof UserManager !== 'undefined') ? UserManager.apiParam().replace('?', sep) : '';
  const full = url + param;
  const res = await fetch(full, { method: 'POST' });
  if (!res.ok) throw new Error(`POST ${full} → ${res.status} ${res.statusText}`);
  return res.json();
}

function fmtNum(n) {
  if (n == null || n === '–') return '–';
  return Number(n).toLocaleString('es-ES');
}

function $(id) {
  const el = document.getElementById(id);
  if (!el) throw new Error(`Elemento #${id} no encontrado`);
  return el;
}

// ── ANIMACIONES ────────────────────────────────────────────────────────────

/**
 * Muestra un número de XP flotando desde una posición en pantalla.
 * @param {number} xpDelta  — cantidad de XP ganada
 * @param {Element} anchorEl — elemento desde el que sube el float
 */
function animXpFloat(xpDelta, anchorEl) {
  if (!xpDelta || xpDelta <= 0) return;

  const rect = anchorEl
    ? anchorEl.getBoundingClientRect()
    : { left: window.innerWidth / 2, top: window.innerHeight / 2, width: 0 };

  const el = document.createElement('span');
  el.className   = 'xp-float';
  el.textContent = `+${fmtNum(xpDelta)} XP`;
  el.style.left  = `${rect.left + rect.width / 2}px`;
  el.style.top   = `${rect.top}px`;
  document.body.appendChild(el);

  // Limpiar después de la animación
  el.addEventListener('animationend', () => el.remove(), { once: true });
}

/**
 * Lanza confeti ASCII desde la parte superior de la pantalla.
 * @param {number} count — número de partículas
 */
function animConfetti(count = 40) {
  for (let i = 0; i < count; i++) {
    const el = document.createElement('span');
    el.className   = 'confetti-particle';
    el.textContent = CONFETTI_SYMBOLS[Math.floor(Math.random() * CONFETTI_SYMBOLS.length)];
    el.setAttribute('aria-hidden', 'true');

    const x    = Math.random() * 100;       // % horizontal
    const dur  = 1.8 + Math.random() * 1.4; // segundos de caída
    const dlay = Math.random() * 0.8;        // escalonar arranque
    const rot  = (Math.random() > 0.5 ? 1 : -1) * (180 + Math.random() * 360);
    const dist = 70 + Math.random() * 25;   // vh de caída

    el.style.left    = `${x}vw`;
    el.style.top     = `-2rem`;
    el.style.color   = `hsl(${Math.random() * 360}, 90%, 65%)`;
    el.style.setProperty('--fall-dur',   `${dur}s`);
    el.style.setProperty('--fall-delay', `${dlay}s`);
    el.style.setProperty('--fall-rot',   `${rot}deg`);
    el.style.setProperty('--fall-dist',  `${dist}vh`);

    document.body.appendChild(el);
    const totalMs = (dur + dlay) * 1000 + 200;
    setTimeout(() => el.remove(), totalMs);
  }
}

/**
 * Muestra el banner de logro en la parte superior.
 * @param {string} icon  — emoji
 * @param {string} title — subtítulo pequeño
 * @param {string} text  — texto principal del logro
 */
function animAchievement(icon, title, text) {
  // Eliminar banner anterior si existe
  document.querySelectorAll('.achievement-banner').forEach(b => b.remove());

  const banner = document.createElement('div');
  banner.className = 'achievement-banner';
  banner.setAttribute('role', 'alert');
  banner.innerHTML = `
    <span class="achievement-icon" aria-hidden="true">${icon}</span>
    <div class="achievement-body">
      <div class="achievement-title">${title}</div>
      <div class="achievement-text">${text}</div>
    </div>
  `;
  document.body.appendChild(banner);
  // La animación CSS se encarga de la salida; limpiamos el DOM tras ella
  setTimeout(() => banner.remove(), 4000);
}

/**
 * Actualiza la barra visual de racha en el panel derecho.
 * La barra se llena hasta un máximo de 30 (racha "full").
 * @param {number} racha — valor actual de racha máxima
 */
function updateStreakBar(racha) {
  State.rachaActual = racha;
  const fill  = document.getElementById('streak-bar-fill');
  const count = document.getElementById('streak-bar-count');
  if (!fill) return;

  const MAX   = 30;
  const pct   = Math.min(100, (racha / MAX) * 100);
  fill.style.width = `${pct}%`;

  if (count) count.textContent = racha;

  // Hito: múltiplo de 5
  if (racha > 0 && racha % 5 === 0) {
    fill.classList.add('streak-milestone');
    fill.addEventListener('animationend', () => fill.classList.remove('streak-milestone'), { once: true });
  }
}

/**
 * Aplica / quita el pulso del botón Jugar.
 * @param {boolean} active
 */
function setPulse(active) {
  const btn = document.getElementById('btn-play');
  if (!btn) return;
  if (active) btn.classList.add('btn-pulse');
  else        btn.classList.remove('btn-pulse');
}

/**
 * Ejecuta una transición fade-out → callback → fade-in en un elemento.
 * @param {Element} el
 * @param {Function} callback — se llama entre fade-out y fade-in
 */
function fadeTransition(el, callback) {
  el.classList.add('fade-out');
  el.addEventListener('animationend', () => {
    el.classList.remove('fade-out');
    callback();
    el.classList.add('fade-in');
    el.addEventListener('animationend', () => el.classList.remove('fade-in'), { once: true });
  }, { once: true });
}

// ── RENDER: mapa de zonas (panel izquierdo) ────────────────────────────────

function renderZonaMap(zonas) {
  const container = $('zone-map');
  container.innerHTML = '';

  if (!zonas || zonas.length === 0) {
    container.innerHTML = '<p style="color:var(--text-muted);padding:1rem;font-size:0.85rem">No se encontraron zonas.</p>';
    return;
  }

  zonas.forEach(zona => {
    const meta     = ZONA_META[zona.nombre] || { icon: '📦', orden: 99 };
    const locked   = zona.bloqueada;
    const complete = zona.completa;
    const pct      = zona.progreso_promedio || 0;

    const card = document.createElement('div');
    card.className = [
      'zone-card',
      locked   ? 'zone-locked'   : '',
      complete ? 'zone-complete' : '',
    ].filter(Boolean).join(' ');

    card.dataset.zona = zona.nombre;
    card.setAttribute('role', 'button');
    card.setAttribute('tabindex', locked ? '-1' : '0');
    card.setAttribute('aria-label',
      `Zona ${zona.nombre}${complete ? ' — completa' : ''}${locked ? ' — bloqueada' : ''}`);

    card.innerHTML = `
      <span class="zone-card-icon" aria-hidden="true">${locked ? '🔒' : meta.icon}</span>
      <div class="zone-card-body">
        <div class="zone-card-name">${zona.nombre}</div>
        <div class="zone-card-meta">${fmtNum(zona.xp)} XP · ${pct}%</div>
        <div class="zone-progress-bar">
          <div class="zone-progress-fill${complete ? ' complete' : ''}"
               style="width:${pct}%"></div>
        </div>
      </div>
      ${complete ? '<span aria-hidden="true" style="color:var(--color-success);font-size:1rem">✓</span>' : ''}
    `;

    if (!locked) {
      card.addEventListener('click',   () => seleccionarZona(zona.nombre));
      card.addEventListener('keydown', e => {
        if (e.key === 'Enter' || e.key === ' ') seleccionarZona(zona.nombre);
      });
    }

    container.appendChild(card);
  });
}

// ── RENDER: estadísticas globales (panel derecho) ──────────────────────────

function renderStats(stats) {
  const grid = $('stats-grid');
  grid.innerHTML = '';

  const items = [
    { icon: '⭐', label: 'XP Total',         value: fmtNum(stats.xp_total) },
    { icon: '🏆', label: 'Zonas completadas', value: `${stats.zonas_completadas} / ${stats.zonas_totales}` },
    { icon: '📚', label: 'Zonas iniciadas',   value: `${stats.zonas_iniciadas} / ${stats.zonas_totales}` },
  ];

  items.forEach(({ icon, label, value }) => {
    const card = document.createElement('div');
    card.className = 'stat-card';
    card.innerHTML = `
      <span class="stat-card-icon" aria-hidden="true">${icon}</span>
      <div class="stat-card-body">
        <div class="stat-card-value">${value}</div>
        <div class="stat-card-label">${label}</div>
      </div>
    `;
    grid.appendChild(card);
  });

  // Racha display + barra
  const streakEl = $('streak-display');
  $('streak-value').textContent = fmtNum(stats.racha_max_global);
  streakEl.style.display = 'flex';

  updateStreakBar(stats.racha_max_global);

  // XP en el header
  $('header-xp').textContent = fmtNum(stats.xp_total);

  // Guardar XP actual para calcular delta tras jugar
  State.xpAnterior = stats.xp_total;
}

// ── RENDER: welcome stats ──────────────────────────────────────────────────

function renderWelcomeStats(stats) {
  const container = $('welcome-stats');
  container.innerHTML = '';

  const items = [
    { value: fmtNum(stats.xp_total), label: 'XP Total' },
    { value: `${stats.zonas_completadas}/${stats.zonas_totales}`, label: 'Zonas' },
    { value: String(stats.racha_max_global), label: 'Racha' },
  ];

  items.forEach(({ value, label }) => {
    const div = document.createElement('div');
    div.className = 'welcome-stat';
    div.innerHTML = `
      <div class="welcome-stat-value">${value}</div>
      <div class="welcome-stat-label">${label}</div>
    `;
    container.appendChild(div);
  });
}

// ── RENDER: detalle de zona (panel central) ────────────────────────────────

function renderZonaDetalle(nombre, detalle) {
  const detailEl  = $('zone-detail');
  const welcomeEl = $('welcome-card');

  // Ocultar la bienvenida con fade, luego mostrar detalle con fade-in
  welcomeEl.classList.add('hidden');
  detailEl.classList.remove('hidden');

  const doRender = () => {
    // Nombre y badges
    $('detail-name').textContent          = nombre;
    $('detail-xp').textContent            = `${fmtNum(detalle.resumen.xp)} XP`;
    $('detail-progress').textContent      = `${detalle.resumen.progreso_promedio}%`;
    $('play-title').innerHTML =
      `<span class="panel-icon" aria-hidden="true">${ZONA_META[nombre]?.icon || '🎮'}</span> ${nombre}`;

    // Inyectar el botón de Teoría
    const playArea = document.querySelector('.play-area');
    
    // Eliminamos si ya existía uno
    document.getElementById('btn-teoria-zone')?.remove();
    
    const btnTeoria = document.createElement('button');
    btnTeoria.id = 'btn-teoria-zone';
    btnTeoria.className = 'btn-teoria';
    btnTeoria.innerHTML = '📖 Estudiar Lección (Teoría)';
    btnTeoria.onclick = () => abrirModalTeoria(nombre);

    // Lo insertamos antes de la grilla de fases
    const gridWrapper = $('phase-grid').parentElement; 
    gridWrapper.insertBefore(btnTeoria, $('phase-grid'));

      // Grid de fases
    const phaseGrid = $('phase-grid');
    phaseGrid.innerHTML = '';

    const fases    = detalle.progreso?.fases || {};
    const faseKeys = ['f1', 'f2', 'f3', 'jefe'];

    faseKeys.forEach(key => {
      const meta     = FASE_META[key];
      const faseDato = fases[key] || {};
      const aprobada = faseDato.aprobada || false;
      const puntaje  = faseDato.mejor_puntaje ?? '–';
      const xp       = faseDato.xp_ganada ?? 0;

      const card = document.createElement('div');
      card.className = `phase-card${aprobada ? ' phase-approved' : ''}`;
      card.dataset.phase = key;
      card.setAttribute('role', 'button');
      card.setAttribute('tabindex', '0');
      card.setAttribute('aria-label', `${meta.nombre}${aprobada ? ', aprobada' : ''}`);

      const scoreClass = (typeof puntaje === 'number' && puntaje >= 85) ? 'high' : '';

      card.innerHTML = `
        <div class="phase-icon" aria-hidden="true">${meta.icon}</div>
        <div class="phase-name">${meta.nombre}</div>
        <div class="phase-score ${scoreClass}">
          ${puntaje !== '–' ? `${puntaje}% · ${fmtNum(xp)} XP` : 'Sin jugar'}
        </div>
      `;

      card.addEventListener('click',   () => seleccionarFase(key, card));
      card.addEventListener('keydown', e => {
        if (e.key === 'Enter' || e.key === ' ') seleccionarFase(key, card);
      });

      phaseGrid.appendChild(card);
    });

    // Reset botón jugar y output
    const btnPlay = $('btn-play');
    btnPlay.disabled  = true;
    btnPlay.innerHTML = '<span aria-hidden="true">▶</span> Selecciona una fase';
    setPulse(false);
    State.faseActiva = null;

    $('play-output').classList.add('hidden');
  };

  // Si ya hay contenido visible, fade out→in; si no, directo
  if (!detailEl.classList.contains('hidden') && detailEl.querySelector('.zone-detail-header')) {
    fadeTransition(detailEl, doRender);
  } else {
    doRender();
    detailEl.classList.add('fade-in');
    detailEl.addEventListener('animationend', () => detailEl.classList.remove('fade-in'), { once: true });
  }
}

// ── ACCIÓN: seleccionar zona ───────────────────────────────────────────────

async function seleccionarZona(nombre) {
  if (State.jugando) return;
  if (State.zonaActiva === nombre) return;

  State.zonaActiva = nombre;
  State.faseActiva = null;

  // Persistir última zona jugada
  ThemeManager.setLastZone(nombre);

  // Marcar zona activa en el mapa
  document.querySelectorAll('.zone-card').forEach(card => {
    card.classList.toggle('zone-active', card.dataset.zona === nombre);
  });

  // Mostrar loader en el panel central
  $('welcome-card').classList.add('hidden');
  $('zone-detail').classList.add('hidden');
  const playArea = document.querySelector('.play-area');

  // Eliminar loader previo si existe
  document.getElementById('detail-loader')?.remove();

  const loader = document.createElement('div');
  loader.id        = 'detail-loader';
  loader.className = 'loading-state fade-in';
  loader.innerHTML = '<span class="spinner"></span> Cargando zona…';
  playArea.appendChild(loader);

  try {
    const data = await apiGet(`/api/zona/${encodeURIComponent(nombre)}`);
    loader.remove();
    renderZonaDetalle(nombre, data);
  } catch (err) {
    loader.remove();
    $('welcome-card').classList.remove('hidden');
    mostrarError(`No se pudo cargar la zona "${nombre}": ${err.message}`);
  }
}

// ── ACCIÓN: seleccionar fase ───────────────────────────────────────────────

function seleccionarFase(faseKey, cardEl) {
  if (State.jugando) return;

  State.faseActiva = faseKey;

  document.querySelectorAll('.phase-card').forEach(c => c.classList.remove('phase-active'));
  cardEl.classList.add('phase-active');

  const btnPlay  = $('btn-play');
  const meta     = FASE_META[faseKey];
  btnPlay.disabled  = false;
  btnPlay.innerHTML = `<span aria-hidden="true">${meta.icon}</span> Jugar: ${meta.nombre}`;

  // Activar pulso en el botón
  setPulse(true);
}

// ── ACCIÓN: jugar fase — JUEGO INTERACTIVO ────────────────────────────────

async function jugarFase() {
  if (!State.zonaActiva || !State.faseActiva || State.jugando) return;

  State.jugando = true;
  setPulse(false);

  // ── Paso 1: Obtener la ronda del servidor ────────────────────────────────
  const btnPlay = $('btn-play');
  const labelOriginal = btnPlay.innerHTML;
  btnPlay.disabled  = true;
  btnPlay.innerHTML = '<span class="spinner" aria-hidden="true"></span> Cargando preguntas…';

  // Snapshot para detectar zona recién completada al final
  const zonaAntes   = State.zonas.find(z => z.nombre === State.zonaActiva);
  const eraCompleta = zonaAntes?.completa || false;

  let ronda;
  try {
    ronda = await apiPost(`/api/jugar/${encodeURIComponent(State.zonaActiva)}/${State.faseActiva}`);
  } catch (err) {
    mostrarError(`No se pudo iniciar la ronda: ${err.message}`);
    State.jugando     = false;
    btnPlay.disabled  = false;
    btnPlay.innerHTML = labelOriginal;
    setPulse(true);
    return;
  }

  const preguntas = ronda.preguntas || [];
  if (!preguntas.length) {
    mostrarError('La ronda llegó vacía. Revisa el motor web.');
    State.jugando     = false;
    btnPlay.disabled  = false;
    btnPlay.innerHTML = labelOriginal;
    setPulse(true);
    return;
  }

  // ── Paso 2: Estado local de la partida ───────────────────────────────────
  let indiceActual   = 0;
  let aciertos       = 0;
  let errores        = 0;
  let rachaActual    = 0;
  let rachaMaxima    = 0;
  let xpGanada       = 0;
  let respuestasErroneas = [];   // [{palabra, tu_respuesta}]
  const XP_ACIERTO   = 10;
  const XP_BONUS_VEL = 5;       // bonus si < 2 s
  const XP_ERROR     = -3;
  let tiempoInicioPregunta = Date.now();

  // ── Helpers de UI de juego ───────────────────────────────────────────────
  const playArea = document.querySelector('.play-area');

  /** Reemplaza el contenido del play-area con un elemento. */
  function _setPlayContent(el) {
    // Ocultar welcome y zone-detail
    $('welcome-card').classList.add('hidden');
    $('zone-detail').classList.add('hidden');
    // Limpiar contenido anterior del juego
    playArea.querySelectorAll('.juego-root').forEach(e => e.remove());
    el.classList.add('juego-root');
    playArea.appendChild(el);
  }

  /** Crea y muestra el feedback (correcto/incorrecto) sobre la tarjeta. */
  function _mostrarFeedback(correcto, textoExtra, container) {
    const fb = document.createElement('div');
    fb.className = `feedback ${correcto ? 'feedback-ok' : 'feedback-err'}`;
    fb.setAttribute('aria-live', 'assertive');
    fb.textContent = correcto ? `✅ ¡Correcto! ${textoExtra}` : `❌ Era: ${textoExtra}`;
    container.appendChild(fb);
    // Forzar reflow para que la animación se dispare
    void fb.offsetWidth;
    fb.classList.add('visible');
    return fb;
  }

  /** Actualiza el marcador live (racha, XP, aciertos) en la tarjeta. */
  function _actualizarMarcador(marcadorEl) {
    if (!marcadorEl) return;
    marcadorEl.innerHTML = `
      <span class="marcador-item">✅ ${aciertos}</span>
      <span class="marcador-item">❌ ${errores}</span>
      <span class="marcador-item">🔥 ${rachaActual}</span>
      <span class="marcador-item">⭐ ${xpGanada}</span>
    `;
  }

  // ── Paso 3: Motor de preguntas ───────────────────────────────────────────

  /** Renderiza la pregunta actual y espera la respuesta del usuario. */
  function _renderPregunta(pregunta, num, total) {
    return new Promise(resolve => {
      tiempoInicioPregunta = Date.now();

      const card = document.createElement('div');
      card.className = 'pregunta-card fade-in';

      // Cabecera de progreso
      const pct = Math.round((num / total) * 100);
      card.innerHTML = `
        <div class="pregunta-progress">
          <div class="pregunta-progress-bar" style="width:${pct}%"></div>
        </div>
        <div class="pregunta-header">
          <span class="pregunta-numero">${num + 1} / ${total}</span>
          <span class="pregunta-contexto">${pregunta.contexto || ''}</span>
        </div>
        <div class="marcador-live" id="marcador-live"></div>
        <p class="pregunta-texto">${pregunta.pregunta}</p>
        <div class="pregunta-opciones" id="pregunta-opciones"></div>
        <div class="pregunta-feedback-zona"></div>
      `;

      _setPlayContent(card);
      _actualizarMarcador(card.querySelector('#marcador-live'));

      const opcionesEl  = card.querySelector('#pregunta-opciones');
      const feedbackZona = card.querySelector('.pregunta-feedback-zona');

      /** Llamada al evaluador y avance. */
      async function _evaluar(respuestaTexto, inputsEl) {
        // Deshabilitar interacción
        card.querySelectorAll('button, input').forEach(el => (el.disabled = true));

        let correcto;
        try {
          const res = await fetch('/api/evaluar', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ pregunta, respuesta: respuestaTexto }),
          });
          const data = await res.json();
          correcto = data.correcto;
        } catch (_) {
          // Fallback local si el endpoint falla
          correcto = respuestaTexto.trim().toLowerCase() ===
                     pregunta.respuesta_correcta.trim().toLowerCase();
        }

        const elapsed = (Date.now() - tiempoInicioPregunta) / 1000;
        const bonus   = (!correcto || elapsed >= 2) ? 0 : XP_BONUS_VEL;

        if (correcto) {
          aciertos++;
          rachaActual++;
          if (rachaActual > rachaMaxima) rachaMaxima = rachaActual;
          const xpEsta = XP_ACIERTO + rachaActual * 2 + bonus;
          xpGanada += xpEsta;
          _mostrarFeedback(true, bonus > 0 ? `+${xpEsta} XP ⚡` : `+${xpEsta} XP`, feedbackZona);
          // Colorear botón/input correcto
          if (inputsEl) inputsEl.classList.add('input-correcta');
        } else {
          errores++;
          rachaActual = 0;
          xpGanada    = Math.max(0, xpGanada + XP_ERROR);
          _mostrarFeedback(false, pregunta.respuesta_correcta, feedbackZona);
          respuestasErroneas.push({
            palabra:       pregunta.respuesta_correcta,
            tu_respuesta:  respuestaTexto,
          });
          // Colorear botón/input incorrecto
          if (inputsEl) inputsEl.classList.add('input-incorrecta');
        }

        // Actualizar marcador en vivo y barra de racha lateral
        _actualizarMarcador(card.querySelector('#marcador-live'));
        updateStreakBar(rachaMaxima);

        // Esperar 1.5 s y avanzar
        setTimeout(() => resolve(correcto), 1500);
      }

      // ── Renderizar según tipo ──────────────────────────────────────────
      if (pregunta.tipo === 'opcion_multiple') {
        (pregunta.opciones || []).forEach(opcion => {
          const btn = document.createElement('button');
          btn.className  = 'opcion-btn';
          btn.textContent = opcion;
          btn.addEventListener('click', () => _evaluar(opcion, btn));
          opcionesEl.appendChild(btn);
        });

      } else if (pregunta.tipo === 'inverso') {
        // DOS inputs: pronunciación + traducción
        const wrap = document.createElement('div');
        wrap.className = 'input-grupo';
        wrap.innerHTML = `
          <input class="input-neon" id="inp-pron" type="text"
                 placeholder="Pronunciación…" autocomplete="off" />
          <input class="input-neon" id="inp-trad" type="text"
                 placeholder="Traducción…" autocomplete="off" />
          <button class="btn btn-primary confirmar-btn" id="btn-confirmar">
            Confirmar ↵
          </button>
        `;
        opcionesEl.appendChild(wrap);

        const inpPron = wrap.querySelector('#inp-pron');
        const inpTrad = wrap.querySelector('#inp-trad');
        const btnConf = wrap.querySelector('#btn-confirmar');

        const confirmarInverso = () => {
          const val = `${inpPron.value.trim()}, ${inpTrad.value.trim()}`;
          _evaluar(val, wrap);
        };
        btnConf.addEventListener('click', confirmarInverso);
        [inpPron, inpTrad].forEach(inp => {
          inp.addEventListener('keydown', e => { if (e.key === 'Enter') confirmarInverso(); });
        });
        inpPron.focus();

      } else {
        // tipo='escribir' (default)
        const wrap = document.createElement('div');
        wrap.className = 'input-grupo';
        wrap.innerHTML = `
          <input class="input-neon" id="inp-escribir" type="text"
                 placeholder="Escribe tu respuesta…" autocomplete="off" />
          <button class="btn btn-primary confirmar-btn" id="btn-confirmar">
            Confirmar ↵
          </button>
        `;
        opcionesEl.appendChild(wrap);

        const inp     = wrap.querySelector('#inp-escribir');
        const btnConf = wrap.querySelector('#btn-confirmar');

        const confirmarEscribir = () => _evaluar(inp.value, inp);
        btnConf.addEventListener('click', confirmarEscribir);
        inp.addEventListener('keydown', e => { if (e.key === 'Enter') confirmarEscribir(); });
        inp.focus();
      }
    });
  }

  // ── Paso 4: Bucle principal de preguntas ─────────────────────────────────
  for (let i = 0; i < preguntas.length; i++) {
    await _renderPregunta(preguntas[i], i, preguntas.length);
  }

  // ── Paso 5: Pantalla de resumen ──────────────────────────────────────────
  const totalPreguntas = preguntas.length;
  const porcentaje     = Math.round((aciertos / totalPreguntas) * 100);
  const aprobado       = porcentaje >= 80;

  const resumen = document.createElement('div');
  resumen.className = 'resumen-card fade-in';

  const iconoFinal = aprobado ? '🏆' : '📚';
  const tituloFinal = aprobado ? '¡Fase Superada!' : 'Sigue practicando';

  // Construir HTML del resumen
  let listaErrores = '';
  if (respuestasErroneas.length) {
    listaErrores = `
      <div class="resumen-errores">
        <h4 class="resumen-errores-titulo">📋 Palabras a repasar</h4>
        <ul class="errores-lista">
          ${respuestasErroneas.map(e =>
            `<li><span class="error-correcta">${e.palabra}</span>
                 <span class="error-sep">→</span>
                 <span class="error-dada">${e.tu_respuesta || '(vacío)'}</span>
             </li>`
          ).join('')}
        </ul>
      </div>`;
  }

  resumen.innerHTML = `
    <div class="resumen-icono" aria-hidden="true">${iconoFinal}</div>
    <h3 class="resumen-titulo">${tituloFinal}</h3>

    <div class="resumen-pct-wrap">
      <div class="resumen-pct-track">
        <div class="resumen-pct-fill ${aprobado ? 'aprobado' : 'no-aprobado'}"
             style="width:0%" data-pct="${porcentaje}"></div>
      </div>
      <span class="resumen-pct-num">${porcentaje}%</span>
    </div>

    <div class="resumen-stats">
      <div class="resumen-stat">
        <span class="resumen-stat-val">${aciertos}</span>
        <span class="resumen-stat-lbl">Aciertos</span>
      </div>
      <div class="resumen-stat">
        <span class="resumen-stat-val">${errores}</span>
        <span class="resumen-stat-lbl">Errores</span>
      </div>
      <div class="resumen-stat">
        <span class="resumen-stat-val">${rachaMaxima}</span>
        <span class="resumen-stat-lbl">Racha máx.</span>
      </div>
      <div class="resumen-stat">
        <span class="resumen-stat-val">+${xpGanada}</span>
        <span class="resumen-stat-lbl">XP Ganada</span>
      </div>
    </div>

    ${listaErrores}

    <div class="resumen-acciones">
      <button class="btn btn-secondary" id="btn-volver-mapa">🗺️ Volver al mapa</button>
      ${!aprobado ? '<button class="btn btn-primary" id="btn-repetir">🔁 Jugar de nuevo</button>' : ''}
    </div>
  `;

  _setPlayContent(resumen);

  // Animar la barra de porcentaje con un pequeño retraso para que el DOM esté listo
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      const fill = resumen.querySelector('.resumen-pct-fill');
      if (fill) fill.style.width = `${porcentaje}%`;
    });
  });

  // Animaciones globales de fin de partida
  if (aprobado) {
    animConfetti(40);
    animAchievement('🏆', aprobado ? '¡Fase Superada!' : 'Completada',
      `${porcentaje}% · +${xpGanada} XP · Racha ${rachaMaxima}`);
  } else {
    animAchievement('📚', 'Ronda terminada',
      `${porcentaje}% · +${xpGanada} XP`);
  }

  // Conectar botones del resumen
  resumen.querySelector('#btn-volver-mapa')?.addEventListener('click', async () => {
    State.jugando    = false;
    State.faseActiva = null;
    resumen.remove();
    // Volver a la vista de detalle de zona
    const detalle = await apiGet(`/api/zona/${encodeURIComponent(State.zonaActiva)}`);
    renderZonaDetalle(State.zonaActiva, detalle);
  });

  resumen.querySelector('#btn-repetir')?.addEventListener('click', () => {
    State.jugando = false;
    resumen.remove();
    jugarFase();   // relanzar la misma fase
  });

  // ── Guardar progreso en el servidor ─────────────────────────────────────
  const usuario = (typeof UserManager !== 'undefined') ? UserManager.getActivo() : null;
  const zonaNum = ZONAS_NUM[State.zonaActiva] || 0;

  if (usuario && zonaNum) {
    try {
      await fetch('/api/guardar-progreso', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          usuario,
          zona:         State.zonaActiva,
          num:          zonaNum,
          fase:         State.faseActiva,
          porcentaje,
          xp_ganada:    xpGanada,
          racha_maxima: rachaMaxima,
          errores:      respuestasErroneas,
        }),
      });
    } catch (e) {
      console.warn('[jugarFase] No se pudo guardar progreso:', e.message);
    }
  }

  // Recargar stats y mapa para reflejar el nuevo progreso
  try {
    const statsNuevos = await apiGet('/api/stats');
    renderStats(statsNuevos);
    animXpFloat(xpGanada, $('header-xp'));

    const zonasNuevas = await apiGet('/api/zonas');
    State.zonas = zonasNuevas.zonas || [];
    renderZonaMap(State.zonas);

    const zonaAhora = State.zonas.find(z => z.nombre === State.zonaActiva);
    if (!eraCompleta && zonaAhora?.completa) {
      setTimeout(() => animConfetti(60), 300);
      setTimeout(() => animAchievement('🏆', '¡Zona Completada!',
        `${ZONA_META[State.zonaActiva]?.icon || ''} ${State.zonaActiva}`), 900);
    }
  } catch (_) { /* no crítico */ }

  State.jugando = false;
}

// ── Mapa zona → número (necesario para guardar progreso) ──────────────────
const ZONAS_NUM = {
  'Alfabeto':       1,
  'Números':        2,
  'Colores':        3,
  'Días':           4,
  'Meses':          5,
  'Saludos':        6,
  'Pronombres':     7,
  'Familia':        8,
  'Objetos':        9,
  'Interrogativas': 10,
  'Adjetivos':      11,
  'G1 - Pronombres': 12,
  'G2 - Verbo To Be': 13,
  'G3 - Artículos A-An': 14,
  'G4 - Plurales': 15,
  'G5 - This-That': 16,
  'G6 - Wh-Questions': 17,
};

// ── MENSAJES DE ERROR (toast) ──────────────────────────────────────────────

function mostrarError(msg) {
  console.error('[App]', msg);
  const toast = document.createElement('div');
  toast.style.cssText = `
    position:fixed;bottom:1.5rem;right:1.5rem;z-index:9999;
    background:var(--color-danger);color:#fff;padding:0.7rem 1.2rem;
    border-radius:8px;font-size:0.85rem;box-shadow:0 4px 20px rgba(0,0,0,0.5);
    animation:fade-in-up 0.2s ease;
  `;
  toast.textContent = msg;
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 5000);
}

// ── CARGA INICIAL DE DATOS ─────────────────────────────────────────────────

async function cargarDatosIniciales() {
  // Mostrar nombre del usuario activo en la tarjeta de bienvenida
  const perfil = (typeof UserManager !== 'undefined') ? UserManager.getActivoPerfil() : null;
  const heading = document.querySelector('.welcome-heading');
  if (heading && perfil) {
    heading.textContent = `¡Bienvenido, ${perfil.nombre_mostrar || perfil.nombre}!`;
  }

  const [zonasData, statsData] = await Promise.allSettled([
    apiGet('/api/zonas'),
    apiGet('/api/stats'),
  ]);

  if (zonasData.status === 'fulfilled') {
    State.zonas = zonasData.value.zonas || [];
    renderZonaMap(State.zonas);
  } else {
    $('zone-map').innerHTML =
      `<p style="color:var(--color-danger);padding:1rem;font-size:0.85rem">
        Error cargando zonas: ${zonasData.reason?.message}
      </p>`;
  }

  if (statsData.status === 'fulfilled') {
    renderStats(statsData.value);
    renderWelcomeStats(statsData.value);
  } else {
    $('stats-grid').innerHTML =
      `<p style="color:var(--color-danger);padding:0.5rem;font-size:0.82rem">
        Error cargando stats
      </p>`;
  }
}

// ── INICIALIZACIÓN ─────────────────────────────────────────────────────────

async function _arrancar() {
  // Conectar botón de jugar
  $('btn-play').addEventListener('click', jugarFase);

  // Cargar datos desde la API (el usuario ya está resuelto por UserManager)
  await cargarDatosIniciales();

  // Decidir qué zona mostrar:
  // 1) Parámetro ?zona=... en la URL
  // 2) Última zona guardada en localStorage
  const params     = new URLSearchParams(window.location.search);
  const zonaParam  = params.get('zona');
  const zonaUltima = ThemeManager.getLastZone();
  const zonaInicio = zonaParam || zonaUltima;

  if (zonaInicio && State.zonas.find(z => z.nombre === zonaInicio)) {
    await seleccionarZona(zonaInicio);
  }
}

// ── FUNCIÓN PARA MOSTRAR LA TEORÍA ────────────────────────────────────────
async function abrirModalTeoria(zonaNombre) {
    try {
        const data = await apiGet(`/api/teoria/${encodeURIComponent(zonaNombre)}`);
        
        let htmlTabla = '';
        if (data.tabla && data.tabla.length > 0) {
            htmlTabla = `<table class="tabla-teoria">
                <tr><th>Inglés</th><th>Pronunciación</th><th>Español</th></tr>
                ${data.tabla.map(f => `<tr><td>${f.en}</td><td>${f.pron}</td><td>${f.es}</td></tr>`).join('')}
            </table>`;
        }

        const modalHTML = `
            <div class="modal-overlay" onclick="this.remove()">
                <div class="modal-content" onclick="event.stopPropagation()">
                    <h2>${data.titulo}</h2>
                    <p>${data.explicacion}</p>
                    ${htmlTabla}
                    <button onclick="this.closest('.modal-overlay').remove()" class="btn-cerrar">Cerrar y Jugar</button>
                </div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', modalHTML);
    } catch (e) {
        mostrarError("Error cargando la teoría: " + e.message);
    }
}

document.addEventListener('DOMContentLoaded', async () => {
  // Esperar a que UserManager resuelva el usuario antes de cargar datos
  if (typeof UserManager !== 'undefined') {
    await UserManager.init();
    // Recargar datos cuando cambie el usuario activo
    document.addEventListener('eq:usuario-cambiado', async (e) => {
      State.zonaActiva = null;
      State.faseActiva = null;
      // Volver a welcome screen
      document.getElementById('zone-detail')?.classList.add('hidden');
      document.getElementById('welcome-card')?.classList.remove('hidden');
      document.querySelectorAll('.zone-card').forEach(c => c.classList.remove('zone-active'));
      await cargarDatosIniciales();
    });
  }
  await _arrancar();
});
