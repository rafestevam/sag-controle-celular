<template>
  <div>
    <h1 class="subtitle">Gerador de Termo de Responsabilidade</h1>
  </div>

  <ModalNotification
    :isActive="modalActive"
    :title="modalTitle"
    :message="modalMessage"
    @onSaveModal="generateTermo(modalFunc)"
    @onCancelModal="closeModalGenerateTermo()"
  />

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
      <!-- Numero de Entradas por pagina -->
      <div class="field is-horizontal">
        <div class="field-body">
          <div class="field is-narrow">
            <div class="control">Mostrando</div>
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
            <div class="control">linhas por página</div>
          </div>
        </div>

        <!-- Input de busca de dados -->
        <div class="field-body">
          <div class="field is-grouped is-grouped-right">
            <div class="control has-icons-right">
              <input
                type="text"
                class="input"
                v-model="search"
                placeholder="Busca..."
              />
              <span class="icon is-small is-right">
                <i class="fa-solid fa-magnifying-glass"></i>
              </span>
            </div>
          </div>
        </div>
      </div>

      <table id="funcionarios" class="table is-fullwidth" v-if="funcionarios">
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
          <tr v-for="funcionario in filteredEntries" :key="funcionario.id">
            <td>{{ funcionario.nome_social }}</td>
            <td>{{ funcionario.cpf }}</td>
            <td>{{ funcionario.centro_custo?.cc_cod }}</td>
            <td>{{ funcionario.cargo }}</td>
            <td>
              <button
                class="button ml-2 is-primary"
                @click="modalGenerateTermo(funcionario)"
              >
                <span class="icon is-small">
                  <i class="fa-solid fa-file-circle-check"></i>
                </span>
                <span class="is-normal">
                  Gerar
                </span>
              </button>
            </td>
          </tr>
        </tbody>
      </table>

      <BoxNotification
        message="Não há Funcionários cadastrados na base de dados"
        v-else
      />

      <!-- Paginação da Tabela -->
      <div class="pagination" role="pagination" aria-label="pagination">
        <ul class="pagination-list">
          <li>
            <a href="#" @click.prevent="pageActive = 1" class="pagination-link"
              >&#171;</a
            >
          </li>
          <li>
            <a
              href="#"
              @click.prevent="
                pageActive = pageActive > 1 ? pageActive - 1 : pageActive
              "
              class="pagination-link"
              >&#8249;</a
            >
          </li>

          <li v-for="(page, index) in renderPagination" :key="index">
            <a
              class="pagination-link"
              :class="{ 'is-current': pageActive === Number(page) }"
              href="#"
              @click.prevent="pageActive = Number(page)"
              >{{ page }}</a
            >
          </li>

          <li>
            <a
              href="#"
              @click.prevent="
                pageActive =
                  pageActive < totalPages ? pageActive + 1 : pageActive
              "
              class="pagination-link"
              >&#8250;</a
            >
          </li>
          <li>
            <a
              href="#"
              @click.prevent="pageActive = totalPages"
              class="pagination-link"
              >&#187;</a
            >
          </li>
        </ul>
      </div>
    </div>
  </section>
</template>

<script lang="ts">
import { useStore } from "@/store";
import useNotificator from "@/hooks/Notificator";
import {
  GENERATE_TERMO,
  GET_ALL_FUNC,
} from "@/store/modules/funcionario/constants/action-type";
import { computed, defineComponent, ref } from "vue";
import BoxNotification from "@/components/BoxNotification/BoxNotification.vue";
import ModalNotification from "@/components/ModalNotification/ModalNotification.vue";
import { array as arr } from "alga-js";
import IFuncionario from "@/interfaces/IFuncionario";
import { NotificationType } from "@/interfaces/INotification";

export default defineComponent({
  name: "ListaFuncionariosViewComponent",
  components: {
    BoxNotification,
    ModalNotification,
  },
  data() {
    return {
      modalTitle: "",
      modalMessage: "",
      modalFunc: {} as IFuncionario,
      modalActive: false,
    };
  },
  setup() {
    const store = useStore();
    const { notify } = useNotificator();
    store.dispatch(GET_ALL_FUNC);

    // Variaveis para Num de Entradas e Paginação da Tabela
    const pageActive = ref<number>(1);
    const limitPerPage = ref<number>(5);
    const totalPages = ref<number>(1);
    const search = ref<string>("");
    const deletedFuncId = ref<string>("");

    return {
      store,
      funcionarios: computed(() => store.state.funcionario.funcionarios),
      notify,

      limitPerPage,
      pageActive,
      totalPages,
      search,
      deletedFuncId,
      // sort,
      // Entradas filtradas de acordo com a paginação
      filteredEntries: computed(() => {
        let newEntries = store.state.funcionario.funcionarios;
        if (search.value.length >= 2) {
          newEntries = arr.search(
            store.state.funcionario.funcionarios,
            search.value
          );
        }
        //newEntries = arr.sort(newEntries, 'cc_cod', 'asc');
        // if (deletedFuncId.value != "") {
        //   newEntries = newEntries.filter(
        //     (func) => func.id != deletedFuncId.value
        //   );
        // }
        // eslint-disable-next-line vue/no-side-effects-in-computed-properties
        totalPages.value = arr.pages(newEntries, limitPerPage.value);
        newEntries = arr.paginate(
          newEntries,
          pageActive.value,
          limitPerPage.value
        );
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
    modalGenerateTermo(funcionario: IFuncionario) {
      (this.modalActive = true), (this.modalTitle = "Gerar Termo");
      this.modalMessage = `Você gostaria realmente gerar o termo do(a) Funcionário(a) ${funcionario.nome_social} ?`;
      this.modalFunc = funcionario;
    },
    closeModalGenerateTermo() {
      this.modalActive = false;
      this.modalTitle = "";
      this.modalMessage = "";
      this.modalFunc = {} as IFuncionario;
    },
    generateTermo(funcionario: IFuncionario) {
      this.store
        .dispatch(GENERATE_TERMO, funcionario.id)
        .then(() => {
          this.notify(
            NotificationType.SUCCESS,
            `Termo para o(a) funcionário(a) ${funcionario.nome_social} gerado com sucesso!`
          );
          this.deletedFuncId = funcionario.id;
          this.modalActive = false;
        })
        .catch((err) => {
          this.notify(NotificationType.DANGER, `${err.response.data.message}`);
          this.modalActive = false;
        });
    },
  },
});
</script>
