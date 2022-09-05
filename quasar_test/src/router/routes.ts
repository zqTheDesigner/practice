import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/LayoutPracticeLayout.vue'),
    children: [{ path: '', component: () => import('pages/IndexPage.vue') }],
  },
  {
    path: '/layout',
    component: () => import('layouts/LayoutPracticeLayout.vue'),
    children: [{ path: '', component: () => import('pages/LayoutExample.vue') }],
  },
  {
    path: '/components',
    component: () => import('layouts/LayoutPracticeLayout.vue'),
    children: [{ path: '', component: () => import('pages/ComponentsExample.vue') }],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
