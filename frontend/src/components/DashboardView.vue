<template>
  <div class="dashboard-page">
    <!-- Top Header -->
    <header class="dashboard-header glass-header">
      <div class="header-inner container">
        <div class="brand">
          <span class="brand-badge">CRUD Admin</span>
          <h1 class="brand-title">Gestión del Portafolio</h1>
        </div>

        <!-- Navigation Tabs -->
        <nav class="crud-tabs">
          <button
            class="tab-btn"
            :class="{ active: activeTab === 'proyectos' }"
            @click="activeTab = 'proyectos'"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
            </svg>
            Proyectos
            <span class="badge">{{ proyectos.length }}</span>
          </button>

          <button
            class="tab-btn"
            :class="{ active: activeTab === 'contacto' }"
            @click="activeTab = 'contacto'"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
              <polyline points="22,6 12,13 2,6"></polyline>
            </svg>
            Contacto
            <span class="badge">{{ contactos.length }}</span>
          </button>

          <button
            class="tab-btn"
            :class="{ active: activeTab === 'tools' }"
            @click="activeTab = 'tools'"
          >
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
            </svg>
            Tools
            <span class="badge">{{ tools.length }}</span>
          </button>
        </nav>

        <!-- Actions -->
        <div class="header-actions">
          <router-link to="/" class="btn-secondary">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
              <polyline points="9 22 9 12 15 12 15 22"></polyline>
            </svg>
            Portafolio
          </router-link>
          <button @click="handleLogout" class="btn-logout">
            Log out
          </button>
        </div>
      </div>
    </header>

    <!-- Main Content Area -->
    <main class="dashboard-main container">
      <!-- Toast Alert -->
      <Transition name="slide-down">
        <div v-if="toast.show" class="toast" :class="toast.type">
          <span>{{ toast.message }}</span>
        </div>
      </Transition>

      <!-- =================================================================== -->
      <!-- TAB 1: CRUD PROYECTOS -->
      <!-- =================================================================== -->
      <section v-if="activeTab === 'proyectos'" class="crud-section">
        <div class="section-toolbar">
          <div>
            <h2 class="section-title">CRUD 1: Modelo Proyecto</h2>
            <p class="section-desc">Administra los proyectos publicados en el portafolio</p>
          </div>
          <button class="btn-primary" @click="openProyectoModal()">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="12" y1="5" x2="12" y2="19"></line>
              <line x1="5" y1="12" x2="19" y2="12"></line>
            </svg>
            Nuevo Proyecto
          </button>
        </div>

        <!-- Table / Grid -->
        <div class="table-card glass-panel">
          <div v-if="loadingProyectos" class="loading-state">Cargando proyectos...</div>
          <div v-else-if="proyectos.length === 0" class="empty-state">No hay proyectos registrados.</div>
          <table v-else class="crud-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Descripción</th>
                <th>Reto</th>
                <th>Estado</th>
                <th>Demo / GitHub</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="p in proyectos" :key="p.id">
                <td>#{{ p.id }}</td>
                <td class="font-bold">{{ p.nombre }}</td>
                <td class="text-truncate" :title="p.descripcion">{{ p.descripcion }}</td>
                <td class="text-truncate" :title="p.reto">{{ p.reto || '-' }}</td>
                <td>
                  <span class="status-badge" :class="p.estado ? 'status-active' : 'status-inactive'">
                    {{ p.estado ? 'En producción' : 'En desarrollo' }}
                  </span>
                </td>
                <td class="links-cell">
                  <a v-if="p.demo" :href="p.demo" target="_blank" class="icon-link">Demo</a>
                  <a v-if="p.github" :href="p.github" target="_blank" class="icon-link">GitHub</a>
                </td>
                <td class="actions-cell">
                  <button class="btn-action edit" @click="openProyectoModal(p)">Editar</button>
                  <button class="btn-action delete" @click="deleteProyecto(p.id)">Eliminar</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- =================================================================== -->
      <!-- TAB 2: CRUD CONTACTO -->
      <!-- =================================================================== -->
      <section v-if="activeTab === 'contacto'" class="crud-section">
        <div class="section-toolbar">
          <div>
            <h2 class="section-title">CRUD 2: Modelo Contacto</h2>
            <p class="section-desc">Administra la información y vías de contacto</p>
          </div>
          <button class="btn-primary" @click="openContactoModal()">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="12" y1="5" x2="12" y2="19"></line>
              <line x1="5" y1="12" x2="19" y2="12"></line>
            </svg>
            Nuevo Contacto
          </button>
        </div>

        <div class="table-card glass-panel">
          <div v-if="loadingContactos" class="loading-state">Cargando contactos...</div>
          <div v-else-if="contactos.length === 0" class="empty-state">No hay registros de contacto.</div>
          <table v-else class="crud-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Correo</th>
                <th>Enlace / Link</th>
                <th>GitHub</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="c in contactos" :key="c.id">
                <td>#{{ c.id }}</td>
                <td class="font-bold">{{ c.correo }}</td>
                <td><a v-if="c.link" :href="c.link" target="_blank" class="text-link">{{ c.link }}</a></td>
                <td><a v-if="c.github" :href="c.github" target="_blank" class="text-link">{{ c.github }}</a></td>
                <td class="actions-cell">
                  <button class="btn-action edit" @click="openContactoModal(c)">Editar</button>
                  <button class="btn-action delete" @click="deleteContacto(c.id)">Eliminar</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- =================================================================== -->
      <!-- TAB 3: CRUD TOOL -->
      <!-- =================================================================== -->
      <section v-if="activeTab === 'tools'" class="crud-section">
        <div class="section-toolbar">
          <div>
            <h2 class="section-title">CRUD 3: Modelo Tool</h2>
            <p class="section-desc">Administra las herramientas y sus áreas/categorías</p>
          </div>
          <button class="btn-primary" @click="openToolModal()">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="12" y1="5" x2="12" y2="19"></line>
              <line x1="5" y1="12" x2="19" y2="12"></line>
            </svg>
            Nueva Tool
          </button>
        </div>

        <div class="table-card glass-panel">
          <div v-if="loadingTools" class="loading-state">Cargando tools...</div>
          <div v-else-if="tools.length === 0" class="empty-state">No hay herramientas registradas.</div>
          <table v-else class="crud-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Área</th>
                <th>Herramientas</th>
                <th>Categoría</th>
                <th>Progreso</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="t in tools" :key="t.id">
                <td>#{{ t.id }}</td>
                <td class="font-bold">{{ t.area }}</td>
                <td>{{ t.herramientas }}</td>
                <td>
                  <span class="category-pill">{{ t.categoria_nombre || 'Sin categoría' }}</span>
                </td>
                <td class="progress-cell">
                  <div class="mini-progress-wrap">
                    <div class="mini-progress-track">
                      <div
                        class="mini-progress-fill"
                        :class="t.progreso >= 80 ? 'fill-high' : t.progreso >= 50 ? 'fill-med' : 'fill-low'"
                        :style="{ width: (t.progreso || 0) + '%' }"
                      ></div>
                    </div>
                    <span class="mini-progress-label">{{ t.progreso || 0 }}%</span>
                  </div>
                </td>
                <td class="actions-cell">
                  <button class="btn-action edit" @click="openToolModal(t)">Editar</button>
                  <button class="btn-action delete" @click="deleteTool(t.id)">Eliminar</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>
    </main>

    <!-- =================================================================== -->
    <!-- MODALES DE EDICION Y CREACION -->
    <!-- =================================================================== -->

    <!-- Modal Proyecto -->
    <Teleport to="body">
      <div v-if="proyectoModal.show" class="modal-overlay" @click.self="proyectoModal.show = false">
        <div class="modal-card glass-panel">
          <h3>{{ proyectoModal.isEdit ? 'Editar Proyecto' : 'Nuevo Proyecto' }}</h3>
          <form @submit.prevent="saveProyecto" class="modal-form">
            <div class="form-group">
              <label>Nombre</label>
              <input v-model="proyectoForm.nombre" required class="form-input" placeholder="Nombre del proyecto" />
            </div>

            <div class="form-group">
              <label>Descripción</label>
              <textarea v-model="proyectoForm.descripcion" rows="2" class="form-input" placeholder="Breve descripción del proyecto..."></textarea>
            </div>

            <div class="form-group">
              <label>Reto</label>
              <textarea v-model="proyectoForm.reto" rows="2" class="form-input" placeholder="Describa el reto o desafío principal..."></textarea>
            </div>

            <!-- ===== CHIP SELECTOR INTERACTIVO ===== -->
            <div class="form-group">
              <div class="label-with-action">
                <label>Herramientas / Tecnologías</label>
                <span class="chip-counter">{{ proyectoForm.herramientasList.length }} seleccionadas</span>
              </div>

              <!-- Selected chips display -->
              <div class="selected-chips-wrap" v-if="proyectoForm.herramientasList.length > 0">
                <span
                  v-for="chip in proyectoForm.herramientasList"
                  :key="chip"
                  class="sel-chip"
                  @click="removeProjectChip(chip)"
                  title="Click para eliminar"
                >
                  {{ chip }}
                  <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                    <line x1="18" y1="6" x2="6" y2="18"/>
                    <line x1="6" y1="6" x2="18" y2="18"/>
                  </svg>
                </span>
              </div>
              <p v-else class="chips-empty-hint">Selecciona o escribe las tecnologías abajo ↓</p>

              <!-- Category filter tabs -->
              <div class="chip-cat-tabs">
                <button
                  v-for="cat in chipCategories"
                  :key="cat.id"
                  type="button"
                  class="chip-cat-btn"
                  :class="{ active: activeProjectChipCat === cat.id }"
                  @click="activeProjectChipCat = cat.id"
                >{{ cat.icon }} {{ cat.label }}</button>
              </div>

              <!-- Preset chips grid -->
              <div class="preset-chips">
                <button
                  v-for="tech in filteredProjectPresetChips"
                  :key="tech"
                  type="button"
                  class="preset-chip"
                  :class="{ selected: proyectoForm.herramientasList.includes(tech) }"
                  @click="toggleProjectChip(tech)"
                >{{ tech }}</button>
              </div>

              <!-- Custom chip input -->
              <div class="custom-chip-row">
                <input
                  v-model="customProjectChipInput"
                  class="form-input custom-chip-input"
                  placeholder="+ Agregar tecnología personalizada..."
                  @keydown.enter.prevent="addCustomProjectChip"
                  @keydown.comma.prevent="addCustomProjectChip"
                />
                <button type="button" class="btn-add-chip" @click="addCustomProjectChip" :disabled="!customProjectChipInput.trim()">
                  Agregar
                </button>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label>Enlace Demo</label>
                <input v-model="proyectoForm.demo" class="form-input" placeholder="https://..." />
              </div>
              <div class="form-group">
                <label>Enlace GitHub</label>
                <input v-model="proyectoForm.github" class="form-input" placeholder="https://github.com/..." />
              </div>
            </div>

            <div class="form-group checkbox-group">
              <label class="checkbox-label">
                <input type="checkbox" v-model="proyectoForm.estado" />
                <span>En producción (desmarcar para En desarrollo)</span>
              </label>
            </div>

            <div class="modal-actions">
              <button type="button" class="btn-cancel" @click="proyectoModal.show = false">Cancelar</button>
              <button type="submit" class="btn-save">Guardar</button>
            </div>
          </form>
        </div>
      </div>
    </Teleport>

    <!-- Modal Contacto -->
    <Teleport to="body">
      <div v-if="contactoModal.show" class="modal-overlay" @click.self="contactoModal.show = false">
        <div class="modal-card glass-panel">
          <h3>{{ contactoModal.isEdit ? 'Editar Contacto' : 'Nuevo Contacto' }}</h3>
          <form @submit.prevent="saveContacto" class="modal-form">
            <div class="form-group">
              <label>Correo Electrónico</label>
              <input v-model="contactoForm.correo" type="email" required class="form-input" placeholder="usuario@correo.com" />
            </div>

            <div class="form-group">
              <label>Enlace (Link)</label>
              <input v-model="contactoForm.link" class="form-input" placeholder="https://..." />
            </div>

            <div class="form-group">
              <label>GitHub</label>
              <input v-model="contactoForm.github" class="form-input" placeholder="https://github.com/..." />
            </div>

            <div class="modal-actions">
              <button type="button" class="btn-cancel" @click="contactoModal.show = false">Cancelar</button>
              <button type="submit" class="btn-save">Guardar</button>
            </div>
          </form>
        </div>
      </div>
    </Teleport>

    <!-- Modal Tool -->
    <Teleport to="body">
      <div v-if="toolModal.show" class="modal-overlay" @click.self="toolModal.show = false">
        <div class="modal-card glass-panel">
          <h3>{{ toolModal.isEdit ? 'Editar Tool' : 'Nueva Tool' }}</h3>
          <form @submit.prevent="saveTool" class="modal-form">
            <div class="form-group">
              <label>Área</label>
              <input v-model="toolForm.area" required class="form-input" placeholder="Ej. Frontend, Backend, DevOps" />
            </div>

            <!-- ===== CHIP SELECTOR INTERACTIVO ===== -->
            <div class="form-group">
              <div class="label-with-action">
                <label>Herramientas / Tecnologías</label>
                <span class="chip-counter">{{ toolForm.selectedChips.length }} seleccionadas</span>
              </div>

              <!-- Selected chips display -->
              <div class="selected-chips-wrap" v-if="toolForm.selectedChips.length > 0">
                <span
                  v-for="chip in toolForm.selectedChips"
                  :key="chip"
                  class="sel-chip"
                  @click="removeChip(chip)"
                  title="Click para eliminar"
                >
                  {{ chip }}
                  <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                    <line x1="18" y1="6" x2="6" y2="18"/>
                    <line x1="6" y1="6" x2="18" y2="18"/>
                  </svg>
                </span>
              </div>
              <p v-else class="chips-empty-hint">Selecciona o escribe las tecnologías abajo ↓</p>

              <!-- Category filter tabs -->
              <div class="chip-cat-tabs">
                <button
                  v-for="cat in chipCategories"
                  :key="cat.id"
                  type="button"
                  class="chip-cat-btn"
                  :class="{ active: activeChipCat === cat.id }"
                  @click="activeChipCat = cat.id"
                >{{ cat.icon }} {{ cat.label }}</button>
              </div>

              <!-- Preset chips grid -->
              <div class="preset-chips">
                <button
                  v-for="tech in filteredPresetChips"
                  :key="tech"
                  type="button"
                  class="preset-chip"
                  :class="{ selected: toolForm.selectedChips.includes(tech) }"
                  @click="toggleChip(tech)"
                >{{ tech }}</button>
              </div>

              <!-- Custom chip input -->
              <div class="custom-chip-row">
                <input
                  v-model="customChipInput"
                  class="form-input custom-chip-input"
                  placeholder="+ Agregar tecnología personalizada..."
                  @keydown.enter.prevent="addCustomChip"
                  @keydown.comma.prevent="addCustomChip"
                />
                <button type="button" class="btn-add-chip" @click="addCustomChip" :disabled="!customChipInput.trim()">
                  Agregar
                </button>
              </div>
            </div>

            <div class="form-group">
              <label>Categoría</label>
              <select v-model="toolForm.id_categorias" class="form-input">
                <option :value="null">-- Seleccionar Categoría --</option>
                <option v-for="cat in categorias" :key="cat.id" :value="cat.id">
                  {{ cat.nombre }}
                </option>
              </select>
            </div>

            <div class="form-group">
              <div class="label-with-action">
                <label>Progreso de Habilidad</label>
                <span class="progress-value-badge" :class="toolForm.progreso >= 80 ? 'badge-high' : toolForm.progreso >= 50 ? 'badge-med' : 'badge-low'">
                  {{ toolForm.progreso >= 80 ? 'Avanzado' : toolForm.progreso >= 50 ? 'Intermedio' : 'En Estudio' }}
                </span>
              </div>
              <div class="slider-wrap">
                <div class="slider-track-container">
                  <div class="slider-track-display">
                    <div
                      class="slider-fill"
                      :class="toolForm.progreso >= 80 ? 'fill-high' : toolForm.progreso >= 50 ? 'fill-med' : 'fill-low'"
                      :style="{ width: toolForm.progreso + '%' }"
                    ></div>
                  </div>
                  <input
                    type="range"
                    v-model.number="toolForm.progreso"
                    min="0" max="100" step="1"
                    class="progress-slider"
                  />
                </div>
                <span class="slider-percent">{{ toolForm.progreso }}%</span>
              </div>
            </div>

            <div class="modal-actions">
              <button type="button" class="btn-cancel" @click="toolModal.show = false">Cancelar</button>
              <button type="submit" class="btn-save">Guardar</button>
            </div>
          </form>
        </div>
      </div>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue';

const activeTab = ref('proyectos');

const proyectos = ref([]);
const contactos = ref([]);
const tools = ref([]);
const categorias = ref([]);

const loadingProyectos = ref(false);
const loadingContactos = ref(false);
const loadingTools = ref(false);

const toast = reactive({ show: false, message: '', type: 'success' });

const showToast = (msg, type = 'success') => {
  toast.message = msg;
  toast.type = type;
  toast.show = true;
  setTimeout(() => { toast.show = false; }, 3000);
};

// -----------------------------------------------------------------------------
// API FETCHERS
// -----------------------------------------------------------------------------
const API_URL = import.meta.env.VITE_API_URL || '';

const fetchProyectos = async () => {
  loadingProyectos.value = true;
  try {
    const res = await fetch(`${API_URL}/api/proyectos/`, { headers: getAuthHeaders() });
    if (res.ok) proyectos.value = await res.json();
  } catch (err) {
    console.error(err);
  } finally {
    loadingProyectos.value = false;
  }
};

const fetchContactos = async () => {
  loadingContactos.value = true;
  try {
    const res = await fetch(`${API_URL}/api/contacto/`, { headers: getAuthHeaders() });
    if (res.ok) contactos.value = await res.json();
  } catch (err) {
    console.error(err);
  } finally {
    loadingContactos.value = false;
  }
};

const fetchTools = async () => {
  loadingTools.value = true;
  try {
    const res = await fetch(`${API_URL}/api/tools/`, { headers: getAuthHeaders() });
    if (res.ok) tools.value = await res.json();
  } catch (err) {
    console.error(err);
  } finally {
    loadingTools.value = false;
  }
};

const fetchCategorias = async () => {
  try {
    const res = await fetch(`${API_URL}/api/categorias/`, { headers: getAuthHeaders() });
    if (res.ok) categorias.value = await res.json();
  } catch (err) {
    console.error(err);
  }
};

onMounted(() => {
  fetchProyectos();
  fetchContactos();
  fetchTools();
  fetchCategorias();
});

// -----------------------------------------------------------------------------
// CRUD 1: PROYECTO LOGIC
// -----------------------------------------------------------------------------
const proyectoModal = reactive({ show: false, isEdit: false, id: null });
const proyectoForm = reactive({
  nombre: '',
  descripcion: '',
  reto: '',
  herramientasList: [],
  demo: '',
  github: '',
  estado: true
});

const customProjectChipInput = ref('');
const activeProjectChipCat   = ref('all');

const filteredProjectPresetChips = computed(() =>
  CHIP_CATALOG[activeProjectChipCat.value] || CHIP_CATALOG.all
);

function toggleProjectChip(tech) {
  const idx = proyectoForm.herramientasList.indexOf(tech);
  if (idx === -1) {
    proyectoForm.herramientasList.push(tech);
  } else {
    proyectoForm.herramientasList.splice(idx, 1);
  }
}

function removeProjectChip(tech) {
  const idx = proyectoForm.herramientasList.indexOf(tech);
  if (idx !== -1) proyectoForm.herramientasList.splice(idx, 1);
}

function addCustomProjectChip() {
  const val = customProjectChipInput.value.trim().replace(/,$/, '');
  if (!val || proyectoForm.herramientasList.includes(val)) {
    customProjectChipInput.value = '';
    return;
  }
  proyectoForm.herramientasList.push(val);
  customProjectChipInput.value = '';
}

const openProyectoModal = (p = null) => {
  customProjectChipInput.value = '';
  activeProjectChipCat.value = 'all';
  if (p) {
    proyectoModal.isEdit = true;
    proyectoModal.id = p.id;
    proyectoForm.nombre = p.nombre || '';
    proyectoForm.descripcion = p.descripcion || '';
    proyectoForm.reto = p.reto || '';
    proyectoForm.herramientasList = Array.isArray(p.herramientas) && p.herramientas.length > 0
      ? [...p.herramientas]
      : [];
    proyectoForm.demo = p.demo || '';
    proyectoForm.github = p.github || '';
    proyectoForm.estado = p.estado !== undefined ? p.estado : true;
  } else {
    proyectoModal.isEdit = false;
    proyectoModal.id = null;
    proyectoForm.nombre = '';
    proyectoForm.descripcion = '';
    proyectoForm.reto = '';
    proyectoForm.herramientasList = [];
    proyectoForm.demo = '';
    proyectoForm.github = '';
    proyectoForm.estado = true;
  }
  proyectoModal.show = true;
};

const saveProyecto = async () => {
  const payload = {
    nombre: proyectoForm.nombre,
    descripcion: proyectoForm.descripcion,
    reto: proyectoForm.reto,
    herramientas: proyectoForm.herramientasList.map(s => s.trim()).filter(Boolean),
    demo: proyectoForm.demo,
    github: proyectoForm.github,
    estado: proyectoForm.estado
  };

  const url = proyectoModal.isEdit ? `${API_URL}/api/proyectos/${proyectoModal.id}/` : `${API_URL}/api/proyectos/`;
  const method = proyectoModal.isEdit ? 'PUT' : 'POST';

  try {
    const res = await fetch(url, {
      method,
      headers: getAuthHeaders(),
      body: JSON.stringify(payload)
    });
    if (res.ok) {
      showToast(proyectoModal.isEdit ? 'Proyecto actualizado' : 'Proyecto creado exitosamente');
      proyectoModal.show = false;
      fetchProyectos();
    }
  } catch (err) {
    showToast('Error al guardar proyecto', 'error');
  }
};

const deleteProyecto = async (id) => {
  if (!confirm('¿Está seguro de eliminar este proyecto?')) return;
  try {
    const res = await fetch(`${API_URL}/api/proyectos/${id}/`, { method: 'DELETE', headers: getAuthHeaders() });
    if (res.ok) {
      showToast('Proyecto eliminado');
      fetchProyectos();
    }
  } catch (err) {
    showToast('Error al eliminar', 'error');
  }
};

// -----------------------------------------------------------------------------
// CRUD 2: CONTACTO LOGIC
// -----------------------------------------------------------------------------
const contactoModal = reactive({ show: false, isEdit: false, id: null });
const contactoForm = reactive({ correo: '', link: '', github: '' });

const openContactoModal = (c = null) => {
  if (c) {
    contactoModal.isEdit = true;
    contactoModal.id = c.id;
    contactoForm.correo = c.correo;
    contactoForm.link = c.link;
    contactoForm.github = c.github;
  } else {
    contactoModal.isEdit = false;
    contactoModal.id = null;
    contactoForm.correo = '';
    contactoForm.link = '';
    contactoForm.github = '';
  }
  contactoModal.show = true;
};

const saveContacto = async () => {
  const url = contactoModal.isEdit ? `${API_URL}/api/contacto/${contactoModal.id}/` : `${API_URL}/api/contacto/`;
  const method = contactoModal.isEdit ? 'PUT' : 'POST';

  try {
    const res = await fetch(url, {
      method,
      headers: getAuthHeaders(),
      body: JSON.stringify(contactoForm)
    });
    if (res.ok) {
      showToast(contactoModal.isEdit ? 'Contacto actualizado' : 'Contacto creado');
      contactoModal.show = false;
      fetchContactos();
    }
  } catch (err) {
    showToast('Error al guardar contacto', 'error');
  }
};

const deleteContacto = async (id) => {
  if (!confirm('¿Está seguro de eliminar este contacto?')) return;
  try {
    const res = await fetch(`${API_URL}/api/contacto/${id}/`, { method: 'DELETE', headers: getAuthHeaders() });
    if (res.ok) {
      showToast('Contacto eliminado');
      fetchContactos();
    }
  } catch (err) {
    showToast('Error al eliminar', 'error');
  }
};

// -----------------------------------------------------------------------------
// CRUD 3: TOOL LOGIC
// -----------------------------------------------------------------------------
const toolModal = reactive({ show: false, isEdit: false, id: null });
const toolForm = reactive({
  area: '',
  herramientas: '',       // CSV final para la API
  selectedChips: [],      // array reactivo de chips seleccionados
  id_categorias: null,
  progreso: 0
});

// ── Global App State ──────────────────────────────────────────────────────────

const getAuthHeaders = () => {
  const token = localStorage.getItem('token');
  return {
    'Content-Type': 'application/json',
    ...(token ? { 'Authorization': `Bearer ${token}` } : {})
  };
};

const handleLogout = async () => {
  const token = localStorage.getItem('token');
  if (token) {
    try {
      await fetch(`${API_URL}/api/logout/`, {
        method: 'POST',
        headers: getAuthHeaders()
      });
    } catch(e) {
      console.error(e);
    }
  }
  localStorage.removeItem('token');
  window.location.href = '/login';
};



// ── Preset technology catalog ────────────────────────────────────────────────
const CHIP_CATALOG = {
  all: [],   // populated below
  data: [
    'Python', 'Pandas', 'NumPy', 'Polars', 'SciPy', 'Matplotlib', 'Seaborn',
    'Plotly', 'Jupyter', 'Scikit-learn', 'TensorFlow', 'PyTorch', 'Keras',
    'Statsmodels', 'Feature Engineering', 'EDA', 'Data Cleaning', 'ETL',
  ],
  web: [
    'JavaScript', 'TypeScript', 'ES6+', 'Vue 3', 'React', 'Angular', 'Svelte',
    'Vite', 'HTML5', 'CSS3', 'Tailwind CSS', 'Bootstrap', 'SASS', 'Flexbox',
    'CSS Grid', 'Fetch API', 'Async/Await', 'DOM', 'Responsive Design',
  ],
  backend: [
    'Django', 'Django REST', 'FastAPI', 'Node.js', 'Express', 'Spring Boot',
    'Laravel', 'ASP.NET Core', 'Python', 'Java', 'C#', 'Go', 'PHP',
    'REST APIs', 'GraphQL', 'JWT', 'OAuth', 'Middleware', 'ORM', 'CRUD',
  ],
  db: [
    'PostgreSQL', 'MySQL', 'SQLite', 'MongoDB', 'Redis', 'SQL', 'Joins',
    'CTEs', 'Window Functions', 'Índices', 'Normalización', 'Modelado ER',
    'JSONB', 'Triggers', 'Migrations', 'Subconsultas',
  ],
  devops: [
    'Docker', 'Docker Compose', 'Git', 'GitHub', 'Git Flow', 'Linux', 'Bash',
    'Nginx', 'Gunicorn', 'SSH', 'VPS', 'HTTPS/SSL', 'Certbot', 'CI/CD',
    'Shell scripting', 'Cron jobs', 'Vim',
  ],
  methods: [
    'Scrum', 'Kanban', 'Agile', 'Sprints', 'Backlog', 'SOLID', 'Clean Architecture',
    'TDD', 'Pytest', 'Jest', 'Unit Testing', 'Mocking', 'Code Review', 'DDD',
  ],
};
CHIP_CATALOG.all = [...new Set(Object.values(CHIP_CATALOG).flat())];

const chipCategories = [
  { id: 'all',     icon: '🌐', label: 'Todas'     },
  { id: 'data',    icon: '📊', label: 'Data'       },
  { id: 'web',     icon: '🖥️', label: 'Frontend'   },
  { id: 'backend', icon: '⚙️', label: 'Backend'    },
  { id: 'db',      icon: '🗄️', label: 'Bases de datos' },
  { id: 'devops',  icon: '🛠️', label: 'DevOps'     },
  { id: 'methods', icon: '📋', label: 'Metodologías' },
];

const filteredPresetChips = computed(() =>
  CHIP_CATALOG[activeChipCat.value] || CHIP_CATALOG.all
);

// ── Chip actions ─────────────────────────────────────────────────────────────
function toggleChip(tech) {
  const idx = toolForm.selectedChips.indexOf(tech);
  if (idx === -1) {
    toolForm.selectedChips.push(tech);
  } else {
    toolForm.selectedChips.splice(idx, 1);
  }
  syncHerramientas();
}

function removeChip(tech) {
  const idx = toolForm.selectedChips.indexOf(tech);
  if (idx !== -1) toolForm.selectedChips.splice(idx, 1);
  syncHerramientas();
}

function addCustomChip() {
  const val = customChipInput.value.trim().replace(/,$/, '');
  if (!val || toolForm.selectedChips.includes(val)) {
    customChipInput.value = '';
    return;
  }
  toolForm.selectedChips.push(val);
  customChipInput.value = '';
  syncHerramientas();
}

function syncHerramientas() {
  toolForm.herramientas = toolForm.selectedChips.join(', ');
}

// ── Modal open/close ─────────────────────────────────────────────────────────
const openToolModal = (t = null) => {
  customChipInput.value  = '';
  activeChipCat.value    = 'all';

  if (t) {
    toolModal.isEdit = true;
    toolModal.id     = t.id;
    toolForm.area    = t.area;
    toolForm.id_categorias = t.id_categorias;
    toolForm.progreso      = t.progreso ?? 0;
    // Parse existing CSV into selected chips
    toolForm.selectedChips = t.herramientas
      ? t.herramientas.split(',').map(s => s.trim()).filter(Boolean)
      : [];
    toolForm.herramientas  = t.herramientas || '';
  } else {
    toolModal.isEdit       = false;
    toolModal.id           = null;
    toolForm.area          = '';
    toolForm.herramientas  = '';
    toolForm.selectedChips = [];
    toolForm.id_categorias = null;
    toolForm.progreso      = 0;
  }
  toolModal.show = true;
};

const saveTool = async () => {
  if (toolForm.selectedChips.length === 0) {
    showToast('Agrega al menos una herramienta', 'error');
    return;
  }
  syncHerramientas();

  const url = toolModal.isEdit ? `${API_URL}/api/tools/${toolModal.id}/` : `${API_URL}/api/tools/`;
  const method = toolModal.isEdit ? 'PUT' : 'POST';
  const payload = {
    area:          toolForm.area,
    herramientas:  toolForm.herramientas,
    id_categorias: toolForm.id_categorias,
    progreso:      toolForm.progreso,
  };

  try {
    const res = await fetch(url, {
      method,
      headers: getAuthHeaders(),
      body: JSON.stringify(payload)
    });
    if (res.ok) {
      showToast(toolModal.isEdit ? 'Tool actualizada ✔' : 'Tool creada ✔');
      toolModal.show = false;
      fetchTools();
    }
  } catch (err) {
    showToast('Error al guardar tool', 'error');
  }
};

const deleteTool = async (id) => {
  if (!confirm('¿Está seguro de eliminar esta tool?')) return;
  try {
    const res = await fetch(`${API_URL}/api/tools/${id}/`, { method: 'DELETE', headers: getAuthHeaders() });
    if (res.ok) {
      showToast('Tool eliminada');
      fetchTools();
    }
  } catch (err) {
    showToast('Error al eliminar', 'error');
  }
};
</script>

<style scoped>
.dashboard-page {
  min-height: 100vh;
  background: var(--bg-main, #080b11);
  color: #f8fafc;
  padding-bottom: 4rem;
}

.dashboard-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(15, 23, 42, 0.9);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding: 1rem 0;
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
}

.brand-badge {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  background: rgba(56, 189, 248, 0.15);
  color: #38bdf8;
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
  font-weight: 700;
}

.brand-title {
  font-size: 1.25rem;
  font-weight: 700;
  margin: 0.2rem 0 0;
}

.crud-tabs {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(0, 0, 0, 0.3);
  padding: 0.35rem;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.tab-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.55rem 1.1rem;
  border-radius: 8px;
  background: transparent;
  border: none;
  color: #94a3b8;
  font-weight: 600;
  font-size: 0.88rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.tab-btn:hover {
  color: #f8fafc;
}

.tab-btn.active {
  background: linear-gradient(135deg, #0284c7, #2563eb);
  color: #ffffff;
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35);
}

.badge {
  background: rgba(255, 255, 255, 0.2);
  font-size: 0.75rem;
  padding: 0.1rem 0.45rem;
  border-radius: 50px;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.5rem 0.9rem;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: #cbd5e1;
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 500;
  transition: all 0.2s;
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.12);
  color: #fff;
}

.btn-logout {
  padding: 0.5rem 0.9rem;
  border-radius: 8px;
  background: rgba(239, 68, 68, 0.15);
  border: 1px solid rgba(239, 68, 68, 0.3);
  color: #fca5a5;
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 500;
  transition: all 0.2s;
}

.btn-logout:hover {
  background: rgba(239, 68, 68, 0.25);
  color: #fff;
}

.dashboard-main {
  margin-top: 2rem;
}

.section-toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;
}

.section-title {
  font-size: 1.4rem;
  font-weight: 700;
  margin: 0 0 0.25rem;
}

.section-desc {
  font-size: 0.88rem;
  color: #94a3b8;
  margin: 0;
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.65rem 1.25rem;
  border-radius: 10px;
  background: linear-gradient(135deg, #0284c7, #2563eb);
  border: none;
  color: #fff;
  font-weight: 600;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s;
  box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(37, 99, 235, 0.5);
}

/* Table Card */
.table-card {
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  overflow: hidden;
}

.crud-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  font-size: 0.9rem;
}

.crud-table th {
  background: rgba(255, 255, 255, 0.03);
  padding: 1rem 1.25rem;
  color: #94a3b8;
  font-weight: 600;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.crud-table td {
  padding: 1rem 1.25rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  color: #e2e8f0;
}

.crud-table tr:hover {
  background: rgba(255, 255, 255, 0.02);
}

.font-bold { font-weight: 600; color: #fff; }
.text-truncate { max-width: 250px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }

.status-badge {
  padding: 0.25rem 0.65rem;
  border-radius: 50px;
  font-size: 0.78rem;
  font-weight: 600;
}

.status-active {
  background: rgba(34, 197, 94, 0.15);
  color: #4ade80;
  border: 1px solid rgba(34, 197, 94, 0.3);
}

.status-inactive {
  background: rgba(239, 68, 68, 0.15);
  color: #fca5a5;
  border: 1px solid rgba(239, 68, 68, 0.3);
}

.category-pill {
  padding: 0.25rem 0.65rem;
  border-radius: 50px;
  background: rgba(56, 189, 248, 0.12);
  color: #38bdf8;
  border: 1px solid rgba(56, 189, 248, 0.3);
  font-size: 0.8rem;
}

.actions-cell {
  display: flex;
  gap: 0.5rem;
}

.btn-action {
  padding: 0.35rem 0.75rem;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  border: none;
  transition: all 0.2s;
}

.btn-action.edit {
  background: rgba(56, 189, 248, 0.15);
  color: #38bdf8;
}
.btn-action.edit:hover { background: rgba(56, 189, 248, 0.3); }

.btn-action.delete {
  background: rgba(239, 68, 68, 0.15);
  color: #fca5a5;
}
.btn-action.delete:hover { background: rgba(239, 68, 68, 0.3); }

.links-cell { display: flex; gap: 0.5rem; }
.icon-link {
  font-size: 0.8rem;
  color: #38bdf8;
  text-decoration: none;
}
.icon-link:hover { text-decoration: underline; }
.text-link { color: #38bdf8; text-decoration: none; }
.text-link:hover { text-decoration: underline; }

.loading-state, .empty-state {
  padding: 3rem;
  text-align: center;
  color: #94a3b8;
}

/* Modal */
.modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 1000;
  background: rgba(4, 6, 12, 0.8);
  backdrop-filter: blur(12px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
}

.modal-card {
  width: 100%;
  max-width: 500px;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  background: rgba(15, 23, 42, 0.95);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
}

.modal-card h3 {
  margin: 0 0 1.25rem;
  font-size: 1.3rem;
  flex-shrink: 0;
}

.modal-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  overflow-y: auto;
  padding-right: 0.5rem;
}

.modal-form::-webkit-scrollbar {
  width: 6px;
}
.modal-form::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.15);
  border-radius: 3px;
}

.form-row { display: flex; gap: 1rem; }
.form-row .form-group { flex: 1; }

.form-group { display: flex; flex-direction: column; gap: 0.4rem; }
.form-group label { font-size: 0.82rem; color: #cbd5e1; font-weight: 600; }

.form-input {
  width: 100%;
  padding: 0.7rem 0.9rem;
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 8px;
  color: #fff;
  outline: none;
  font-size: 0.9rem;
}
.form-input:focus { border-color: #38bdf8; }

.label-with-action {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.btn-add-item {
  background: none;
  border: none;
  color: #38bdf8;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  padding: 0;
  transition: color 0.2s;
}

.btn-add-item:hover {
  color: #7dd3fc;
  text-decoration: underline;
}

.dynamic-items-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.dynamic-item-row {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.btn-remove-item {
  background: rgba(239, 68, 68, 0.15);
  border: 1px solid rgba(239, 68, 68, 0.3);
  color: #fca5a5;
  border-radius: 6px;
  width: 32px;
  height: 32px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 0.85rem;
  transition: all 0.2s;
}

.btn-remove-item:hover {
  background: rgba(239, 68, 68, 0.3);
  color: #fff;
}

.checkbox-group { margin-top: 0.5rem; }
.checkbox-label { display: flex; align-items: center; gap: 0.6rem; cursor: pointer; color: #cbd5e1; }

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 0.75rem;
  margin-top: 1rem;
}

.btn-cancel {
  padding: 0.6rem 1.1rem;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: #cbd5e1;
  cursor: pointer;
}

.btn-save {
  padding: 0.6rem 1.25rem;
  border-radius: 8px;
  background: linear-gradient(135deg, #0284c7, #2563eb);
  border: none;
  color: #fff;
  font-weight: 600;
  cursor: pointer;
}

/* Toast */
.toast {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  z-index: 2000;
  padding: 0.85rem 1.5rem;
  border-radius: 10px;
  background: #0284c7;
  color: #fff;
  font-weight: 600;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
}
.toast.error { background: #ef4444; }

.slide-down-enter-active, .slide-down-leave-active { transition: all 0.3s ease; }
.slide-down-enter-from, .slide-down-leave-to { opacity: 0; transform: translateY(20px); }

/* ---- Mini Progress (table) ---- */
.progress-cell { min-width: 140px; }

.mini-progress-wrap {
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.mini-progress-track {
  flex: 1;
  height: 6px;
  background: rgba(255, 255, 255, 0.07);
  border-radius: 3px;
  overflow: hidden;
}

.mini-progress-fill {
  height: 100%;
  border-radius: 3px;
  transition: width 0.5s ease;
}

.fill-high { background: linear-gradient(90deg, #00d4ff, #3a6ef5); }
.fill-med  { background: linear-gradient(90deg, #3a6ef5, #6366f1); }
.fill-low  { background: linear-gradient(90deg, #f0316d, #fb923c); }

.mini-progress-label {
  font-size: 0.75rem;
  font-weight: 600;
  color: #94a3b8;
  white-space: nowrap;
  min-width: 32px;
}

/* ---- Slider (modal) ---- */
.slider-wrap {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  margin-top: 0.5rem;
}

.slider-track-container {
  position: relative;
  flex: 1;
  height: 24px;
  display: flex;
  align-items: center;
}

.slider-track-display {
  position: absolute;
  left: 0;
  right: 0;
  height: 6px;
  background: rgba(255, 255, 255, 0.07);
  border-radius: 3px;
  overflow: hidden;
  pointer-events: none;
}

.slider-fill {
  height: 100%;
  border-radius: 3px;
  transition: width 0.1s ease;
}

.progress-slider {
  -webkit-appearance: none;
  width: 100%;
  height: 100%;
  background: transparent;
  outline: none;
  cursor: pointer;
  position: absolute;
  left: 0;
  top: 0;
  z-index: 10;
  margin: 0;
}

.progress-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #38bdf8;
  cursor: pointer;
  box-shadow: 0 0 8px rgba(56, 189, 248, 0.6);
  transition: transform 0.2s, box-shadow 0.2s;
  margin-top: 0px;
}

.progress-slider::-webkit-slider-thumb:hover {
  transform: scale(1.2);
  box-shadow: 0 0 14px rgba(56, 189, 248, 0.8);
}

.progress-slider::-webkit-slider-runnable-track {
  width: 100%;
  height: 100%;
  background: transparent;
  border: none;
}

.slider-percent {
  font-size: 0.85rem;
  font-weight: 700;
  color: #38bdf8;
  min-width: 40px;
  text-align: right;
}

/* ---- Progress value badge ---- */
.progress-value-badge {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
}

.badge-high {
  background: rgba(0, 212, 255, 0.15);
  color: #00d4ff;
}

.badge-med {
  background: rgba(58, 110, 245, 0.15);
  color: #818cf8;
}

.badge-low {
  background: rgba(240, 49, 109, 0.15);
  color: #f0316d;
}

/* =====================================================================
   CHIP SELECTOR INTERACTIVO
===================================================================== */

/* Counter badge */
.chip-counter {
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.15rem 0.55rem;
  border-radius: 50px;
  background: rgba(56, 189, 248, 0.15);
  color: #38bdf8;
}

/* Selected chips row */
.selected-chips-wrap {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  padding: 0.65rem 0.8rem;
  background: rgba(56, 189, 248, 0.04);
  border: 1px solid rgba(56, 189, 248, 0.18);
  border-radius: 8px;
  min-height: 42px;
}

.sel-chip {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.25rem 0.55rem 0.25rem 0.7rem;
  border-radius: 5px;
  background: rgba(56, 189, 248, 0.15);
  color: #38bdf8;
  border: 1px solid rgba(56, 189, 248, 0.3);
  cursor: pointer;
  transition: all 0.15s ease;
  user-select: none;
}

.sel-chip:hover {
  background: rgba(239, 68, 68, 0.18);
  border-color: rgba(239, 68, 68, 0.4);
  color: #fca5a5;
}

.sel-chip svg { flex-shrink: 0; }

/* Empty hint */
.chips-empty-hint {
  font-size: 0.8rem;
  color: #475569;
  font-style: italic;
  padding: 0.2rem 0;
}

/* Category filter tabs */
.chip-cat-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
  margin-top: 0.5rem;
}

.chip-cat-btn {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 0.28rem 0.7rem;
  border-radius: 50px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  background: transparent;
  color: #64748b;
  cursor: pointer;
  transition: all 0.18s ease;
  white-space: nowrap;
  font-family: inherit;
}

.chip-cat-btn:hover {
  border-color: rgba(56, 189, 248, 0.3);
  color: #94a3b8;
  background: rgba(56, 189, 248, 0.04);
}

.chip-cat-btn.active {
  border-color: #38bdf8;
  background: rgba(56, 189, 248, 0.12);
  color: #38bdf8;
  box-shadow: 0 0 10px rgba(56, 189, 248, 0.1);
}

/* Preset chips grid */
.preset-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-top: 0.5rem;
  max-height: 140px;
  overflow-y: auto;
  padding: 0.5rem 0.5rem 0.5rem 0;
  scrollbar-width: thin;
  scrollbar-color: rgba(255,255,255,0.08) transparent;
}

.preset-chips::-webkit-scrollbar {
  width: 4px;
}
.preset-chips::-webkit-scrollbar-thumb {
  background: rgba(255,255,255,0.1);
  border-radius: 2px;
}

.preset-chip {
  font-size: 0.73rem;
  font-weight: 600;
  padding: 0.28rem 0.65rem;
  border-radius: 5px;
  border: 1px solid rgba(255, 255, 255, 0.08);
  background: rgba(255, 255, 255, 0.03);
  color: #64748b;
  cursor: pointer;
  transition: all 0.15s ease;
  font-family: inherit;
  white-space: nowrap;
}

.preset-chip:hover {
  border-color: rgba(56, 189, 248, 0.3);
  background: rgba(56, 189, 248, 0.06);
  color: #94a3b8;
  transform: translateY(-1px);
}

.preset-chip.selected {
  border-color: #38bdf8;
  background: rgba(56, 189, 248, 0.14);
  color: #38bdf8;
  box-shadow: 0 0 8px rgba(56, 189, 248, 0.12);
}

.preset-chip.selected::before {
  content: '✓ ';
  font-size: 0.65rem;
}

/* Custom chip input row */
.custom-chip-row {
  display: flex;
  gap: 0.5rem;
  margin-top: 0.6rem;
}

.custom-chip-input {
  flex: 1;
}

.btn-add-chip {
  padding: 0 1rem;
  border-radius: 8px;
  background: rgba(56, 189, 248, 0.12);
  border: 1px solid rgba(56, 189, 248, 0.25);
  color: #38bdf8;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.18s ease;
  font-family: inherit;
}

.btn-add-chip:hover:not(:disabled) {
  background: rgba(56, 189, 248, 0.22);
  border-color: #38bdf8;
  box-shadow: 0 0 12px rgba(56, 189, 248, 0.2);
}

.btn-add-chip:disabled {
  opacity: 0.35;
  cursor: not-allowed;
}
</style>

