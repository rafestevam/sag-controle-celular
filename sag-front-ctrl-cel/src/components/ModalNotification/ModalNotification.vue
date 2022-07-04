<template>
  <div class="modal" :class="{ 'is-active': isActive }">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">{{ title }}</p>
        <button class="delete" aria-label="close" @click="emitOnCancelModal"></button>
      </header>
      <section class="modal-card-body">
        <!-- Content ... -->
        <div class="content">
            <p>{{ message }}</p>
        </div>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-success" @click="emitOnSaveModal">Confirmar</button>
        <button class="button" @click="emitOnCancelModal">Cancelar</button>
      </footer>
    </div>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent } from "vue";
import { useStore } from "@/store";

export default defineComponent({
  name: "ModalNotificationComponent",
  props: {
    title: {
      type: String,
      required: true,
    },
    message: {
      type: String,
      required: true,
    },
    isActive: {
      type: Boolean,
    }
  },
  emits: ['onSaveModal', 'onCancelModal'],
  setup() {
      const store = useStore();
      return {
          modalNotifications: computed(() => store.state.modalNotifications),
      }
  },
  methods: {
      emitOnSaveModal() {
          this.$emit('onSaveModal');
      },
      emitOnCancelModal() {
          this.$emit('onCancelModal');
      },
  },
});
</script>
