import httpClient from "@/http";
import IAparelho from "@/interfaces/IAparelho";
import { AppState } from "@/store";
import { Module } from "vuex";
import { GET_ALL_APARELHOS } from "./constants/action-type";
import { LIST_ALL_APARELHOS } from "./constants/mutation-type";

export interface AparelhoState {
    aparelhos: IAparelho[],
}

export const aparelho: Module<AparelhoState, AppState> = {
    mutations: {
        [LIST_ALL_APARELHOS](state, aparelhos: IAparelho[]){
            state.aparelhos = aparelhos;
        }
    },
    actions: {
        [GET_ALL_APARELHOS]({ commit }){
            httpClient.get("aparelhos")
                .then(resp => commit(LIST_ALL_APARELHOS, resp.data));
        }
    }
}