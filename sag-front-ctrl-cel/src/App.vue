<template>
  <main class="is-gapless is-multiline">
    <header>
      <MainNavigation />
    </header>
    <Notification @onCloseNotification="closeNotification" />
    <router-view></router-view>
  </main>
</template>

<script lang="ts">
import { defineComponent, onBeforeMount } from "vue";
import MainNavigation from "./components/MainNavigation.vue";
import Notification from "./components/Notifications/Notification.vue";
import { useStore } from "@/store";
import { DELETE_NOTIFICATION } from "./store/modules/notif/constants/mutation-type";

export default defineComponent({
  name: "App",
  components: {
    MainNavigation,
    Notification,
  },
  setup() {
    const store = useStore();
    // const authenticated = useIsAuthenticated();
    // const { instance } = useMsal();
    onBeforeMount(() => {
      // if(!authenticated.value){
      //   console.log(authenticated)
      //   instance.loginRedirect(loginRequest)
      // }
    });
    return {
      store,
    };
  },
  methods: {
    closeNotification(idNotif: string) {
      this.store.commit(DELETE_NOTIFICATION, idNotif);
    },
  },
});
</script>

<style>
.main-window {
  padding: 1.25rem;
}
.main-form {
  padding-top: 1.5rem;
}
.sag-button {
  padding-bottom: 1rem;
}
</style>
