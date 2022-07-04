<template>
  <div>
    <h1 class="subtitle">Lista de Aparelhos Telefônicos</h1>
  </div>
  <ModalNotification
   :isActive="modalActive" 
   :title="modalTitle" 
   :message="modalMessage"
   @onSaveModal="deleteAparelho(modalAparelhoID, modalAparelhoSpec)"
   @onCancelModal="closeModalDeleteAparelho()"/>
  <section class="main-form">
    <div class="sag-button">
      <router-link to="/aparelhos/novo" class="button">
        <span class="icon is-small">
          <i class="fas fa-plus"></i>
        </span>
        <span>Adicionar</span>
      </router-link>
    </div>
    <div class="container is-widescreen">
      <table class="table is-fullwidth" v-if="aparelhos">
        <thead>
          <tr>
            <td>Num. Série</td>
            <td>IMEI</td>
            <td>Marca</td>
            <td>Fabricante</td>
            <td>Status</td>
            <td>Ações</td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="aparelho in aparelhos" :key="aparelho.id">
            <td>{{ aparelho.numero_serie }}</td>
            <td>{{ aparelho.imei }}</td>
            <td>{{ aparelho.marca }}</td>
            <td>{{ aparelho.fabricante }}</td>
            <td>{{ aparelho.status }}</td>
            <td>
              <router-link :to="`/aparelhos/${aparelho.id}`" class="button">
                <span class="icon is-small">
                  <i class="fas fa-pencil-alt"></i>
                </span>
              </router-link>
              <button class="button ml-2 is-danger" @click="modalDeleteAparelho(aparelho.id, aparelho.marca.concat('&nbsp', aparelho.modelo))">
                <span class="icon is-small">
                  <i class="fas fa-trash"></i>
                </span>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <BoxNotification message="Não há aparelhos cadastrados na base de dados" v-else />
    </div>
  </section>
</template>

<script lang="ts">
import { useStore } from "@/store";
import useNotificator from "@/hooks/Notificator";
import { DELETE_APARELHO, GET_ALL_APARELHOS } from "@/store/modules/aparelho/constants/action-type";
import { computed, defineComponent } from "vue";
import BoxNotification from "@/components/BoxNotification/BoxNotification.vue";
import ModalNotification from "@/components/ModalNotification/ModalNotification.vue";
import { NotificationType } from "@/interfaces/INotification";

export default defineComponent({
  name: "ListaAparelhosViewComponent",
  components: {
    BoxNotification,
    ModalNotification,
  },
  data() {
    return {
      modalActive: false,
      modalTitle: "",
      modalMessage: "",
      modalAparelhoID: "",
      modalAparelhoSpec: "",
    }
  },
  setup() {
    const store = useStore();
    const { notify } = useNotificator();
    store.dispatch(GET_ALL_APARELHOS);
    return {
      aparelhos: computed(() => store.state.aparelho.aparelhos),
      store,
      notify,
    }
  },
  methods: {
    deleteAparelho(id: string, aparelhoSpec: string){
      this.store
        .dispatch(DELETE_APARELHO, id)
        .then(() => {
          this.notify(
            NotificationType.SUCCESS,
            `Aparelho ${aparelhoSpec} excluído com sucesso!`
          );
          this.modalActive = false;
        })
        .catch(err => {
          this.notify(NotificationType.DANGER, `${err.response.data.message}`);
        });
    },
    modalDeleteAparelho(id: string, aparelhoSpec: string){
      this.modalActive = true;
      this.modalTitle = 'Excluir Aparelho';
      this.modalMessage = `Você realmente deseja excluir o aparelho ${aparelhoSpec} ?`;
      this.modalAparelhoID = id;
      this.modalAparelhoSpec = aparelhoSpec;
    },
    closeModalDeleteAparelho(){
      this.modalActive = false;
      this.modalTitle = "";
      this.modalMessage = "";
      this.modalAparelhoID = "";
      this.modalAparelhoSpec = "";
    }
  },
});
</script>
