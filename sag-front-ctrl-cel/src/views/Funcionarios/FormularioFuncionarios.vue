<template>
  <div>
    <h1 class="subtitle">Adicionar ou Alterar Funcionário</h1>
  </div>
  <section class="main-form">
    <div class="container is-widescreen">
      <Form
        @submit="saveFuncionario"
        :validation-schema="funcionarioSchema"
        v-slot="{ errors }"
      >
        <!-- <div>{{ selectedCostCenter }}</div> -->
        <!-- <div>{{ funcionario.centro_custo_id }}</div> -->
        <!-- Nome/Sobrenome -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Nome/Sobrenome</label>
          </div>
          <div class="field-body">
            <div class="field">
              <p class="control is-expanded">
                <!-- <input type="text" class="input" placeholder="Nome" /> -->
                <Field
                  v-model="funcionario.nome"
                  name="iNome"
                  class="input"
                  as="input"
                  placeholder="Nome"
                  :class="{ 'is-danger': errors.iNome }"
                />
              </p>
              <p class="help is-danger">{{ errors.iNome }}</p>
            </div>
            <div class="field">
              <p class="control is-expanded">
                <!-- <input type="text" class="input" placeholder="Sobrenome" /> -->
                <Field
                  v-model="funcionario.sobrenome"
                  name="iSobrenome"
                  class="input"
                  as="input"
                  placeholder="Sobrenome"
                  :class="{ 'is-danger': errors.iSobrenome }"
                />
              </p>
              <p class="help is-danger">{{ errors.iSobrenome }}</p>
            </div>
          </div>
        </div>

        <!-- Nome do Crachá -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Nome no Crachá</label>
          </div>
          <div class="field-body">
            <div class="field">
              <p class="control is-expanded">
                <!-- <input type="text" class="input" placeholder="" /> -->
                <Field
                  v-model="funcionario.nome_social"
                  name="iNomeCracha"
                  class="input"
                  as="input"
                  :class="{ 'is-danger': errors.iNomeCracha }"
                />
              </p>
              <p class="help is-danger">{{ errors.iNomeCracha }}</p>
            </div>
          </div>
        </div>

        <!-- Admissão -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Admissão</label>
          </div>
          <div class="field-body">
            <div class="field is-narrow">
              <p class="control is-expanded">
                <Field
                  v-model="funcionario.admissao"
                  name="iAdmissao"
                  class="input"
                  type="date"
                  :class="{ 'is-danger': errors.iAdmissao }"
                />
              </p>
              <p class="help is-danger">{{ errors.iAdmissao }}</p>
            </div>
          </div>
        </div>

        <!-- Data de Nascimento -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Nascimento</label>
          </div>
          <div class="field-body">
            <div class="field is-narrow">
              <p class="control is-expanded">
                <Field
                  v-model="funcionario.data_nascimento"
                  name="iNascimento"
                  class="input"
                  type="date"
                  :class="{ 'is-danger': errors.iNascimento }"
                />
              </p>
              <p class="help is-danger">{{ errors.iNascimento }}</p>
            </div>
          </div>
        </div>

        <!-- RG/CPF -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">RG/CPF</label>
          </div>
          <div class="field-body">
            <div class="field">
              <p class="control is-expanded">
                <Field
                  v-model="funcionario.rg"
                  name="iRG"
                  class="input"
                  as="input"
                  v-maska="'##.###.###-#'"
                  placeholder="RG"
                  :class="{ 'is-danger': errors.iRG }"
                />
              </p>
              <p class="help is-danger" v-if="errors.iRG">{{ errors.iRG }}</p>
              <p class="help" v-else>Entrar RG no formato 99.999.999-9</p>
            </div>
            <div class="field">
              <p class="control is-expanded">
                <Field
                  v-model="funcionario.cpf"
                  name="iCPF"
                  class="input"
                  as="input"
                  v-maska="'###.###.###-##'"
                  placeholder="CPF"
                  :class="{ 'is-danger': errors.iCPF }"
                />
              </p>
              <p class="help is-danger" v-if="errors.iCPF">{{ errors.iCPF }}</p>
              <p class="help" v-else>Entrar CPF no formato 999.999.999-99</p>
            </div>
          </div>
        </div>

        <!-- Cargo -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Cargo</label>
          </div>
          <div class="field-body">
            <div class="field">
              <p class="control is-expanded">
                <Field
                  v-model="funcionario.cargo"
                  name="iCargo"
                  class="input"
                  as="input"
                  :class="{ 'is-danger': errors.iCargo }"
                />
              </p>
              <p class="help is-danger">{{ errors.iCargo }}</p>
            </div>
          </div>
        </div>

        <!-- Centro de Custo -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Centro de Custo</label>
          </div>
          <div class="field-body">
            <div class="field is-narrow">
              <div class="control">
                <div class="select is-fullwidth">
                  <!-- <Field
                    v-model="selectedCostCenter"
                    name="iCentroCusto"
                    as="select"
                    class="input"
                    :class="{ 'is-danger': errors.iCentroCusto }"
                  > -->
                  <Field
                    v-model="funcionario.centro_custo_id"
                    name="iCentroCusto"
                    as="select"
                    class="input"
                    :class="{ 'is-danger': errors.iCentroCusto }"
                  >
                    <option value="" default>Selecione um CC</option>
                    <option
                      v-for="centrocusto in ccs"
                      :key="centrocusto.id"
                      :value="centrocusto.id"
                    >
                      {{ centrocusto.cc_cod }} - {{ centrocusto.cc_nome }}
                    </option>
                  </Field>
                </div>
                <p class="help is-danger">{{ errors.iCentroCusto }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Telefones em Posse -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Telefones em Posse</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control is-expanded">
                <table class="table">
                  <thead>
                    <th><abbr title="Aparelho"></abbr></th>
                    <th><abbr title="Marca"></abbr></th>
                    <th><abbr title="Modelo"></abbr></th>
                    <th><abbr title="Num. Série"></abbr></th>
                    <th><abbr title="Num. Linha"></abbr></th>
                  </thead>
                </table>
              </div>
            </div>
          </div>
        </div>

        <!-- Aparelho em Posse -->

        <!-- Submeter Formulario -->
        <div class="field is-horizontal">
          <div class="field-label">
            <!-- Left empty for spacing -->
          </div>
          <div class="field-body">
            <div class="field is-grouped">
              <div class="control">
                <input type="submit" class="button is-primary" value="Salvar">
              </div>
              <div class="control">
                <router-link to="/funcionarios" class="button is-light">Cancelar</router-link>
              </div>
            </div>
          </div>
        </div>
      </Form>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent, computed, ref } from "vue";
import { useStore } from "@/store";
import { GET_ALL_CC } from "@/store/modules/centrocusto/constants/action-type";
import { Form, Field } from "vee-validate";
import * as Yup from "yup";
import IFuncionario from "@/interfaces/IFuncionario";
import {
  POST_FUNC,
  PUT_FUNC,
} from "@/store/modules/funcionario/constants/action-type";
import useNotificator from "@/hooks/Notificator";
import { NotificationType } from "@/interfaces/INotification";

export default defineComponent({
  name: "FormularioFuncionariosViewComponent",
  components: {
    Form,
    Field,
  },
  props: {
    id: {
      type: String,
    },
  },
  setup(props) {
    const store = useStore();
    store.dispatch(GET_ALL_CC);

    const funcionario = ref({} as IFuncionario);
    const { notify } = useNotificator();

    const selectedCostCenter = ref('');

    if (props.id) {
      const employee = store.state.funcionario?.funcionarios.find(
        (empl) => empl.id == props.id
      );
      funcionario.value = employee as IFuncionario;
      selectedCostCenter.value = employee?.centro_custo_id || "";
    }

    return {
      store,
      notify,
      ccs: computed(() => store.state.centrocusto.ccs),
      funcionario,
      selectedCostCenter,
    };
  },
  data() {
    const funcionarioSchema = Yup.object().shape({
      iNome: Yup.string().required("O campo NOME é obrigatório"),
      iSobrenome: Yup.string().required("O campo SOBRENOME é obrigatório"),
      iNomeCracha: Yup.string().required(
        "O campo NOME NO CRACHÁ é obrigatório"
      ),
      iAdmissao: Yup.string().required("O campo ADMISSÃO é obrigatório"),
      iNascimento: Yup.string().required("O campo NASCIMENTO é obrigatório"),
      iRG: Yup.string().required("O campo RG é obrigatório"),
      iCPF: Yup.string().required("O campo CPF é obrigatório"),
      iCargo: Yup.string().required("O campo CARGO é obrigatório"),
      iCentroCusto: Yup.string().required(
        "O campo CENTRO DE CUSTO é obrigatório"
      ),
      iLinhas: Yup.array().of(
        Yup.string().required("O campo LINHA é obrigatório")
      ),
      iAparelhos: Yup.array().of(
        Yup.string().required("O campo APARELHO é obrigatório")
      ),
    });
    return {
      funcionarioSchema,
      // selectedCostCenter: '',
    };
  },
  methods: {
    saveFuncionario() {
      if (this.id) {
        //this.funcionario.centro_custo_id = this.selectedCostCenter;
        console.log(this.funcionario);
        this.store
          .dispatch(PUT_FUNC, this.funcionario)
          .then(() => {
            this.notify(
              NotificationType.SUCCESS,
              `Funcionario ${this.funcionario.nome_social} alterado com sucesso!`
            );
            this.$router.push("/funcionarios");
          })
          .catch((err) =>
            this.notify(NotificationType.DANGER, err.response.data)
          );
      } else {
        //this.funcionario.centro_custo_id = this.selectedCostCenter;
        console.log(this.funcionario);
        this.store
          .dispatch(POST_FUNC, this.funcionario)
          .then(() => {
            this.notify(
              NotificationType.SUCCESS,
              `Funcionario ${this.funcionario.nome_social} criado com sucesso!`
            );
            this.$router.push("/funcionarios");
          })
          .catch((err) =>
            this.notify(NotificationType.DANGER, err.response.data)
          );
      }
    },
    selectCostCenter(){
      console.log('Centro de Custo selecionado');
    },
  },
  computed: {
    employeeCostCenter() {
      return this.funcionario.centro_custo?.id || "";
    },
  },
});
</script>
