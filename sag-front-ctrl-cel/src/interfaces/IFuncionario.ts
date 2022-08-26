import IAparelho from "./IAparelho";
import ICentroCusto from "./ICentroCusto";
import ILinha from "./ILinha";

export default interface IFuncionario {
    id: string,
    nome: string,
    sobrenome: string,
    nome_social: string,
    admissao: string,
    data_nascimento: string,
    cargo: string,
    rg: string,
    cpf: string,
    centro_custo_id: string,
    centro_custo: ICentroCusto,
    aparelhos: IAparelho[],
    linhas: ILinha[],
}