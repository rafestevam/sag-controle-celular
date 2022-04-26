<template>
  <router-link class="navbar-item" v-if="!isDropDown" :to="route">
    <i :class="icon" class="icon-padding" v-if="icon"></i>
    {{ label }}
  </router-link>
  <div class="navbar-item has-dropdown is-hoverable" v-show="isDropDown">
    <a class="navbar-link" v-show="isDropDown">
      <i :class="icon" class="icon-padding" v-if="icon"></i>
      {{ label }}
    </a>
    <div class="navbar-dropdown">
      <router-link
        class="navbar-item"
        v-for="(ddItem, index) in dropDownItems"
        :key="index"
        :to="ddItem.route"
      >
        {{ ddItem.label }}
      </router-link>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";
import ItemNav from './ItemNavInterface';

export default defineComponent({
  name: "MainNavItemComponent",
  props: {
    icon: {
      type: String,
    },
    label: {
      type: String,
      required: true,
    },
    isDropDown: {
      type: Boolean,
      required: true,
    },
    route: {
      type: String,
    },
    dropDownItems: {
      type: Array as PropType<ItemNav[]>,
      default: () => [{
        label: '',
        route: '',
      }],
    },
  },
  // data() {
  //   return {
  //     ddItems: this.dropDownItems,
  //   };
  // },
});
</script>

<style scoped>
.icon-padding {
  padding: 0.3rem;
}
</style>
