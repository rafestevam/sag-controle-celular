import IAparelho from "./IAparelho";
import ICentroCusto from "./ICentroCusto";

export default interface IFuncionario {
    id: string,
    nome: string,
    nome_social: string,
    admissao: string,
    data_nascimento: string,
    cargo: string,
    rg: string,
    cpf: string,
    centro_custo: ICentroCusto,
    aparelho: IAparelho,
}