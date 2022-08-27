<!-- eslint-disable vue/no-side-effects-in-computed-properties -->
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

      <table id="centros_custo" class="table is-fullwidth" v-if="centros_custo">
        <thead>
          <tr>
            <th>Código</th>
            <th>Nome</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          <!-- <tr v-for="cc in centros_custo" :key="cc.id"> -->
          <tr v-for="cc in filteredEntries" :key="cc.id">
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
import { defineComponent, computed, ref } from "vue";
import { useStore } from "@/store";
import useNotificator from "@/hooks/Notificator";
import {
  DELETE_CC,
  GET_ALL_CC,
} from "@/store/modules/centrocusto/constants/action-type";
import { NotificationType } from "@/interfaces/INotification";
import BoxNotification from "@/components/BoxNotification/BoxNotification.vue";
import ModalNotification from "@/components/ModalNotification/ModalNotification.vue";
import { array as arr } from 'alga-js';

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

    // Variaveis para Num de Entradas e Paginação da Tabela
    const pageActive = ref<number>(1);
    const limitPerPage = ref<number>(5);
    const totalPages = ref<number>(1);
    const search = ref<string>('');

    return {
      centros_custo: computed(() => store.state.centrocusto.ccs),
      store,
      notify,
      
      limitPerPage,
      pageActive,
      totalPages,
      search,
      // sort,
      // Entradas filtradas de acordo com a paginação
      filteredEntries: computed(() => {
        let newEntries = store.state.centrocusto.ccs;
        if(search.value.length >= 2) {
          newEntries = arr.search(store.state.centrocusto.ccs, search.value);
        }
        //newEntries = arr.sort(newEntries, 'cc_cod', 'asc');
        // eslint-disable-next-line vue/no-side-effects-in-computed-properties
        totalPages.value = arr.pages(newEntries, limitPerPage.value);
        newEntries = arr.paginate(newEntries, pageActive.value, limitPerPage.value);
        return newEntries;
      }),

      // Renderização da paginação
      renderPagination: computed(() => {
        let pagination = arr.pagination(totalPages.value, pageActive.value, 2);
        return pagination;
      })
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