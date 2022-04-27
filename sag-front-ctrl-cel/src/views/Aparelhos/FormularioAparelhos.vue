<template>
  <div>
    <h1 class="subtitle">Adicionar ou Alterar Aparelho</h1>
  </div>
  <section class="main-form">
    <Form
      @submit.prevent="saveAparelho"
      :validation-schema="aparelhoSchema"
      v-slot="{ errors }"
    >
      <div class="container is-widescreen">
        <!-- IMEI/IMEI2 -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">IMEI/IMEI2</label>
          </div>
          <div class="field-body">
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
            </div>
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
            </div>
          </div>
        </div>

        <!-- Linha Vinculada -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Linha Telefônica</label>
          </div>
          <div class="field-body">
            <div class="field">
              <p class="control is-expanded">
                <label class="input">{{ aparelho.linha ? `(${aparelho.linha.ddd}) ${aparelho.linha.numero}` : 'N/D' }}</label>
              </p>
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
                <label class="input">{{ aparelho.funcionario ? aparelhoStatus.EM_USO : aparelhoStatus.DISPONIVEL }}</label>
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
                <button class="button is-primary">Salvar</button>
              </div>
              <div class="control">
                <button class="button is-light">Cancelar</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Form>
  </section>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { Form, Field } from "vee-validate";
import * as Yup from "yup";
import { useStore } from "@/store";
import useNotificator from "@/hooks/Notificator";
import IAparelho, { AparelhoStatus } from "@/interfaces/IAparelho";
import { POST_APARELHO } from "@/store/modules/aparelho/constants/action-type";
import { NotificationType } from "@/interfaces/INotification";

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
      iIMEI: Yup.number()
        .required('O campo IMEI é obrigatório')
        .typeError('O campo IMEI deve conter somente números')
        .max(17, 'O campo IMEI deve conter entre 15 e 17 números')
        .min(15, 'O campo IMEI deve conter entre 15 e 17 números'),
      iIMEI2: Yup.number()
        .required('O campo IMEI é obrigatório')
        .typeError('O campo IMEI deve conter somente números')
        .max(17, 'O campo IMEI deve conter entre 15 e 17 números')
        .min(15, 'O campo IMEI deve conter entre 15 e 17 números'),
      iFabricante: Yup.string()
        .required('O campo Fabricante é obrigatório'),
      iMarca: Yup.string()
        .required('O campo Fabricante é obrigatório'),
      iModelo: Yup.string()
        .required('O campo Fabricante é obrigatório'),
      iNumSerie: Yup.string()
        .required('O campo Número de Série é obrigatório')
    });
    return {
      aparelhoSchema,
    };
  },
  setup(props) {
    const store = useStore();
    const { notify } = useNotificator();
    const aparelho = ref({} as IAparelho);
    const aparelhoStatus = AparelhoStatus;
    if (props.id) {
      const device = store.state.aparelho?.aparelhos.find(
        (apar) => apar.id == props.id
      );
      aparelho.value = device as IAparelho;
    }

    return {
      store,
      notify,
      aparelho,
      aparelhoStatus,
    };
  },
  methods: {
    saveAparelho() {
      if(this.id){
        console.log('ALTERANDO APARELHO');
      }else {
        this.store
          .dispatch(POST_APARELHO, this.aparelho)
          .then(() => {
            this.notify(NotificationType.SUCCESS, `Aparelho ${this.aparelho.marca}-${this.aparelho.modelo} cadastrado com sucesso!`);
          })
          .catch(err => {
            this.notify(NotificationType.DANGER, err.response.data.mensagem);
          });
      }
    },
  },
});
</script>
