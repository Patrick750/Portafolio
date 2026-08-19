<template>
  <section id="skills" class="section skills-section">
    <div class="container">

      <!-- ===== SECTION INTRO ===== -->
      <div class="section-intro fade-up">
        <span class="section-label">// 01 · Expertise</span>
        <h2 class="section-title">Habilidades Técnicas</h2>
        <p class="section-subtitle">Tecnologías que aplico en el desarrollo de soluciones reales</p>
      </div>

      <!-- ===== LOADING SKELETON ===== -->
      <div v-if="loading" class="sk-wrap fade-up">
        <div class="sk-tabs">
          <div v-for="n in 4" :key="n" class="sk-tab"></div>
        </div>
        <div class="sk-grid">
          <div v-for="n in 6" :key="n" class="sk-card glass">
            <div class="sk-ring"></div>
            <div class="sk-lines">
              <div class="sk-line sk-title"></div>
              <div class="sk-line sk-badge"></div>
            </div>
          </div>
        </div>
      </div>

      <template v-else-if="groupedCategories.length > 0">

        <!-- ===== CATEGORY TABS ===== -->
        <div 
          class="cat-tabs-wrap fade-up"
          ref="tabsWrap"
          @mousedown="onDragStart"
          @mouseleave="onDragEnd"
          @mouseup="onDragEnd"
          @mousemove="onDragMove"
        >
          <nav class="cat-tabs" role="tablist" aria-label="Categorías de habilidades">
            <button
              v-for="cat in groupedCategories"
              :key="cat.id"
              class="cat-tab"
              :class="{ active: activeCatId === cat.id }"
              @click="setCategory(cat.id)"
              role="tab"
              :aria-selected="activeCatId === cat.id"
            >
              <span class="tab-icon" aria-hidden="true" v-html="cat.icon"></span>
              <span class="tab-name">{{ cat.nombre }}</span>
              <div class="tab-right">
                <span class="tab-count">{{ cat.skills.length }}</span>
                <span class="tab-avg" :class="`avg-${getLevelKey(getAvgProgress(cat.skills))}`">
                  {{ getAvgProgress(cat.skills) }}%
                </span>
              </div>
            </button>
          </nav>
        </div>

        <!-- ===== SKILLS GRID ===== -->
        <TransitionGroup
          name="card-anim"
          tag="div"
          class="skills-grid"
          @before-enter="onBeforeEnter"
          @enter="onEnter"
          @leave="onLeave"
        >
          <div
            v-for="(skill, idx) in visibleSkills"
            :key="skill.id"
            class="skill-card"
            :class="[`card-${getLevelKey(skill.progreso)}`, { flipped: skill.flipped }]"
            :data-idx="idx"
            @click="toggleFlip(skill)"
            role="button"
            tabindex="0"
            @keydown.enter="toggleFlip(skill)"
            @keydown.space.prevent="toggleFlip(skill)"
            :aria-label="`${skill.area} – ${getLevelLabel(skill.progreso)} ${skill.progreso}%. Haz click para ver detalles.`"
          >
            <div class="card-inner">

              <!-- ======= FRONT ======= -->
              <div class="face face-front glass">
                <div class="accent-line" :class="`line-${getLevelKey(skill.progreso)}`"></div>

                <!-- SVG Progress Ring -->
                <div class="ring-wrap">
                  <svg class="ring-svg" viewBox="0 0 130 130" xmlns="http://www.w3.org/2000/svg">
                    <defs>
                      <linearGradient :id="`gh-${skill.id}`" x1="0" y1="0" x2="1" y2="1">
                        <stop offset="0%" stop-color="#00d4ff"/>
                        <stop offset="100%" stop-color="#3a6ef5"/>
                      </linearGradient>
                      <linearGradient :id="`gm-${skill.id}`" x1="0" y1="0" x2="1" y2="1">
                        <stop offset="0%" stop-color="#3a6ef5"/>
                        <stop offset="100%" stop-color="#818cf8"/>
                      </linearGradient>
                      <linearGradient :id="`gl-${skill.id}`" x1="0" y1="0" x2="1" y2="1">
                        <stop offset="0%" stop-color="#f0316d"/>
                        <stop offset="100%" stop-color="#fb923c"/>
                      </linearGradient>
                      <filter :id="`glow-${skill.id}`" x="-20%" y="-20%" width="140%" height="140%">
                        <feGaussianBlur stdDeviation="3.5" result="blur"/>
                        <feMerge>
                          <feMergeNode in="blur"/>
                          <feMergeNode in="SourceGraphic"/>
                        </feMerge>
                      </filter>
                    </defs>

                    <!-- Track -->
                    <circle cx="65" cy="65" r="56" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="9"/>

                    <!-- Progress arc -->
                    <circle
                      cx="65" cy="65" r="56"
                      fill="none"
                      :stroke="`url(#g${getLevelKey(skill.progreso)[0]}-${skill.id})`"
                      stroke-width="9"
                      stroke-linecap="round"
                      :stroke-dasharray="CIRCUMFERENCE"
                      :stroke-dashoffset="skill.animated ? getOffset(skill.progreso) : CIRCUMFERENCE"
                      :filter="`url(#glow-${skill.id})`"
                      class="ring-arc"
                    />
                  </svg>

                  <!-- Center -->
                  <div class="ring-center">
                    <span class="ring-emoji" v-html="getSkillIcon(skill.area)"></span>
                    <div class="ring-pct" :class="`pct-${getLevelKey(skill.progreso)}`">
                      {{ skill.progreso }}<sup>%</sup>
                    </div>
                  </div>
                </div>

                <!-- Info -->
                <div class="front-info">
                  <h3 class="skill-name">{{ skill.area }}</h3>
                  <span class="level-badge" :class="`badge-${getLevelKey(skill.progreso)}`">
                    <span class="badge-pulse"></span>
                    {{ getLevelLabel(skill.progreso) }}
                  </span>
                </div>

                <!-- Flip hint -->
                <div class="flip-hint" aria-hidden="true">
                  <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="1 4 1 10 7 10"/>
                    <path d="M3.51 15a9 9 0 1 0 .49-3.16"/>
                  </svg>
                  Ver tecnologías
                </div>
              </div>

              <!-- ======= BACK ======= -->
              <div class="face face-back glass">
                <div class="accent-line" :class="`line-${getLevelKey(skill.progreso)}`"></div>

                <!-- Header -->
                <div class="back-header">
                  <span class="back-emoji" v-html="getSkillIcon(skill.area)"></span>
                  <div>
                    <h3 class="skill-name back-skill-name">{{ skill.area }}</h3>
                    <span class="level-badge" :class="`badge-${getLevelKey(skill.progreso)}`">
                      <span class="badge-pulse"></span>
                      {{ getLevelLabel(skill.progreso) }}
                    </span>
                  </div>
                </div>

                <!-- Progress bar -->
                <div class="back-bar-wrap">
                  <div class="back-bar-track">
                    <div
                      class="back-bar-fill"
                      :class="`fill-${getLevelKey(skill.progreso)}`"
                      :style="{ width: skill.animated ? skill.progreso + '%' : '0%' }"
                    ></div>
                  </div>
                  <span class="back-bar-pct">{{ skill.progreso }}%</span>
                </div>

                <!-- Tech chips -->
                <div class="back-chips">
                  <span
                    v-for="chip in parseChips(skill.herramientas)"
                    :key="chip"
                    class="chip"
                    :class="`chip-${getLevelKey(skill.progreso)}`"
                  >{{ chip }}</span>
                </div>

                <!-- Flip hint -->
                <div class="flip-hint back-hint" aria-hidden="true">
                  <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                    <polyline points="23 20 23 14 17 14"/>
                    <path d="M20.49 9A9 9 0 1 0 21 12"/>
                  </svg>
                  Volver
                </div>
              </div>

            </div>
          </div>
        </TransitionGroup>

      </template>

      <!-- ===== EMPTY STATE ===== -->
      <div v-else-if="!loading" class="empty-state fade-up">
        <span class="empty-icon" v-html="ICONS.tool"></span>
        <p>No hay habilidades registradas.<br>Usa el <strong>Dashboard</strong> para agregar tus skills.</p>
      </div>

    </div>
  </section>
</template>

<script setup>
import { ref, computed, reactive, onMounted, nextTick } from 'vue';

// ── Constants ────────────────────────────────────────────────────────────────
const CIRCUMFERENCE = 2 * Math.PI * 56; // r = 56 → ≈ 351.86

// ── Raw API data ─────────────────────────────────────────────────────────────
const rawTools      = ref([]);
const rawCategorias = ref([]);
const loading       = ref(true);

// ── UI state (keyed by skill ID) ──────────────────────────────────────────────
const skillState = reactive({}); // { [id]: { flipped, animated } }

function getState(skill) {
  if (!skillState[skill.id]) {
    skillState[skill.id] = { flipped: false, animated: false };
  }
  return skillState[skill.id];
}

// ── Active category ───────────────────────────────────────────────────────────
const activeCatId = ref(null);

// ── Helpers: level ────────────────────────────────────────────────────────────
function getLevelKey(p)   { return p >= 80 ? 'high' : p >= 50 ? 'med' : 'low'; }
function getLevelLabel(p) { return p >= 80 ? 'Avanzado' : p >= 50 ? 'Intermedio' : 'En Estudio'; }
function getOffset(p)     { return CIRCUMFERENCE * (1 - p / 100); }

function getAvgProgress(skills) {
  if (!skills.length) return 0;
  return Math.round(skills.reduce((s, sk) => s + (sk.progreso || 0), 0) / skills.length);
}

// ── Helpers: icons ────────────────────────────────────────────────────────────
const svgBase = (path) => `<svg viewBox="0 0 24 24" width="1em" height="1em" style="display: block; margin-top: -1px;" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">${path}</svg>`;

const ICONS = {
  code: svgBase('<polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline>'),
  database: svgBase('<ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>'),
  server: svgBase('<rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect><line x1="6" y1="6" x2="6.01" y2="6"></line><line x1="6" y1="18" x2="6.01" y2="18"></line>'),
  cloud: svgBase('<path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"></path>'),
  chart: svgBase('<line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line>'),
  terminal: svgBase('<polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line>'),
  layout: svgBase('<rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line>'),
  tool: svgBase('<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>'),
  box: svgBase('<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line>'),
  git: svgBase('<circle cx="12" cy="18" r="3"></circle><circle cx="6" cy="6" r="3"></circle><circle cx="18" cy="9" r="3"></circle><path d="M18 12v-1a2 2 0 0 0-2-2h-3"></path><path d="M12 15V9"></path><path d="M6 9v8"></path>'),
  python: svgBase('<path d="M14 9V5a3 3 0 0 0-3-3H7a3 3 0 0 0-3 3v4a3 3 0 0 0 3 3h7a3 3 0 0 1 3 3v4a3 3 0 0 1-3 3h-4a3 3 0 0 1-3-3v-4"/><path d="M14 9h4a3 3 0 0 1 3 3v4a3 3 0 0 1-3 3h-4"/><circle cx="7" cy="6" r="1"/><circle cx="17" cy="18" r="1"/>'),
  vue: svgBase('<path d="M3 4l9 16l9-16H3z"/><path d="M8 4l4 7l4-7H8z" fill="currentColor"/>'),
  search: svgBase('<circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line>'),
  bot: svgBase('<rect x="3" y="11" width="18" height="10" rx="2"></rect><circle cx="12" cy="5" r="2"></circle><path d="M12 7v4"></path><line x1="8" y1="16" x2="8" y2="16"></line><line x1="16" y1="16" x2="16" y2="16"></line>'),
  rocket: svgBase('<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z"></path><path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"></path><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"></path><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"></path>'),
  board: svgBase('<rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line><line x1="15" y1="3" x2="15" y2="21"></line>')
};

const ICON_MAP = [
  ['python',      ICONS.python], ['pandas',     ICONS.chart], ['analisis',   ICONS.search],
  ['visualiz',    ICONS.chart], ['machine',    ICONS.bot], ['sql',        ICONS.database],
  ['postgres',    ICONS.database], ['diseño de b',ICONS.layout], ['nosql',      ICONS.server],
  ['mongo',       ICONS.server], ['redis',      ICONS.server], ['javascript', ICONS.code],
  ['vue',         ICONS.vue], ['html',       ICONS.layout], ['css',        ICONS.layout],
  ['django',      ICONS.code], ['docker',     ICONS.box], ['git',        ICONS.git],
  ['linux',       ICONS.terminal], ['despliegue', ICONS.rocket], ['scrum',      ICONS.board],
  ['agile',       ICONS.board], ['clean',      ICONS.box], ['api',        ICONS.code],
  ['testing',     ICONS.search], ['backend',    ICONS.server], ['frontend',   ICONS.layout],
  ['data',        ICONS.chart], ['web',        ICONS.layout], ['devops',     ICONS.tool],
];

function getSkillIcon(area = '') {
  const a = area.toLowerCase();
  for (const [kw, icon] of ICON_MAP) {
    if (a.includes(kw)) return icon;
  }
  return ICONS.tool;
}

const CAT_ICON_MAP = {
  'data': ICONS.chart, 'analytics': ICONS.chart, 'web': ICONS.layout, 'bases': ICONS.database,
  'database': ICONS.database, 'devops': ICONS.tool, 'tools': ICONS.tool,
  'herramienta': ICONS.tool, 'metodolog': ICONS.board, 'backend': ICONS.server,
  'frontend': ICONS.layout, 'cloud': ICONS.cloud, 'mobile': ICONS.code,
};

function getCatIcon(nombre = '') {
  const n = nombre.toLowerCase();
  for (const [kw, icon] of Object.entries(CAT_ICON_MAP)) {
    if (n.includes(kw)) return icon;
  }
  return ICONS.code;
}

// ── Chips ──────────────────────────────────────────────────────────────────
function parseChips(h = '') {
  return h.split(',').map(c => c.trim()).filter(Boolean);
}

// ── Computed: grouped ─────────────────────────────────────────────────────────
const groupedCategories = computed(() =>
  rawCategorias.value
    .map(cat => ({
      ...cat,
      icon: getCatIcon(cat.nombre),
      skills: rawTools.value.filter(t => t.id_categorias === cat.id),
    }))
    .filter(cat => cat.skills.length > 0)
);

// ── Skills proxy with reactive state ─────────────────────────────────────────
const visibleSkills = computed(() => {
  const cat = groupedCategories.value.find(c => c.id === activeCatId.value);
  if (!cat) return [];
  return cat.skills.map(skill => ({
    ...skill,
    get flipped()   { return getState(skill).flipped; },
    get animated()  { return getState(skill).animated; },
  }));
});

// ── Flip ──────────────────────────────────────────────────────────────────────
function toggleFlip(skill) {
  getState(skill).flipped = !getState(skill).flipped;
}

// ── Category change with stagger animation ────────────────────────────────────
function setCategory(id) {
  if (activeCatId.value !== id) {
    activeCatId.value = id;
    triggerAnimations();
  }
}

// ── Drag to scroll tabs ───────────────────────────────────────────────────────
const tabsWrap = ref(null);
let isDragging = false;
let startX;
let scrollLeft;

function onDragStart(e) {
  isDragging = true;
  startX = e.pageX - tabsWrap.value.offsetLeft;
  scrollLeft = tabsWrap.value.scrollLeft;
}

function onDragEnd() {
  isDragging = false;
}

function onDragMove(e) {
  if (!isDragging) return;
  e.preventDefault();
  const x = e.pageX - tabsWrap.value.offsetLeft;
  const walk = (x - startX) * 2;
  tabsWrap.value.scrollLeft = scrollLeft - walk;
}

// ── Animations ────────────────────────────────────────────────────────────────
function triggerAnimations() {
  // Reset animations for the new category's skills
  const cat = groupedCategories.value.find(c => c.id === activeCatId.value);
  if (!cat) return;
  cat.skills.forEach(skill => {
    getState(skill).animated  = false;
    getState(skill).flipped   = false;
  });
  // Stagger animate
  nextTick(() => {
    cat.skills.forEach((skill, i) => {
      setTimeout(() => {
        getState(skill).animated = true;
      }, 200 + i * 110);
    });
  });
}

// ── TransitionGroup hooks ─────────────────────────────────────────────────────
function onBeforeEnter(el) {
  el.style.opacity   = '0';
  el.style.transform = 'translateY(22px) scale(0.93)';
  el.style.filter    = 'blur(4px)';
}

function onEnter(el, done) {
  const idx = parseInt(el.dataset.idx) || 0;
  const delay = idx * 70;
  el.style.transition = [
    `opacity 0.42s ease ${delay}ms`,
    `transform 0.42s cubic-bezier(0.34, 1.56, 0.64, 1) ${delay}ms`,
    `filter 0.42s ease ${delay}ms`,
  ].join(', ');
  requestAnimationFrame(() => {
    el.style.opacity   = '1';
    el.style.transform = 'translateY(0) scale(1)';
    el.style.filter    = 'blur(0)';
  });
  setTimeout(done, 420 + delay);
}

function onLeave(el, done) {
  el.style.transition = 'opacity 0.18s ease, transform 0.18s ease';
  el.style.opacity    = '0';
  el.style.transform  = 'scale(0.9)';
  setTimeout(done, 180);
}

// ── Fetch ─────────────────────────────────────────────────────────────────────
async function fetchData() {
  loading.value = true;
  try {
    const [rt, rc] = await Promise.all([
      fetch('/api/tools/'),
      fetch('/api/categorias/'),
    ]);
    if (rt.ok) rawTools.value      = await rt.json();
    if (rc.ok) rawCategorias.value = await rc.json();

    if (groupedCategories.value.length > 0) {
      activeCatId.value = groupedCategories.value[0].id;
    }
  } catch (err) {
    console.error('[Skills] Error al cargar:', err);
  } finally {
    loading.value = false;
  }
}

// ── Fade-up observer ──────────────────────────────────────────────────────────
function observeFadeUp() {
  const obs = new IntersectionObserver(
    entries => entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); }),
    { threshold: 0.1 }
  );
  document.querySelectorAll('.fade-up').forEach(el => obs.observe(el));
}

// ── Lifecycle ─────────────────────────────────────────────────────────────────
onMounted(async () => {
  await fetchData();
  await nextTick();
  observeFadeUp();
  triggerAnimations();
});
</script>

<style scoped>
/* =====================================================================
   SECTION
===================================================================== */
.skills-section { overflow: hidden; }
.section-intro  { margin-bottom: 2.5rem; }

/* =====================================================================
   SKELETON
===================================================================== */
.sk-wrap { display: flex; flex-direction: column; gap: 2rem; }

.sk-tabs {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.sk-tab {
  width: 140px; height: 44px;
  border-radius: 50px;
  background: rgba(255,255,255,0.05);
  animation: shimmer 1.6s ease-in-out infinite;
}

.sk-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
  gap: 1.5rem;
}

.sk-card {
  height: 280px;
  display: flex; flex-direction: column;
  align-items: center;
  padding: 1.5rem;
  gap: 1rem;
}

.sk-ring {
  width: 130px; height: 130px;
  border-radius: 50%;
  animation: shimmer 1.6s ease-in-out infinite;
  background: linear-gradient(90deg,rgba(255,255,255,0.04) 25%,rgba(255,255,255,0.09) 50%,rgba(255,255,255,0.04) 75%);
  background-size: 200% 100%;
}

.sk-lines { width: 100%; display: flex; flex-direction: column; gap: 0.5rem; align-items: center; }

.sk-line {
  border-radius: 50px;
  animation: shimmer 1.6s ease-in-out infinite;
  background: linear-gradient(90deg,rgba(255,255,255,0.04) 25%,rgba(255,255,255,0.09) 50%,rgba(255,255,255,0.04) 75%);
  background-size: 200% 100%;
}
.sk-title { width: 68%; height: 13px; }
.sk-badge { width: 44%; height: 22px; }

@keyframes shimmer {
  from { background-position: -200% 0; }
  to   { background-position:  200% 0; }
}

/* =====================================================================
   CATEGORY TABS
===================================================================== */
.cat-tabs-wrap {
  margin-bottom: 2.5rem;
  overflow-x: auto;
  padding-bottom: 0.25rem;
  /* Hide scrollbar */
  scrollbar-width: none;
  cursor: grab;
}
.cat-tabs-wrap:active { cursor: grabbing; }
.cat-tabs-wrap::-webkit-scrollbar { display: none; }

.cat-tabs {
  display: flex;
  gap: 0.65rem;
  min-width: max-content;
}

.cat-tab {
  display: flex;
  align-items: center;
  gap: 0.55rem;
  padding: 0.6rem 1.1rem;
  border-radius: 50px;
  border: 1px solid var(--border-subtle);
  background: rgba(255,255,255,0.02);
  color: var(--text-secondary);
  cursor: pointer;
  font-size: 0.85rem;
  font-weight: 600;
  font-family: var(--font-body);
  transition: all 0.25s var(--ease-smooth);
  white-space: nowrap;
  position: relative;
  overflow: hidden;
}

.cat-tab::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 120%, rgba(0,212,255,0.08), transparent 70%);
  opacity: 0;
  transition: opacity 0.25s;
}

.cat-tab:hover { border-color: rgba(0,212,255,0.3); color: var(--text-primary); }
.cat-tab:hover::before { opacity: 1; }

.cat-tab.active {
  border-color: var(--accent-cyan);
  background: rgba(0,212,255,0.08);
  color: var(--accent-cyan);
  box-shadow: 0 0 20px rgba(0,212,255,0.12), inset 0 0 20px rgba(0,212,255,0.04);
}
.cat-tab.active::before { opacity: 1; }

.tab-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
}
.tab-name  { letter-spacing: 0.01em; }

.tab-right {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  margin-left: 0.2rem;
}

.tab-count {
  background: rgba(255,255,255,0.08);
  border-radius: 50px;
  padding: 0.1rem 0.5rem;
  font-size: 0.72rem;
  font-weight: 700;
}
.cat-tab.active .tab-count { background: rgba(0,212,255,0.18); }

.tab-avg {
  font-size: 0.7rem;
  font-weight: 700;
  padding: 0.12rem 0.5rem;
  border-radius: 50px;
}
.avg-high { background: rgba(0,212,255,0.12);  color: #00d4ff; }
.avg-med  { background: rgba(99,102,241,0.12); color: #818cf8; }
.avg-low  { background: rgba(240,49,109,0.12); color: #f0316d; }

/* =====================================================================
   SKILLS GRID
===================================================================== */
.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
  gap: 1.5rem;
  /* position needed for TransitionGroup absolute */
}

/* =====================================================================
   SKILL CARD — 3D Flip
===================================================================== */
.skill-card {
  height: 290px;
  perspective: 900px;
  cursor: pointer;
  outline: none;
}

.skill-card:focus-visible .card-inner {
  box-shadow: 0 0 0 2px var(--accent-cyan);
  border-radius: var(--radius-lg);
}

.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.7s cubic-bezier(0.4, 0, 0.2, 1);
}

.skill-card.flipped .card-inner { transform: rotateY(180deg); }

/* ---- Faces ---- */
.face {
  position: absolute;
  inset: 0;
  border-radius: var(--radius-lg);
  backface-visibility: hidden;
  -webkit-backface-visibility: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.2rem 1.1rem 1rem;
  overflow: hidden;
  transition: visibility 0s 0.35s, box-shadow 0.3s ease, border-color 0.3s ease;
}

.face-front {
  visibility: visible;
}

.skill-card.flipped .face-front {
  visibility: hidden;
}

.face-back { 
  transform: rotateY(180deg); 
  align-items: flex-start;
  visibility: hidden;
}

.skill-card.flipped .face-back {
  visibility: visible;
}

/* Hover glow per level */
.card-high .face-front:hover {
  box-shadow: 0 0 32px rgba(0,212,255,0.2), 0 4px 24px rgba(0,0,0,0.4);
  border-color: rgba(0,212,255,0.3);
}
.card-med .face-front:hover {
  box-shadow: 0 0 32px rgba(99,102,241,0.2), 0 4px 24px rgba(0,0,0,0.4);
  border-color: rgba(99,102,241,0.3);
}
.card-low .face-front:hover {
  box-shadow: 0 0 32px rgba(240,49,109,0.2), 0 4px 24px rgba(0,0,0,0.4);
  border-color: rgba(240,49,109,0.3);
}

/* ---- Accent line (top) ---- */
.accent-line {
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  border-radius: var(--radius-lg) var(--radius-lg) 0 0;
}
.line-high { background: linear-gradient(90deg, #00d4ff, #3a6ef5); }
.line-med  { background: linear-gradient(90deg, #3a6ef5, #818cf8); }
.line-low  { background: linear-gradient(90deg, #f0316d, #fb923c); }

/* =====================================================================
   SVG RING
===================================================================== */
.ring-wrap {
  position: relative;
  width: 138px;
  height: 138px;
  margin-bottom: 0.9rem;
  flex-shrink: 0;
}

.ring-svg { width: 100%; height: 100%; overflow: visible; }

.ring-arc {
  transform: rotate(-90deg);
  transform-origin: 65px 65px;
  transition: stroke-dashoffset 1.3s cubic-bezier(0.4, 0, 0.2, 1) 0.15s;
}

.ring-center {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.1rem;
}

.ring-emoji {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.55rem;
  filter: drop-shadow(0 0 6px rgba(0,0,0,0.5));
}

.ring-pct {
  font-family: var(--font-display);
  font-size: 1.1rem;
  font-weight: 700;
  line-height: 1;
}
.ring-pct sup { font-size: 0.6em; }
.pct-high { color: #00d4ff; text-shadow: 0 0 12px rgba(0,212,255,0.5); }
.pct-med  { color: #818cf8; text-shadow: 0 0 12px rgba(99,102,241,0.5); }
.pct-low  { color: #f0316d; text-shadow: 0 0 12px rgba(240,49,109,0.5); }

/* =====================================================================
   FRONT INFO
===================================================================== */
.front-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  text-align: center;
}

.skill-name {
  font-family: var(--font-display);
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--text-primary);
  line-height: 1.3;
  text-align: center;
}

/* ---- Level badge ---- */
.level-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding: 0.22rem 0.65rem;
  border-radius: 50px;
}
.badge-high { background: rgba(0,212,255,0.12);  color: #00d4ff; }
.badge-med  { background: rgba(99,102,241,0.12); color: #818cf8; }
.badge-low  { background: rgba(240,49,109,0.12); color: #f0316d; }

.badge-pulse {
  width: 5px; height: 5px;
  border-radius: 50%;
  background: currentColor;
  animation: pulse-dot 2.2s ease-in-out infinite;
}

@keyframes pulse-dot {
  0%, 100% { opacity: 1; transform: scale(1); }
  50%       { opacity: 0.4; transform: scale(0.65); }
}

/* ---- Flip hint ---- */
.flip-hint {
  position: absolute;
  bottom: 0.8rem;
  right: 1rem;
  display: flex;
  align-items: center;
  gap: 0.3rem;
  font-size: 0.65rem;
  color: var(--text-muted);
  font-weight: 500;
  opacity: 0;
  transition: opacity 0.2s;
}
.skill-card:hover .flip-hint { opacity: 1; }
.back-hint { right: auto; left: 1rem; bottom: 0.8rem; }

/* =====================================================================
   CARD BACK
===================================================================== */
.back-header {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  width: 100%;
  margin-bottom: 0.8rem;
  margin-top: 0.3rem;
}

.back-emoji {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.9rem;
  flex-shrink: 0;
}
.back-skill-name { text-align: left; margin-bottom: 0.3rem; }

/* Progress bar on back */
.back-bar-wrap {
  display: flex;
  align-items: center;
  gap: 0.55rem;
  width: 100%;
  margin-bottom: 1rem;
}

.back-bar-track {
  flex: 1;
  height: 5px;
  background: rgba(255,255,255,0.06);
  border-radius: 3px;
  overflow: hidden;
}

.back-bar-fill {
  height: 100%;
  border-radius: 3px;
  transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1) 0.3s;
}
.fill-high { background: linear-gradient(90deg, #00d4ff, #3a6ef5); }
.fill-med  { background: linear-gradient(90deg, #3a6ef5, #818cf8); }
.fill-low  { background: linear-gradient(90deg, #f0316d, #fb923c); }

.back-bar-pct {
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--text-secondary);
  white-space: nowrap;
}

/* Tech chips */
.back-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  overflow-y: auto;
  max-height: 118px;
  width: 100%;
  scrollbar-width: none;
  padding-bottom: 1.6rem; /* room for hint */
}
.back-chips::-webkit-scrollbar { display: none; }

.chip {
  font-size: 0.7rem;
  font-weight: 600;
  padding: 0.22rem 0.6rem;
  border-radius: 5px;
  letter-spacing: 0.01em;
  white-space: nowrap;
  transition: transform 0.15s ease;
}
.chip:hover { transform: translateY(-1px); }

.chip-high { background: rgba(0,212,255,0.08);  color: #00d4ff; border: 1px solid rgba(0,212,255,0.18); }
.chip-med  { background: rgba(99,102,241,0.08); color: #818cf8; border: 1px solid rgba(99,102,241,0.18); }
.chip-low  { background: rgba(240,49,109,0.08); color: #f0316d; border: 1px solid rgba(240,49,109,0.18); }

/* =====================================================================
   EMPTY STATE
===================================================================== */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  padding: 5rem 2rem;
  text-align: center;
  color: var(--text-muted);
}
.empty-state span { font-size: 2.8rem; }
.empty-state strong { color: var(--accent-cyan); }

/* =====================================================================
   TRANSITION GROUP ANIMATIONS (handled by JS hooks)
   These classes are for Vue's auto-managed leave transition
===================================================================== */
.card-anim-move {
  transition: transform 0.4s ease;
}

/* =====================================================================
   RESPONSIVE
===================================================================== */
@media (max-width: 900px) {
  .skills-grid { grid-template-columns: repeat(auto-fill, minmax(190px, 1fr)); gap: 1.2rem; }
  .skill-card  { height: 275px; }
  .ring-wrap   { width: 124px; height: 124px; }
}

@media (max-width: 620px) {
  .skills-grid { grid-template-columns: repeat(2, 1fr); gap: 0.9rem; }
  .skill-card  { height: 255px; }
  .ring-wrap   { width: 112px; height: 112px; }
  .tab-name    { display: none; }
  .tab-right   { margin-left: 0; }
}

@media (max-width: 380px) {
  .skills-grid { grid-template-columns: 1fr 1fr; gap: 0.75rem; }
  .skill-card  { height: 235px; }
}
</style>
