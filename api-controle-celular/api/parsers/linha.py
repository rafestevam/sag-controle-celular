import pandas as pd
from models.linha import LinhaModel
from models.aparelho import AparelhoModel
from models.funcionario import FuncionarioModel
import sys

class LinhaParser:

    @classmethod
    def parseCSV(cls, file_path):
        try:
            col_names = [
                'operacao',
                'ddd',
                'numero',
                'classificacao',
                'status',
                'aparelho_imei'
            ]
            csv_data = pd.read_csv(file_path, names=col_names, header=None)

            # Iteração sobre o CSV para insersão no Banco de Dados
            for i, row in csv_data.iterrows():
                if i == 0:
                    # Validação das colunas esperadas
                    if(row['operacao'] != 'operacao' or
                       row['ddd'] != 'ddd' or
                       row['numero'] != 'numero' or
                       row['classificacao'] != 'classificacao' or
                       row['status'] != 'status' or
                       row['funcionario_cpf'] != 'funcionario_cpf' or
                       row['aparelho_imei'] != 'aparelho_imei'):
                        raise RuntimeError("As colunas esperadas para o arquivo são 'ddd', 'numero', 'classificacao', 'status', 'funcionario_cpf' e 'aparelho_imei'")
                else:
                    operacao = str(row['operacao']).strip()
                    ddd = str(row['ddd']).strip()
                    numero = str(row['numero']).strip()
                    classificacao = str(row['classificacao']).strip()
                    status = str(row['status']).strip()
                    funcionario_cpf = str(row['funcionario_cpf']).strip()
                    aparelho_imei = str(row['aparelho_imei']).strip()
                    
                    aparelho_id = ''
                    funcionario_id = ''
                    if not operacao or operacao == 'nan':
                        raise RuntimeError(f"Para a Linha com número {numero}, é necessário apontar uma operação ('CRIAR', 'ALTERAR', 'DELETAR'")

                    if not (operacao == 'CRIAR' or operacao == 'ALTERAR' or operacao == 'DELETAR'):
                        raise RuntimeError("As operações esperadas são 'CRIAR', 'ALTERAR' ou 'DELETAR'")

                    if(status != 'em uso' and aparelho_imei):
                        status = 'em uso'

                    if(operacao == 'CRIAR'):
                        ln = LinhaModel.find_by_numero(numero)
                        if ln:
                            raise RuntimeError(f"Linha {numero} já existente")

                        if(status == 'em uso' and not (aparelho_imei or funcionario_cpf)):
                            raise RuntimeError(f"Para a linha {numero} com status 'em uso', a linha deve estar atribuída a um aparelho ou a um funcionário")

                        aparelho = AparelhoModel.find_by_imei(aparelho_imei)
                        if aparelho:
                            aparelho_id = aparelho.id

                        func = FuncionarioModel.find_by_cpf(funcionario_cpf)
                        if funcionario:
                            funcionario_id = func.id
                    
                    if(operacao == 'ALTERAR'):
                        ln = LinhaModel.find_by_numero(numero)
                        if not ln:
                            raise RuntimeError(f"Linha {numero} não existente")

                        if(status == 'em uso' and not (aparelho_imei or funcionario_cpf)):
                            raise RuntimeError(f"Para a linha {numero} com status 'em uso', a linha deve estar atribuída a um aparelho ou a um funcionario")
                    
                        if(aparelho_imei and aparelho_imei != 'nan'):
                            aparelho = AparelhoModel.find_by_imei(aparelho_imei)
                            if aparelho:
                                aparelho_id = aparelho.id

                        if(funcionario_cpf and funcionario_cpf != 'nan'):
                            func = FuncionarioModel.find_by_cpf(funcionario_cpf)
                            if func:
                                funcionario_id = func.id

                    if(operacao == 'CRIAR' or operacao == 'ALTERAR'):
                        linha = LinhaModel(
                            ddd,
                            numero,
                            classificacao,
                            status,
                            funcionario_id,
                            aparelho_id
                        )
                        linha.upsert()

                    if(operacao == 'DELETAR'):
                        line = LinhaModel.find_by_numero(numero)
                        if line:
                            line.delete()
                        else:
                            raise RuntimeError(f"A linha de numero {numero} não existe para deleção")
        except:
            error = error = sys.exc_info()[1]
            raise RuntimeError(error)                    
