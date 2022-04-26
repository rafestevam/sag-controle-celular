<template>
    <div class="main-window">
        <h1 class="title">Funcionários</h1>
        <router-view></router-view>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
    name: 'FuncionariosViewComponent',
});
</script>