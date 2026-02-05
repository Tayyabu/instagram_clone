import { onMounted, onUnmounted } from "vue";
import { axiosPrivate } from "../api/api";
import { useAuthStore } from "../store/authStore";
import useRefresh from "./useRefresh";
export function useAxiosPrivate() {
  const store = useAuthStore();
  const refresh = useRefresh();
  let requestInterceptor: number;
  let responseInterceptor: number;
  onMounted(() => {
    requestInterceptor = axiosPrivate.interceptors.request.use(
      async (req) => {
        if (!req.headers.Authorization) {
          req.headers.Authorization = `Bearer ${store.accessToken}`;
        }

        return req;
      },
      (err) => Promise.reject(err),
    );

    responseInterceptor = axiosPrivate.interceptors.response.use(
      (response) => response,
      async (err) => {
        const prevReq = err?.config;

        if ((err.status === 403 || err.status === 401) && prevReq.sent) {
          const newAccessToken = await refresh();
          prevReq.headers["Authorization"] = `Bearer ${newAccessToken}`;
          
          err.config.sent = true;
          return axiosPrivate(prevReq);
        }

        return Promise.reject(err);
      },
    );
  });

  onUnmounted(() => {
    axiosPrivate.interceptors.request.eject(requestInterceptor);
    axiosPrivate.interceptors.response.eject(responseInterceptor);
  });

  return axiosPrivate;
}
