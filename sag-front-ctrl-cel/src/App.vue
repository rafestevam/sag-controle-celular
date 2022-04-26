<template>
  <main class="is-gapless is-multiline">
    <header>
      <MainNavigation/>
    </header>
    <Notification/>
    <router-view></router-view>
  </main>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import MainNavigation from './components/MainNavigation.vue';
import Notification from './components/Notifications/Notification.vue';

export default defineComponent({
  name: 'App',
  components: {
    MainNavigation,
    Notification,
  }
});
</script>

<style>
  .main-window {
    padding: 1.25rem;
  }
  .main-form {
    padding-top: 1.50rem;
  }
</style>
