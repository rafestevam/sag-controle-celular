import pandas as pd
from models.aparelho import AparelhoModel
from models.funcionario import FuncionarioModel
import sys

class AparelhoParser:

    @classmethod
    def parseCSV(cls, file_path):
        try:
            col_names = [
                'operacao',
                'imei', 
                'imei_2', 
                'fabricante', 
                'marca', 
                'modelo', 
                'numero_serie',
                'acessorios',
                'status', 
                'funcionario_cpf'
            ]
            csv_data = pd.read_csv(file_path, names=col_names, header=None)

            # Iteração sobre o CSV para insersão no Banco de Dados
            for i, row in csv_data.iterrows():
                if i == 0:
                    # Validação das colunas esperadas
                    if(row['operacao'] != 'operacao' or
                       row['imei'] != 'imei' or
                       row['imei_2'] != 'imei_2' or
                       row['fabricante'] != 'fabricante' or
                       row['marca'] != 'marca' or
                       row['modelo'] != 'modelo' or
                       row['numero_serie'] != 'numero_serie' or
                       row['acessorios'] != 'acessorios' or
                       row['status'] != 'status' or
                       row['funcionario_cpf'] != 'funcionario_cpf'):
                        raise RuntimeError("As colunas esperadas para o arquivo são 'operacao', 'imei', 'imei_2', 'fabricante', 'marca', 'modelo', 'numero_serie', 'acessorios', 'status' e 'funcionario_cpf'")
                else:
                    operacao = str(row['operacao']).strip()
                    imei = str(row['imei']).strip()
                    imei_2 = str(row['imei_2']).strip()
                    fabricante = str(row['fabricante']).strip()
                    marca = str(row['marca']).strip()
                    modelo = str(row['modelo']).strip()
                    numero_serie = str(row['numero_serie']).strip()
                    acessorios = str(row['acessorios']).strip()
                    status = str(row['status']).strip()
                    funcionario_cpf = str(row['funcionario_cpf']).strip()
                    funcionario_id = ''

                    if not operacao or operacao == 'nan':
                        raise RuntimeError(f"Para o Aparelho com o IMEI {imei}, é necessário apontar uma operação ('CRIAR', 'ALTERAR', 'DELETAR'")

                    if not (operacao == 'CRIAR' or operacao == 'ALTERAR' or operacao == 'DELETAR'):
                        raise RuntimeError("As operações esperadas são 'CRIAR', 'ALTERAR' ou 'DELETAR'")

                    if status == 'em uso' and not funcionario_cpf:
                        raise RuntimeError(f"Para o Aparelho com IMEI {imei}, com status 'Em Uso', o aparelho deve estar atribuído a um funcionário")
                        
                    if status != 'em uso' and funcionario_cpf != 'nan' and funcionario_cpf:
                        status = 'em uso'

                    if (funcionario_cpf != 'nan' and funcionario_cpf):
                        funcionario = FuncionarioModel.find_by_cpf(funcionario_cpf)
                        if funcionario:
                            funcionario_id = funcionario.id
                    
                    if (operacao == 'CRIAR'):
                        # Validação de duplicidade de registros
                        apar = AparelhoModel.find_by_imei(imei)
                        if apar:
                            raise RuntimeError(f"Aparelho com IMEI {imei} já cadastrado")
                        aparelho = AparelhoModel(
                            imei,
                            imei_2,
                            fabricante,
                            marca,
                            modelo,
                            numero_serie,
                            acessorios,
                            status,
                            funcionario_id
                        )
                        aparelho.upsert()

                    if (operacao == 'ALTERAR'):
                        # Verificação da existencia do registro
                        apar = AparelhoModel.find_by_imei(imei)
                        if not apar:
                            raise RuntimeError(f"Aparelho com IMEI {imei} não existente")
                        apar.imei = imei
                        apar.imei_2 = imei_2
                        apar.fabricante = fabricante
                        apar.marca = marca
                        apar.modelo = modelo
                        apar.numero_serie = numero_serie
                        apar.acessorios = acessorios
                        apar.status = status
                        apar.funcionario_id = funcionario_id
                        apar.upsert()

                    if (operacao == 'DELETAR'):
                        aparelho = AparelhoModel.find_by_imei(imei)
                        if aparelho:
                            aparelho.delete()
                        else:
                            raise RuntimeError(f"O Aparelho com o IMEI {imei} não existe para deleção")
        except:
            error = error = sys.exc_info()[1]
            raise RuntimeError(error)
