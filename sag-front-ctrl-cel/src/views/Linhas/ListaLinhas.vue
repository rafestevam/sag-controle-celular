<template>
    <div>
    <h1 class="subtitle">Lista de Linhas Telefônicas</h1>
  </div>
  <section class="main-form">
    <div class="container is-widescreen">
      <table class="table is-fullwidth">
        <thead>
          <tr>
            <td>Número</td>
            <td>Status</td>
            <td>Ações</td>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>(11) 91234-5678</td>
            <td>Disponível</td>
            <td>
              <button class="button">
                <span class="icon is-small">
                  <i class="fas fa-pencil-alt"></i>
                </span>
              </button>
              <button class="button ml-2 is-danger">
                <span class="icon is-small">
                  <i class="fas fa-trash"></i>
                </span>
              </button>
            </td>
          </tr>
          <tr>
            <td>(61) 98765-4321</td>
            <td>Em Uso</td>
            <td>
              <button class="button">
                <span class="icon is-small">
                  <i class="fas fa-pencil-alt"></i>
                </span>
              </button>
              <button class="button ml-2 is-danger">
                <span class="icon is-small">
                  <i class="fas fa-trash"></i>
                </span>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
export default defineComponent({
    name: 'ListaLinhasViewComponent',
});
</script>