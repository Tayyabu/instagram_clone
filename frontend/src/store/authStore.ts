import { defineStore } from "pinia";
// import api from "../api/api";
import { ref } from "vue";

export const useAuthStore = defineStore("auth", {
  state: () => {
    const accessToken = ref<string | null>(null);
   
    return {
      accessToken,
      
    };
  },
});
