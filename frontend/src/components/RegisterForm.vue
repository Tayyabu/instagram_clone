<script lang="ts" setup>
import { ref, watch } from "vue";
import api from "../api/api";

import { debounce } from "../lib/utils";
import { useAsyncState } from "@vueuse/core";
import type { AxiosError } from "axios";
const username = ref("");
const password = ref("");



const { error, state, isLoading, execute } = useAsyncState(checkUsername, "", {
  immediate: false,
});

async function checkUsername(username: string): Promise<string> {
  try {
    const response = await api.post("/api/check-username/", {
      username,
    });

    return response.data?.message ?? "";
  } catch (error) {
    const err = error as AxiosError;
    if (!err.status) {
      return `<h1 class="text-red-500">Network Error<h1>`;
    } else if (err.status === 500) {
      return `<h1 class="text-red-500">Server Error<h1>`;
    } else return `<h1 class="text-red-500">Bad Request<h1>`;
  }
}

watch(
  username,
  debounce(async (newUsername: string, old: string) => {
    if (!newUsername) return;

    if (old !== newUsername) {
      execute(500, newUsername);
    }
  }, 500),
);
</script>
<template>
  <form
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

      <Transition name="check-username-slide-up">
        <div class="p-4" v-if="isLoading">
          <h1 class="absolute">Loading...</h1>
        </div>
        <div class="p-4" v-else v-html="state ? state : error"></div>
      </Transition>
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

    <button class="btn btn-neutral mt-4" type="submit">Login</button>
  </form>
</template>
<style>
.check-username-slide-up-enter-active,
.check-username-slide-up-leave-active {
  transition: all 0.25s ease-out;
}

.check-username-slide-up-enter-from {
  opacity: 0;
}

.check-username-slide-up-leave-to {
  opacity: 0;
}
</style>
