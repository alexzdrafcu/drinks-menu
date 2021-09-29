import { RouteRecordRaw } from "vue-router";

const routes: RouteRecordRaw[] = [
  // {
  //   path: "/",
  //   component: () => import("layouts/MainLayout.vue"),
  //   children: [{ path: "", component: () => import("pages/Index.vue") }],
  // },
  {
    path: "/",
    component: () => import("pages/Index.vue"),
  },
  {
    path: "/categories",
    component: () => import("pages/Categories.vue"),
  },
  {
    path: "/categories/cocktailuri",
    component: () => import("pages/Drinks.vue"),
  },
  {
    path: "/categories/nucocktailuri",
    component: () => import("pages/Drinks.vue"),
  },
  {
    path: "/categories/shoturi",
    component: () => import("pages/Drinks.vue"),
  },
  {
    path: "/categories/longdrinks",
    component: () => import("pages/Drinks.vue"),
  },
  {
    path: "/drink",
    component: () => import("pages/Recipe.vue"),
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/Error404.vue"),
  },
];

export default routes;
