<template>
  <div class="main-window">
    <h1 class="title">Bem Vindo, {{ loggedUser.name }}!</h1>

    <div class="tile is-ancestor">
      <div class="tile is-vertical">
        <div class="tile">
          <div class="tile is-parent">
            <DashboardTile>
              <DoughnutChart />
            </DashboardTile>
          </div>
          <div class="tile is-parent">
            <DashboardTile>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus
              eleifend nulla non diam iaculis, non vulputate arcu sollicitudin.
              Phasellus et luctus lacus. Phasellus ultrices lobortis ex auctor
              mollis. Suspendisse potenti. Aenean lacinia turpis fermentum,
              efficitur lectus quis, rutrum lacus. Donec quis augue viverra,
              sagittis metus vel, ornare lectus.
            </DashboardTile>
          </div>
          <div class="tile is-parent">
            <DashboardTile>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus
              eleifend nulla non diam iaculis, non vulputate arcu sollicitudin.
              Phasellus et luctus lacus. Phasellus ultrices lobortis ex auctor
              mollis. Suspendisse potenti. Aenean lacinia turpis fermentum,
              efficitur lectus quis, rutrum lacus. Donec quis augue viverra,
              sagittis metus vel, ornare lectus.
            </DashboardTile>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent } from "vue";
import DashboardTile from "@/components/DashboardTile/DashboardTile.vue";
import DoughnutChart from "@/components/Charts/DoughnutChart/DoughnutChart.vue";
import { useStore } from "@/store";
export default defineComponent({
  name: "HomeViewComponent",
  components: {
    DashboardTile,
    DoughnutChart,
  },
  setup() {
    const store = useStore();
    return {
      loggedUser: computed(() => store.state.usuario.user),
    }
  }
});
</script>
