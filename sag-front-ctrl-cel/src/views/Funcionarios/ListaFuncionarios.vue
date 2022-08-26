<template>
    <div>
    <h1 class="subtitle">Lista de Funcionários</h1>
  </div>
  <section class="main-form">
    <div class="sag-button">
      <router-link to="/funcionarios/novo" class="button">
        <span class="icon is-small">
          <i class="fas fa-plus"></i>
        </span>
        <span>Adicionar</span>
      </router-link>
    </div>
    <div class="container is-widescreen">
      <table class="table is-fullwidth">
        <thead>
          <tr>
            <td>Nome do Crachá</td>
            <td>CPF</td>
            <td>Centro de Custo</td>
            <td>Cargo</td>
            <td>Ações</td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="funcionario in funcionarios" :key="funcionario.id">
            <td>{{ funcionario.nome_social }}</td>
            <td>{{ funcionario.cpf}}</td>
            <td>{{ funcionario.centro_custo?.cc_cod }}</td>
            <td>{{ funcionario.cargo }}</td>
            <td>
              <router-link :to="`/funcionarios/${funcionario.id}`" class="button">
                <span class="icon is-small">
                  <i class="fas fa-pencil-alt"></i>
                </span>
              </router-link>
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
import { useStore } from '@/store';
import { GET_ALL_FUNC } from '@/store/modules/funcionario/constants/action-type';
import { computed, defineComponent } from 'vue'
export default defineComponent({
    name: 'ListaFuncionariosViewComponent',
    setup() {
      const store = useStore();
      store.dispatch(GET_ALL_FUNC);
      return {
        store,
        funcionarios: computed(() => store.state.funcionario.funcionarios),
      }
    },
});
</script>