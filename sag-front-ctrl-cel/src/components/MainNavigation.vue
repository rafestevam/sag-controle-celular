<template>
  <nav class="navbar is-black" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="https://bulma.io">
        <img
          src="@/assets/sag-light-logo.png"
          width="112"
          height="28"
        />
      </a>

      <a
        role="button"
        class="navbar-burger"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbarBasicExample"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div id="navbarBasicExample" class="navbar-menu">
      <div class="navbar-start">
        <!-- Home -->
        <MainNavItem icon="fa-solid fa-house-user" label="Home" :isDropDown="false" route="/"/>

        <!-- Documentação -->
        <MainNavItem icon="fa-solid fa-landmark" label="Documentação" :isDropDown="false" route="/"/>

        <!-- Modulo: Centros de Custos -->
        <MainNavItem 
          label="Centro de Custo" 
          icon="fa-solid fa-euro-sign" 
          :isDropDown="true" 
          :dropDownItems="[
            {label: 'Adicionar Novo', route: '/cc/novo'},
            {label: 'Listar Todos', route: '/cc'}
          ]"/>

        <!-- Modulo: Aparelhos de Telefone -->
        <MainNavItem 
          label="Aparelhos" 
          icon="fa-solid fa-mobile-screen-button" 
          :isDropDown="true" 
          :dropDownItems="[
            {label: 'Adicionar Novo', route: '/aparelhos/novo'},
            {label: 'Listar Todos', route: '/aparelhos'}
          ]"/>

        <!-- Modulo: Linhas de Telefone -->
        <MainNavItem 
          label="Linhas" 
          icon="fa-solid fa-tower-cell" 
          :isDropDown="true" 
          :dropDownItems="[
            {label: 'Adicionar Nova', route: '/linhas/nova'},
            {label: 'Listar Todas', route: '/linhas'}
          ]"/>

        <!-- Modulo: Funcionarios -->
        <MainNavItem 
          label="Funcionários" 
          icon="fa-solid fa-user-group" 
          :isDropDown="true" 
          :dropDownItems="[
            {label: 'Adicionar Novo', route: '/funcionarios/novo'},
            {label: 'Listar Todos', route: '/funcionarios'}
          ]"/>

      </div>

      <!-- <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <a class="button is-primary">
              <strong>Sign up</strong>
            </a>
            <a class="button is-light"> Log in </a>
          </div>
        </div>
      </div> -->
    </div>
  </nav>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import MainNavItem from "./MainNavigation/MainNavItem.vue";

export default defineComponent({
  name: "MainNavigationComponent",
  components: {
      MainNavItem,
  }
});
</script>
