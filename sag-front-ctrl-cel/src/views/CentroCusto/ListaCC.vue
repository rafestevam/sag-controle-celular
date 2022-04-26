<template>
    <div>
    <h1 class="subtitle">Lista de Centros de Custo</h1>
  </div>
  <section class="main-form">
    <div class="sag-button">
    <router-link to="/cc/novo" class="button">
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
            <td>Código</td>
            <td>Nome</td>
            <td>Ações</td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="cc in centros_custo" :key="cc.id">
            <td>{{ cc.cc_cod }}</td>
            <td>{{ cc.cc_nome }}</td>
            <td>
              <router-link :to="`/cc/${cc.id}`" class="button">
                <span class="icon is-small">
                  <i class="fas fa-pencil-alt"></i>
                </span>
              </router-link>
              <button class="button ml-2 is-danger" @click="deleteCentroCusto(cc.id, cc.cc_cod)">
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
import { defineComponent, computed } from 'vue';
import { useStore } from '@/store';
import useNotificator from '@/hooks/Notificator';
import { DELETE_CC, GET_ALL_CC } from '@/store/modules/centrocusto/constants/action-type';
import { NotificationType } from '@/interfaces/INotification';

export default defineComponent({
    name: 'ListaCCViewComponent',
    setup () {
      const store = useStore();
      const { notify } = useNotificator();
      store.dispatch(GET_ALL_CC);
      return {
        centros_custo: computed(() => store.state.centrocusto.ccs),
        store,
        notify,
      }
    },
    methods: {
      deleteCentroCusto(id: string, cc_cod: string) {
        this.store
          .dispatch(DELETE_CC, id)
          .then(() => {
            this.notify(NotificationType.SUCCESS, `Centro de Custo ${cc_cod} excluído com sucesso!`);
          })
          .catch(err => {
            this.notify(NotificationType.DANGER, `${err.response.data.mensagem}`);
          });
      }
    }
});
</script>

<style scoped>
.sag-button {
  padding-bottom: 1.00rem;
}
</style>