<template>
  <header class="navbar" :class="{ 'scrolled': isScrolled }">
    <nav class="navbar-inner container">
      <!-- Logo -->
      <a href="#" class="navbar-logo" id="navbar-logo">
        <span class="logo-box">PO</span>
        <span class="logo-name">Patrick Ortiz</span>
      </a>

      <!-- Links -->
      <ul class="navbar-links">
        <li v-for="link in links" :key="link.href">
          <a :href="link.href" class="nav-link" :class="{ active: activeSection === link.section }">
            {{ link.label }}
          </a>
        </li>
      </ul>

      <!-- CTA -->
      <div class="navbar-cta">
        <span class="available-badge">
          <span class="pulse-dot"></span>
          Disponible
        </span>
      </div>

      <!-- Mobile toggle -->
      <button class="mobile-toggle" @click="menuOpen = !menuOpen" aria-label="Toggle menu">
        <span :class="menuOpen ? 'open' : ''"></span>
        <span :class="menuOpen ? 'open' : ''"></span>
        <span :class="menuOpen ? 'open' : ''"></span>
      </button>
    </nav>

    <!-- Mobile menu -->
    <div class="mobile-menu" :class="{ 'menu-open': menuOpen }">
      <a v-for="link in links" :key="link.href" :href="link.href" class="mobile-link" @click="menuOpen = false">
        {{ link.label }}
      </a>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const isScrolled = ref(false);
const activeSection = ref('hero');
const menuOpen = ref(false);

const links = [
  { href: '#skills',   label: 'Habilidades', section: 'skills' },
  { href: '#projects', label: 'Proyectos',   section: 'projects' },
  { href: '#contact',  label: 'Contacto',    section: 'contact' },
];



const handleScroll = () => {
  isScrolled.value = window.scrollY > 50;
  const sections = ['skills', 'projects', 'contact'];
  for (const id of sections) {
    const el = document.getElementById(id);
    if (el) {
      const rect = el.getBoundingClientRect();
      if (rect.top <= 120 && rect.bottom >= 120) {
        activeSection.value = id;
        return;
      }
    }
  }
  if (window.scrollY < 200) activeSection.value = 'hero';
};

onMounted(() => window.addEventListener('scroll', handleScroll, { passive: true }));
onUnmounted(() => window.removeEventListener('scroll', handleScroll));
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  padding: 1.25rem 0;
  transition: all 300ms var(--ease-smooth);
}

.navbar.scrolled {
  background: rgba(8, 11, 17, 0.85);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border-bottom: 1px solid var(--border-subtle);
  padding: 0.85rem 0;
}

.navbar-inner {
  display: flex;
  align-items: center;
  gap: 2rem;
}

/* Logo */
.navbar-logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  text-decoration: none;
  flex-shrink: 0;
}

.logo-box {
  width: 36px;
  height: 36px;
  background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-display);
  font-size: 0.85rem;
  font-weight: 700;
  color: #fff;
  transition: transform var(--duration-base) var(--ease-bounce);
}

.navbar-logo:hover .logo-box {
  transform: rotate(-6deg) scale(1.1);
}

.logo-name {
  font-family: var(--font-display);
  font-weight: 600;
  font-size: 0.95rem;
  color: var(--text-primary);
}

/* Links */
.navbar-links {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  margin-left: auto;
}

.nav-link {
  padding: 0.45rem 0.9rem;
  border-radius: var(--radius-sm);
  font-size: 0.88rem;
  font-weight: 500;
  color: var(--text-secondary);
  transition: all var(--duration-fast) var(--ease-smooth);
  position: relative;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 50%;
  transform: translateX(-50%) scaleX(0);
  width: 70%;
  height: 2px;
  background: var(--accent-cyan);
  border-radius: 1px;
  transition: transform var(--duration-base) var(--ease-smooth);
}

.nav-link:hover,
.nav-link.active {
  color: var(--text-primary);
}

.nav-link.active::after,
.nav-link:hover::after {
  transform: translateX(-50%) scaleX(1);
}

/* CTA */
.navbar-cta {
  flex-shrink: 0;
}

.available-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.4rem 1rem;
  border-radius: 50px;
  border: 1px solid rgba(34, 197, 94, 0.3);
  background: rgba(34, 197, 94, 0.08);
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--accent-green);
  letter-spacing: 0.02em;
}

.pulse-dot {
  width: 7px;
  height: 7px;
  background: var(--accent-green);
  border-radius: 50%;
  animation: pulse 2s ease-in-out infinite;
}

.navbar-cta {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  flex-shrink: 0;
}

.login-nav-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.45rem 1rem;
  border-radius: 50px;
  background: linear-gradient(135deg, #0284c7, #2563eb);
  color: #ffffff;
  border: none;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(37, 99, 235, 0.3);
}

.login-nav-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.45);
}

.user-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.35rem 0.85rem;
  border-radius: 50px;
  background: rgba(56, 189, 248, 0.1);
  border: 1px solid rgba(56, 189, 248, 0.3);
  font-size: 0.8rem;
  color: #38bdf8;
  font-weight: 500;
}

.logout-btn {
  background: none;
  border: none;
  color: #94a3b8;
  cursor: pointer;
  padding: 0;
  font-size: 0.8rem;
  display: flex;
  align-items: center;
}

.logout-btn:hover {
  color: #ef4444;
}

@keyframes pulse {
  0%, 100% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.5); }
  50%       { box-shadow: 0 0 0 5px rgba(34, 197, 94, 0); }
}


/* Mobile */
.mobile-toggle {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
  margin-left: auto;
}

.mobile-toggle span {
  display: block;
  width: 24px;
  height: 2px;
  background: var(--text-primary);
  border-radius: 2px;
  transition: all var(--duration-base) var(--ease-smooth);
}

.mobile-toggle span.open:nth-child(1) { transform: rotate(45deg) translate(5px, 5px); }
.mobile-toggle span.open:nth-child(2) { opacity: 0; transform: scaleX(0); }
.mobile-toggle span.open:nth-child(3) { transform: rotate(-45deg) translate(5px, -5px); }

.mobile-menu {
  display: none;
  flex-direction: column;
  gap: 0;
  background: var(--bg-surface);
  border-top: 1px solid var(--border-subtle);
  max-height: 0;
  overflow: hidden;
  transition: max-height var(--duration-slow) var(--ease-smooth);
}

.mobile-menu.menu-open { max-height: 300px; }

.mobile-link {
  padding: 1rem 1.5rem;
  font-size: 1rem;
  font-weight: 500;
  color: var(--text-secondary);
  border-bottom: 1px solid var(--border-subtle);
  transition: color var(--duration-fast);
}

.mobile-link:hover { color: var(--accent-cyan); }

@media (max-width: 768px) {
  .navbar-links, .navbar-cta { display: none; }
  .mobile-toggle { display: flex; }
  .mobile-menu { display: flex; }
}
</style>
