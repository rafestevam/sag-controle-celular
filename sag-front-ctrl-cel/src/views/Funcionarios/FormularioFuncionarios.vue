<template>
  <div>
    <h1 class="subtitle">Adicionar ou Alterar Funcionário</h1>
  </div>
  <section class="main-form">
    <div class="container is-widescreen">

      <!-- Nome/Sobrenome -->
      <div class="field is-horizontal">
        <div class="field-label is-normal">
          <label class="label">Nome/Sobrenome</label>
        </div>
        <div class="field-body">
          <div class="field">
            <p class="control is-expanded">
              <input type="text" class="input" placeholder="Nome" />
            </p>
          </div>
          <div class="field">
            <p class="control is-expanded">
              <input type="text" class="input" placeholder="Sobrenome" />
            </p>
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
              <input type="text" class="input" placeholder="" />
            </p>
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
              <input type="date" class="input" placeholder="" />
            </p>
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
              <input type="date" class="input" placeholder="" />
            </p>
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
              <input type="text" class="input" placeholder="RG" />
            </p>
            <p class="help">Entrar RG no formato 99.999.999-99</p>
          </div>
          <div class="field">
            <p class="control is-expanded">
              <input type="text" class="input" placeholder="CPF" />
            </p>
            <p class="help">Entrar CPF no formato 999.999.999-99</p>
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
              <input type="text" class="input" placeholder="" />
            </p>
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
                <select>
                  <option>Selecione um CC</option>
                  <option>123456 - Customer Support BR</option>
                  <option>789012 - Professional Services BR</option>
                </select>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Aparelho em Posse -->
      <div class="field is-horizontal">
        <div class="field-label is-normal">
          <label class="label">Linha Atribuída</label>
        </div>
        <div class="field-body">
          <div class="field is-narrow">
            <div class="control">
              <div class="select is-fullwidth">
                <select>
                  <option>Selecione uma Linha</option>
                  <option>(11) 91234-5678</option>
                  <option>(61) 98765-4321</option>
                </select>
              </div>
            </div>
          </div>
          <div class="field">
              <p class="control is-narrow">
                <input type="text" class="input" value="111111111111111111111 - IPhone 7 SE" disabled/>
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
  name: "FormularioFuncionariosViewComponent",
});
</script>
