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

      <!-- Numero de Entradas por pagina -->
      <div class="field is-horizontal">
        <div class="field-body">
          <div class="field is-narrow">
            <div class="control">
              Mostrando
            </div>
          </div>
          <div class="field is-narrow">
            <div class="control">
              <div class="select">
                <select v-model="limitPerPage">
                  <option :value="5">5</option>
                  <option :value="10">10</option>
                  <option :value="25">25</option>
                  <option :value="50">50</option>
                  <option :value="100">100</option>
                </select>
              </div>
            </div>
          </div>
          <div class="field is-narrow">
            <div class="control">
              linhas por página
            </div>
          </div>
        </div>

        <!-- Input de busca de dados -->
        <div class="field-body">
          <div class="field is-grouped is-grouped-right">
            <div class="control has-icons-right">
              <input type="text" class="input" v-model="search" placeholder="Busca...">
              <span class="icon is-small is-right">
                <i class="fa-solid fa-magnifying-glass"></i>
              </span>
            </div>
          </div>
        </div>
      </div>

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
          <tr v-for="aparelho in filteredEntries" :key="aparelho.id">
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
      
      <!-- Paginação da Tabela -->
      <div class="pagination" role="pagination" aria-label="pagination">
        <ul class="pagination-list">
          <li><a href="#" @click.prevent="pageActive = 1" class="pagination-link">&#171;</a></li>
          <li><a href="#" @click.prevent="pageActive = (pageActive > 1) ? pageActive - 1 : pageActive" class="pagination-link">&#8249;</a></li>

          <li v-for="(page, index) in renderPagination" :key="index">
            <a class="pagination-link" :class="{'is-current': pageActive === Number(page)}" href="#" @click.prevent="pageActive = Number(page)">{{ page }}</a>
          </li>

          <li><a href="#" @click.prevent="pageActive = (pageActive < totalPages) ? pageActive + 1 : pageActive" class="pagination-link">&#8250;</a></li>
          <li><a href="#" @click.prevent="pageActive = totalPages" class="pagination-link">&#187;</a></li>
        </ul>
      </div>

    </div>
  </section>
</template>

<script lang="ts">
import { useStore } from "@/store";
import useNotificator from "@/hooks/Notificator";
import { DELETE_APARELHO, GET_ALL_APARELHOS } from "@/store/modules/aparelho/constants/action-type";
import { computed, defineComponent, ref } from "vue";
import BoxNotification from "@/components/BoxNotification/BoxNotification.vue";
import ModalNotification from "@/components/ModalNotification/ModalNotification.vue";
import { NotificationType } from "@/interfaces/INotification";
import { array as arr } from 'alga-js';

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

    // Variaveis para Num de Entradas e Paginação da Tabela
    const pageActive = ref<number>(1);
    const limitPerPage = ref<number>(5);
    const totalPages = ref<number>(1);
    const search = ref<string>('');
    const deletedAparelhoID = ref<string>('');

    return {
      aparelhos: computed(() => store.state.aparelho.aparelhos),
      store,
      notify,

      limitPerPage,
      pageActive,
      totalPages,
      search,
      deletedAparelhoID,
      // sort,
      // Entradas filtradas de acordo com a paginação
      filteredEntries: computed(() => {
        let newEntries = store.state.aparelho.aparelhos;
        if(search.value.length >= 2) {
          newEntries = arr.search(store.state.aparelho.aparelhos, search.value);
        }
        //newEntries = arr.sort(newEntries, 'cc_cod', 'asc');
        if(deletedAparelhoID.value != ""){
          newEntries = newEntries.filter(
            (dvc) => dvc.id != deletedAparelhoID.value
          );
        }
        // eslint-disable-next-line vue/no-side-effects-in-computed-properties
        totalPages.value = arr.pages(newEntries, limitPerPage.value);
        newEntries = arr.paginate(newEntries, pageActive.value, limitPerPage.value);
        return newEntries;
      }),

      // Renderização da paginação
      renderPagination: computed(() => {
        let pagination = arr.pagination(totalPages.value, pageActive.value, 2);
        return pagination;
      }),
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
          this.deletedAparelhoID = id;
          this.modalActive = false;
        })
        .catch(err => {
          this.notify(NotificationType.DANGER, `${err.response.data.message}`);
          this.modalActive = false;
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
