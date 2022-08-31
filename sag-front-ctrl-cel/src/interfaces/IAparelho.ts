import ILinha from "./ILinha";

export enum AparelhoStatus {
    EM_USO = 'Em Uso',
    DISPONIVEL = 'Disponível',
}
export default interface IAparelho {
    id: string,
    imei: string,
    imei_2: string,
    fabricante: string,
    marca: string,
    modelo: string,
    numero_serie: string,
    acessorios: string,
    status: string,
    funcionario_id: string,
    linha: ILinha,
}