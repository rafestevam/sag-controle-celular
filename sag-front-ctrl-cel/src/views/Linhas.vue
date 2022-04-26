<template>
    <div class="main-window">
        <h1 class="title">Linhas Telefônicas</h1>
        <router-view></router-view>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
    name: 'LinhasViewComponent',
});
</script>

<style scoped>
.main-window {
    padding: 1.25rem
}
</style>