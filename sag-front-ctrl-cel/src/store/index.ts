import INotification from "@/interfaces/INotification";
import { InjectionKey } from "vue";
import { createStore, Store, useStore as vuexUseStore } from "vuex";
import { aparelho, AparelhoState } from "./modules/aparelho";
import { centrocusto, CentroCustoState } from "./modules/centrocusto";
import { NOTIFY } from "./modules/notif/constants/mutation-type";

export interface AppState {
    centrocusto: CentroCustoState,
    aparelho: AparelhoState,
    // notif: NotificationState,
    notifications: INotification[],
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
        notifications: [],
    },
    mutations: {
        [NOTIFY](state, newNotification: INotification){
            newNotification.id = new Date().toISOString();
            state.notifications.push(newNotification);
            setTimeout(() => {
                state.notifications = state.notifications
                    .filter(notif => notif.id != newNotification.id);
            }, 3000);
        }
    },
    modules: {
        centrocusto,
        aparelho,
    },
});

export function useStore(): Store<AppState> {
    return vuexUseStore(key);
}