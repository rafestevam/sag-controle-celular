import pandas as pd
from models.centro_custo import CentroCustoModel
import sys

class CentroCustoParser:

    @classmethod
    def parseCSV(cls, file_path):
        try:
            col_names = ['cc_cod', 'cc_nome']
            csvData = pd.read_csv(file_path, names=col_names, header=None)

            # Iteração sobre o CSV para insersão no Banco de Dados
            for i, row in csvData.iterrows():
                if i == 0:
                    # Validação das colunas esperadas
                    if(row['cc_cod'] != 'cc_cod' or row['cc_nome'] != 'cc_nome'):
                        raise RuntimeError("As colunas esperadas para o arquivo são 'cc_cod' e 'cc_nome'")
                else:
                    cc_cod = str(row['cc_cod'])
                    cc_nome = str(row['cc_nome'])
                    
                    # Verificação de duplicidade de registros
                    cc = CentroCustoModel.find_by_cc_cod(cc_cod)
                    if cc:
                        raise RuntimeError(f"Centro de Custo {cc_cod} já existente.")

                    centro_custo = CentroCustoModel(cc_cod.strip(), cc_nome.strip())
                    centro_custo.upsert()
        except:
            error = error = sys.exc_info()[1]
            raise RuntimeError(error)