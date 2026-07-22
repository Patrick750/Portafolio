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
    ]
  },
  {
    title: 'App Móvil',
    icon: '📱',
    status: 'Completado',
    challenge: 'Construir una aplicación móvil nativa con flujo intuitivo que resuelva necesidades específicas del usuario final con mínima fricción.',
    description: 'Aplicación Android compilada (.apk) con ciclo de vida gestionado correctamente, interfaz limpia orientada a la experiencia de usuario y lógica de negocio robusta.',
    techs: [
      { name: 'Android',         category: 'cat-mobile' },
      { name: 'Java / Kotlin',   category: 'cat-mobile' },
      { name: 'UI/UX',           category: 'cat-frontend' },
      { name: 'SQLite',          category: 'cat-db' },
    ]
  },
  {
    title: 'Tecnogamer',
    icon: '🎮',
    status: 'Completado',
    challenge: 'Modelar una base de datos relacional completa para una plataforma de gestión e-commerce orientada al rubro de hardware y videojuegos.',
    description: 'Diseño de modelo entidad-relación normalizado, implementación de consultas SQL avanzadas y arquitectura backend para soportar operaciones CRUD de alto volumen.',
    techs: [
      { name: 'SQL Avanzado',    category: 'cat-db' },
      { name: 'Diagramado ER',   category: 'cat-db' },
      { name: 'Backend',         category: 'cat-backend' },
      { name: 'APIs RESTful',    category: 'cat-backend' },
    ]
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
