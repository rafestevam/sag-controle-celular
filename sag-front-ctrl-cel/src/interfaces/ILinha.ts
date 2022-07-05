import IFuncionario from "./IFuncionario";

export enum LinhaStatus {
    EM_USO = 'Em Uso',
    DISPONIVEL = 'Disponível',
}
export default interface ILinha {
    id: string,
    ddd: string,
    numero: string,
    classificacao: string,
    status: string,
    funcionario: IFuncionario,
}