import httpClient from "@/http";
import ILinha from "@/interfaces/ILinha";
import { AppState, store } from "@/store";
import { Module } from "vuex";
import { DELETE_LINHA, GET_ALL_LINHAS, POST_LINHA, PUT_LINHA } from "./constants/action-type";
import { LIST_ALL_LINHAS } from "./constants/mutation-type";

export interface LinhaState {
    linhas: ILinha[],
}

export const linha: Module<LinhaState, AppState> = {
    mutations: {
        [LIST_ALL_LINHAS](state, linhas: ILinha[]){
            state.linhas = linhas
        }
    },
    actions: {
        [GET_ALL_LINHAS]({ commit }){
            httpClient
                .get("linhas")
                .then((resp) => commit(LIST_ALL_LINHAS, resp.data));
        },
        [POST_LINHA](ctx, linha: ILinha){
            return httpClient.post("linhas", linha, {
                headers: {
                    'Content-Type': 'application/json',
                },
            });
        },
        [PUT_LINHA](ctx, linha: ILinha){
            return httpClient.put(`/linhas/${linha.id}`,{
                'classificacao': linha.classificacao,
                'status': linha.status,
                'funcionario_id': linha.funcionario.id,
            },{
                headers: {
                    'Content-Type': 'application/json',
                },
            })
            .then(() => {
                const index = store.state.linha.linhas.findIndex(
                    line => line.id == linha.id
                );
                store.state.linha.linhas[index] = linha;
            });
        },
        [DELETE_LINHA](ctx, idLinha: string){
            return httpClient
                    .delete(`/linhas/${idLinha}`)
                    .then(() => {
                        store.state.linha.linhas = store.state.linha.linhas.filter(
                            (line) => line.id != idLinha
                        );
                    });
        }
    }
}