import { createRouter, RouteRecordRaw, createWebHistory } from "vue-router";
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
import Utilitarios from "@/views/Utilitarios.vue";
import BulkLoading from "@/views/Utilitarios/BulkLoading.vue";
import TermoComposer from "@/views/Utilitarios/TermoComposer.vue";
import Login from "@/views/Login.vue";

const routes:  RouteRecordRaw[] = [
    {
        path: '/',
        name: 'Login',
        component: Login,
    },
    {
        path: '/home',
        name: 'Home',
        component: Home,
        // meta: {
        //     requiresAuth: true,
        // }
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
            {
                path: ':id',
                name: 'AtualizarLinha',
                component: FormularioLinhas,
                props: true,
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
            {
                path: ':id',
                name: 'AtualizarAparelho',
                component: FormularioAparelhos,
                props: true,
            }
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
            },
            {
                path: ':id',
                name: 'AtualizarFuncionario',
                component: FormularioFuncionarios,
                props: true,
            },
        ]
    },
    {
        path: '/utilities',
        component: Utilitarios,
        children: [
            {
                path: 'bulk',
                name: 'CargaEmLote',
                component: BulkLoading,
            },
            {
                path: 'termo',
                name: 'GeradorDeTermos',
                component: TermoComposer,
            }
        ]
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

router.beforeEach((to, from, next) => {
    if (to.name !== 'Login'){
        const token = localStorage.getItem('jwt');
        if (!token) {
            next('/')
        }
    }
    next();
});

// registerGuard(router);

export default router;
