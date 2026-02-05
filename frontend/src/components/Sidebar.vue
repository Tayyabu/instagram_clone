<script lang="ts" setup>
import { faInstagram } from "@fortawesome/free-brands-svg-icons";
import { Transition, ref } from "vue";
import {
  faHome,
  faPlayCircle,
  faMessage,
  faCompass,
  faHeart,
  faSquarePlus,
} from "@fortawesome/free-regular-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faUser } from "@fortawesome/free-regular-svg-icons/faUser";
import {  faBars } from "@fortawesome/free-solid-svg-icons";

const isfullSidebar = ref(false);

function showFullSidebar() {
  isfullSidebar.value = true;
}

function hideFullSidebar() {
  isfullSidebar.value = false;
}

const links = [
  { text: "Home", url: "/", icon: faHome },
  { text: "Reels", url: "/reels", icon: faPlayCircle },
  { text: "Messages", url: "/messages", icon: faMessage },
  { text: "Explore", url: "/exlore", icon: faCompass },
  { text: "Notifications", url: "/notifications", icon: faHeart },
  { text: "Create", url: "/create", icon: faSquarePlus },
  { text: "Profile", url: "/:username", icon: faUser },
];
</script>
<template>
  <aside
    @mouseover="showFullSidebar()"
    @mouseleave="hideFullSidebar"
    class="h-full bg-base-100 transition-all duration-1000 p-3 pt-5 flex flex-col gap-2 fixed left-0"
    :class="isfullSidebar ? 'w-60' : ''"
  >
    <a
      href="#"
      :key="'1'"
      class=" p-3 max-w-12 grid place-content-center rounded-2xl hover:bg-base-200 cursor-pointer"
    >
      <FontAwesomeIcon :icon="faInstagram" size="xl" />
    </a>
    <RouterLink
      v-for="link in links"
      :to="link.url"
      :key="link.url"
      class="py-4 px-3 flex gap-2 rounded-2xl my-link hover:bg-base-200 cursor-pointer"
    >
      <FontAwesomeIcon :icon="link.icon" size="xl" />
      <Transition name="list">
        <span v-show="isfullSidebar" class="transition-all duration-500">{{
          link.text
        }}</span>
      </Transition>
    </RouterLink>

    <!-- Menu -->
    <button
      class="py-4 px-3 flex gap-2 rounded-2xl my-link hover:bg-base-200 cursor-pointer"
    >
      <FontAwesomeIcon :icon="faBars" size="xl" />
      <Transition name="list">
        <span v-show="isfullSidebar" class="transition-all duration-500">
          Menu
        </span>
      </Transition>
    </button>
  </aside>
</template>
<style>
.list-move, /* apply transition to moving elements */
.list-enter-active,
.list-leave-active {
  transition: transform 0.2s ease-out;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(-30px);
}

/* ensure leaving items are taken out of layout flow so that moving
   animations can be calculated correctly. */
.list-leave-active {
  position: absolute;
}
</style>
