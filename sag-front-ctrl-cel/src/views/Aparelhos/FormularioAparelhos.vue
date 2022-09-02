<template>
  <div>
    <h1 class="subtitle">Adicionar ou Alterar Aparelho</h1>
  </div>
  <section class="main-form">
    <Form @submit="saveAparelho" :validation-schema="aparelhoSchema" v-slot="{ errors }">
      <div class="container is-widescreen">
        <!-- IMEI/IMEI2 -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">IMEI/IMEI2</label>
          </div>
          <div class="field-body">
            <!-- <div class="field" v-if="id">
              <p class="control is-expanded">
                <label class="input">{{ aparelho.imei }}</label>
              </p>
            </div> -->
            <div class="field">
              <p class="control is-expanded">
                <!-- <input type="text" class="input" placeholder="IMEI" /> -->
                <Field
                  name="iIMEI"
                  as="input"
                  class="input"
                  v-model="aparelho.imei"
                  :class="{ 'is-danger': errors.iIMEI }"
                  placeholder="IMEI"
                />
              </p>
              <p class="help is-danger">{{ errors.iIMEI }}</p>
            </div>
            <!-- <div class="field" v-if="id">
              <p class="control is-expanded">
                <label class="input">{{ aparelho.imei_2 }}</label>
              </p>
            </div> -->
            <div class="field">
              <p class="control is-expanded">
                <!-- <input type="text" class="input" placeholder="IMEI2" /> -->
                <Field
                  name="iIMEI2"
                  as="input"
                  class="input"
                  v-model="aparelho.imei_2"
                  :class="{ 'is-danger': errors.iIMEI2 }"
                  placeholder="IMEI2"
                />
              </p>
              <p class="help is-danger">{{ errors.iIMEI2 }}</p>
            </div>
          </div>
        </div>

        <!-- Fabricante -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Fabricante</label>
          </div>
          <div class="field-body">
            <!-- <div class="field" v-if="id">
              <p class="control is-expanded">
                <label class="input">{{ aparelho.fabricante }}</label>
              </p>
            </div> -->
            <div class="field">
              <p class="control is-expanded">
                <!-- <input type="text" class="input" placeholder="" /> -->
                <Field
                  name="iFabricante"
                  as="input"
                  class="input"
                  v-model="aparelho.fabricante"
                  :class="{ 'is-danger': errors.iFabricante }"
                />
              </p>
              <p class="help is-danger">{{ errors.iFabricante }}</p>
            </div>
          </div>
        </div>

        <!-- Marca/Modelo -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Marca/Modelo</label>
          </div>
          <div class="field-body">
            <!-- <div class="field" v-if="id">
              <p class="control is-expanded">
                <label class="input">{{ aparelho.marca }}</label>
              </p>
            </div> -->
            <div class="field">
              <p class="control is-expanded">
                <!-- <input type="text" class="input" placeholder="Marca" /> -->
                <Field
                  name="iMarca"
                  as="input"
                  class="input"
                  v-model="aparelho.marca"
                  :class="{ 'is-danger': errors.iMarca }"
                  placeholder="Marca"
                />
              </p>
              <p class="help is-danger">{{ errors.iMarca }}</p>
            </div>
            <!-- <div class="field" v-if="id">
              <p class="control is-expanded">
                <label class="input">{{ aparelho.modelo }}</label>
              </p>
            </div> -->
            <div class="field">
              <p class="control is-expanded">
                <!-- <input type="text" class="input" placeholder="Modelo" /> -->
                <Field
                  name="iModelo"
                  as="input"
                  class="input"
                  v-model="aparelho.modelo"
                  :class="{ 'is-danger': errors.iModelo }"
                  placeholder="Modelo"
                />
              </p>
              <p class="help is-danger">{{ errors.iModelo }}</p>
            </div>
          </div>
        </div>

        <!-- Numero Serie -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Número Série</label>
          </div>
          <div class="field-body">
            <div class="field">
              <p class="control is-expanded">
                <!-- <input type="text" class="input" placeholder="" /> -->
                <Field
                  name="iNumSerie"
                  as="input"
                  class="input"
                  v-model="aparelho.numero_serie"
                  :class="{ 'is-danger': errors.iNumSerie }"
                />
              </p>
              <p class="help is-danger">{{ errors.iNumSerie }}</p>
            </div>
          </div>
        </div>

        <!-- Acessorios -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Acessórios</label>
          </div>
          <div class="field-body">
            <div class="field">
              <p class="control is-expanded">
                <!-- <input type="text" class="input" placeholder="" /> -->
                <Field
                  name="iAcessorios"
                  as="textarea"
                  class="textarea"
                  v-model="aparelho.acessorios"
                  :class="{ 'is-danger': errors.iAcessorios }"
                />
              </p>
              <p class="help is-danger">{{ errors.iAcessorios }}</p>
            </div>
          </div>
        </div>

        <!-- Linha Vinculada -->
        <div class="field is-horizontal" v-if="aparelho.linha">
          <div class="field-label is-normal">
            <label class="label">Linha Vinculada</label>
          </div>
          <div class="field-body">
            <div class="field is-narrow">
              <div class="control">
                <label class="input">
                  {{
                    `(${aparelho.linha.ddd}) ${aparelho.linha.numero.substring(
                      0,
                      5
                    )}-${aparelho.linha.numero.substring(5, 9)}`
                  }}
                </label>
                <!-- <div class="select">
                  <Field name="iLinha" as="select" v-model="linhaTelefonica">
                    <option value="" selected>Selecione uma linha</option>
                    <option value="1">(11) 91234-5678</option>
                    <option value="2">(61) 98765-4321</option>
                  </Field>
                </div> -->
              </div>
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
                  <v-select
                    v-model="funcionarioVinculado"
                    placeholder="Escolha um funcionário..."
                    :options="funcionarios"
                    label="nome_social"
                    :multiple="false"
                    :clearable="true"
                  >
                  </v-select>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Status -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Status do Aparelho</label>
          </div>
          <div class="field-body">
            <div class="field">
              <p class="control is-expanded">
                <label class="input">{{
                  aparelho.funcionario_id
                    ? aparelhoStatus.EM_USO
                    : aparelhoStatus.DISPONIVEL
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
                <!-- <button class="button is-primary">Salvar</button> -->
                <input type="submit" class="button is-primary" value="Salvar" />
              </div>
              <div class="control">
                <router-link to="/aparelhos" class="button is-light"
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
import { defineComponent, ref, computed } from "vue";
import { Form, Field } from "vee-validate";
import * as Yup from "yup";
import { useStore } from "@/store";
import useNotificator from "@/hooks/Notificator";
import IAparelho, { AparelhoStatus } from "@/interfaces/IAparelho";
import {
  DELETE_APARELHO,
  POST_APARELHO,
  PUT_APARELHO,
} from "@/store/modules/aparelho/constants/action-type";
import { NotificationType } from "@/interfaces/INotification";
import IFuncionario from "@/interfaces/IFuncionario";
import { GET_ALL_FUNC } from "@/store/modules/funcionario/constants/action-type";

export default defineComponent({
  name: "FormularioAparelhosViewComponent",
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
    const aparelhoSchema = Yup.object().shape({
      iIMEI: Yup.string()
        .required("O campo IMEI é obrigatório")
        .matches(/^[0-9]{15,17}$/i, "O campo IMEI deve conter entre 15 e 17 números"),
      iIMEI2: Yup.string()
        .required("O campo IMEI é obrigatório")
        .matches(/^[0-9]{15,17}$/i, "O campo IMEI deve conter entre 15 e 17 números"),
      iFabricante: Yup.string().required("O campo Fabricante é obrigatório"),
      iMarca: Yup.string().required("O campo Fabricante é obrigatório"),
      iModelo: Yup.string().required("O campo Fabricante é obrigatório"),
      iNumSerie: Yup.string().required("O campo Número de Série é obrigatório"),
      iAcessorios: Yup.string().required("O campo Acessórios é obrigatório"),
    });
    return {
      aparelhoSchema,
      options: ["Teste1", "Teste2"],
    };
  },
  setup(props) {
    const store = useStore();
    const { notify } = useNotificator();
    const aparelho = ref({} as IAparelho);
    const aparelhoStatus = AparelhoStatus;
    const funcionarioVinculado = ref({} as IFuncionario);
    store.dispatch(GET_ALL_FUNC);

    if (props.id) {
      const device = store.state.aparelho?.aparelhos.find((apar) => apar.id == props.id);
      aparelho.value = device as IAparelho;

      if (device?.funcionario_id) {
        const employee = store.state.funcionario?.funcionarios.find(
          (empl) => empl.id == device?.funcionario_id
        );
        funcionarioVinculado.value = employee as IFuncionario;
      }
    }

    return {
      store,
      notify,
      aparelho,
      aparelhoStatus,
      funcionarios: computed(() => store.state.funcionario.funcionarios),
      funcionarioVinculado,
    };
  },
  methods: {
    saveAparelho() {
      if (this.id) {
        console.log("ALTERANDO APARELHO");
        if (this.funcionarioVinculado) {
          this.aparelho.funcionario_id = this.funcionarioVinculado.id;
          this.aparelho.status = this.aparelhoStatus.EM_USO;
        } else {
          this.aparelho.funcionario_id = '';
          this.aparelho.status = this.aparelhoStatus.DISPONIVEL;
        }
        this.store
          .dispatch(PUT_APARELHO, this.aparelho)
          .then(() => {
            this.notify(
              NotificationType.SUCCESS,
              `Aparelho ${this.aparelho.marca}-${this.aparelho.modelo} alterado com sucesso!`
            );
            this.$router.push("/aparelhos");
          })
          .catch((err) => {
            this.notify(NotificationType.DANGER, err.response.data.message);
          });
      } else {
        this.aparelho.status = this.aparelhoStatus.DISPONIVEL;
        if (this.funcionarioVinculado) {
          this.aparelho.funcionario_id = this.funcionarioVinculado.id;
          this.aparelho.status = this.aparelhoStatus.EM_USO;
        }
        this.store
          .dispatch(POST_APARELHO, this.aparelho)
          .then(() => {
            this.notify(
              NotificationType.SUCCESS,
              `Aparelho ${this.aparelho.marca}-${this.aparelho.modelo} cadastrado com sucesso!`
            );
            this.$router.push("/aparelhos");
          })
          .catch((err) => {
            this.notify(NotificationType.DANGER, err.response.data.message);
          });
      }
    },
    deleteAparelho(aparelho: IAparelho) {
      this.store
        .dispatch(DELETE_APARELHO, aparelho.id)
        .then(() => {
          this.notify(
            NotificationType.SUCCESS,
            `Aparelho ${aparelho.marca}-${aparelho.modelo} excluído com sucesso!`
          );
        })
        .catch((err) => {
          this.notify(NotificationType.DANGER, err.response.data.message);
        });
    },
  },
});
</script>
