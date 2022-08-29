from flask_restful import Resource, reqparse
from models.funcionario import FuncionarioModel

class FuncionarioResource(Resource):
    data_parser = reqparse.RequestParser()
    data_parser.add_argument("nome",
        type=str,
        required=False,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("sobrenome",
        type=str,
        required=False,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("nome_social",
        type=str,
        required=False,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("admissao",
        type=str,
        required=False,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("data_nascimento",
        type=str,
        required=False,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("cargo",
        type=str,
        required=False,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("rg",
        type=str,
        required=False,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("cpf",
        type=str,
        required=False,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("centro_custo_id",
        type=str,
        required=False,
        help="Um funcionário deve pertencer a um centro de custo"
    )
    # data_parser.add_argument("linhas",
    #     type=str,
    #     action='append'
    # )
    # data_parser.add_argument("aparelhos",
    #     type=str,
    #     action='append'
    # )
    
    def get(self, id):
        try:
            funcionario = FuncionarioModel.find_by_id(id)
            if not funcionario:
                return {"message": "Funcionario não encontrado"}, 400
            return funcionario.to_json()
        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500

    def put(self, id):
        try:
            data = FuncionarioResource.data_parser.parse_args()
            funcionario = FuncionarioModel.find_by_id(id)
            if not funcionario:
                return {"message": "Funcionario não encontrado"}, 400
            
            funcionario.nome = data["nome"]
            funcionario.sobrenome = data["sobrenome"]
            funcionario.nome_social = data["nome_social"]
            funcionario.admissao = data["admissao"]
            funcionario.data_nascimento = data["data_nascimento"]
            funcionario.cargo = data["cargo"]
            funcionario.rg = data["rg"]
            funcionario.cpf = data["cpf"]
            funcionario.centros_custo_id = data["centro_custo_id"]
            # funcionario.linhas = data["linhas"]
            # funcionario.aparelhos = data["aparelhos"]
            funcionario.upsert()
            return funcionario.to_json()
        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500

    def delete(self, id):
        try:
            funcionario = FuncionarioModel.find_by_id(id)
            if not funcionario:
                return {"message": "Funcionario não encontrado"}, 400
            funcionario.delete()
            return {"message": "Funcionário excluído com sucesso"}, 200
        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500


class FuncionarioListResource(Resource):
    data_parser = reqparse.RequestParser()
    data_parser.add_argument("nome",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("sobrenome",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("nome_social",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("admissao",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("data_nascimento",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("cargo",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("rg",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("cpf",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("centro_custo_id",
        type=str,
        required=True,
        help="Um funcionário deve pertencer a um centro de custo"
    )
    data_parser.add_argument("linhas",
        type=list
    )
    data_parser.add_argument("aparelhos",
        type=list
    )

    def post(self):
        try:
            data = FuncionarioListResource.data_parser.parse_args()
            cpf = data["cpf"]
            funcionario = FuncionarioModel.find_by_cpf(cpf)
            if funcionario:
                return {"message": f"Funcionario com o CPF {cpf} já existente"}
            
            data["linhas"] = []
            data["aparelhos"] = []

            funcionario = FuncionarioModel(**data)
            funcionario.upsert()
            return funcionario.to_json(), 201
        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500

    def get(self):
        try:
            funcionarios = FuncionarioModel.get_all()
            if funcionarios:
                return {"funcionarios": funcionarios}, 200
            return {"message": "Não há funcionários cadastrados na base"}, 400
        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500