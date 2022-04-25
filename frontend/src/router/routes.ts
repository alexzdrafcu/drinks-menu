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
    path: "/categories/new",
    component: () => import("pages/Drinks.vue"),
  },
  {
    path: "/categories/softdrinks",
    component: () => import("pages/Drinks.vue"),
  },
  {
    path: "/categories/shots",
    component: () => import("pages/Drinks.vue"),
  },
  {
    path: "/categories/cocktails",
    component: () => import("pages/Drinks.vue"),
  },
  {
    path: "/categories/beerandwine",
    component: () => import("pages/Drinks.vue"),
  },
  {
    path: "/categories/coffeeandtea",
    component: () => import("pages/Drinks.vue"),
  },
  {
    path: "/drink/:id",
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
