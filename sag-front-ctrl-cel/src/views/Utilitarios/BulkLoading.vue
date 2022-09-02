<template>
  <div>
    <h1 class="subtitle">Carga de Dados em Lote</h1>
  </div>
  <section class="main-form">
    <div class="container is-widescreen">
      <Form @submit="submitBulkFile" :validation-schema="bulkSchema" v-slot="{ errors }">

        <!-- Tipo de Objeto -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Tipo de Objeto</label>
          </div>
          <div class="field-body">
            <div class="field is-narrow">
              <div class="control">
                <div class="select is-fullwidth">
                  <Field v-model="tipoObjeto"
                    name="iTipoObjeto"
                    as="select"
                    class="input"
                    :class="{'is-danger': errors.iTipoObjeto}"
                  >
                    <option value="" selected>Selecione um Tipo de Objeto</option>
                    <option value="cc">Centro de Custo</option>
                    <option value="device">Aparelho</option>
                    <option value="line">Linha</option>
                    <option value="employee">Funcionário</option>
                  </Field>
                </div>
                <p class="help is-danger">{{ errors.iTipoObjeto }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Arquivo -->
        <div class="field is-horizontal">
          <div class="field-label is-normal">
            <label class="label">Arquivo de Carga</label>
          </div>
          <div class="field-body">
            <div class="field is-narrow">
              <div class="control">
                <div class="file is-medium is-boxed has-name">
                  <label class="file-label">
                    <input class="file-input" type="file" name="file" @change="onFilePicked">
                    <span class="file-cta">
                      <span class="file-icon">
                        <i class="fas fa-upload"></i>
                      </span>
                      <span class="file-label">
                        Escolha um arquivo
                      </span>
                    </span>
                    <span class="file-name">
                      {{ fileName }}
                    </span>
                  </label>
                </div>
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
                <input type="submit" class="button is-primary" value="Salvar">
              </div>
              <div class="control">
                <router-link to="/" class="button is-light">Cancelar</router-link>
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
import useNotificator from "@/hooks/Notificator";
import { Form, Field } from "vee-validate";
import { POST_BULK_CC } from "@/store/modules/centrocusto/constants/action-type";
import { NotificationType } from "@/interfaces/INotification";
import { POST_BULK_APARELHOS } from "@/store/modules/aparelho/constants/action-type";
import { POST_BULK_LINHAS } from "@/store/modules/linha/constants/action-type";
import { POST_BULK_FUNC } from "@/store/modules/funcionario/constants/action-type";
import * as Yup from "yup";

export default defineComponent({
  name: "BulkLoadingViewComponent",
  components: {
    Form,
    Field,
  },
  data() {
    const bulkSchema = Yup.object().shape({
      iTipoObjeto: Yup.string().required(
        "O campo TIPO DE OBJETO é obrigatório"
      ),
    });
    return{
      bulkSchema,
    }
  },
  setup() {
    const store = useStore();
    const { notify } = useNotificator();

    const tipoObjeto = ref('');
    const file = ref(null);
    const fileName = ref('');
    const fileType = ref('');

    const onFilePicked = (evt: any) => {
      const files = evt.target.files
      file.value = files[0] != undefined ? files[0] : undefined;
      fileName.value = files[0] != undefined ? files[0].name : '';
      fileType.value = files[0] != undefined ? files[0].type : '';
    }

    return {
      store,
      notify,
      tipoObjeto,
      file,
      fileName,
      fileType,
      onFilePicked,
    }
  },
  methods: {
    submitBulkFile(){
      console.log('Bulk File submitted');
      if(this.file != undefined){
        
        // Validação do Tipo de Arquivo
        if(this.fileType != 'text/csv'){
          this.notify(
            NotificationType.DANGER,
            'Tipo de Arquivo não suportado. Selecione somente arquivos do tipo CSV!'
          );
          this.$router.push("/");
          return;
        }

        let formData = new FormData();
        formData.append('file', this.file);
        
        // POST Bulk Data - Centro de Custo
        if(this.tipoObjeto == 'cc'){
          this.store
            .dispatch(POST_BULK_CC, formData)
            .then(() => {
              this.notify(
                NotificationType.SUCCESS,
                'Centros de Custo carregados com sucesso!'
              );
            })
            .catch((err) => 
              this.notify(NotificationType.DANGER, err.response.data)
            );
        }

        //POST Bulk Data - Aparelhos
        if(this.tipoObjeto == 'device'){
          this.store
            .dispatch(POST_BULK_APARELHOS, formData)
            .then(() => {
              this.notify(
                NotificationType.SUCCESS,
                'Aparelhos carregados com sucesso!'
              );
            })
            .catch((err) => 
              this.notify(NotificationType.DANGER, err.response.data)
            );
        }

        //POST Bulk Data - Linhas
        if(this.tipoObjeto == 'line'){
          this.store
            .dispatch(POST_BULK_LINHAS, formData)
            .then(() => {
              this.notify(
                NotificationType.SUCCESS,
                'Linhas carregadas com sucesso!'
              );
            })
            .catch((err) => 
              this.notify(NotificationType.DANGER, err.response.data)
            );
        }

        //POST Bulk Data - Funcionarios
        if(this.tipoObjeto == 'employee'){
          this.store
            .dispatch(POST_BULK_FUNC, formData)
            .then(() => {
              this.notify(
                NotificationType.SUCCESS,
                'Funcionários carregados com sucesso!'
              );
            })
            .catch((err) => 
              this.notify(NotificationType.DANGER, err.response.data)
            );
        }
      } else {
        this.notify(
          NotificationType.DANGER,
          'Favor selecionar um arquivo para carga'
        );
      }
    }
  }
});
</script>
