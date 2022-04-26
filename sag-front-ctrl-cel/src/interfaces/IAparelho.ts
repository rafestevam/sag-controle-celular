import IFuncionario from "./IFuncionario";
import ILinha from "./ILinha";

export default interface IAparelho {
    id: string,
    imei: string,
    imei_2: string,
    fabricante: string,
    marca: string,
    modelo: string,
    numero_serie: string,
    status: string,
    linha: ILinha,
    funcionario: IFuncionario,
}