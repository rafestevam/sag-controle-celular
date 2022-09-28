import IUsuarioLogado, { IMyToken, IUsuario } from "@/interfaces/IUsuario";
import { AppState } from "@/store";
import { Module } from "vuex";
import { LOGIN_FAILURE, LOGIN_SUCCESS, LOGOUT } from "./constants/mutation-type";
import jwt_decode from 'jwt-decode';
import { USER_LOGIN, USER_LOGOUT } from "./constants/action-type";
import httpClient from "@/http";

export default interface UserState {
    user: IUsuarioLogado,
}

export const usuario: Module<UserState, AppState> = {
    mutations: {
        [LOGIN_SUCCESS](state, token: string){
            const decodedToken = jwt_decode<IMyToken>(token);
            const user = {} as IUsuarioLogado;
            user.name = decodedToken.name;
            user.email = decodedToken.username;
            user.accessToken = token;
            user.loggedIn = true;
            state.user = user;
            // localStorage.setItem('user', JSON.stringify(user));
            // localStorage.setItem('jwt', token);
        },
        [LOGIN_FAILURE](state){
            // const user = {} as IUsuarioLogado;
            // user.name = '';
            // user.email = '';
            // user.accessToken = '';
            // user.loggedIn = false;
            state.user = {} as IUsuarioLogado;
            // localStorage.removeItem('user');
            // localStorage.removeItem('jwt');
        },
        [LOGOUT](state){
            // const user = {} as IUsuarioLogado;
            // user.name = '';
            // user.email = '';
            // user.accessToken = '';
            // user.loggedIn = false;
            state.user = {} as IUsuarioLogado;
            // localStorage.removeItem('user');
            // localStorage.removeItem('jwt');
        }
    },

    actions: {
        [USER_LOGIN](ctx, usuario: IUsuario){
            return httpClient.post("login",
                {
                    'username': usuario.username,
                    'password': usuario.password,
                },{
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                .then((resp) => {
                    localStorage.setItem('jwt', resp.data.access_token);
                    ctx.commit(LOGIN_SUCCESS, resp.data.access_token);
                })
                // .catch((err) => ctx.commit(LOGIN_FAILURE, err));
        },
        [USER_LOGOUT](ctx){
            return httpClient.post("logout")
                .then(() => {
                    localStorage.removeItem('jwt');
                    ctx.commit(LOGOUT);
                });
        }
    }

}