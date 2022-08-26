import INotification, { IModalNotification } from "@/interfaces/INotification";
import { InjectionKey } from "vue";
import { createStore, Store, useStore as vuexUseStore } from "vuex";
import { aparelho, AparelhoState } from "./modules/aparelho";
import { centrocusto, CentroCustoState } from "./modules/centrocusto";
import { funcionario, FuncionarioState } from "./modules/funcionario";
import { linha, LinhaState } from "./modules/linha";
import { DELETE_NOTIFICATION, NOTIFY } from "./modules/notif/constants/mutation-type";

export interface AppState {
    centrocusto: CentroCustoState,
    aparelho: AparelhoState,
    linha: LinhaState,
    funcionario: FuncionarioState,
    // notif: NotificationState,
    notifications: INotification[],
    modalNotifications: IModalNotification[],
}

export const key: InjectionKey<Store<AppState>> = Symbol();

export const store = createStore<AppState>({
    state: {
        centrocusto: {
            ccs: [],
        },
        aparelho: {
            aparelhos: [],
        },
        linha: {
            linhas: [],
        },
        funcionario: {
            funcionarios: []
        },
        notifications: [],
        modalNotifications: [],
    },
    mutations: {
        [NOTIFY](state, newNotification: INotification){
            newNotification.id = new Date().toISOString();
            state.notifications.push(newNotification);
            setTimeout(() => {
                state.notifications = state.notifications
                    .filter(notif => notif.id != newNotification.id);
            }, 3000);
        },
        [DELETE_NOTIFICATION](state, idNotification: string){
            state.notifications = state.notifications.filter(
                notif => notif.id != idNotification
            );
        },
        // [MODAL_NOTIFY](state, modalNotification: IModalNotification) {
        //     // console.log(modalNotification);
        //     state.modalNotifications.push(modalNotification);
        // },
    },
    modules: {
        centrocusto,
        aparelho,
        linha,
        funcionario,
    },
});

export function useStore(): Store<AppState> {
    return vuexUseStore(key);
}