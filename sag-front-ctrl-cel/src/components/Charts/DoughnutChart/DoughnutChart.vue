
<template>
  <Doughnut
    :chart-data="chartData"
    :chart-options="chartOptions"
  />
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';
import { Doughnut } from 'vue-chartjs';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
  Plugin,
} from "chart.js";
ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale);
// import DoughnutChart from './doughnutChart';

export default defineComponent({
  name: 'DoughnutChartComponent',
  components: {
    Doughnut,
  },
  props: {
    chartId: {
      type: String,
      default: "doughnut-chart",
    },
    width: {
      type: Number,
      default: 300,
    },
    height: {
      type: Number,
      default: 300,
    },
    plugins: {
      type: Array as PropType<Plugin<"doughnut">[]>,
      default: () => [],
    },
  },
  data () {
    return {
      chartData: {
        labels: ['Disponível', 'Em Uso'],
        datasets: [
          { 
            data: [138, 29],
            backgroundColor: ["#41B883", "#E46651"],
           }
          // {
          //   label: 'Disponível',
          //   backgroundColor: '#41B883',
          //   data: [129],
          // },
          // {
          //   label: 'Em Uso',
          //   backgroundColor: '#E46651',
          //   data: [38],
          // }
        ]
      },
      chartOptions: {
        responsive: true,
      }
    }
  }
})
</script>