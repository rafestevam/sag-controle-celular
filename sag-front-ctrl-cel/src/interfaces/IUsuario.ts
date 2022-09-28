export default interface IUsuarioLogado {
    name: string,
    email: string,
    accessToken: string,
    loggedIn: boolean,
}

export interface IMyToken {
    iat: number,
    jti: string,
    type: string,
    sub: string,
    nbf: string,
    exp: string,
    name: string,
    username: string,
}

export interface IUsuario {
    username: string,
    password: string,
}