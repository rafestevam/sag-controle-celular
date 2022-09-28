<template>
  <main class="is-gapless is-multiline">
    <header v-if="showNavBar">
      <MainNavigation @aoUserLogout="userLogout()"/>
    </header>
    <Notification @onCloseNotification="closeNotification" />
    <router-view></router-view>
  </main>
</template>

<script lang="ts">
import { computed, defineComponent, onBeforeMount } from "vue";
import MainNavigation from "./components/MainNavigation.vue";
import Notification from "./components/Notifications/Notification.vue";
import { useStore } from "@/store";
import { DELETE_NOTIFICATION } from "./store/modules/notif/constants/mutation-type";
import { USER_LOGOUT } from "./store/modules/usuario/constants/action-type";
import IUsuarioLogado from "./interfaces/IUsuario";

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
      loggedUser: computed(() => store.state.usuario.user),
      showNavBar: computed(() => {
        const user = store.state.usuario.user || {} as IUsuarioLogado;
        if(user.loggedIn){
          return true;
        }
        return false;
      })
    };
  },
  methods: {
    closeNotification(idNotif: string) {
      this.store.commit(DELETE_NOTIFICATION, idNotif);
    },
    userLogout(){
      this.store
        .dispatch(USER_LOGOUT)
        .then(() => this.$router.push("/"));
    }
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
