import ICentroCusto from "@/interfaces/ICentroCusto";
import { Module } from "vuex";
import { AppState, store } from "@/store";
import { DELETE_CC, GET_ALL_CC, GET_CC, POST_BULK_CC, POST_CC, PUT_CC } from "./constants/action-type";
import { LIST_ALL_CC, LIST_ONE_CC } from "./constants/mutation-type";
import http from "@/http";

export interface CentroCustoState {
  ccs: ICentroCusto[];
}

export const centrocusto: Module<CentroCustoState, AppState> = {
  mutations: {
    [LIST_ALL_CC](state, ccs: ICentroCusto[]) {
      state.ccs = ccs;
    },
  },
  actions: {
    [GET_ALL_CC]({ commit }) {
      http.get("cc").then((resp) => commit(LIST_ALL_CC, resp.data));
    },
    [POST_CC](ctx, centrocusto: ICentroCusto) {
      return http.post("/cc", centrocusto, {
        headers: {
          "Content-Type": "application/json",
        },
      });
    },
    [PUT_CC](ctx, centrocusto: ICentroCusto) {
      return http
        .put(`/cc/${centrocusto.id}`, centrocusto, {
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then(() => {
          const index = store.state.centrocusto.ccs.findIndex(
            (cc) => cc.id == centrocusto.id
          );
          store.state.centrocusto.ccs[index] = centrocusto;
        });
    },
    [DELETE_CC](ctx, idCentroCusto: string) {
        return http
            .delete(`/cc/${idCentroCusto}`)
            .then(() => {
                store.state.centrocusto.ccs = store.state.centrocusto.ccs
                    .filter(cc => cc.id != idCentroCusto);
            });
    },
    [GET_CC](ctx, idCentroCusto: string) {
      return http
        .get(`/cc/${idCentroCusto}`)
        .then((resp) => {
          const ccs = ctx.state.ccs;
          ccs.push(resp.data);
          ctx.commit(LIST_ONE_CC, resp.data)}
        );
    },
    [POST_BULK_CC](ctx, file){
      return http
        .post('/bulk/cc', file, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
    }
  },
};
