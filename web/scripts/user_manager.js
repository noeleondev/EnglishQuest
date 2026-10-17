/**
 * user_manager.js — v1
 * ─────────────────────────────────────────────────────────────
 * Gestiona el sistema multi-usuario de English Quest.
 *
 * Responsabilidades:
 *   1. Detectar si hay un usuario activo en localStorage.
 *   2. Si no hay, mostrar el modal de bienvenida.
 *   3. Crear nuevo usuario (POST /api/usuarios/crear).
 *   4. Cargar usuario existente (GET /api/usuarios).
 *   5. Cambiar de usuario, reiniciar progreso, eliminar usuario.
 *   6. Mantener el header actualizado con el nombre/avatar.
 *   7. Exponer UserManager como global para app.js.
 *
 * Uso desde app.js:
 *   await UserManager.init();
 *   UserManager.getActivo();         // → "Mr_Leon"
 *   UserManager.getActivoPerfil();   // → { nombre, nombre_mostrar, avatar, ... }
 *   UserManager.apiParam();          // → "?usuario=Mr_Leon"
 * ─────────────────────────────────────────────────────────────
 */

const UserManager = (() => {
  const STORAGE_KEY = 'eq_usuario';   // nombre interno del usuario activo
  const AVATARS     = ['🎮','⚔️','🏆','🎯','🌟','🦄','🐉','🔮','🎭','🦊'];

  let _perfilActivo = null;           // cache del perfil del usuario activo

  // ── localStorage ──────────────────────────────────────────────────────────

  function getActivo() {
    return localStorage.getItem(STORAGE_KEY) || null;
  }

  function _setActivo(nombre) {
    localStorage.setItem(STORAGE_KEY, nombre);
  }

  function _clearActivo() {
    localStorage.removeItem(STORAGE_KEY);
  }

  function getActivoPerfil() {
    return _perfilActivo;
  }

  /** Devuelve "?usuario=<nombre>" para añadir a las URLs de la API. */
  function apiParam() {
    const u = getActivo();
    return u ? `?usuario=${encodeURIComponent(u)}` : '';
  }

  // ── API calls ──────────────────────────────────────────────────────────────

  async function _fetchJSON(url, opts = {}) {
    const res = await fetch(url, {
      headers: { 'Content-Type': 'application/json' },
      ...opts,
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(data.error || `HTTP ${res.status}`);
    return data;
  }

  async function crearUsuario(nombre, nombreMostrar, avatar) {
    return _fetchJSON('/api/usuarios/crear', {
      method: 'POST',
      body: JSON.stringify({ nombre, nombre_mostrar: nombreMostrar, avatar }),
    });
  }

  async function listarUsuarios() {
    return _fetchJSON('/api/usuarios');
  }

  async function cargarPerfil(nombre) {
    return _fetchJSON(`/api/usuarios/${encodeURIComponent(nombre)}`);
  }

  async function eliminarUsuario(nombre) {
    return _fetchJSON(`/api/usuarios/${encodeURIComponent(nombre)}`, { method: 'DELETE' });
  }

  async function reiniciarProgreso(nombre) {
    return _fetchJSON(`/api/usuarios/${encodeURIComponent(nombre)}/reiniciar`, { method: 'POST' });
  }

  // ── Modal de bienvenida ───────────────────────────────────────────────────

  function _mostrarModal() {
    document.getElementById('user-modal')?.classList.remove('hidden');
    document.getElementById('user-modal-input')?.focus();
  }

  function _ocultarModal() {
    document.getElementById('user-modal')?.classList.add('hidden');
  }

  /** Rellena el select de usuarios existentes en el modal. */
  async function _rellenarListaUsuarios() {
    const selectEl = document.getElementById('modal-usuario-existente');
    if (!selectEl) return;
    try {
      const data = await listarUsuarios();
      const users = data.usuarios || [];
      selectEl.innerHTML = users.length === 0
        ? '<option value="">— Ninguno aún —</option>'
        : users.map(u =>
            `<option value="${u.nombre}">${u.avatar || '🎮'} ${u.nombre_mostrar || u.nombre}</option>`
          ).join('');
      document.getElementById('modal-cargar-btn')?.toggleAttribute('disabled', users.length === 0);
    } catch (_) {
      selectEl.innerHTML = '<option value="">Error cargando usuarios</option>';
    }
  }

  /** Construye el selector de avatares en el modal. */
  function _rellenarAvatares() {
    const wrap = document.getElementById('modal-avatares');
    if (!wrap) return;
    wrap.innerHTML = AVATARS.map((em, i) =>
      `<button type="button" class="avatar-btn${i === 0 ? ' selected' : ''}"
               data-avatar="${em}" aria-label="Avatar ${em}">${em}</button>`
    ).join('');
    wrap.querySelectorAll('.avatar-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        wrap.querySelectorAll('.avatar-btn').forEach(b => b.classList.remove('selected'));
        btn.classList.add('selected');
      });
    });
  }

  function _getAvatarSeleccionado() {
    return document.querySelector('#modal-avatares .avatar-btn.selected')?.dataset.avatar || '🎮';
  }

  // ── Actualizar UI del header ───────────────────────────────────────────────

  function _actualizarHeader(perfil) {
    const btnEl   = document.getElementById('user-btn');
    const nameEl  = document.getElementById('user-btn-name');
    const avatarEl= document.getElementById('user-btn-avatar');
    if (!btnEl) return;

    if (perfil) {
      if (nameEl)   nameEl.textContent  = perfil.nombre_mostrar || perfil.nombre;
      if (avatarEl) avatarEl.textContent = perfil.avatar || '🎮';
      btnEl.classList.remove('user-btn-empty');
    } else {
      if (nameEl)   nameEl.textContent  = 'Iniciar sesión';
      if (avatarEl) avatarEl.textContent = '👤';
      btnEl.classList.add('user-btn-empty');
    }
  }

  // ── Dropdown de usuario ───────────────────────────────────────────────────

  function _toggleDropdown() {
    const dd = document.getElementById('user-dropdown');
    if (!dd) return;
    const open = !dd.classList.contains('hidden');
    dd.classList.toggle('hidden', open);
    if (!open) {
      // Cerrar al hacer clic fuera
      setTimeout(() => {
        document.addEventListener('click', _cerrarDropdown, { once: true });
      }, 50);
    }
  }

  function _cerrarDropdown() {
    document.getElementById('user-dropdown')?.classList.add('hidden');
  }

  // ── Flujos de acción ──────────────────────────────────────────────────────

  /** Activa un usuario: carga perfil, guarda en localStorage, actualiza header. */
  async function activarUsuario(nombre) {
    try {
      _perfilActivo = await cargarPerfil(nombre);
      _setActivo(nombre);
      _actualizarHeader(_perfilActivo);
      _ocultarModal();
      // Disparar evento para que app.js recargue datos
      document.dispatchEvent(new CustomEvent('eq:usuario-cambiado', { detail: { nombre } }));
      return _perfilActivo;
    } catch (err) {
      _mostrarToast(`Error al cargar usuario: ${err.message}`, 'error');
      return null;
    }
  }

  /** Flujo completo: crear + activar. */
  async function crearYActivar(nombre, nombreMostrar, avatar) {
    try {
      const res = await crearUsuario(nombre, nombreMostrar || nombre, avatar);
      return activarUsuario(res.perfil.nombre);
    } catch (err) {
      _mostrarToast(`No se pudo crear: ${err.message}`, 'error');
      return null;
    }
  }

  /** Flujo de eliminación con confirmación de doble paso. */
  async function pedirEliminar(nombre, nombreMostrar) {
    const confirmEl = document.getElementById('confirm-delete-wrap');
    const inputEl   = document.getElementById('confirm-delete-input');
    const btnEl     = document.getElementById('confirm-delete-btn');
    if (!confirmEl || !inputEl || !btnEl) return;

    confirmEl.classList.remove('hidden');
    inputEl.value = '';
    inputEl.placeholder = 'Escribe BORRAR para confirmar';
    inputEl.focus();

    const handler = async () => {
      if (inputEl.value.trim().toUpperCase() !== 'BORRAR') {
        inputEl.classList.add('input-shake');
        setTimeout(() => inputEl.classList.remove('input-shake'), 500);
        return;
      }
      btnEl.removeEventListener('click', handler);
      confirmEl.classList.add('hidden');
      try {
        await eliminarUsuario(nombre);
        if (getActivo() === nombre) {
          _clearActivo();
          _perfilActivo = null;
          _actualizarHeader(null);
          await _rellenarListaUsuarios();
          _mostrarModal();
          document.dispatchEvent(new CustomEvent('eq:usuario-cambiado', { detail: { nombre: null } }));
        }
        _mostrarToast(`Usuario ${nombreMostrar} eliminado`, 'info');
      } catch (err) {
        _mostrarToast(`Error al eliminar: ${err.message}`, 'error');
      }
    };
    btnEl.addEventListener('click', handler);
  }

  // ── Toast helper ──────────────────────────────────────────────────────────

  function _mostrarToast(msg, tipo = 'info') {
    const color = tipo === 'error' ? 'var(--color-danger)' : 'var(--accent)';
    const toast = document.createElement('div');
    toast.style.cssText = `
      position:fixed;bottom:1.5rem;right:1.5rem;z-index:9999;
      background:${color};color:#fff;padding:0.7rem 1.2rem;
      border-radius:8px;font-size:0.85rem;box-shadow:0 4px 20px rgba(0,0,0,0.5);
      animation:fade-in-up 0.2s ease;
    `;
    toast.textContent = msg;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 4000);
  }

  // ── Inicialización ────────────────────────────────────────────────────────

  async function init() {
    // 1. Preparar modal y avatares
    _rellenarAvatares();
    await _rellenarListaUsuarios();

    // 2. Conectar botón de usuario en el header
    document.getElementById('user-btn')?.addEventListener('click', (e) => {
      e.stopPropagation();
      _toggleDropdown();
    });

    // 3. Conectar opciones del dropdown
    document.getElementById('dd-cambiar')?.addEventListener('click', async () => {
      _cerrarDropdown();
      await _rellenarListaUsuarios();
      _mostrarModal();
    });

    document.getElementById('dd-nuevo')?.addEventListener('click', () => {
      _cerrarDropdown();
      // Cambiar el modal al tab de crear
      document.getElementById('modal-tab-crear')?.click();
      _mostrarModal();
    });

    document.getElementById('dd-reiniciar')?.addEventListener('click', async () => {
      _cerrarDropdown();
      const nombre = getActivo();
      if (!nombre) return;
      if (!confirm(`¿Reiniciar todo el progreso de "${_perfilActivo?.nombre_mostrar || nombre}"?`)) return;
      try {
        await reiniciarProgreso(nombre);
        _mostrarToast('Progreso reiniciado ✓', 'info');
        document.dispatchEvent(new CustomEvent('eq:usuario-cambiado', { detail: { nombre } }));
      } catch (err) {
        _mostrarToast(`Error: ${err.message}`, 'error');
      }
    });

    document.getElementById('dd-eliminar')?.addEventListener('click', () => {
      _cerrarDropdown();
      const nombre = getActivo();
      if (!nombre) return;
      pedirEliminar(nombre, _perfilActivo?.nombre_mostrar || nombre);
    });

    // 4. Conectar formulario de CREAR usuario en el modal
    document.getElementById('modal-crear-form')?.addEventListener('submit', async (e) => {
      e.preventDefault();
      const nombreInput    = document.getElementById('modal-nombre-input');
      const displayInput   = document.getElementById('modal-display-input');
      const nombre         = (nombreInput?.value || '').trim();
      const nombreMostrar  = (displayInput?.value || nombre).trim();
      const avatar         = _getAvatarSeleccionado();

      if (!nombre) { nombreInput?.focus(); return; }
      await crearYActivar(nombre, nombreMostrar, avatar);
    });

    // 5. Conectar botón de CARGAR usuario existente
    document.getElementById('modal-cargar-btn')?.addEventListener('click', async () => {
      const sel = document.getElementById('modal-usuario-existente');
      const nombre = sel?.value;
      if (!nombre) return;
      await activarUsuario(nombre);
    });

    // 6. Tabs del modal (Crear / Cargar)
    document.querySelectorAll('.modal-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        document.querySelectorAll('.modal-tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.modal-tab-panel').forEach(p => p.classList.add('hidden'));
        tab.classList.add('active');
        document.getElementById(tab.dataset.panel)?.classList.remove('hidden');
      });
    });

    // 7. Restaurar usuario activo de localStorage
    const guardado = getActivo();
    if (guardado) {
      try {
        _perfilActivo = await cargarPerfil(guardado);
        _actualizarHeader(_perfilActivo);
        return _perfilActivo;
      } catch (_) {
        // El usuario ya no existe en el servidor
        _clearActivo();
      }
    }

    // 8. No hay usuario → mostrar modal
    _mostrarModal();
    return null;
  }

  // ── API pública ────────────────────────────────────────────────────────────

  return {
    init,
    getActivo,
    getActivoPerfil,
    apiParam,
    activarUsuario,
    crearYActivar,
    pedirEliminar,
    reiniciarProgreso: async () => {
      const n = getActivo();
      if (n) await reiniciarProgreso(n);
    },
  };
})();
