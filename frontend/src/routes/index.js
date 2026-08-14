import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../components/HomeView.vue'
import LoginView from '../components/LoginView.vue'
import DashboardView from '../components/DashboardView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/login/',
    redirect: { name: 'Login' }
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: DashboardView
  },
  {
    path: '/dashboard/',
    redirect: { name: 'Dashboard' }
  },
  {
    path: '/panel',
    redirect: { name: 'Dashboard' }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

