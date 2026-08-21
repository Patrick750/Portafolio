<template>
  <section id="contact" class="section contact-section">
    <!-- Background glow -->
    <div class="contact-glow" aria-hidden="true"></div>

    <div class="container">
      <div class="contact-centered">
        <span class="section-label">// 04 · Contacto</span>
        <h2 class="contact-title">Hablemos</h2>
        <p class="contact-sub">
          Estoy abierto a oportunidades laborales, proyectos freelance y colaboraciones. No dudes en escribirme.
        </p>

        <div class="contact-links">
          <!-- Email -->
          <a
            :href="contacto.correo ? `mailto:${contacto.correo}` : '#'"
            target="_blank"
            rel="noopener"
            class="contact-link-item"
            id="contact-email"
          >
            <span class="link-icon">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><polyline points="22,4 12,13 2,4"/></svg>
            </span>
            {{ contacto.correo || 'Cargando...' }}
          </a>

          <!-- GitHub -->
          <a
            :href="contacto.github || '#'"
            target="_blank"
            rel="noopener"
            class="contact-link-item"
            id="contact-github"
          >
            <span class="link-icon">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.3 3.438 9.8 8.205 11.387.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 21.795 24 17.295 24 12c0-6.63-5.37-12-12-12z"/></svg>
            </span>
            {{ contacto.github ? 'GitHub' : 'Cargando...' }}
          </a>

          <!-- LinkedIn (from link field) -->
          <a
            v-if="contacto.link"
            :href="contacto.link"
            target="_blank"
            rel="noopener"
            class="contact-link-item"
            id="contact-linkedin"
          >
            <span class="link-icon">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
            </span>
            LinkedIn
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="container footer-inner">
      <span class="footer-name">Patrick Ortiz</span>
      <span class="footer-copy">© 2026 · Todos los derechos reservados</span>
      <div class="footer-social">
        <a
          :href="contacto.github || '#'"
          target="_blank"
          rel="noopener"
          class="social-icon"
          id="footer-github"
          aria-label="GitHub"
        >
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.3 3.438 9.8 8.205 11.387.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 21.795 24 17.295 24 12c0-6.63-5.37-12-12-12z"/></svg>
        </a>
        <a
          :href="contacto.link || '#'"
          target="_blank"
          rel="noopener"
          class="social-icon"
          id="footer-linkedin"
          aria-label="LinkedIn"
        >
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
        </a>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { reactive, onMounted } from 'vue';

// Fallback data in case the API is down
const contacto = reactive({
  correo: '',
  link:   '',
  github: ''
});

import clienteAxios from '../api/axios';

const fetchContacto = async () => {
  try {
    const res = await clienteAxios.get(`/api/contacto/`);
    const data = res.data;
    if (Array.isArray(data) && data.length > 0) {
      const first = data[0];
      contacto.correo = first.correo || '';
      contacto.link   = first.link   || '';
      contacto.github = first.github || '';
    }
  } catch (err) {
    console.error('[Footer] Error al cargar contacto:', err);
  }
};

onMounted(async () => {
  await fetchContacto();

  const els = document.querySelectorAll('.fade-up');
  const observer = new IntersectionObserver(
    (entries) => entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); }),
    { threshold: 0.1 }
  );
  els.forEach(el => observer.observe(el));
});
</script>

<style scoped>
/* ---- Section ---- */
.contact-section {
  position: relative;
  overflow: hidden;
}

.contact-glow {
  position: absolute;
  bottom: -200px;
  left: 50%;
  transform: translateX(-50%);
  width: 700px;
  height: 400px;
  background: radial-gradient(ellipse, rgba(58, 110, 245, 0.15) 0%, transparent 70%);
  pointer-events: none;
}

/* ---- Centered layout ---- */
.contact-centered {
  max-width: 540px;
  margin: 0 auto;
  text-align: center;
}

.contact-title {
  font-size: clamp(1.9rem, 3.5vw, 2.8rem);
  font-weight: 700;
  letter-spacing: -0.025em;
  margin-bottom: 1.25rem;
  line-height: 1.2;
  margin-top: 0.75rem;
}

.contact-sub {
  font-size: 1rem;
  color: var(--text-secondary);
  line-height: 1.7;
  margin-bottom: 2.5rem;
  max-width: 400px;
  margin-left: auto;
  margin-right: auto;
}

.contact-links {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.contact-link-item {
  display: flex;
  align-items: center;
  gap: 0.9rem;
  font-size: 0.95rem;
  color: var(--text-secondary);
  font-weight: 500;
  transition: color var(--duration-fast);
  text-decoration: none;
}

.contact-link-item:hover { color: var(--accent-cyan); }

.link-icon {
  width: 38px; height: 38px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-subtle);
  background: rgba(255,255,255,0.03);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  transition: border-color var(--duration-base), background var(--duration-base);
}

.contact-link-item:hover .link-icon {
  border-color: var(--accent-cyan);
  background: rgba(0, 212, 255, 0.08);
  color: var(--accent-cyan);
}

/* ---- Footer ---- */
.footer {
  border-top: 1px solid var(--border-subtle);
  padding: 1.75rem 0;
  background: var(--bg-surface);
}

.footer-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 1rem;
}

.footer-name {
  font-family: var(--font-display);
  font-weight: 600;
  font-size: 0.95rem;
  color: var(--text-primary);
}

.footer-copy {
  font-size: 0.82rem;
  color: var(--text-muted);
}

.footer-social {
  display: flex;
  gap: 0.75rem;
}

.social-icon {
  width: 34px; height: 34px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-subtle);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-muted);
  transition: all var(--duration-fast);
  text-decoration: none;
}

.social-icon:hover {
  border-color: var(--accent-cyan);
  color: var(--accent-cyan);
  background: rgba(0, 212, 255, 0.08);
}

/* Responsive */
@media (max-width: 800px) {
  .contact-inner {
    grid-template-columns: 1fr;
    gap: 3rem;
  }
}

@media (max-width: 560px) {
  .footer-inner {
    flex-direction: column;
    text-align: center;
  }
}
</style>
