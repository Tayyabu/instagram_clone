import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import HomePage from "./pages/HomePage.vue";
import LoginPage from "./pages/LoginPage.vue";
import RegisterPage from "./pages/RegisterPage.vue";
import { createPinia } from "pinia";
import {
  createRouter,
  createWebHistory,
  type RouteRecordRaw,
} from "vue-router";
import Layout from "./layouts/Layout.vue";
import AuthLayout from "./layouts/AuthLayout.vue";
import AboutPage from "./pages/AboutPage.vue";
import { useAuthStore } from "./store/authStore";
import useRefresh from "./composables/useRefresh";

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    component: Layout,
    beforeEnter: async (_to, _from, next) => {
      const store = useAuthStore();
      const refresh = useRefresh();
     
      if (store.accessToken) return next();
      await refresh();

      if (!store.accessToken) return next({ name: "login" });
      else next();
    },
    children: [
      {
        path: "",
        component: HomePage,
        name: "home",
      },
      {
        path: "about",
        component: AboutPage,
        name: "about",
      },
    ],
  },
  {
    path: "/auth",
    component: AuthLayout,
    children: [
      { path: "login", component: LoginPage, name: "login" },
      { path: "register", component: RegisterPage, name: "register" },
    ],
  },
];
export const router = createRouter({
  history: createWebHistory(),
  routes,
});

const pinia = createPinia();
createApp(App).use(pinia).use(router).mount("#app");
