import pandas as pd
from models.linha import LinhaModel
import sys

class LinhaParser:

    @classmethod
    def parseCSV(cls, file_path):
        try:
            col_names = [
                'ddd',
                'numero',
                'classificacao',
                'status',
                'aparelho_id'
            ]
            csv_data = pd.read_csv(file_path, names=col_names, header=None)

            # Iteração sobre o CSV para insersão no Banco de Dados
            for i, row in csv_data.iterrows():
                if i == 0:
                    # Validação das colunas esperadas
                    if(row['ddd'] != 'ddd' or
                       row['numero'] != 'numero' or
                       row['classificacao'] != 'classificacao' or
                       row['status'] != 'status' or
                       row['aparelho_id'] != 'aparelho_id'):
                        raise RuntimeError("As colunas esperadas para o arquivo são 'ddd', 'numero', 'classificacao', 'status' e 'aparelho_id'")
                else:
                    ddd = str(row['ddd']).strip()
                    numero = str(row['numero']).strip()
                    classificacao = str(row['classificacao']).strip()
                    status = str(row['status']).strip()
                    aparelho_id = str(row['aparelho_id']).strip()

                    ln = LinhaModel.find_by_numero(numero)
                    if ln:
                        raise RuntimeError(f"Linha {numero} já existente")

                    if(status == 'em uso' and not aparelho_id):
                        raise RuntimeError(f"Para a linha {numero} com status 'em uso', a linha deve estar atribuída a um aparelho")

                    linha = LinhaModel(
                        ddd,
                        numero,
                        classificacao,
                        status,
                        aparelho_id
                    )
                    linha.upsert()
        except:
            error = error = sys.exc_info()[1]
            raise RuntimeError(error)                    
