import type { AxiosError } from "axios";
import api from "../api/api";
import { useAuthStore } from "../store/authStore";

const useRefresh = () => {
  const store = useAuthStore();
  const refresh = async () => {
    try {
      const response = await api.post("/accounts/token/refresh/", {
        withCredentials: true,
      });
      store.$patch({ accessToken: response.data?.access });
      return response.data.access;
    } catch (err) {
      return (err as AxiosError).status;
    }
  };

  return refresh;
};

export default useRefresh;
