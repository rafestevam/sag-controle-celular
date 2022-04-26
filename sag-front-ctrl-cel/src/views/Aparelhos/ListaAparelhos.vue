<template>
  <div>
    <h1 class="subtitle">Lista de Aparelhos Telefônicos</h1>
  </div>
  <section class="main-form">
    <div class="container is-widescreen">
      <table class="table is-fullwidth">
        <thead>
          <tr>
            <td>Num. Série</td>
            <td>Marca</td>
            <td>Fabricante</td>
            <td>Status</td>
            <td>Ações</td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="aparelho in aparelhos" :key="aparelho.id">
            <td>{{ aparelho.numero_serie }}</td>
            <td>{{ aparelho.marca }}</td>
            <td>{{ aparelho.fabricante }}</td>
            <td>{{ aparelho.status }}</td>
            <td>
              <button class="button">
                <span class="icon is-small">
                  <i class="fas fa-pencil-alt"></i>
                </span>
              </button>
              <button class="button ml-2 is-danger">
                <span class="icon is-small">
                  <i class="fas fa-trash"></i>
                </span>
              </button>
            </td>
          </tr>
          <!-- <tr>
            <td>222222222222222222222</td>
            <td>Apple</td>
            <td>IPhone 8+</td>
            <td>
              <button class="button">
                <span class="icon is-small">
                  <i class="fas fa-pencil-alt"></i>
                </span>
              </button>
              <button class="button ml-2 is-danger">
                <span class="icon is-small">
                  <i class="fas fa-trash"></i>
                </span>
              </button>
            </td>
          </tr> -->
        </tbody>
      </table>
    </div>
  </section>
</template>

<script lang="ts">
import { useStore } from "@/store";
import { GET_ALL_APARELHOS } from "@/store/modules/aparelho/constants/action-type";
import { computed, defineComponent } from "vue";
export default defineComponent({
  name: "ListaAparelhosViewComponent",
  setup() {
    const store = useStore();
    store.dispatch(GET_ALL_APARELHOS);
    return {
      aparelhos: computed(() => store.state.aparelho.aparelhos),
    }
  }
});
</script>
