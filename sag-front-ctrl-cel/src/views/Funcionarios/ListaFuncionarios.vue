<template>
    <div>
    <h1 class="subtitle">Lista de Funcionários</h1>
  </div>
  <section class="main-form">
    <div class="container is-widescreen">
      <table class="table is-fullwidth">
        <thead>
          <tr>
            <td>CPF</td>
            <td>Nome do Crachá</td>
            <td>Cargo</td>
            <td>Ações</td>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>333.333.333-33</td>
            <td>José das Couves</td>
            <td>Consultor PS I</td>
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
            <td>555.555.555-55</td>
            <td>Antônio da Silva</td>
            <td>Consultor TI</td>
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
    name: 'ListaFuncionariosViewComponent',
});
</script>