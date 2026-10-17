/**
 * theme_manager.js — v2
 * ─────────────────────────────────────────────────────────────
 * Gestiona el sistema de temas de English Quest.
 *
 * Novedades v2:
 *   - Modo Sorpresa: al cargar la página, 10% de probabilidad de aplicar
 *     un tema aleatorio (excluye el preferido por el usuario).
 *   - localStorage para tema, modo sorpresa on/off y última zona jugada.
 *   - API pública ampliada: setSurpriseMode(), isSurprise(), setLastZone(),
 *     getLastZone().
 *   - El dropdown muestra una opción "🎲 Modo Sorpresa: ON/OFF" separada.
 *
 * Uso desde app.js:
 *   ThemeManager.apply('theme_halloween');
 *   ThemeManager.current();          // → 'theme_halloween'
 *   ThemeManager.isSurprise();       // → true/false
 *   ThemeManager.setSurpriseMode(false);
 *   ThemeManager.setLastZone('Alfabeto');
 *   ThemeManager.getLastZone();      // → 'Alfabeto' | null
 * ─────────────────────────────────────────────────────────────
 */

const ThemeManager = (() => {
  // ── Configuración de temas ─────────────────────────────────────────────
  const THEMES = {
    theme_default: {
      label:      '🌌 Cyberpunk',
      headerIcon: '⚔️',
      welcomeIcon:'⚔️',
      decos: ['⚡', '🔷', '◈', '▸', '⬡', '⚡', '◈'],
    },
    theme_halloween: {
      label:      '🎃 Halloween',
      headerIcon: '🎃',
      welcomeIcon:'👻',
      decos: ['🎃', '👻', '🦇', '🕷️', '🕸️', '🎃', '💀'],
    },
    theme_christmas: {
      label:      '❄️ Christmas',
      headerIcon: '🎄',
      welcomeIcon:'🎁',
      decos: ['❄️', '🎄', '🎁', '⭐', '🔔', '❄️', '🎅'],
    },
  };

  const THEME_KEYS      = Object.keys(THEMES);
  const STORAGE_THEME   = 'eq_theme';
  const STORAGE_SURPRISE= 'eq_surprise';   // 'on' | 'off'
  const STORAGE_ZONE    = 'eq_last_zone';
  const DEFAULT_THEME   = 'theme_default';
  const DECO_CLASS      = 'theme-deco';
  const DECO_COUNT      = 8;
  const SURPRISE_CHANCE = 0.10;            // 10 %

  // ── Lectura de preferencias ────────────────────────────────────────────
  function getSaved() {
    const saved = localStorage.getItem(STORAGE_THEME);
    return (saved && THEMES[saved]) ? saved : DEFAULT_THEME;
  }

  function isSurprise() {
    // Por defecto ON si nunca se ha guardado la preferencia
    return localStorage.getItem(STORAGE_SURPRISE) !== 'off';
  }

  function setSurpriseMode(enabled) {
    localStorage.setItem(STORAGE_SURPRISE, enabled ? 'on' : 'off');
    _syncSurpriseCheckbox();
  }

  function getLastZone() {
    return localStorage.getItem(STORAGE_ZONE) || null;
  }

  function setLastZone(nombre) {
    if (nombre) localStorage.setItem(STORAGE_ZONE, nombre);
  }

  // ── Aplicar un tema ────────────────────────────────────────────────────
  /**
   * @param {string} themeKey  - clave del tema
   * @param {boolean} persist  - si false, NO guarda en localStorage
   *                             (usado para el tema sorpresa temporal)
   */
  function apply(themeKey, persist = true) {
    if (!THEMES[themeKey]) {
      console.warn(`[ThemeManager] Tema desconocido: "${themeKey}". Usando default.`);
      themeKey = DEFAULT_THEME;
    }

    const meta = THEMES[themeKey];

    // 1. Cambiar el <link> de hoja de estilo
    const link = document.getElementById('theme-stylesheet');
    if (link) link.href = `styles/${themeKey}.css`;

    // 2. Marcar el body con data-theme para los selectores CSS
    document.body.setAttribute('data-theme', themeKey);

    // 3. Sincronizar el dropdown de temas (solo si persiste)
    if (persist) {
      const select = document.getElementById('theme-select');
      if (select && select.value !== themeKey) select.value = themeKey;
    }

    // 4. Actualizar iconos dinámicos del tema
    _updateIcons(meta);

    // 5. Reemplazar decoraciones flotantes
    _injectDecos(meta.decos);

    // 6. Guardar en localStorage solo si es una elección permanente
    if (persist) localStorage.setItem(STORAGE_THEME, themeKey);
  }

  // ── Modo Sorpresa ──────────────────────────────────────────────────────
  /**
   * Si el modo sorpresa está activo y la ruleta acierta (10%),
   * aplica un tema aleatorio (distinto al preferido) SIN guardarlo,
   * y muestra un banner informativo.
   * Devuelve true si se aplicó el tema sorpresa.
   */
  function tryApplySurprise() {
    if (!isSurprise()) return false;
    if (Math.random() > SURPRISE_CHANCE) return false;

    const preferred = getSaved();
    const options   = THEME_KEYS.filter(k => k !== preferred);
    const pick      = options[Math.floor(Math.random() * options.length)];

    // Aplicar sin persistir (el dropdown no cambia)
    apply(pick, false);

    // Mostrar banner de aviso
    _showSurpriseBanner(THEMES[pick].label);

    return true;
  }

  // ── Helpers privados ───────────────────────────────────────────────────
  function _updateIcons(meta) {
    const headerIcon  = document.getElementById('header-icon');
    const welcomeIcon = document.getElementById('welcome-icon');
    if (headerIcon)  headerIcon.textContent  = meta.headerIcon;
    if (welcomeIcon) welcomeIcon.textContent = meta.welcomeIcon;
  }

  function _injectDecos(symbols) {
    document.querySelectorAll(`.${DECO_CLASS}`).forEach(el => el.remove());

    for (let i = 0; i < DECO_COUNT; i++) {
      const el = document.createElement('span');
      el.className   = DECO_CLASS;
      el.textContent = symbols[i % symbols.length];
      el.setAttribute('aria-hidden', 'true');

      el.style.left      = `${Math.random() * 95}vw`;
      el.style.top       = `${Math.random() * 90}vh`;
      el.style.fontSize  = `${1.2 + Math.random() * 1.2}rem`;

      const dur   = 5 + Math.random() * 5;
      const delay = -(Math.random() * dur);
      el.style.animationDuration = `${dur}s`;
      el.style.animationDelay   = `${delay}s`;

      document.body.appendChild(el);
    }
  }

  function _showSurpriseBanner(themeLabel) {
    const banner = document.createElement('div');
    banner.className   = 'surprise-banner';
    banner.textContent = `🎲 ¡Modo Sorpresa activado! Tema: ${themeLabel}`;
    banner.setAttribute('aria-live', 'polite');
    document.body.appendChild(banner);
    // Limpiar tras la animación (4 s entrada + 0.4 s salida + margen)
    setTimeout(() => banner.remove(), 5000);
  }

  function _syncSurpriseCheckbox() {
    // Actualiza el label del option de sorpresa si existe
    const opt = document.getElementById('surprise-option');
    if (opt) opt.textContent = isSurprise() ? '🎲 Sorpresa: ON' : '🎲 Sorpresa: OFF';
  }

  // ── Inicialización ─────────────────────────────────────────────────────
  function init() {
    const saved = getSaved();

    // 1. Aplicar tema preferido guardado (evita FOUC)
    apply(saved);

    // 2. Intentar modo sorpresa (sobreescribe temporalmente)
    tryApplySurprise();

    // 3. Sincronizar option de sorpresa
    _syncSurpriseCheckbox();

    // 4. Escuchar cambios en el dropdown de temas
    const select = document.getElementById('theme-select');
    if (select) {
      select.addEventListener('change', (e) => {
        const val = e.target.value;
        if (val === '__surprise_toggle__') {
          // Toggle del modo sorpresa
          setSurpriseMode(!isSurprise());
          // Restaurar el dropdown al tema actual
          select.value = getSaved();
        } else {
          apply(val);
        }
      });
    }
  }

  // ── API pública ────────────────────────────────────────────────────────
  return {
    init,
    apply,
    current:         getSaved,
    isSurprise,
    setSurpriseMode,
    getLastZone,
    setLastZone,
    themes:          THEMES,
  };
})();

// Ejecutar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => ThemeManager.init());
