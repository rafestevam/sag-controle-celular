import pandas as pd
from models.centro_custo import CentroCustoModel
import sys

class CentroCustoParser:

    @classmethod
    def parseCSV(cls, file_path):
        try:
            col_names = ['operacao', 'cc_cod', 'cc_nome']
            csv_data = pd.read_csv(file_path, names=col_names, header=None)

            # Iteração sobre o CSV para insersão no Banco de Dados
            for i, row in csv_data.iterrows():
                if i == 0:
                    # Validação das colunas esperadas
                    if( row['operacao'] != 'operacao' or
                        row['cc_cod'] != 'cc_cod' or 
                        row['cc_nome'] != 'cc_nome'):
                        raise RuntimeError("As colunas esperadas para o arquivo são 'operacao', 'cc_cod' e 'cc_nome'")
                else:
                    operacao = str(row['operacao']).strip()
                    cc_cod = str(row['cc_cod']).strip()
                    cc_nome = str(row['cc_nome']).strip()

                    if not operacao or operacao == 'nan':
                        raise RuntimeError(f"Para o Centro de Custo {cc_cod}, é necessário apontar uma operação ('CRIAR', 'ALTERAR', 'DELETAR'")

                    if not (operacao == 'CRIAR' or operacao == 'ALTERAR' or operacao == 'DELETAR'):
                        raise RuntimeError("As operações esperadas são 'CRIAR', 'ALTERAR' ou 'DELETAR'")

                    if(operacao == 'CRIAR'):
                        # Verificação de duplicidade de registros
                        cc = CentroCustoModel.find_by_cc_cod(cc_cod)
                        if cc:
                            raise RuntimeError(f"Centro de Custo {cc_cod} já existente.")

                    if(operacao == 'ALTERAR'):
                        # Verificação de existencia do registro
                        cc = CentroCustoModel.find_by_cc_cod(cc_cod)
                        if not cc:
                            raise RuntimeError(f"Centro de Custo {cc_cod} não existente.")

                    if(opreacao == 'CRIAR' or operacao == 'ALTERAR'):
                        centro_custo = CentroCustoModel(cc_cod, cc_nome)
                        centro_custo.upsert()

                    if(operacao == 'DELETAR'):
                        centro_custo = CentroCustoModel.find_by_cc_cod(cc_cod)
                        if centro_custo:
                            centro_custo.delete()
                        else:
                            raise RuntimeError(f"O Centro de Custo {cc_cod} não existe para deleção")
        except:
            error = error = sys.exc_info()[1]
            raise RuntimeError(error)