import httpClient from "@/http";
import ICentroCusto from "@/interfaces/ICentroCusto";
import IFuncionario from "@/interfaces/IFuncionario";
import { AppState, store } from "@/store";
import { Module } from "vuex";
import {
  DELETE_FUNC,
  GET_ALL_FUNC,
  POST_FUNC,
  PUT_FUNC,
  TEST_API,
} from "./constants/action-type";
import { ADD_CC_2_FUNC, LIST_ALL_FUNC } from "./constants/mutation-type";

export interface FuncionarioState {
  funcionarios: IFuncionario[];
}

export const funcionario: Module<FuncionarioState, AppState> = {
  mutations: {
    [LIST_ALL_FUNC](state, funcionarios: IFuncionario[]) {
      state.funcionarios = funcionarios;
    },
    [ADD_CC_2_FUNC](state, ccs: ICentroCusto[]) {
      state.funcionarios.forEach((func: IFuncionario) => {
        const idx = ccs.findIndex((cc) => cc.id == func.centro_custo_id);
        func.centro_custo = ccs[idx];
      });
    },
  },

  actions: {
    [GET_ALL_FUNC](ctx) {
      httpClient.get("funcionarios").then((resp) => {
        ctx.commit(LIST_ALL_FUNC, resp.data.funcionarios);
        httpClient.get("cc").then((resp) => {
          ctx.commit(ADD_CC_2_FUNC, resp.data);
        });
      });
    },
    [POST_FUNC](ctx, funcionario: IFuncionario) {
      return httpClient.post("/funcionarios", funcionario, {
        headers: {
          "Content-Type": "application/json",
        },
      });
    },
    [PUT_FUNC](ctx, funcionario: IFuncionario) {
      return httpClient
        .put(
          `/funcionarios/${funcionario.id}`,
          {
            "nome": funcionario.nome,
            "sobrenome": funcionario.sobrenome,
            "nome_social": funcionario.nome_social,
            "admissao": funcionario.admissao,
            "data_nascimento": funcionario.data_nascimento,
            "cargo": funcionario.cargo,
            "rg": funcionario.rg,
            "cpf": funcionario.cpf,
            "centro_custo_id": funcionario.centro_custo_id,
          },
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        )
        .then(() => {
          const index = store.state.funcionario.funcionarios.findIndex(
            (func) => func.id == funcionario.id
          );
          store.state.funcionario.funcionarios[index] = funcionario;
        });
    },
    [DELETE_FUNC](ctx, idFuncionario: string) {
      return httpClient.delete(`/funcionarios/${idFuncionario}`).then(() => {
        store.state.funcionario.funcionarios.filter(
          (func) => func.id != idFuncionario
        );
      });
    },
    [TEST_API](ctx){
      return httpClient.get('/hello').then(() => {
        console.log('Teste de API realizado com sucesso!');
      });
    }
  },
};
