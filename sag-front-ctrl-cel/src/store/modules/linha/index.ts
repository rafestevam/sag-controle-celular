import httpClient from "@/http";
import IAparelho from "@/interfaces/IAparelho";
import IFuncionario from "@/interfaces/IFuncionario";
import ILinha from "@/interfaces/ILinha";
import { AppState, store } from "@/store";
import { Module } from "vuex";
import { DELETE_LINHA, GET_ALL_LINHAS, POST_BULK_LINHAS, POST_LINHA, PUT_LINHA } from "./constants/action-type";
import { ADD_DEVICE_2_LINHAS, ADD_FUNC_2_LINHAS, ADD_LASTFUNC_2_LINHAS, LIST_ALL_LINHAS } from "./constants/mutation-type";

export interface LinhaState {
    linhas: ILinha[],
}

export const linha: Module<LinhaState, AppState> = {
    mutations: {
        [LIST_ALL_LINHAS](state, linhas: ILinha[]){
            state.linhas = linhas;
        },
        [ADD_LASTFUNC_2_LINHAS](state, lastFuncs: IFuncionario[]){
            state.linhas.forEach((line: ILinha) => {
                const idx = lastFuncs.findIndex((empl) => empl.id == line.last_funcionario_id);
                if(lastFuncs[idx] != undefined){
                    line.lastFuncionario = lastFuncs[idx];
                } else{
                    line.lastFuncionario = {} as IFuncionario;
                }
            });
        },
        [ADD_FUNC_2_LINHAS](state, funcionarios: IFuncionario[]){
            state.linhas.forEach((line: ILinha) => {
                const idx = funcionarios.findIndex((empl) => empl.id == line.funcionario_id);
                if(funcionarios[idx] != undefined){
                    line.funcionarioVinculado = funcionarios[idx];
                } else{
                    line.funcionarioVinculado = {} as IFuncionario;
                }
            });
        },
        [ADD_DEVICE_2_LINHAS](state, aparelhos: IAparelho[]){
            state.linhas.forEach((line: ILinha) => {
                const idx = aparelhos.findIndex((empl) => empl.id == line.aparelho_id);
                if(aparelhos[idx] != undefined){
                    line.aparelhoVinculado = aparelhos[idx];
                } else{
                    line.aparelhoVinculado = {} as IAparelho;
                }
            });
        }
    },
    actions: {
        [GET_ALL_LINHAS]({ commit }){
            httpClient
                .get("linhas")
                .then((resp) => {
                    commit(LIST_ALL_LINHAS, resp.data);
                    httpClient
                        .get("funcionarios")
                        .then((resp) => {
                            commit(ADD_LASTFUNC_2_LINHAS, resp.data.funcionarios);
                            commit(ADD_FUNC_2_LINHAS, resp.data.funcionarios);
                        });
                    httpClient
                        .get("aparelhos")
                        .then((resp) => commit(ADD_DEVICE_2_LINHAS, resp.data));
                });
                // .then((resp) => commit(LIST_ALL_LINHAS, resp.data));
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
                'funcionario_id': linha.funcionario_id,
                'aparelho_id': linha.aparelho_id,
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
        },
        [POST_BULK_LINHAS](ctx, file){
            return httpClient
              .post('/bulk/linhas', file, {
                headers: {
                  'Content-Type': 'multipart/form-data'
                }
              });
          }
    }
}