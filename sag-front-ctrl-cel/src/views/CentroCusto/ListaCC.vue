<template>
  <div>
    <h1 class="subtitle">Lista de Centros de Custo</h1>
  </div>
  <ModalNotification 
   :isActive="modalActive" 
   :title="modalTitle" 
   :message="modalMessage"
   @onSaveModal="deleteCentroCusto(modalCCid, modalCCcod)"
   @onCancelModal="closeModalDeleteCC()"/>
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
      <table id="centros_custo" class="table is-fullwidth" v-if="centros_custo">
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
              <!-- <button
                class="button ml-2 is-danger"
                @click="deleteCentroCusto(cc.id, cc.cc_cod)"
              > -->
              <button
                class="button ml-2 is-danger"
                @click="modalDeleteCC(cc.id, cc.cc_cod)"
              >
                <span class="icon is-small">
                  <i class="fas fa-trash"></i>
                </span>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <BoxNotification
        message="Não há Centros de Custo cadastrados na base de dados"
        v-else
      />
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent, computed } from "vue";
import { useStore } from "@/store";
import useNotificator from "@/hooks/Notificator";
import {
  DELETE_CC,
  GET_ALL_CC,
} from "@/store/modules/centrocusto/constants/action-type";
import { NotificationType } from "@/interfaces/INotification";
import BoxNotification from "@/components/BoxNotification/BoxNotification.vue";
import ModalNotification from "@/components/ModalNotification/ModalNotification.vue";

export default defineComponent({
  name: "ListaCCViewComponent",
  components: {
    BoxNotification,
    ModalNotification,
  },
  data() {
    return {
      modalTitle: "",
      modalMessage: "",
      modalCCcod: "",
      modalCCid: "",
      modalActive: false,
    }
  },
  setup() {
    const store = useStore();
    const { notify } = useNotificator();
    store.dispatch(GET_ALL_CC);

    return {
      centros_custo: computed(() => store.state.centrocusto.ccs),
      store,
      notify,
    };
  },
  methods: {
    modalDeleteCC(id: string, cc_cod: string){
      this.modalActive = true;
      this.modalTitle = "Excluir Centro de Custo";
      this.modalMessage = `Você gostaria realmente de excluir o Centro de Custo ${cc_cod} ?`;
      this.modalCCcod = cc_cod;
      this.modalCCid = id;
    },
    closeModalDeleteCC() {
      this.modalActive = false;
      this.modalTitle = "";
      this.modalMessage = "";
      this.modalCCcod = "";
      this.modalCCid = "";
    },
    deleteCentroCusto(id: string, cc_cod: string) {
      this.store
        .dispatch(DELETE_CC, id)
        .then(() => {
          this.notify(
            NotificationType.SUCCESS,
            `Centro de Custo ${cc_cod} excluído com sucesso!`
          );
          this.modalActive = false;
        })
        .catch((err) => {
          this.notify(NotificationType.DANGER, `${err.response.data.message}`);
        });
    },
  },
});
</script>