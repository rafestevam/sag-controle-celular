import httpClient from "@/http";
import IAparelho from "@/interfaces/IAparelho";
import { AppState, store } from "@/store";
import { Module } from "vuex";
import {
  DELETE_APARELHO,
  GET_ALL_APARELHOS,
  POST_APARELHO,
  PUT_APARELHO,
} from "./constants/action-type";
import { LIST_ALL_APARELHOS } from "./constants/mutation-type";

export interface AparelhoState {
  aparelhos: IAparelho[];
}

export const aparelho: Module<AparelhoState, AppState> = {
  mutations: {
    [LIST_ALL_APARELHOS](state, aparelhos: IAparelho[]) {
      state.aparelhos = aparelhos;
    },
  },
  actions: {
    [GET_ALL_APARELHOS]({ commit }) {
      httpClient
        .get("aparelhos")
        .then((resp) => commit(LIST_ALL_APARELHOS, resp.data));
    },
    [POST_APARELHO](ctx, aparelho: IAparelho) {
      return httpClient.post("aparelhos", aparelho, {
        headers: {
          "Content-Type": "application/json",
        },
      });
    },
    [PUT_APARELHO](ctx, aparelho: IAparelho) {
      return httpClient
        .put(`/aparelhos/${aparelho.id}`, aparelho, {
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then(() => {
          const index = store.state.aparelho.aparelhos.findIndex(
            (device) => device.id == aparelho.id
          );
          store.state.aparelho.aparelhos[index] = aparelho;
        });
    },
    [DELETE_APARELHO](ctx, idAparelho: string) {
      return httpClient.delete(`/aparelhos/${idAparelho}`).then(() => {
        store.state.aparelho.aparelhos = store.state.aparelho.aparelhos.filter(
          (device) => device.id != idAparelho
        );
      });
    },
  },
};
