/**
 * theme_manager.js — v3 (Modo Neón Reactivo)
 */

const ThemeManager = (() => {
  // 1. Paleta de colores (Movido fuera del objeto THEMES)
  const NEON_COLORS = ['#00e5ff', '#ff00ff', '#39ff7e', '#ffcc00', '#ff3d71', '#a78bfa'];

  // 2. Configuración de temas
  const THEMES = {
    theme_default: {
      label:      '🌌 Cyberpunk',
      headerIcon: '⚔️',
      welcomeIcon:'⚔️',
      decos: ['⚡', '🔷', '◈', '▸', '⬡', '⚡', '◈'],
      confetti: ['★', '✦', '◆', '▲', '●', '✱', '❋', '⬟', '✿', '❂'] // Confeti Cyberpunk
    },
    theme_halloween: {
      label:      '🎃 Halloween',
      headerIcon: '🎃',
      welcomeIcon:'👻',
      decos: ['🎃', '👻', '🦇', '🕷️', '🕸️', '💀', '🧙‍♂️', '🧪'],
      confetti: ['🎃', '👻', '🦇', '💀', '🕷️', '🕸️', '🍬'] // Confeti Halloween
    },
    theme_christmas: {
      label:      '❄️ Christmas',
      headerIcon: '🎄',
      welcomeIcon:'🎁',
      decos: ['❄️', '🎄', '🎁', '⭐', '🔔', '❄️', '🎅'],
      confetti: ['❄️', '🎁', '⭐', '🔔', '🎄', '🍬'] // Confeti Navidad
    },
  };

  const THEME_KEYS      = Object.keys(THEMES);
  const STORAGE_THEME   = 'eq_theme';
  const STORAGE_SURPRISE= 'eq_surprise';
  const STORAGE_ZONE    = 'eq_last_zone';
  const DEFAULT_THEME   = 'theme_default';
  const DECO_CLASS      = 'theme-deco';
  const DECO_COUNT      = 8;

  // ── Lectura de preferencias ────────────────────────────────────────────
  function getSaved() {
    const saved = localStorage.getItem(STORAGE_THEME);
    return (saved && THEMES[saved]) ? saved : DEFAULT_THEME;
  }

  function isSurprise() {
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
  function apply(themeKey, persist = true) {
    if (!THEMES[themeKey]) {
      console.warn(`[ThemeManager] Tema desconocido: "${themeKey}". Usando default.`);
      themeKey = DEFAULT_THEME;
    }

    const meta = THEMES[themeKey];

    // 1. Cambiar el <link> de hoja de estilo
    const link = document.getElementById('theme-stylesheet');
    if (link) link.href = `styles/${themeKey}.css`;

    // 2. Marcar el body
    document.body.setAttribute('data-theme', themeKey);

    // 3. Sincronizar el dropdown
    if (persist) {
      const select = document.getElementById('theme-select');
      if (select && select.value !== themeKey) select.value = themeKey;
    }

    // 4. Actualizar iconos y decoraciones
    _updateIcons(meta);
    _injectDecos(meta.decos);

    // 5. Guardar en localStorage solo si es una elección permanente
    if (persist) localStorage.setItem(STORAGE_THEME, themeKey);
    
    // 6. Limpiar colores neón si se cambia a un tema normal
    if (themeKey !== 'theme_default') {
        document.documentElement.style.removeProperty('--accent');
        document.documentElement.style.removeProperty('--glow-accent');
        document.documentElement.style.removeProperty('--glow-accent-strong');
    }
  }

  // ── Modo Neón Reactivo ──────────────────────────────────────────────────
  function tryApplySurprise() {
    if (!isSurprise()) return false;
    applyNeonMode();
    return true;
  }

  function applyNeonMode() {
    const randomColor = NEON_COLORS[Math.floor(Math.random() * NEON_COLORS.length)];
    document.documentElement.style.setProperty('--accent', randomColor);
    document.documentElement.style.setProperty('--glow-accent', `0 0 8px ${randomColor}55`);
    document.documentElement.style.setProperty('--glow-accent-strong', `0 0 18px ${randomColor}aa`);
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

  function _syncSurpriseCheckbox() {
    const opt = document.getElementById('surprise-option');
    if (opt) opt.textContent = isSurprise() ? '🎲 Sorpresa: ON' : '🎲 Sorpresa: OFF';
  }

  // ── Inicialización ─────────────────────────────────────────────────────
  function init() {
    // Escuchar cuando el juego pide un cambio de neón
    document.addEventListener('eq:neon-change', () => {
        applyNeonMode();
    });

    const saved = getSaved();
    apply(saved);
    tryApplySurprise();
    _syncSurpriseCheckbox();

    const select = document.getElementById('theme-select');
    if (select) {
      select.addEventListener('change', (e) => {
        const val = e.target.value;
        if (val === '__surprise_toggle__') {
          setSurpriseMode(!isSurprise());
          select.value = getSaved();
        } else {
          apply(val);
        }
      });
    }
  }

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

document.addEventListener('DOMContentLoaded', () => ThemeManager.init());