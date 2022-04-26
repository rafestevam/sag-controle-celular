<template>
  <div>
    <h1 class="subtitle">Adicionar ou Alterar Aparelho</h1>
  </div>
  <section class="main-form">
    <div class="container is-widescreen">
      <!-- IMEI/IMEI2 -->
      <div class="field is-horizontal">
        <div class="field-label is-normal">
          <label class="label">IMEI/IMEI2</label>
        </div>
        <div class="field-body">
          <div class="field">
            <p class="control is-expanded">
              <input type="text" class="input" placeholder="IMEI" />
            </p>
          </div>
          <div class="field">
            <p class="control is-expanded">
              <input type="text" class="input" placeholder="IMEI2" />
            </p>
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
              <input type="text" class="input" placeholder="" />
            </p>
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
              <input type="text" class="input" placeholder="Marca" />
            </p>
          </div>
          <div class="field">
            <p class="control is-expanded">
              <input type="text" class="input" placeholder="Modelo" />
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
              <input type="text" class="input" placeholder="" />
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
                <label class="input">(11) 91234-5678</label>
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
                <label class="input">Em Uso</label>
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
  </section>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "FormularioAparelhosViewComponent",
});
</script>
