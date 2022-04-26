import INotification from "@/interfaces/INotification";
import { AppState } from "@/store";
import { Module } from "vuex";
import { NOTIFY } from "./constants/mutation-type";

export interface NotificationState {
    notifications: INotification[],
}

export const notif: Module<NotificationState, AppState> = {
    mutations: {
        [NOTIFY](state, newNotification: INotification){
            newNotification.id = new Date().toISOString();
            state.notifications.push(newNotification);
            setTimeout(() => {
                state.notifications = state.notifications
                    .filter(notif => notif.id != newNotification.id);
            }, 2000);
        }
    }
}