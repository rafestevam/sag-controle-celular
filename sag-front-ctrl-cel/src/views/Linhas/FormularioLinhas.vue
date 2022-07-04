<template>
  <div>
    <h1 class="subtitle">Adicionar ou Alterar Linha Telefônica</h1>
  </div>
  <section class="main-form">
    <Form @submit="saveLinha" :validation-schema="linhaSchema" v-slot="{ errors }">
    <div class="container is-widescreen">
      <!-- Numero da Linha -->
      <div class="field is-horizontal">
        <div class="field-label"></div>
        <div class="field-body">
          <div class="field is-expanded">
            <div class="field has-addons">
              <p class="control">
                <a class="button" :class="{ 'is-danger': errors.iTelefone && !id, 'is-static': !errors.iTelefone || id }"> +55 </a>
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
                <Field v-model="numeroTelefone" v-if="!id"
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
              <Field v-model="linha.classificacao"
               name="iClassificacao"
               as="input"
               type="text" 
               class="input" 
               placeholder="" />
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
                <label class="input">{{ linha.funcionario_id ? linhaStatus.EM_USO : linhaStatus.DISPONIVEL }}</label>
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
              <input type="submit" class="button is-primary" value="Salvar">
            </div>
            <div class="control">
              <router-link to="/linhas" class="button is-light">Cancelar</router-link>
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
import { defineComponent, ref } from "vue";
import { Form, Field } from "vee-validate";
import * as Yup from "yup";
import { useStore } from "@/store";
import useNotificator from "@/hooks/Notificator";
import { POST_LINHA, PUT_LINHA } from "@/store/modules/linha/constants/action-type";
import { NotificationType } from "@/interfaces/INotification";
import IFuncionario from "@/interfaces/IFuncionario";

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
        .matches(/^\([1-9]{2}\) [9]{0,1}[6-9]{1}[0-9]{3}-[0-9]{4}$/, "Entrar o número de Telefone no formato (99) 99999-9999"),
    });
    return {
      linhaSchema,
    }
  },
  methods: {
    saveLinha() {
      if(this.id){
        console.log('ALTERAR LINHA');
        this.linha.status = this.linha.funcionario_id ? LinhaStatus.EM_USO : LinhaStatus.DISPONIVEL;
        this.store
          .dispatch(PUT_LINHA, this.linha)
          .then(() => {
            this.notify(NotificationType.SUCCESS, `Linha #${this.numeroTelefone} alterada com sucesso!`)
          })
          .catch(err => {
            this.notify(NotificationType.DANGER, err.response.data.message);
          });
      } else {
        const numTel = this.numeroTelefone.replace(/[^0-9]/g, '');
        const funcionario = {} as IFuncionario;
        funcionario.id = ""
        this.linha.ddd = numTel.substring(0,2);
        this.linha.numero = numTel.substring(2, 11);
        this.linha.status = LinhaStatus.DISPONIVEL;
        this.linha.funcionario_id = funcionario.id;
        this.store
          .dispatch(POST_LINHA, this.linha)
          .then(() => {
            this.notify(NotificationType.SUCCESS, `Linha #${this.numeroTelefone} cadastrada com sucesso!`);
            this.$router.push('/linhas');
          })
          .catch(err => {
            this.notify(NotificationType.DANGER, err.response.data);
          });
      }
    }
  },
  setup(props) {
    const store = useStore();
    const { notify } = useNotificator();
    const linha = ref({} as ILinha);
    const numeroTelefone = ref('');
    const linhaStatus = LinhaStatus;

    if(props.id){
      const line = store.state.linha?.linhas.find(
        (ln) => ln.id == props.id
      );
      linha.value = line as ILinha;
      numeroTelefone.value = `(${line?.ddd}) ${line?.numero.substring(0,5)}-${line?.numero.substring(5,9)}`;
    }

    return {
      store,
      notify,
      linha,
      linhaStatus,
      numeroTelefone,
    }
  }
});
</script>
