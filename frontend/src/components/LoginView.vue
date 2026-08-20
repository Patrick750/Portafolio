<template>
  <div class="login-page">
    <div class="background-glow"></div>
    <div class="login-container">
      <div class="login-card glass-panel" id="login-card">
        <!-- Logo Header -->
        <div class="brand-header">
          <a href="/" class="logo-box">PO</a>
          <h1 class="login-title">Iniciar Sesión</h1>
          <p class="login-subtitle">Acceso exclusivo al sistema</p>
        </div>

        <!-- Alert for Incorrect Credentials -->
        <Transition name="slide-down">
          <div v-if="errorMessage" class="alert error-alert" id="login-error-alert" role="alert">
            <svg class="alert-icon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="12" y1="8" x2="12" y2="12"></line>
              <line x1="12" y1="16" x2="12.01" y2="16"></line>
            </svg>
            <span>{{ errorMessage }}</span>
          </div>
        </Transition>

        <!-- Alert for Success -->
        <Transition name="slide-down">
          <div v-if="successMessage" class="alert success-alert" id="login-success-alert" role="alert">
            <svg class="alert-icon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
              <polyline points="22 4 12 14.01 9 11.01"></polyline>
            </svg>
            <span>{{ successMessage }}</span>
          </div>
        </Transition>

        <!-- Form -->
        <form @submit.prevent="handleLogin" class="login-form" id="login-page-form">
          <!-- Email field -->
          <div class="form-group">
            <label for="login-email" class="form-label">Correo Electrónico</label>
            <div class="input-wrapper">
              <svg class="input-icon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                <polyline points="22,6 12,13 2,6"></polyline>
              </svg>
              <input
                id="login-email"
                v-model="form.correo"
                type="email"
                placeholder="ejemplo@correo.com"
                required
                class="form-input"
                :disabled="loading"
                autocomplete="email"
              />
            </div>
          </div>

          <!-- Password field -->
          <div class="form-group">
            <label for="login-password" class="form-label">Contraseña</label>
            <div class="input-wrapper">
              <svg class="input-icon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
              </svg>
              <input
                id="login-password"
                v-model="form.contrasena"
                :type="showPassword ? 'text' : 'password'"
                placeholder="••••••••"
                required
                class="form-input"
                :disabled="loading"
                autocomplete="current-password"
              />
              <button
                type="button"
                class="toggle-pwd-btn"
                @click="showPassword = !showPassword"
                aria-label="Mostrar u ocultar contraseña"
              >
                <svg v-if="!showPassword" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                  <circle cx="12" cy="12" r="3"></circle>
                </svg>
                <svg v-else xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path>
                  <line x1="1" y1="1" x2="23" y2="23"></line>
                </svg>
              </button>
            </div>
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            class="btn-submit"
            id="login-page-submit-btn"
            :disabled="loading"
          >
            <span v-if="loading" class="spinner"></span>
            <span v-else>Ingresar</span>
          </button>
        </form>

        <div class="back-home">
          <a href="/" class="back-link">← Volver al portafolio</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';

const form = reactive({
  correo: '',
  contrasena: ''
});

const showPassword = ref(false);
const loading = ref(false);
const errorMessage = ref('');
const successMessage = ref('');

const handleLogin = async () => {
  errorMessage.value = '';
  successMessage.value = '';
  loading.value = true;

  try {
    const response = await fetch('/api/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        correo: form.correo,
        contrasena: form.contrasena
      }),
    });

    const data = await response.json();

    if (response.ok && data.success) {
      if (data.token) localStorage.setItem('token', data.token);
      successMessage.value = data.message || 'Inicio de sesión exitoso';
      setTimeout(() => {
        window.location.href = '/dashboard';
      }, 1200);
    } else {
      errorMessage.value = data.error || 'Credenciales incorrectas. Verifique su correo y contraseña.';
    }
  } catch (err) {
    console.error('Error en login:', err);
    errorMessage.value = 'Error de conexión con el servidor. Intente nuevamente.';
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  background: var(--bg-main, #080b11);
  overflow: hidden;
  padding: 2rem 1rem;
}

.background-glow {
  position: absolute;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(56, 189, 248, 0.15) 0%, rgba(37, 99, 235, 0.05) 50%, transparent 70%);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none;
}

.login-container {
  width: 100%;
  max-width: 440px;
  position: relative;
  z-index: 1;
}

.login-card {
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  padding: 2.75rem 2.25rem;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5), 0 0 30px rgba(56, 189, 248, 0.1);
}

.brand-header {
  text-align: center;
  margin-bottom: 2rem;
}

.logo-box {
  width: 44px;
  height: 44px;
  margin: 0 auto 1.25rem;
  background: linear-gradient(135deg, #38bdf8, #2563eb);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-display, sans-serif);
  font-weight: 700;
  font-size: 1.1rem;
  color: #fff;
  text-decoration: none;
  box-shadow: 0 4px 12px rgba(56, 189, 248, 0.3);
}

.login-title {
  font-size: 1.65rem;
  font-weight: 700;
  color: #f8fafc;
  margin: 0 0 0.5rem;
}

.login-subtitle {
  font-size: 0.9rem;
  color: #94a3b8;
  margin: 0;
}

/* Alerts */
.alert {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.85rem 1rem;
  border-radius: 10px;
  font-size: 0.85rem;
  font-weight: 500;
  margin-bottom: 1.25rem;
}

.error-alert {
  background: rgba(239, 68, 68, 0.12);
  border: 1px solid rgba(239, 68, 68, 0.3);
  color: #fca5a5;
}

.success-alert {
  background: rgba(34, 197, 94, 0.12);
  border: 1px solid rgba(34, 197, 94, 0.3);
  color: #86efac;
}

.alert-icon {
  flex-shrink: 0;
}

/* Form */
.login-form {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-label {
  font-size: 0.85rem;
  font-weight: 600;
  color: #cbd5e1;
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon {
  position: absolute;
  left: 1rem;
  color: #64748b;
  pointer-events: none;
}

.form-input {
  width: 100%;
  padding: 0.8rem 1rem 0.8rem 2.75rem;
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 12px;
  color: #f8fafc;
  font-size: 0.92rem;
  outline: none;
  transition: all 0.2s ease;
}

.form-input:focus {
  border-color: #38bdf8;
  box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2);
  background: rgba(15, 23, 42, 0.9);
}

.toggle-pwd-btn {
  position: absolute;
  right: 0.75rem;
  background: none;
  border: none;
  color: #64748b;
  cursor: pointer;
  padding: 0.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.toggle-pwd-btn:hover {
  color: #94a3b8;
}

.btn-submit {
  width: 100%;
  padding: 0.85rem;
  margin-top: 0.5rem;
  background: linear-gradient(135deg, #0284c7, #2563eb);
  border: none;
  border-radius: 12px;
  color: #fff;
  font-weight: 600;
  font-size: 0.95rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
  box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35);
}

.btn-submit:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(37, 99, 235, 0.5);
}

.btn-submit:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.back-home {
  margin-top: 1.5rem;
  text-align: center;
}

.back-link {
  color: #64748b;
  text-decoration: none;
  font-size: 0.85rem;
  transition: color 0.2s ease;
}

.back-link:hover {
  color: #38bdf8;
}

/* Spinner */
.spinner {
  width: 20px;
  height: 20px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  border-top-color: #fff;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.slide-down-enter-active, .slide-down-leave-active {
  transition: all 0.3s ease;
}
.slide-down-enter-from, .slide-down-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
