/**
 * router/index.ts
 *
 * Automatic routes for `./src/pages/*.vue`
 */

// Composables
import { createRouter, createWebHistory } from 'vue-router/auto'
// import { setupLayouts } from 'virtual:generated-layouts'

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  // extendRoutes: setupLayouts,
  routes: [
    {
      path: '/upload',
      name: 'upload',
      component: () => import('../pages/UploadView.vue')
    }
  ]
})

export default router
