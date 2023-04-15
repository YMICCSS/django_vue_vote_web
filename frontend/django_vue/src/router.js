import { createRouter, createWebHistory } from 'vue-router'
import Admin from '@/components/Admin.vue'
import Vote from '@/components/Vote.vue'

const routes = [
    {
      path: '/',
      name: 'Admin',
      component: Admin
    },
    {
      path: '/vote',
      name: 'Vote',
      component: Vote
    }
  ];

export const router = createRouter({
  history: createWebHistory(),
  routes
})
