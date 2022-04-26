import { createRouter, RouteRecordRaw, createWebHashHistory } from "vue-router";
import Home from '@/views/Home.vue';
import CentroCusto from '@/views/CentroCusto.vue';
import FormularioCC from "@/views/CentroCusto/FormularioCC.vue";
import ListaCC from "@/views/CentroCusto/ListaCC.vue";
import Linhas from "@/views/Linhas.vue";
import FormularioLinhas from "@/views/Linhas/FormularioLinhas.vue";
import ListaLinhas from "@/views/Linhas/ListaLinhas.vue";
import Aparelhos from "@/views/Aparelhos.vue";
import FormularioAparelhos from "@/views/Aparelhos/FormularioAparelhos.vue";
import ListaAparelhos from "@/views/Aparelhos/ListaAparelhos.vue";
import Funcionarios from "@/views/Funcionarios.vue";
import FormularioFuncionarios from "@/views/Funcionarios/FormularioFuncionarios.vue";
import ListaFuncionarios from "@/views/Funcionarios/ListaFuncionarios.vue";

const routes:  RouteRecordRaw[] = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/cc',
        component: CentroCusto,
        children: [
            {
                path: '',
                name: 'ListaCC',
                component: ListaCC,
            },
            {
                path: 'novo',
                name: 'CriarCC',
                component: FormularioCC,
            },
            {
                path: ':id',
                name: 'AtualizarCC',
                component: FormularioCC,
                props: true,
            }
        ],
    },
    {
        path: '/linhas',
        component: Linhas,
        children: [
            {
                path: '',
                name: 'ListaLinhas',
                component: ListaLinhas,
            },
            {
                path:'nova',
                name: 'FormularioLinhas',
                component: FormularioLinhas,
            },
        ],
    },
    {
        path: '/aparelhos',
        component: Aparelhos,
        children: [
            {
                path: '',
                name: 'ListaAparelhos',
                component: ListaAparelhos,
            },
            {
                path: 'novo',
                name: 'FormularioAparelhos',
                component: FormularioAparelhos,
            },
        ],
    },
    {
        path: '/funcionarios',
        component: Funcionarios,
        children: [
            {
                path: '',
                name: 'ListaFuncionarios',
                component: ListaFuncionarios
            },
            {
                path: 'novo',
                name: 'FormularioFuncionarios',
                component: FormularioFuncionarios
            }
        ]
    }
];

const router = createRouter({
    history: createWebHashHistory(),
    routes
});

export default router;
