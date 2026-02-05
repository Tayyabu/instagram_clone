import { useAsyncState } from "@vueuse/core";
import { useAxiosPrivate } from "./useAxiosPrivate";
import { onMounted, onUnmounted, type Ref } from "vue";
import type { User } from "../models/user";

export default function useCurrentUser() {
  const abortController = new AbortController();

  const axiosPrivate = useAxiosPrivate();
  const { state, error, isLoading, executeImmediate } = useAsyncState(
    getCurrentUser,
    null,
    {
      immediate: false,
    },
  );

  async function getCurrentUser() {
    const response = await axiosPrivate.get("accounts/me/", {
      signal: abortController.signal,
    });
    return response.data;
  }

  onMounted(() => {
    executeImmediate();
  });
  onUnmounted(() => {
    abortController.abort();
  });

  return {
    currentUser: state as Ref<User | null, User | null>,
    isUserLoadingError: error,
    isUserLoading: isLoading,
  };
}
