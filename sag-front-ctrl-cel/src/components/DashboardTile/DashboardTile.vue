<template>
  <article class="tile is-child notification" :class="color">
    <p class="title">Vertical...</p>
    <p class="subtitle">Top tile</p>
    <div class="content">
        <!-- Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Phasellus eleifend nulla non diam iaculis, non vulputate arcu sollicitudin. 
        Phasellus et luctus lacus. Phasellus ultrices lobortis ex auctor mollis. 
        Suspendisse potenti. Aenean lacinia turpis fermentum, efficitur lectus quis, 
        rutrum lacus. Donec quis augue viverra, sagittis metus vel, ornare lectus.  -->
        <slot></slot>
    </div>
  </article>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "DashboardTileComponent",
  props: {
      color: {
          type: String
      }
  }
});
</script>
