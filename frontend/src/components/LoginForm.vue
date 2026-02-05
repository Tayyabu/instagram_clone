<script lang="ts" setup>
import { ref } from "vue";
import api from "../api/api";
import { useAuthStore } from "../store/authStore";
import { useAsyncState } from "@vueuse/core";

import { useRouter } from "vue-router";
const username = ref("");
const password = ref("");

const store = useAuthStore();
const router = useRouter();

const { isLoading, executeImmediate } = useAsyncState(login, null, {
  immediate: false,
  onSuccess: (data) => {
    if (data?.access) {
      store.accessToken = data?.access;
      console.log(data);
      router.push({ name: "home" });
    }
  },
  onError(error) {
    console.error(error);
  },
});

async function login(
  username: string,
  password: string,
): Promise<{ access: string }> {
  const response = await api.post("/accounts/token/", {
    username,
    password,
  });

  return response.data;
}

async function handleSubmit() {
  if (username && password) {
    await executeImmediate(username.value, password.value);
  }
}
</script>
<template>
  <form
    @submit.prevent="handleSubmit()"
    class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4"
  >
    <h1 class="text-2xl text-center">Login</h1>
    <fieldset class="fieldset">
      <label class="label">Username</label>
      <input
        type="text"
        class="input validator"
        placeholder="Username"
        required
        v-model="username"
      />
    </fieldset>

    <fieldset class="fieldset">
      <label class="label">Password</label>
      <input
        type="password"
        v-model="password"
        class="input validator"
        placeholder="********"
        required
      />
      <p class="validator-hint hidden">Required</p>
    </fieldset>
   

    <button class="btn btn-primary mt-4" :disabled="isLoading" type="submit">
      {{ isLoading ? "Submitting..." : "Submit" }}
    </button>
  </form>
</template>
