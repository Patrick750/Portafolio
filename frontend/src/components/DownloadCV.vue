<template>
  <section id="resume" class="section cv-section fade-up">
    <div class="cv-glow" aria-hidden="true"></div>
    <div class="container">
      <div class="cv-centered">
        <h2 class="cv-title">Mi Currículum</h2>
        <p class="cv-sub">
          Descarga mi CV para conocer más detalles sobre mi experiencia, habilidades y formación académica.
        </p>
        <a href="/CV_Patrick.pdf" download="CV_Patrick.pdf" class="btn-primary cv-btn">
          <span class="btn-text">Descargar CV</span>
          <span class="btn-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
              <polyline points="7 10 12 15 17 10"></polyline>
              <line x1="12" y1="15" x2="12" y2="3"></line>
            </svg>
          </span>
        </a>
      </div>
    </div>
  </section>
</template>

<style scoped>
.cv-section {
  position: relative;
  overflow: hidden;
  padding: 5rem 0;
}

.cv-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(0, 212, 255, 0.08) 0%, transparent 60%);
  pointer-events: none;
}

.cv-centered {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-lg);
  padding: 3rem 2rem;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  position: relative;
  z-index: 1;
}

.cv-title {
  font-size: clamp(1.8rem, 3vw, 2.5rem);
  font-weight: 700;
  margin-bottom: 1rem;
  color: var(--text-primary);
}

.cv-sub {
  font-size: 1rem;
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: 2rem;
}

.cv-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.8rem 1.8rem;
  background: var(--accent-cyan);
  color: #000;
  font-weight: 600;
  border-radius: var(--radius-sm);
  text-decoration: none;
  transition: all var(--duration-fast);
}

.cv-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 212, 255, 0.3);
}

.btn-icon {
  display: flex;
  align-items: center;
}
</style>
