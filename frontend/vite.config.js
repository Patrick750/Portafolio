import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '');
  const apiUrl = env.VITE_API_URL || 'http://127.0.0.1:8000';

  return {
    plugins: [vue()],
    server: {
      proxy: {
        '/api': {
          target: apiUrl,
          changeOrigin: true,
        },
        '/login': {
          target: apiUrl,
          changeOrigin: true,
          bypass(req) {
            if (req.headers.accept && req.headers.accept.includes('html')) {
              return '/index.html'
            }
          }
        }
      }
    }
  }
})


