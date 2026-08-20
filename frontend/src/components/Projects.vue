<template>
  <section id="projects" class="section">
    <div class="container">
      <div class="section-intro fade-up">
        <span class="section-label">// 03 · Proyectos</span>
        <h2 class="section-title">Proyectos Destacados</h2>
        <p class="section-subtitle">Soluciones desarrolladas desde la concepción hasta el despliegue</p>
      </div>

      <!-- Loading skeleton -->
      <div v-if="loading" class="projects-list">
        <div v-for="n in 2" :key="n" class="project-card glass skeleton-card fade-up">
          <div class="sk-line sk-title"></div>
          <div class="sk-line sk-body"></div>
          <div class="sk-line sk-body short"></div>
        </div>
      </div>

      <!-- Empty state -->
      <div v-else-if="projects.length === 0" class="empty-state fade-up">
        <span class="empty-icon">🗂️</span>
        <p>No hay proyectos registrados aún.</p>
      </div>

      <div v-else class="projects-list">
        <article
          v-for="(project, index) in projects"
          :key="project.id"
          class="project-card glass fade-up"
        >
          <!-- Number accent -->
          <span class="project-number">{{ String(index + 1).padStart(2, '0') }}</span>

          <div class="project-body">
            <!-- Top row -->
            <div class="project-top">
              <div>
                <div class="project-status">
                  <span class="status-dot" :class="project.estado ? 'dot-done' : 'dot-wip'"></span>
                  <span class="status-text">{{ project.estado ? 'Completado' : 'En desarrollo' }}</span>
                </div>
                <h3 class="project-title">{{ project.nombre }}</h3>
              </div>
              <div class="project-icon-wrap">
                <span class="project-icon">{{ getProjectIcon(project.nombre) }}</span>
              </div>
            </div>

            <!-- Challenge -->
            <div v-if="project.reto" class="project-challenge">
              <span class="challenge-label">Reto</span>
              <p class="challenge-text">{{ project.reto }}</p>
            </div>

            <!-- Description -->
            <p class="project-desc">{{ project.descripcion }}</p>

            <!-- Tech badges from herramientas array -->
            <div class="project-techs" v-if="project.herramientas && project.herramientas.length">
              <span
                v-for="tech in project.herramientas"
                :key="tech"
                class="tech-chip"
                :class="getTechCategory(tech)"
              >{{ tech }}</span>
            </div>

            <!-- Links -->
            <div class="project-links">
              <a
                :href="project.demo || '#'"
                target="_blank"
                rel="noopener noreferrer"
                class="project-link-btn"
                :class="{ 'disabled-link': !project.demo }"
                @click="!project.demo && $event.preventDefault()"
              >
                <span>Ver Demo / Proyecto</span>
                <svg class="redirect-icon" viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                  <polyline points="15 3 21 3 21 9"></polyline>
                  <line x1="10" y1="14" x2="21" y2="3"></line>
                </svg>
              </a>
              <a
                :href="project.github || '#'"
                target="_blank"
                rel="noopener noreferrer"
                class="project-link-btn secondary"
                :class="{ 'disabled-link': !project.github }"
                @click="!project.github && $event.preventDefault()"
              >
                <span>Repositorio</span>
                <svg class="redirect-icon" viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                  <polyline points="15 3 21 3 21 9"></polyline>
                  <line x1="10" y1="14" x2="21" y2="3"></line>
                </svg>
              </a>
            </div>
          </div>

          <!-- Hover line animation -->
          <div class="card-line"></div>
        </article>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const projects = ref([]);
const loading  = ref(true);

// Classify tech chips by category based on keyword matching
const FRONTEND_KEYS  = ['vue', 'react', 'angular', 'svelte', 'html', 'css', 'tailwind', 'vite', 'nuxt', 'next', 'chart', 'bootstrap', 'sass', 'ui'];
const BACKEND_KEYS   = ['django', 'node', 'express', 'fastapi', 'spring', 'laravel', 'api', 'rest', 'graphql', 'python', 'java', 'php', 'ruby', 'golang', 'c#', 'asp', '.net', 'jwt', 'auth'];
const DB_KEYS        = ['sql', 'postgres', 'mysql', 'mongodb', 'redis', 'sqlite', 'oracle', 'supabase', 'db', 'database', 'diagrama', 'normaliz', 'er'];
const MOBILE_KEYS    = ['mobile', 'android', 'ios', 'flutter', 'react native', 'biometría', 'biometria', 'facial', 'gps'];

function getTechCategory(tech) {
  const t = tech.toLowerCase();
  if (MOBILE_KEYS.some(k  => t.includes(k))) return 'cat-mobile';
  if (DB_KEYS.some(k      => t.includes(k))) return 'cat-db';
  if (BACKEND_KEYS.some(k => t.includes(k))) return 'cat-backend';
  return 'cat-frontend';
}

const ICONS = [
  ['amazonia', '🌿'], ['softvar', '💼'], ['portafolio', '🗂️'], ['ecommerce', '🛒'],
  ['blog', '✍️'], ['chat', '💬'], ['admin', '⚙️'], ['api', '🔌'], ['data', '📊'],
  ['machine', '🤖'], ['analisis', '🔍'], ['game', '🎮'],
];

function getProjectIcon(nombre = '') {
  const n = nombre.toLowerCase();
  for (const [keyword, icon] of ICONS) {
    if (n.includes(keyword)) return icon;
  }
  return '🚀';
}

const fetchProyectos = async () => {
  loading.value = true;
  try {
    const API_URL = import.meta.env.VITE_API_URL || '';
    const res = await fetch(`${API_URL}/api/proyectos/`);
    if (res.ok) projects.value = await res.json();
  } catch (err) {
    console.error('[Projects] Error al cargar proyectos:', err);
  } finally {
    loading.value = false;
  }
};

onMounted(async () => {
  await fetchProyectos();

  // Animate fade-up after data is loaded
  requestAnimationFrame(() => {
    const els = document.querySelectorAll('.fade-up');
    const observer = new IntersectionObserver(
      (entries) => entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); }),
      { threshold: 0.1 }
    );
    els.forEach(el => observer.observe(el));
  });
});
</script>

<style scoped>
.section-intro { margin-bottom: 3.5rem; }

.projects-list {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

/* ---- Skeleton ---- */
.skeleton-card {
  min-height: 180px;
  padding: 2.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.sk-line {
  height: 16px;
  border-radius: 6px;
  background: linear-gradient(90deg, rgba(255,255,255,0.04) 25%, rgba(255,255,255,0.09) 50%, rgba(255,255,255,0.04) 75%);
  background-size: 200% 100%;
  animation: shimmer 1.6s ease-in-out infinite;
}

.sk-title  { width: 55%; height: 24px; }
.sk-body   { width: 85%; }
.sk-body.short { width: 60%; }

@keyframes shimmer {
  from { background-position: -200% 0; }
  to   { background-position: 200% 0; }
}

/* ---- Empty state ---- */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  padding: 4rem 2rem;
  color: var(--text-muted);
  text-align: center;
}

.empty-icon { font-size: 2.5rem; }

/* ---- Card ---- */
.project-card {
  position: relative;
  overflow: hidden;
  padding: 2.5rem;
  transition: transform var(--duration-base) var(--ease-smooth),
              box-shadow var(--duration-base) var(--ease-smooth),
              border-color var(--duration-base);
}

.project-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--glow-cyan);
  border-color: var(--border-glow);
}

/* Number accent */
.project-number {
  position: absolute;
  top: 1.8rem;
  right: 2.2rem;
  font-family: var(--font-display);
  font-size: 4.5rem;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.03);
  line-height: 1;
  letter-spacing: -0.04em;
  pointer-events: none;
  user-select: none;
  transition: color var(--duration-slow);
}

.project-card:hover .project-number {
  color: rgba(0, 212, 255, 0.06);
}

.project-body {
  position: relative;
  z-index: 1;
}

/* Top row */
.project-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.project-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.status-dot {
  width: 8px; height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.dot-done { background: var(--accent-green); box-shadow: 0 0 6px var(--accent-green); }
.dot-wip  { background: #facc15; box-shadow: 0 0 6px #facc15; }

.status-text {
  font-size: 0.78rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-muted);
}

.project-title {
  font-size: 1.65rem;
  font-weight: 700;
  color: var(--text-primary);
  letter-spacing: -0.02em;
}

.project-icon-wrap {
  background: rgba(255,255,255,0.04);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-md);
  width: 56px; height: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  transition: background var(--duration-base), transform var(--duration-base) var(--ease-bounce);
}

.project-card:hover .project-icon-wrap {
  background: rgba(0, 212, 255, 0.08);
  transform: scale(1.08) rotate(-4deg);
}

.project-icon { font-size: 1.8rem; }

/* Challenge box */
.project-challenge {
  background: rgba(0, 212, 255, 0.04);
  border-left: 2px solid var(--accent-cyan);
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  padding: 0.85rem 1.1rem;
  margin-bottom: 1.25rem;
}

.challenge-label {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--accent-cyan);
  display: block;
  margin-bottom: 0.3rem;
}

.challenge-text {
  font-size: 0.92rem;
  color: var(--text-secondary);
  line-height: 1.55;
}

.project-desc {
  font-size: 0.95rem;
  color: var(--text-secondary);
  line-height: 1.65;
  margin-bottom: 1.5rem;
}

/* Tech chips */
.project-techs {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.tech-chip {
  font-size: 0.78rem;
  font-weight: 600;
  padding: 0.3rem 0.8rem;
  border-radius: 6px;
  letter-spacing: 0.02em;
}

.cat-frontend {
  background: rgba(0, 212, 255, 0.1);
  color: var(--accent-cyan);
  border: 1px solid rgba(0, 212, 255, 0.18);
}

.cat-backend {
  background: rgba(58, 110, 245, 0.1);
  color: #818cf8;
  border: 1px solid rgba(58, 110, 245, 0.2);
}

.cat-db {
  background: rgba(139, 92, 246, 0.1);
  color: #c084fc;
  border: 1px solid rgba(139, 92, 246, 0.2);
}

.cat-mobile {
  background: rgba(240, 49, 109, 0.1);
  color: var(--accent-pink);
  border: 1px solid rgba(240, 49, 109, 0.18);
}

/* Links & Redirection buttons */
.project-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 1rem;
}

.project-link-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--accent-cyan);
  background: rgba(0, 212, 255, 0.06);
  border: 1px solid rgba(0, 212, 255, 0.2);
  border-radius: var(--radius-sm);
  text-decoration: none;
  transition: all var(--duration-base) var(--ease-smooth);
}

.project-link-btn:hover:not(.disabled-link) {
  background: rgba(0, 212, 255, 0.15);
  border-color: var(--accent-cyan);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 212, 255, 0.15);
}

.project-link-btn.secondary {
  color: var(--text-secondary);
  background: rgba(255, 255, 255, 0.03);
  border-color: var(--border-subtle);
}

.project-link-btn.secondary:hover:not(.disabled-link) {
  color: var(--text-primary);
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(255, 255, 255, 0.3);
}

.project-link-btn.disabled-link {
  opacity: 0.6;
  cursor: pointer;
}

.redirect-icon {
  transition: transform var(--duration-base);
}

.project-link-btn:hover:not(.disabled-link) .redirect-icon {
  transform: translate(2px, -2px);
}

/* Hover line */
.card-line {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 2px;
  width: 0;
  background: linear-gradient(90deg, var(--accent-cyan), var(--accent-blue));
  transition: width 0.5s var(--ease-smooth);
  border-radius: 0 0 0 0;
}

.project-card:hover .card-line { width: 100%; }

/* Responsive */
@media (max-width: 600px) {
  .project-card { padding: 1.75rem; }
  .project-number { font-size: 3rem; }
}
</style>
