import pandas as pd
from models.aparelho import AparelhoModel
import sys

class AparelhoParser:

    @classmethod
    def parseCSV(cls, file_path):
        try:
            col_names = [
                'imei', 
                'imei_2', 
                'fabricante', 
                'marca', 
                'modelo', 
                'numero_serie', 
                'status', 
                'funcionario_id'
            ]
            csvData = pd.read_csv(file_path, names=col_names, header=None)

            # Iteração sobre o CSV para insersão no Banco de Dados
            for i, row in csvData.iterrows():
                if i == 0:
                    # Validação das colunas esperadas
                    if(row['imei'] != 'imei' or
                       row['imei_2'] != 'imei_2' or
                       row['fabricante'] != 'fabricante' or
                       row['marca'] != 'marca' or
                       row['modelo'] != 'modelo' or
                       row['numero_serie'] != 'numero_serie' or
                       row['status'] != 'status' or
                       row['funcionario_id'] != 'funcionario_id'):
                        raise RuntimeError("As colunas esperadas para o arquivo são 'imei', 'imei_2', 'fabricante', 'marca', 'modelo', 'numero_serie', 'status' e 'funcionario_id'")
                else:
                    imei = str(row['imei']).strip()
                    imei_2 = str(row['imei_2']).strip()
                    fabricante = str(row['fabricante']).strip()
                    marca = str(row['marca']).strip()
                    modelo = str(row['modelo']).strip()
                    numero_serie = str(row['numero_serie']).strip()
                    status = str(row['status']).strip()
                    funcionario_id = str(row['funcionario_id']).strip()

                    # Validação de duplicidade de registros
                    apar = AparelhoModel.find_by_imei(imei)
                    if apar:
                        raise RuntimeError(f"Aparelho com IMEI {imei} já cadastrado")

                    # Validação de status e vinculação com funcionario
                    if status == 'em uso' and not funcionario_id:
                        raise RuntimeError(f"Para o Aparelho com IMEI {imei}, com status 'Em Uso', o aparelho deve estar atribuído a um funcionário")

                    aparelho = AparelhoModel(
                        imei,
                        imei_2,
                        fabricante,
                        marca,
                        modelo,
                        numero_serie,
                        status,
                        funcionario_id
                    )
                    aparelho.upsert()
        except:
            error = error = sys.exc_info()[1]
            raise RuntimeError(error)
