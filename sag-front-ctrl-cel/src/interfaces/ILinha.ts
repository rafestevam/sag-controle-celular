import IAparelho from "./IAparelho";
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
    funcionario_id: string,
    funcionarioVinculado: IFuncionario,
    aparelho_id: string,
    aparelhoVinculado: IAparelho,
    last_funcionario_id: string,
    lastFuncionario: IFuncionario,
}