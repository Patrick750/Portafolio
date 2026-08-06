<template>
  <section id="projects" class="section">
    <div class="container">
      <div class="section-intro fade-up">
        <span class="section-label">// 03 · Proyectos</span>
        <h2 class="section-title">Proyectos Destacados</h2>
        <p class="section-subtitle">Soluciones desarrolladas desde la concepción hasta el despliegue</p>
      </div>

      <div class="projects-list">
        <article
          v-for="(project, index) in projects"
          :key="project.title"
          class="project-card glass fade-up"
        >
          <!-- Number accent -->
          <span class="project-number">{{ String(index + 1).padStart(2, '0') }}</span>

          <div class="project-body">
            <!-- Top row -->
            <div class="project-top">
              <div>
                <div class="project-status">
                  <span class="status-dot" :class="project.status === 'Completado' ? 'dot-done' : 'dot-wip'"></span>
                  <span class="status-text">{{ project.status }}</span>
                </div>
                <h3 class="project-title">{{ project.title }}</h3>
              </div>
              <div class="project-icon-wrap">
                <span class="project-icon">{{ project.icon }}</span>
              </div>
            </div>

            <!-- Challenge -->
            <div class="project-challenge">
              <span class="challenge-label">Reto</span>
              <p class="challenge-text">{{ project.challenge }}</p>
            </div>

            <!-- Description -->
            <p class="project-desc">{{ project.description }}</p>

            <!-- Tech badges -->
            <div class="project-techs">
              <span
                v-for="tech in project.techs"
                :key="tech.name"
                class="tech-chip"
                :class="tech.category"
              >{{ tech.name }}</span>
            </div>

            <!-- Links / Redirection section -->
            <div class="project-links">
              <a
                :href="project.links.demo || '#'"
                target="_blank"
                rel="noopener noreferrer"
                class="project-link-btn"
                :class="{ 'disabled-link': !project.links.demo }"
                @click="!project.links.demo && $event.preventDefault()"
              >
                <span>Ver Demo / Proyecto</span>
                <svg class="redirect-icon" viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                  <polyline points="15 3 21 3 21 9"></polyline>
                  <line x1="10" y1="14" x2="21" y2="3"></line>
                </svg>
              </a>
              <a
                :href="project.links.repo || '#'"
                target="_blank"
                rel="noopener noreferrer"
                class="project-link-btn secondary"
                :class="{ 'disabled-link': !project.links.repo }"
                @click="!project.links.repo && $event.preventDefault()"
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

const projects = ref([
  {
    title: 'Amazonia Viva',
    icon: '🌿',
    status: 'Completado',
    challenge: 'Diseñar un sistema escalable capaz de centralizar y gestionar procesos ecológicos y comerciales de una región geográfica extensa.',
    description: 'Plataforma web completa con modelo de datos relacional normalizado, interfaz responsiva en Vue.js y arquitectura orientada a la escalabilidad y mantenibilidad.',
    techs: [
      { name: 'Vue.js',          category: 'cat-frontend' },
      { name: 'CSS / UI',        category: 'cat-frontend' },
      { name: 'SQL',             category: 'cat-db' },
      { name: 'Diagramas ER',    category: 'cat-db' },
      { name: 'Arquitectura',    category: 'cat-backend' },
    ],
    links: {
      demo: 'https://amazoniaviva.adsoproject.dev/',
      repo: ''
    }
  },
  {
    title: 'SoftVar — Sistema de Control de Asistencia y Nómina',
    icon: '💼',
    status: 'Completado',
    challenge: 'Implementar un sistema web integral de control de asistencia biométrica facial con GPS y liquidación de nómina según la legislación colombiana (CST) para PyMES.',
    description: 'Sistema SPA + API REST (Vue 3 + Django 6) con reconocimiento facial (face-api.js), validación geográfica GPS, motor de liquidación de horas extra, generación de desprendibles PDF, exportación ACH y dashboard interactivo con Chart.js.',
    techs: [
      { name: 'Vue 3',           category: 'cat-frontend' },
      { name: 'Vite',            category: 'cat-frontend' },
      { name: 'Chart.js',        category: 'cat-frontend' },
      { name: 'Python / Django', category: 'cat-backend' },
      { name: 'Django REST',     category: 'cat-backend' },
      { name: 'SQLite',          category: 'cat-db' },
      { name: 'Biometría Facial',category: 'cat-mobile' }
    ],
    links: {
      demo: 'https://softvar.adsoproject.dev/',
      repo: ''
    }
  }
]);

onMounted(() => {
  const els = document.querySelectorAll('.fade-up');
  const observer = new IntersectionObserver(
    (entries) => entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); }),
    { threshold: 0.1 }
  );
  els.forEach(el => observer.observe(el));
});
</script>

<style scoped>
.section-intro { margin-bottom: 3.5rem; }

.projects-list {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

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
