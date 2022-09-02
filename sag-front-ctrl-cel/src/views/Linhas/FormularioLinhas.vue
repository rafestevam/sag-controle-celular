<template>
  <div>
    <h1 class="subtitle">Adicionar ou Alterar Linha Telefônica</h1>
  </div>
  <section class="main-form">
    <Form
      @submit="saveLinhaTelefonica"
      :validation-schema="linhaSchema"
      v-slot="{ errors }"
    >
      <div class="container is-widescreen">
        <!-- Numero da Linha -->
        <div class="field is-horizontal">
          <div class="field-label"></div>
          <div class="field-body">
            <div class="field is-expanded">
              <div class="field has-addons">
                <p class="control">
                  <a
                    class="button"
                    :class="{
                      'is-danger': errors.iTelefone && !id,
                      'is-static': !errors.iTelefone || id,
                    }"
                  >
                    +55
                  </a>
                </p>
                <!-- <div class="control">
                <div class="select is-fullwidth">
                  <select>
                    <option>11</option>
                    <option>12</option>
                  </select>
                </div>
              </div> -->
                <p class="control is-expanded">
                  <Field
                    v-model="numeroTelefone"
                    v-if="!id"
                    name="iTelefone"
                    as="input"
                    class="input"
                    :class="{ 'is-danger': errors.iTelefone }"
                    placeholder="Entrar o número de telefone no formato (99) 99999-9999"
                    v-maska="'(##) #####-####'"
                    
                  />
                  <label class="input" v-else>{{ numeroTelefone }}</label>
                </p>
              </div>
              <p class="help is-danger" v-if="!id">{{ errors.iTelefone }}</p>
            </div>
          </div>
        </div>

        <!-- Classificação -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Classificação</label>
          </div>
          <div class="field-body">
            <div class="field">
              <p class="control is-expanded">
                <Field
                  v-model="linha.classificacao"
                  name="iClassificacao"
                  as="input"
                  type="text"
                  class="input"
                  placeholder=""
                />
              </p>
            </div>
          </div>
        </div>

        <!-- Funcionario Vinculado -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Funcionário</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <div class="is-fullwidth">
                  <v-select v-model="linha.funcionario_id" v-if="!linha.aparelho_id"
                    placeholder="Escolha um funcionário..."
                    :options="funcionarios"
                    label="nome_social"
                    :reduce="(func: IFuncionario) => func.id"
                    :multiple="false"
                    :clearable="true"
                  >
                    <template #option="{nome_social}">
                      <p>{{ nome_social }}</p>
                    </template>
                  </v-select>
                  <label class="input" v-else>N/A</label>
                  <!-- <v-select
                    v-model="linha.funcionarioVinculado"
                    placeholder="Escolha um funcionário..."
                    :options="funcionarios"
                    :getOptionsLabel="(empl: IFuncionario) => empl.nome_social"
                    :multiple="false"
                    :clearable="true"
                    :disabled="
                      linha.aparelhoVinculado?.id != undefined ? true : false
                    "
                  >
                    <template #option="{ nome, sobrenome, nome_social }">
                      <h3 style="margin: 0">{{ nome_social }}</h3>
                      <em>{{ nome }} {{ sobrenome }}</em>
                    </template>
                  </v-select> -->
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Aparelho Vinculado -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Aparelho</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <div class="is-fullwidth">
                  <v-select v-model="linha.aparelho_id" v-if="!linha.funcionario_id"
                    placeholder="Escolha um aparelho..."
                    :options="aparelhos"
                    :label="'imei'"
                    :value="(dvc: IAparelho) => dvc.imei"
                    :reduce="(dvc: IAparelho) => dvc.id"
                    :multiple="false"
                    :clearable="true"
                  >
                    <template #option="{imei}">
                      <p>{{ imei }}</p>
                    </template>
                  </v-select>
                  <label class="input" v-else>N/A</label>
                  <!-- <v-select
                    v-model="linha.aparelhoVinculado"
                    placeholder="Escolha um funcionário..."
                    :options="aparelhos"
                    :getOptionLabel="(device: IAparelho) => device.imei"
                    :multiple="false"
                    :clearable="true"
                    :disabled="
                      linha.funcionarioVinculado?.id != undefined ? true : false
                    "
                  >
                    <template #option="{ imei, marca, modelo }">
                      <h3 style="margin: 0">{{ imei }}</h3>
                      <em>{{ imei }} - {{ marca }} - {{ modelo }}</em>
                    </template>
                  </v-select> -->
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Ultimo Func. Vinculado à Linha -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Último Funcionário</label>
          </div>
          <div class="field-body">
            <div class="field">
              <p class="control is-expanded">
                <label class="input">
                  {{ linha.lastFuncionario?.nome_social || "" }}
                </label>
              </p>
            </div>
          </div>
        </div>

        <!-- Aparelho em Posse -->
        <!-- <div class="field is-horizontal">
        <div class="field-label is-normal">
          <label class="label">Aparelho Vinculado</label>
        </div>
        <div class="field-body">
          <div class="field is-narrow">
            <div class="control">
              <div class="select is-fullwidth">
                <select>
                  <option>Selecione um Aparelho</option>
                  <option>111111111111111111111 - IPhone 7 SE</option>
                  <option>222222222222222222222 - IPhone 8+</option>
                </select>
              </div>
            </div>
          </div>
        </div>
      </div> -->

        <!-- Status -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Status da Linha</label>
          </div>
          <div class="field-body">
            <div class="field">
              <p class="control is-expanded">
                <label class="input">{{
                  linha.funcionarioVinculado.id || linha.aparelhoVinculado.id
                    ? linhaStatus.EM_USO
                    : linhaStatus.DISPONIVEL
                }}</label>
              </p>
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
                <input type="submit" class="button is-primary" value="Salvar" v-if="!id">
                <input type="submit" class="button is-primary" value="Salvar" @click="saveLinhaTelefonica" v-else>
              </div>
              <div class="control">
                <router-link to="/linhas" class="button is-light"
                  >Cancelar</router-link
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </Form>
  </section>
</template>

<script lang="ts">
import ILinha, { LinhaStatus } from "@/interfaces/ILinha";
import { defineComponent, ref, computed } from "vue";
import { Form, Field } from "vee-validate";
import * as Yup from "yup";
import { useStore } from "@/store";
import useNotificator from "@/hooks/Notificator";
import {
  POST_LINHA,
  PUT_LINHA,
} from "@/store/modules/linha/constants/action-type";
import { NotificationType } from "@/interfaces/INotification";
import { GET_ALL_APARELHOS } from "@/store/modules/aparelho/constants/action-type";
import { GET_ALL_FUNC } from "@/store/modules/funcionario/constants/action-type";
import IFuncionario from "@/interfaces/IFuncionario";
import IAparelho from "@/interfaces/IAparelho";

export default defineComponent({
  name: "FormularioLinhasViewComponent",
  components: {
    Form,
    Field,
  },
  props: {
    id: {
      type: String,
    },
  },
  data() {
    const linhaSchema = Yup.object().shape({
      iTelefone: Yup.string()
        .required("O campo Número de Telefone é obrigatório")
        .matches(
          /^\([1-9]{2}\) [9]{0,1}[0-9]{1}[0-9]{3}-[0-9]{4}$/,
          "Entrar o número de Telefone no formato (99) 99999-9999"
        ),
    });
    return {
      linhaSchema,
    };
  },
  setup(props) {
    const store = useStore();
    const { notify } = useNotificator();
    const linha = ref({} as ILinha);
    const numeroTelefone = ref("");
    const linhaStatus = LinhaStatus;

    store.dispatch(GET_ALL_FUNC);
    // store.dispatch(GET_APARELHOS_NO_LINHAS);
    store.dispatch(GET_ALL_APARELHOS);

    if (props.id) {
      const line = store.state.linha?.linhas.find((ln) => ln.id == props.id);
      linha.value = line as ILinha;
      numeroTelefone.value = `(${line?.ddd}) ${line?.numero.substring(
        0,
        5
      )}-${line?.numero.substring(5, 9)}`;
    } else {
      linha.value.funcionarioVinculado = {} as IFuncionario;
      linha.value.lastFuncionario = {} as IFuncionario;
      linha.value.aparelhoVinculado = {} as IAparelho;
    }

    return {
      store,
      notify,
      linha,
      linhaStatus,
      numeroTelefone,
      funcionarios: computed(() => store.state.funcionario.funcionarios),
      aparelhos: computed(() => store.state.aparelho.aparelhos),
    };
  },
  methods: {
    saveLinhaTelefonica() {
      if (this.id) {
        console.log("ALTERAR LINHA");
        // this.linha.status =
        //   this.linha.funcionarioVinculado.id || this.linha.aparelhoVinculado.id
        //     ? LinhaStatus.EM_USO
        //     : LinhaStatus.DISPONIVEL;
        if(this.linha.funcionario_id) {
          this.linha.status = LinhaStatus.EM_USO;
        } else {
          this.linha.funcionario_id = '';
          this.linha.status = LinhaStatus.DISPONIVEL;
        }
        if(this.linha.aparelho_id) {
          this.linha.status = LinhaStatus.EM_USO;
        } else {
          this.linha.aparelho_id = '';
          this.linha.status = LinhaStatus.DISPONIVEL;
        }

        this.store
          .dispatch(PUT_LINHA, this.linha)
          .then(() => {
            this.notify(
              NotificationType.SUCCESS,
              `Linha #${this.numeroTelefone} alterada com sucesso!`
            );
            this.$router.push('/linhas');
          })
          .catch((err) => {
            this.notify(NotificationType.DANGER, err.response.data.message);
          });
      } else {
        const numTel = this.numeroTelefone.replace(/[^0-9]/g, "");
        this.linha.ddd = numTel.substring(0, 2);
        this.linha.numero = numTel.substring(2, 11);
        this.linha.status =
          this.linha.funcionario_id || this.linha.aparelho_id
            ? LinhaStatus.EM_USO
            : LinhaStatus.DISPONIVEL;
        this.store
          .dispatch(POST_LINHA, this.linha)
          .then(() => {
            this.notify(
              NotificationType.SUCCESS,
              `Linha #${this.numeroTelefone} cadastrada com sucesso!`
            );
            this.$router.push("/linhas");
          })
          .catch((err) => {
            this.notify(NotificationType.DANGER, err.response.data);
          });
      }
    },
  },
});
</script>
