import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { key, store } from './store';
import { msalPlugin } from './plugins/msalPlugin';
import { msalInstance } from './authConfig';
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";

import '@fortawesome/fontawesome-free/css/all.css';
import { maska } from 'maska';

createApp(App)
    .use(router)
    .use(store, key)
    .use(msalPlugin, msalInstance)
    .component('v-select', vSelect)
    .directive('maska', maska)
    .mount('#app');
