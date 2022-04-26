<template>
  <div>
    <h1 class="subtitle">Adicionar ou Alterar Centro de Custo</h1>
  </div>
  <section class="main-form">
    <div class="container is-widescreen">
      <Form @submit.prevent="saveCentroCusto" :validation-schema="schema" v-slot="{ errors }">
      <!-- Código -->
      <div class="field is-horizontal">
        <div class="field-label is-normal">
          <label class="label">Código</label>
        </div>
        <div class="field-body">
          <div class="field">
            <p class="control is-expanded">
              <Field name="iCodigo" class="input" as="input" v-model="centro_custo.cc_cod" :class="{ 'is-danger': errors.iCodigo }" />
            </p>
            <p class="help is-danger">{{ errors.iCodigo }}</p>
          </div>
        </div>
      </div>

      <!-- Nome -->
      <div class="field is-horizontal">
        <div class="field-label is-normal">
          <label class="label">Nome</label>
        </div>
        <div class="field-body">
          <div class="field">
            <p class="control is-expanded">
              <Field name="iNome" class="input" as="input" v-model="centro_custo.cc_nome" :class="{ 'is-danger': errors.iNome }" />
            </p>
            <p class="help is-danger">{{ errors.iNome }}</p>
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
                <router-link 
                  to="/cc" 
                  class="button is-light">Cancelar
                </router-link>
              </div>
            </div>
          </div>
        </div>

      </Form>
    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import { useStore } from "@/store";
import ICentroCusto from "@/interfaces/ICentroCusto";
import useNotificator  from "@/hooks/Notificator";
import { POST_CC, PUT_CC } from "@/store/modules/centrocusto/constants/action-type";
import { NotificationType } from "@/interfaces/INotification";
import { Form, Field } from "vee-validate";
import * as Yup from "yup";

export default defineComponent({
  name: "FormularioCCViewComponent",
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
    const schema = Yup.object().shape({
      iCodigo: Yup.number()
        .required('O campo Código é obrigatório')
        .typeError('O campo Código deve conter somente números')
        .max(6, 'O campo Código deve conter somente 6 números'), 
      iNome: Yup.string()
        .required('O campo Nome é obrigatório'),
    });
    return {
      schema,
    }
  },
  setup(props) {
    const store = useStore();
    const { notify } = useNotificator()
    const centro_custo = ref({} as ICentroCusto);
    if (props.id) {
      const cc = store.state.centrocusto?.ccs.find(
        (ccusto) => ccusto.id == props.id
      );
      centro_custo.value = cc as ICentroCusto;
    }

    return {
      store,
      centro_custo,
      notify,
    };
  },
  methods: {
    saveCentroCusto() {
      if(this.id){
        this.store
          .dispatch(PUT_CC, this.centro_custo)
          .then(() => {
            this.notify(NotificationType.SUCCESS, `Centro de Custo ${this.centro_custo.cc_cod} alterado com sucesso!`);
            this.$router.push('/cc');
          })
          .catch(err => {
            this.notify(NotificationType.DANGER, `${err.response.data.mensagem}`);
          });
      } else {
        this.store
          .dispatch(POST_CC, this.centro_custo)
          .then(() => {
            this.notify(NotificationType.SUCCESS, `Centro de Custo ${this.centro_custo.cc_cod} criado com sucesso!`);
            this.$router.push('/cc');
          })
          .catch(err => {
            this.notify(NotificationType.DANGER, `${err.response.data.mensagem}`);
          })
      }
    },
  },
});
</script>