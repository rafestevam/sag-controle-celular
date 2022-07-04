<template>
  <div>
    <h1 class="subtitle">Lista de Linhas Telefônicas</h1>
  </div>
  <ModalNotification
    title="Excluir Linha Telefônica"
    :message="`Você tem certeza que quer excluir a linha telefônica ${linhaSelFormatada}?`"
    :isActive="modalActive"
    @onCancelModal="closeModal()"
    @onSaveModal="deleteLinha(modalLinhaID, linhaSelFormatada)"
  />
  <section class="main-form">
    <div class="sag-button">
      <router-link to="/linhas/nova" class="button">
        <span class="icon is-small">
          <i class="fas fa-plus"></i>
        </span>
        <span>Adicionar</span>
      </router-link>
    </div>
    <div class="container is-widescreen">
      <table class="table is-fullwidth" v-if="linhas">
        <thead>
          <tr>
            <td>Número</td>
            <td>Status</td>
            <td>Ações</td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="linha in linhas" :key="linha.id">
            <td>
              {{
                `(${linha.ddd}) ${linha.numero.substring(
                  0,
                  5
                )}-${linha.numero.substring(5, 9)}`
              }}
            </td>
            <td>{{ linha.status }}</td>
            <td>
              <router-link :to="`/linhas/${linha.id}`" class="button">
                <span class="icon is-small">
                  <i class="fas fa-pencil-alt"></i>
                </span>
              </router-link>
              <button
                class="button ml-2 is-danger"
                @click="confirmDelete(linha)"
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
        message="Não há Linhas Telefônicas cadastradas na base de dados"
        v-show="!linhas"
      />
    </div>
  </section>
</template>

<script lang="ts">
import { useStore } from "@/store";
import { computed, defineComponent } from "vue";
import useNotificator from "@/hooks/Notificator";
// import useModalNotificator from "@/hooks/ModalNotificator";
import {
  DELETE_LINHA,
  GET_ALL_LINHAS,
} from "@/store/modules/linha/constants/action-type";
import { NotificationType } from "@/interfaces/INotification";
import ILinha from "@/interfaces/ILinha";
import ModalNotification from "@/components/ModalNotification/ModalNotification.vue";
import BoxNotification from "@/components/BoxNotification/BoxNotification.vue";

export default defineComponent({
  name: "ListaLinhasViewComponent",
  components: {
    ModalNotification,
    BoxNotification,
  },
  data() {
    return {
      modalLinhaID: "",
      linhaSelFormatada: "",
      modalType: null as NotificationType | null,
      modalActive: false,
      componentKey: 0,
    };
  },
  setup() {
    const store = useStore();
    const { notify } = useNotificator();
    // const { modalNotify } = useModalNotificator();
    store.dispatch(GET_ALL_LINHAS);
    return {
      store,
      notify,
      // modalNotify,
      linhas: computed(() => store.state.linha.linhas),
    };
  },
  methods: {
    confirmDelete(linha: ILinha) {
      // this.linhaSelecionada = linha;
      this.modalActive = true;
      this.modalLinhaID = linha.id;
      this.linhaSelFormatada = `(${linha.ddd}) ${linha.numero.substring(0, 5)}-${linha.numero.substring(5, 9)}`;
      // this.modalNotify(
      //   'Excluir Linha Telefônica',
      //   `Você tem certeza que quer excluir a linha telefônica
      //     (${linha.ddd}) ${linha.numero.substring(0, 5)}-${linha.numero.substring(5, 9)}`,
      //   NotificationType.DANGER
      // );
    },
    closeModal(){ 
      this.modalActive = false;
    },
    forceRenderer() {
      this.componentKey += 1;
    },
    deleteLinha(id: string, linhaFormatada: string) {
      this.store
        .dispatch(DELETE_LINHA, id)
        .then(() => {
          this.notify(
            NotificationType.SUCCESS,
            `A linha de telefone ${linhaFormatada} foi excluída com sucesso!`
          );
          this.modalActive = false;
          //this.linhas = this.store.state?.linha.linhas;
          // this.$router.push('/linhas');
        })
        .catch((err) => {
          this.notify(NotificationType.DANGER, err.response.data.message);
        });
    },
  },
});
</script>
