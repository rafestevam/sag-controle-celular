<template>
  <div>
    <h1 class="subtitle">Adicionar ou Alterar Linha Telefônica</h1>
  </div>
  <section class="main-form">
    <div class="container is-widescreen">
      <!-- Numero da Linha -->
      <div class="field is-horizontal">
        <div class="field-label"></div>
        <div class="field-body">
          <div class="field is-expanded">
            <div class="field has-addons">
              <p class="control">
                <a class="button is-static"> +55 </a>
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
                <input
                  class="input"
                  type="tel"
                  placeholder="Número da Linha Telefônica"
                />
              </p>
            </div>
            <p class="help">Entrar o número no formato (99) 99999-9999</p>
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
              <input type="text" class="input" placeholder="" />
            </p>
          </div>
        </div>
      </div>

      <!-- Aparelho em Posse -->
      <div class="field is-horizontal">
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
      </div>

      <!-- Status -->
      <div class="field is-horizontal">
        <div class="field-label is-normal">
          <label class="label">Status da Linha</label>
        </div>
        <div class="field-body">
          <div class="field is-narrow">
            <div class="control">
              <div class="select is-fullwidth">
                <select>
                  <option>Em Uso</option>
                  <option>Disponível</option>
                </select>
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
              <button class="button is-primary">Salvar</button>
            </div>
            <div class="control">
              <button class="button is-light">Cancelar</button>
            </div>
          </div>
        </div>
      </div>

    </div>
  </section>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "FormularioLinhasViewComponent",
});
</script>
