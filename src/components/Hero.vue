<template>
  <section id="hero" class="hero">
    <!-- Animated grid background -->
    <div class="hero-grid" aria-hidden="true"></div>
    <!-- Glow orbs -->
    <div class="orb orb-1" aria-hidden="true"></div>
    <div class="orb orb-2" aria-hidden="true"></div>

    <div class="hero-inner container">
      <!-- Left column -->
      <div class="hero-content">
        <p class="hero-eyebrow">👋 Hola, soy</p>

        <h1 class="hero-name">Patrick Ortiz</h1>

        <!-- Rotating role -->
        <div class="hero-role-wrapper" aria-live="polite">
          
          <span class="hero-role gradient-text">{{ roles[currentRole] }}</span>
          <span class="hero-cursor">|</span>
        </div>

        <p class="hero-tagline">
          Construyo software que resuelve problemas reales. Apasionado por la arquitectura limpia, los datos y las interfaces que enamoran.
        </p>

        <div class="hero-actions">
          <a href="#projects" class="btn btn-primary" id="hero-cta-projects">
            Ver proyectos
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </a>
          <a href="#contact" class="btn btn-ghost" id="hero-cta-contact">Contáctame</a>
        </div>

        <!-- Stats row -->
        <div class="hero-stats">
          <div class="stat-item" v-for="stat in stats" :key="stat.label">
            <span class="stat-value gradient-text">{{ stat.value }}</span>
            <span class="stat-label">{{ stat.label }}</span>
          </div>
        </div>
      </div>

      <!-- Right column: photo card -->
      <div class="hero-card glass">
        <div class="card-topbar">
          <span class="dot dot-red"></span>
          <span class="dot dot-yellow"></span>
          <span class="dot dot-green"></span>
          <span class="card-filename">profile.jpg</span>
        </div>
        <div class="card-image-wrapper">
          <img 
            :src="profileImg" 
            alt="Patrick Ortiz" 
            class="profile-img"
            @error="hasError = true"
            v-if="!hasError"
          />
          <div class="image-placeholder" v-else>
            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
            <p>Coloca tu foto en <code>public/profile.jpg</code></p>
          </div>
        </div>
      </div>
    </div>

    <!-- Scroll cue -->
    <a href="#skills" class="scroll-cue" aria-label="Ir a habilidades">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
    </a>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import profileImg from '../assets/profile.jpg';

const hasError = ref(false);

const roles = ['Desarrollador Backend', 'Analista de Datos', 'Dev Frontend', 'Solucionador de problemas'];
const currentRole = ref(0);
let interval;

const stats = [
  { value: '3+',  label: 'Proyectos' },
  { value: '8+',  label: 'Tecnologías' },
  { value: '100%', label: 'Disponible' },
];

onMounted(() => {
  interval = setInterval(() => {
    currentRole.value = (currentRole.value + 1) % roles.length;
  }, 2800);
});

onUnmounted(() => clearInterval(interval));
</script>

<style scoped>
/* ---- Layout ---- */
.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  padding-top: 5rem;
}

.hero-inner {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
  width: 100%;
  padding-top: 3rem;
}

/* ---- Background grid ---- */
.hero-grid {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(var(--border-subtle) 1px, transparent 1px),
    linear-gradient(90deg, var(--border-subtle) 1px, transparent 1px);
  background-size: 60px 60px;
  mask-image: radial-gradient(ellipse 80% 80% at 50% 40%, black 30%, transparent 100%);
  -webkit-mask-image: radial-gradient(ellipse 80% 80% at 50% 40%, black 30%, transparent 100%);
}

/* ---- Glow orbs ---- */
.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  pointer-events: none;
  opacity: 0.35;
}
.orb-1 {
  width: 500px; height: 500px;
  background: radial-gradient(circle, var(--accent-cyan), transparent 70%);
  top: -120px; right: -80px;
  animation: float 12s ease-in-out infinite;
}
.orb-2 {
  width: 380px; height: 380px;
  background: radial-gradient(circle, var(--accent-blue), transparent 70%);
  bottom: -100px; left: -60px;
  animation: float 15s ease-in-out infinite reverse;
}

@keyframes float {
  0%, 100% { transform: translate(0, 0) scale(1); }
  33%       { transform: translate(20px, -30px) scale(1.05); }
  66%       { transform: translate(-15px, 20px) scale(0.97); }
}

/* ---- Content ---- */
.hero-content {
  position: relative;
  z-index: 2;
}

.hero-eyebrow {
  font-size: 1rem;
  color: var(--text-secondary);
  margin-bottom: 0.5rem;
}

.hero-name {
  font-size: clamp(2.8rem, 5vw, 4.5rem);
  font-weight: 700;
  letter-spacing: -0.03em;
  color: var(--text-primary);
  margin-bottom: 0.75rem;
  line-height: 1.05;
}

.hero-role-wrapper {
  font-size: clamp(1.2rem, 2.2vw, 1.6rem);
  font-family: var(--font-display);
  font-weight: 500;
  color: var(--text-secondary);
  margin-bottom: 1.5rem;
  height: 2.2rem;
  display: flex;
  align-items: center;
  gap: 0.3rem;
}

.hero-role {
  display: inline-block;
  animation: fadeRoleIn 0.5s var(--ease-smooth);
}

@keyframes fadeRoleIn {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0); }
}

.hero-cursor {
  color: var(--accent-cyan);
  animation: blink 1s step-end infinite;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0; }
}

.hero-tagline {
  font-size: 1.05rem;
  color: var(--text-secondary);
  line-height: 1.7;
  max-width: 480px;
  margin-bottom: 2.5rem;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  margin-bottom: 3rem;
}

/* ---- Stats ---- */
.hero-stats {
  display: flex;
  gap: 2.5rem;
  padding-top: 2rem;
  border-top: 1px solid var(--border-subtle);
}

.stat-item {
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}

.stat-value {
  font-family: var(--font-display);
  font-size: 1.6rem;
  font-weight: 700;
  line-height: 1;
}

.stat-label {
  font-size: 0.78rem;
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

/* ---- Code card ---- */
.hero-card {
  position: relative;
  z-index: 2;
  overflow: hidden;
}

.card-topbar {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.9rem 1.2rem;
  border-bottom: 1px solid var(--border-subtle);
  background: rgba(0, 0, 0, 0.25);
}

.dot {
  width: 10px; height: 10px;
  border-radius: 50%;
}
.dot-red    { background: #ff5f57; }
.dot-yellow { background: #febc2e; }
.dot-green  { background: #28c840; }

.card-filename {
  margin-left: 0.5rem;
  font-size: 0.78rem;
  color: var(--text-muted);
  font-family: 'Courier New', monospace;
}

.card-image-wrapper {
  position: relative;
  width: 100%;
  aspect-ratio: 4 / 3;
  overflow: hidden;
  background: rgba(0, 0, 0, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
}

.profile-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), filter 0.6s ease;
  will-change: transform;
}

.hero-card:hover .profile-img {
  transform: scale(1.08);
  filter: brightness(1.05);
}

.image-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  padding: 2rem;
  text-align: center;
  color: var(--text-muted);
}

.image-placeholder code {
  color: var(--accent-cyan);
  background: rgba(255, 255, 255, 0.05);
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  font-size: 0.85rem;
}

/* ---- Scroll cue ---- */
.scroll-cue {
  position: absolute;
  bottom: 2.5rem;
  left: 50%;
  transform: translateX(-50%);
  color: var(--text-muted);
  animation: bounce 2s ease-in-out infinite;
  transition: color var(--duration-fast);
  z-index: 2;
}

.scroll-cue:hover { color: var(--accent-cyan); }

@keyframes bounce {
  0%, 100% { transform: translateX(-50%) translateY(0); }
  50%       { transform: translateX(-50%) translateY(8px); }
}

/* ---- Responsive ---- */
@media (max-width: 900px) {
  .hero-inner {
    grid-template-columns: 1fr;
    gap: 3rem;
    text-align: center;
  }

  .hero-tagline { margin: 0 auto 2.5rem; }

  .hero-actions { justify-content: center; }

  .hero-stats {
    justify-content: center;
  }

  .hero-role-wrapper { justify-content: center; }

  .hero-card { max-width: 520px; margin: 0 auto; }
}

@media (max-width: 480px) {
  .hero-stats { gap: 1.5rem; }
}
</style>
