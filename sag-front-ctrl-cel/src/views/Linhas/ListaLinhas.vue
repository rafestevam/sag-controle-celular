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

      <table class="table is-fullwidth" v-if="linhas">
        <thead>
          <tr>
            <td>Número</td>
            <td>Status</td>
            <td>Ações</td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="linha in filteredEntries" :key="linha.id">
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
import { computed, defineComponent, ref } from "vue";
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
import { array as arr } from 'alga-js';

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

    // Variaveis para Num de Entradas e Paginação da Tabela
    const pageActive = ref<number>(1);
    const limitPerPage = ref<number>(5);
    const totalPages = ref<number>(1);
    const search = ref<string>("");
    const deletedLinhaID = ref<string>('');

    return {
      store,
      notify,
      // modalNotify,
      linhas: computed(() => store.state.linha.linhas),

      limitPerPage,
      pageActive,
      totalPages,
      search,
      deletedLinhaID,
      // sort,
      // Entradas filtradas de acordo com a paginação
      filteredEntries: computed(() => {
        let newEntries = store.state.linha.linhas;
        if (search.value.length >= 2) {
          newEntries = arr.search(store.state.linha.linhas, search.value);
        }
        //newEntries = arr.sort(newEntries, 'cc_cod', 'asc');
        if(deletedLinhaID.value != ''){
          newEntries = newEntries.filter(
            (linha) => linha.id != deletedLinhaID.value
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
          this.deletedLinhaID = id;
          this.modalActive = false;
        })
        .catch((err) => {
          this.notify(NotificationType.DANGER, err.response.data.message);
        });
    },
  },
});
</script>
