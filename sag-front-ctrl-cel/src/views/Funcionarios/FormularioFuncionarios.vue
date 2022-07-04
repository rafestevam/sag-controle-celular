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
        <!-- Nome/Sobrenome -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Nome/Sobrenome</label>
          </div>
          <div class="field-body">
            <div class="field">
              <p class="control is-expanded">
                <!-- <input type="text" class="input" placeholder="Nome" /> -->
                <Field v-model="funcionario.nome"
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
                <Field v-model="funcionario.sobrenome"
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
                <Field v-model="funcionario.nome_social"
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
                <!-- <input type="date" class="input" placeholder="" /> -->
                <Field v-model="funcionario.admissao"
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
                <!-- <input type="date" class="input" placeholder="" /> -->
                <Field v-model="funcionario.data_nascimento"
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
                <!-- <input type="text" v-maska="'##.###.###-#'" class="input" placeholder="RG" /> -->
                <Field v-model="funcionario.rg"
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
                <!-- <input type="text" v-maska="'###.###.###-##'" class="input" placeholder="CPF" /> -->
                <Field v-model="funcionario.cpf"
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
                <!-- <input type="text" class="input" placeholder="" /> -->
                <Field v-model="funcionario.cargo"
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
                  <Field v-model="funcionario.centro_custo"
                    name="iCentroCusto"
                    as="select"
                    class="input"
                    :class="{ 'is-danger': errors.iCentroCusto }"
                  >
                    <option value="" default>Selecione um CC</option>
                    <!-- <option>123456 - Customer Support BR</option>
                  <option>789012 - Professional Services BR</option> -->
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

        <!-- Aparelho em Posse -->
        <div
          class="field is-horizontal"
          v-for="(lineAssigned, index) in linesAssigned"
          :key="index"
        >
          <div class="field-label is-normal">
            <label class="label">Linha Atribuída #{{ index + 1 }}</label>
          </div>
          <div class="field-body">
            <div class="field is-grouped is-narrow">
              <div class="control">
                <div class="select is-fullwidth">
                  <Field v-model="funcionario.linhas[index].id"
                    :name="`iLinhas[${index}]`"
                    class="input"
                    as="select"
                    rules="required"
                    :class="{ 'is-danger': errors[`iLinhas[${index}]`] }"
                  >
                    <option value="" default>Selecione uma Linha</option>
                    <!-- <option>(11) 91234-5678</option>
                  <option>(61) 98765-4321</option> -->
                    <option
                      v-for="linha in linhas"
                      :key="linha.id"
                      :value="linha.id"
                    >
                      {{
                        `(${linha.ddd}) ${linha.numero.substring(
                          0,
                          5
                        )}-${linha.numero.substring(5, 9)}`
                      }}
                    </option>
                  </Field>
                </div>
              </div>
              <div class="control">
                <button class="button is-light" @click="addLinhasAssigned">
                  <i class="fa-solid fa-plus"></i>
                </button>
              </div>
              <div class="control">
                <button
                  class="button is-light"
                  @click="removeLinhasAssigned(index)"
                >
                  <i class="fa-solid fa-minus"></i>
                </button>
              </div>
            </div>
            <div class="field is-narrow">
              <div class="control">
                <p class="help is-danger">{{ errors[`iLinhas[${index}]`] }}</p>
              </div>
            </div>
            <!-- <div class="field">
            <p class="control is-narrow">
              <input type="text" class="input" value="111111111111111111111 - IPhone 7 SE" disabled/>
            </p>
          </div> -->
          </div>
        </div>

        <!-- Aparelho em Posse -->
        <div
          class="field is-horizontal"
          v-for="(deviceAssigned, index) in devicesAssigned"
          :key="index"
        >
          <div class="field-label is-normal">
            <label class="label">Aparelho Atribuído #{{ index + 1 }}</label>
          </div>
          <div class="field-body">
            <div class="field is-narrow is-grouped">
              <div class="control">
                <div class="select is-fullwidth">
                  <Field v-model="funcionario.aparelhos[index].id"
                    :name="`iAparelhos[${index}]`"
                    as="select"
                    rules="required"
                    class="input"
                    :class="{ 'is-danger': errors[`iAparelhos[${index}]`] }"
                  >
                    <option value="" default>Selecione um Aparelho</option>
                    <!-- <option>Apple iPhone SE - 987654321</option>
                  <option>Apple iPhone 7 - 456123789</option> -->
                    <option
                      v-for="aparelho in aparelhos"
                      :key="aparelho.id"
                      :value="aparelho.id"
                    >
                      {{ aparelho.marca }} {{ aparelho.modelo }} -
                      {{ aparelho.imei }}
                    </option>
                  </Field>
                </div>
              </div>
              <div class="control">
                <button class="button is-light" @click="addDeviceAssigned">
                  <i class="fa-solid fa-plus"></i>
                </button>
              </div>
              <div class="control">
                <button
                  class="button is-light"
                  @click="removeDeviceAssigned(index)"
                >
                  <i class="fa-solid fa-minus"></i>
                </button>
              </div>
            </div>
            <!-- <div class="field">
            <p class="control is-narrow">
              <input type="text" class="input" value="111111111111111111111 - IPhone 7 SE" disabled/>
            </p>
          </div> -->
            <div class="field is-narrow">
              <div class="control">
                <p class="help is-danger">{{ errors[`iAparelhos[${index}]`] }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Submeter Formulario -->
        <div class="field is-horizontal">
          <div class="field-label">
            <!-- Left empty for spacing -->
          </div>
          <div class="field-body">
            <div class="field is-grouped">
              <div class="control">
                <button class="button is-primary">Salvar</button>
              </div>
              <div class="control">
                <button class="button is-light">Cancelar</button>
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
import { GET_ALL_LINHAS } from "@/store/modules/linha/constants/action-type";
import ILinha, { LinhaStatus } from "@/interfaces/ILinha";
import IAparelho, { AparelhoStatus } from "@/interfaces/IAparelho";
import { GET_ALL_APARELHOS } from "@/store/modules/aparelho/constants/action-type";
import { Form, Field } from "vee-validate";
import * as Yup from "yup";
import IFuncionario from "@/interfaces/IFuncionario";

export default defineComponent({
  name: "FormularioFuncionariosViewComponent",
  components: {
    Form,
    Field,
  },
  setup() {
    const store = useStore();
    store.dispatch(GET_ALL_CC);
    store.dispatch(GET_ALL_LINHAS);
    store.dispatch(GET_ALL_APARELHOS);

    const funcionario = ref({} as IFuncionario);

    const linesAssigned = ref([] as ILinha[]);
    linesAssigned.value.push({} as ILinha);

    const devicesAssigned = ref([] as IAparelho[]);
    devicesAssigned.value.push({} as IAparelho);

    return {
      store,
      ccs: computed(() => store.state.centrocusto.ccs),
      linhas: computed(() =>
        store.state.linha.linhas?.filter(
          (linha) => linha.status == LinhaStatus.DISPONIVEL
        )
      ),
      aparelhos: computed(() =>
        store.state.aparelho.aparelhos?.filter(
          (device) => device.status == AparelhoStatus.DISPONIVEL
        )
      ),
      linesAssigned,
      devicesAssigned,
      funcionario,
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
    };
  },
  methods: {
    addLinhasAssigned() {
      this.linesAssigned.push({} as ILinha);
    },
    removeLinhasAssigned(index: number) {
      if (this.linesAssigned.length > 1) {
        this.linesAssigned.splice(index, 1);
      }
    },
    addDeviceAssigned() {
      this.devicesAssigned.push({} as IAparelho);
    },
    removeDeviceAssigned(index: number) {
      if (this.devicesAssigned.length > 1) {
        this.devicesAssigned.splice(index, 1);
      }
    },
    saveFuncionario() {
      console.log(JSON.stringify(this.funcionario));
    },
  },
});
</script>
