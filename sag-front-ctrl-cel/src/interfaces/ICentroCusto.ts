import IFuncionario from "./IFuncionario";

export default interface ICentroCusto {
    id: string,
    cc_cod: string,
    cc_nome: string,
    funcionarios: IFuncionario[],
}