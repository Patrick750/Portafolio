<template>
  <section id="skills" class="section">
    <div class="container">
      <div class="section-intro fade-up">
        <span class="section-label">// 01 · Expertise</span>
        <h2 class="section-title">Habilidades Técnicas</h2>
        <p class="section-subtitle">Tecnologías que aplico en el desarrollo de soluciones reales</p>
      </div>

      <!-- Categories -->
      <div v-for="cat in categories" :key="cat.id" class="category-block fade-up">
        <div class="category-header">
          <span class="category-icon">{{ cat.icon }}</span>
          <h3 class="category-name">{{ cat.name }}</h3>
        </div>

        <div class="skills-list">
          <div
            v-for="(skill, idx) in cat.skills"
            :key="skill.name"
            class="skill-row glass"
            :class="{ 'row-open': skill.isOpen }"
            @click="toggleSkill(skill)"
          >
            <!-- Header row -->
            <div class="skill-row-header">
              <span class="skill-icon-sm">{{ skill.icon }}</span>
              <div class="skill-meta">
                <span class="skill-name">{{ skill.name }}</span>
                <!-- Progress bar -->
                <div class="progress-track">
                  <div
                    class="progress-fill"
                    :class="skill.levelClass"
                    :style="{ width: skill.isOpen || skill.animatated ? skill.progress + '%' : '0%' }"
                  ></div>
                </div>
              </div>
              <span class="skill-badge" :class="skill.levelClass">{{ skill.level }}</span>
              <svg class="chevron" :class="{ rotated: skill.isOpen }" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="18" height="18">
                <polyline points="6 9 12 15 18 9"/>
              </svg>
            </div>

            <!-- Expandable detail -->
            <div class="skill-detail" :class="{ expanded: skill.isOpen }">
              <p class="skill-description">{{ skill.description }}</p>
              <div class="skill-chips">
                <span v-for="chip in skill.chips" :key="chip" class="chip">{{ chip }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Learning in Progress -->
      <div class="section-intro learning-intro fade-up">
        <span class="section-label" style="color: var(--accent-pink)">// 02 · En Proceso</span>
        <h2 class="section-title" style="font-size: 1.8rem;">Aprendizaje Activo</h2>
        <p class="section-subtitle">Tecnologías que estoy incorporando a mi stack</p>
      </div>

      <div class="skills-list learning-list fade-up">
        <div
          v-for="skill in learningSkills"
          :key="skill.name"
          class="skill-row glass learning-row"
          :class="{ 'row-open': skill.isOpen }"
          @click="toggleSkill(skill)"
        >
          <div class="skill-row-header">
            <span class="skill-icon-sm">{{ skill.icon }}</span>
            <div class="skill-meta">
              <span class="skill-name">{{ skill.name }}</span>
              <div class="progress-track">
                <div class="progress-fill level-learning" style="width: 30%"></div>
              </div>
            </div>
            <span class="skill-badge level-learning">En Estudio</span>
            <svg class="chevron" :class="{ rotated: skill.isOpen }" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" width="18" height="18">
              <polyline points="6 9 12 15 18 9"/>
            </svg>
          </div>
          <div class="skill-detail" :class="{ expanded: skill.isOpen }">
            <p class="skill-description">{{ skill.description }}</p>
            <div class="skill-chips">
              <span v-for="chip in skill.chips" :key="chip" class="chip chip-learning">{{ chip }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const toggleSkill = (skill) => {
  skill.isOpen = !skill.isOpen;
  skill.animatated = true;
};

const categories = ref([
  {
    id: 'data',
    icon: '📊',
    name: 'Data & Python',
    skills: [
      {
        name: 'Python Data Science',
        icon: '🐍',
        level: 'Avanzado',
        levelClass: 'level-high',
        progress: 88,
        isOpen: false,
        animatated: false,
        description: 'Análisis, transformación y visualización de datos a gran escala para extraer insights accionables de conjuntos complejos de datos.',
        chips: ['Pandas', 'Polars', 'NumPy', 'Matplotlib', 'Data Cleaning', 'EDA']
      },
    ]
  },
  {
    id: 'web',
    icon: '🌐',
    name: 'Web Development',
    skills: [
      {
        name: 'JavaScript Avanzado',
        icon: '💻',
        level: 'Avanzado',
        levelClass: 'level-high',
        progress: 85,
        isOpen: false,
        animatated: false,
        description: 'Dominio de lógica compleja y asincronismo. Sólida experiencia en la comunicación entre frontend y backend mediante APIs RESTful.',
        chips: ['ES6+', 'Async/Await', 'Fetch API', 'DOM avanzado', 'Módulos', 'Closures']
      },
      {
        name: 'Vue.js & Tailwind CSS',
        icon: '⚡',
        level: 'Intermedio',
        levelClass: 'level-med',
        progress: 65,
        isOpen: false,
        animatated: false,
        description: 'Desarrollo de SPAs reactivas aplicando principios SOLID para componentes modulares, con estilizado ágil y moderno usando Tailwind.',
        chips: ['Vue 3', 'Composition API', 'Reactivity', 'Tailwind CSS', 'SPA', 'Componentes']
      },
      {
        name: 'Desarrollo Backend',
        icon: '⚙️',
        level: 'Intermedio',
        levelClass: 'level-med',
        progress: 65,
        isOpen: false,
        animatated: false,
        description: 'Construcción de servicios con arquitectura limpia. Diseño de APIs RESTful y manejo de autenticación/autorización segura.',
        chips: ['APIs RESTful', 'JWT', 'Principios SOLID', 'Clean Architecture', 'HTTP', 'Auth']
      },
    ]
  },
  {
    id: 'db',
    icon: '🗄️',
    name: 'Bases de Datos',
    skills: [
      {
        name: 'Bases de Datos Relacionales',
        icon: '🗄️',
        level: 'Avanzado',
        levelClass: 'level-high',
        progress: 85,
        isOpen: false,
        animatated: false,
        description: 'Diseño de modelos de entidad-relación, consultas SQL optimizadas y garantía de integridad referencial en sistemas de producción.',
        chips: ['SQL', 'Diagramado ER', 'Normalización', 'Joins complejos', 'Integridad referencial', 'Índices']
      },
    ]
  },
  {
    id: 'tools',
    icon: '🛠️',
    name: 'Herramientas & Metodologías',
    skills: [
      {
        name: 'Git & Control de Versiones',
        icon: '🌿',
        level: 'Intermedio',
        levelClass: 'level-med',
        progress: 70,
        isOpen: false,
        animatated: false,
        description: 'Gestión profesional del código fuente, flujos de trabajo colaborativos, resolución de conflictos y commits semánticos.',
        chips: ['Git Flow', 'Branching', 'Merge/Rebase', 'GitHub', 'Commits semánticos']
      },
      {
        name: 'Metodologías Ágiles',
        icon: '📋',
        level: 'Intermedio',
        levelClass: 'level-med',
        progress: 70,
        isOpen: false,
        animatated: false,
        description: 'Aplicación constante de metodologías ágiles para la entrega de valor continuo y gestión eficiente de proyectos en equipo.',
        chips: ['Scrum', 'Kanban', 'Sprints', 'Backlog', 'Daily standups', 'Retrospectivas']
      },
    ]
  }
]);

const learningSkills = ref([
  {
    name: 'Docker & Despliegue VPS',
    icon: '🐳',
    isOpen: false,
    description: 'Profundizando en contenerización de aplicaciones y despliegue eficiente de servicios web en servidores virtuales (VPS).',
    chips: ['Docker', 'Containers', 'VPS', 'Nginx', 'CI/CD básico']
  },
  {
    name: 'ASP.NET Core',
    icon: '🌐',
    isOpen: false,
    description: 'Explorando el ecosistema Microsoft con C# para la construcción de arquitecturas web empresariales robustas y escalables.',
    chips: ['C#', 'ASP.NET Core', 'MVC', 'Entity Framework', '.NET']
  }
]);

// Intersection Observer para animaciones fade-up
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
.section-intro {
  margin-bottom: 3rem;
}

.category-block {
  margin-bottom: 3.5rem;
}

.category-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 1.25rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid var(--border-subtle);
}

.category-icon { font-size: 1.4rem; }

.category-name {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

/* ---- Skill row ---- */
.skills-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.skill-row {
  cursor: pointer;
  transition: border-color var(--duration-base), box-shadow var(--duration-base);
  overflow: hidden;
}

.skill-row:hover {
  border-color: var(--border-glow);
  box-shadow: var(--glow-cyan);
}

.skill-row-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.1rem 1.4rem;
}

.skill-icon-sm {
  font-size: 1.6rem;
  flex-shrink: 0;
  width: 36px;
  text-align: center;
}

.skill-meta {
  flex: 1;
  min-width: 0;
}

.skill-name {
  display: block;
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-primary);
  margin-bottom: 0.45rem;
}

/* Progress bar */
.progress-track {
  height: 4px;
  background: rgba(255,255,255,0.06);
  border-radius: 2px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  border-radius: 2px;
  transition: width 0.8s var(--ease-smooth);
}

.level-high  .progress-fill,
.progress-fill.level-high  { background: linear-gradient(90deg, var(--accent-cyan), var(--accent-blue)); }
.level-med   .progress-fill,
.progress-fill.level-med   { background: linear-gradient(90deg, var(--accent-blue), #6366f1); }
.level-learning .progress-fill,
.progress-fill.level-learning { background: linear-gradient(90deg, var(--accent-pink), #fb923c); }

.skill-badge {
  flex-shrink: 0;
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding: 0.25rem 0.7rem;
  border-radius: 4px;
}

.level-high {
  background: rgba(0, 212, 255, 0.12);
  color: var(--accent-cyan);
}

.level-med {
  background: rgba(58, 110, 245, 0.12);
  color: #818cf8;
}

.level-learning {
  background: rgba(240, 49, 109, 0.12);
  color: var(--accent-pink);
}

.chevron {
  flex-shrink: 0;
  color: var(--text-muted);
  transition: transform var(--duration-base) var(--ease-smooth), color var(--duration-fast);
}

.skill-row:hover .chevron { color: var(--text-secondary); }
.chevron.rotated { transform: rotate(180deg); }

/* Expandable detail */
.skill-detail {
  max-height: 0;
  overflow: hidden;
  opacity: 0;
  transition: max-height 0.45s var(--ease-smooth), opacity 0.3s var(--ease-smooth), padding 0.3s;
  padding: 0 1.4rem;
  border-top: 0px solid var(--border-subtle);
}

.skill-detail.expanded {
  max-height: 200px;
  opacity: 1;
  padding: 1.25rem 1.4rem;
  border-top: 1px solid var(--border-subtle);
}

.skill-description {
  font-size: 0.93rem;
  color: var(--text-secondary);
  line-height: 1.65;
  margin-bottom: 1rem;
}

.skill-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.chip {
  font-size: 0.78rem;
  font-weight: 600;
  padding: 0.3rem 0.75rem;
  border-radius: 6px;
  background: rgba(0, 212, 255, 0.08);
  color: var(--accent-cyan);
  border: 1px solid rgba(0, 212, 255, 0.15);
  letter-spacing: 0.01em;
}

.chip-learning {
  background: rgba(240, 49, 109, 0.08);
  color: var(--accent-pink);
  border-color: rgba(240, 49, 109, 0.2);
}

/* Learning section */
.learning-intro {
  margin-top: 5rem;
}

.learning-row {
  border: 1px dashed rgba(240, 49, 109, 0.2);
  background: rgba(240, 49, 109, 0.03);
}

.learning-row:hover {
  border-color: rgba(240, 49, 109, 0.45);
  box-shadow: 0 0 20px rgba(240, 49, 109, 0.12);
}

/* Overriding glass border for learning rows */
.learning-list .glass {
  border: 1px dashed rgba(240, 49, 109, 0.2);
}
</style>
