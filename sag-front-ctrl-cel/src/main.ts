import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import { key, store } from './store';
import { msalPlugin } from './plugins/msalPlugin';
import { msalInstance } from './authConfig';
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";
import { VueCookieNext } from 'vue-cookie-next';

import '@fortawesome/fontawesome-free/css/all.css';
import { maska } from 'maska';

require('@/assets/main.scss');

VueCookieNext.config({
    expire: '1d',
    path: '/',
    domain: '',
    secure: '',
    sameSite: '',
});

createApp(App)
    .use(router)
    .use(store, key)
    .use(msalPlugin, msalInstance)
    .use(VueCookieNext)
    .component('v-select', vSelect)
    .directive('maska', maska)
    .mount('#app');
