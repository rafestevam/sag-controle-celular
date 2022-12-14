from typing_extensions import Required
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from flask_cors import cross_origin
from models.linha import LinhaModel

class LinhaResource(Resource):
    data_parser = reqparse.RequestParser()
    data_parser.add_argument("classificacao",
        type=str,
        required=False,
        # help="Este campo não pode estar vazio"
    )
    data_parser.add_argument("status",
        type=str,
        required=True,
        help="Este campo não pode estar vazio"
    )
    data_parser.add_argument("funcionario_id",
        type=str,
        required=False,
        # help="Este campo não pode estar vazio"
    )
    data_parser.add_argument("aparelho_id",
        type=str
    )

    @jwt_required()
    def get(self, id):
        try:
            linha = LinhaModel.find_by_id(id)
            if not linha:
                return {"message": "Linha não encontrada"}, 400
            return linha.to_json(), 200
        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500

    @jwt_required()
    def put(self, id):
        try:
            data = LinhaResource.data_parser.parse_args()
            linha = LinhaModel.find_by_id(id)
            if not linha:
                return {"message": "Linha não encontrada"}, 400

            linha.last_funcionario_id = linha.funcionario_id
            linha.classificacao = data["classificacao"]
            linha.status = data["status"]
            linha.funcionario_id = data["funcionario_id"]

            if (data["aparelho_id"] != '' and linha.aparelho_id != data["aparelho_id"]):
                linha_vinc = LinhaModel.find_by_aparelho(data["aparelho_id"])
                if linha_vinc:
                    return {"message": "Esta linha já está vinculada a um aparelho"}, 400

            linha.aparelho_id = data["aparelho_id"]

            if(linha.status == "em uso" and not linha.aparelho_id):
                return {"message": "Para status 'Em Uso', a linha deve estar atribuída a um aparelho"}, 400

            if(linha.aparelho_id and linha.funcionario_id):
                return {"message": "A linha não pode estar atribuída a um aparelho e a um funcionário ao mesmo tempo"}, 400

            linha.upsert()
            return linha.to_json(), 200
        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500
    
    @jwt_required()
    def delete(self, id):
        try:
            linha = LinhaModel.find_by_id(id)
            if not linha:
                return {"message": "Linha não encontrada"}, 400
            if linha.funcionario_id:
                return {"message": "Linha está atribuída a um funcionário"}, 400
            if linha.aparelho_id:
                return {"message": "Linha está atribuída a um aparelho"}, 400
            linha.delete()
            return {"message": "Linha excluída com sucesso"}, 200
        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500


class LinhaListResource(Resource):
    data_parser = reqparse.RequestParser()
    data_parser.add_argument("numero",
        type=str,
        required=True,
        help="Este campo não pode estar vazio"
    )
    data_parser.add_argument("ddd",
        type=str,
        required=True,
        help="Este campo não pode estar vazio"
    )
    data_parser.add_argument("classificacao",
        type=str,
        required=False,
        # help="Este campo não pode estar vazio"
    )
    data_parser.add_argument("status",
        type=str,
        required=True,
        help="Este campo não pode estar vazio"
    )
    data_parser.add_argument("funcionario_id",
        type=str,
        required=False,
        # help="Este campo não pode estar vazio"
    )
    data_parser.add_argument("aparelho_id",
        type=str,
        required=False,
    )
    data_parser.add_argument("last_funcionario_id",
        type=str,
        default='',
    )

    @jwt_required()
    def post(self):
        try:
            data = LinhaListResource.data_parser.parse_args()
            numero = data["numero"]
            linha = LinhaModel.find_by_numero(numero)
            if linha:
                return {"message": f"Linha {numero} já existente"}, 400

            funcionario_id = data["funcionario_id"]
            # if status == "em uso" and not funcionario:
            #     return {"message": "Para status 'Em Uso', a linha deve estar atribuída a um funcionário"}, 400
            status = data["status"]
            aparelho_id = data["aparelho_id"]
            if (status == "em uso") and not (aparelho_id or funcionario_id):
                return {"message": "Para status 'em uso', a linha deve estar atribuída a um aparelho ou a um funcionário"}, 400

            if(aparelho_id and funcionario_id):
                return {"message": "A linha não pode estar atribuída a um aparelho e a um funcionário ao mesmo tempo"}, 400

            if(aparelho_id):
                linha = LinhaModel.find_by_aparelho(aparelho_id)
                if linha:
                    return {"message": "Esta linha já está vinculada a um aparelho"}, 400

            linha = LinhaModel(**data)

            linha.upsert()
            return linha.to_json(), 201
        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500

    @jwt_required()
    def get(self):
        try:
            linhas = LinhaModel.get_all()
            if not linhas:
                return {"message": "Não há linhas cadastradas na base"}, 400
            return linhas, 200
        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500