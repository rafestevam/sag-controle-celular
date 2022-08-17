import pandas as pd
from models.funcionario import FuncionarioModel
from models.centro_custo import CentroCustoModel
import sys, re

class FuncionarioParser:

    @classmethod
    def parseCSV(cls, file_path):
        try:
            col_names = [
                'nome',
                'sobrenome',
                'nome_social',
                'admissao',
                'data_nascimento',
                'cargo',
                'rg',
                'cpf',
                'centro_custo_cod'
            ]
            csv_data = pd.read_csv(file_path, names=col_names, header=None)
            rex = re.compile("\\d{4}-\\d{2}-\\d{2}")

            # Iteração sobre o CSV para insersão no Banco de Dados
            for i, row in csv_data.iterrows():
                if i == 0:
                    # Validação das colunas esperadas
                    if(row['nome'] != 'nome' or
                       row['sobrenome'] != 'sobrenome' or
                       row['nome_social'] != 'nome_social' or
                       row['admissao'] != 'admissao' or
                       row['data_nascimento'] != 'data_nascimento' or
                       row['cargo'] != 'cargo' or
                       row['rg'] != 'rg' or
                       row['cpf'] != 'cpf' or
                       row['centro_custo_cod'] != 'centro_custo_cod'):
                        raise RuntimeError("As colunas esperadas para o arquivo são 'nome', 'sobrenome', 'nome_social', 'admissao', 'data_nascimento', 'cargo', 'rg', 'cpf' e 'centro_custo_cod'")
                else:
                    nome = str(row['nome']).strip()
                    sobrenome = str(row['sobrenome']).strip()
                    nome_social = str(row['nome_social']).strip()
                    admissao = str(row['admissao']).strip()
                    data_nascimento = str(row['data_nascimento']).strip()
                    cargo = str(row['cargo']).strip()
                    rg = str(row['rg']).strip()
                    cpf = str(row['cpf']).strip()
                    centro_custo_cod = str(row['centro_custo_cod']).strip()

                    if not rex.match(admissao):
                        raise RuntimeError(f"Funcionario com o CPF {cpf} - Campo 'admissao' deve estar no formato YYYY-MM-DD")
                    
                    if not rex.match(data_nascimento):
                        raise RuntimeError(f"Funcionario com o CPF {cpf} - Campo 'data_nascimento' deve estar no formato YYYY-MM-DD")

                    employee = FuncionarioModel.find_by_cpf(cpf)
                    if employee:
                        raise RuntimeError(f"Funcionario com o CPF {cpf} já existente")

                    if not centro_custo_cod:
                        raise RuntimeError(f"Funcionario com o CPF {cpf} deve pertencer a um centro de custo")

                    centros_custo_id = ''
                    cc = CentroCustoModel.find_by_cc_cod(centro_custo_cod)
                    if cc:
                        centros_custo_id = cc.id

                    funcionario = FuncionarioModel(
                        nome,
                        sobrenome,
                        nome_social,
                        admissao,
                        data_nascimento,
                        cargo,
                        rg,
                        cpf,
                        centros_custo_id
                    )
                    funcionario.upsert()
        except:
            error = error = sys.exc_info()[1]
            raise RuntimeError(error)