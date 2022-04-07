from flask_restful import Resource, reqparse
from models.linha import LinhaModel

class LinhaResource(Resource):
    data_parser = reqparse.RequestParser()
    data_parser.add_argument("classificacao",
        type=str,
        required=True,
        help="Este campo não pode estar vazio"
    )
    data_parser.add_argument("status",
        type=str,
        required=True,
        help="Este campo não pode estar vazio"
    )

    def get(self, id):
        try:
            linha = LinhaModel.find_by_id(id)
            if not linha:
                return {"mensagem": "Linha não encontrada"}, 400
            return linha.to_json(), 200
        except RuntimeError as e:
            return {"mensagem": f"Erro interno {str(e)}"}, 500

    def put(self, id):
        try:
            data = LinhaResource.data_parser.parse_args()
            linha = LinhaModel.find_by_id(id)
            if not linha:
                return {"mensagem": "Linha não encontrada"}, 400
            
            linha.classificacao = data["classificacao"]
            linha.status = data["status"]
            linha.upsert()
            return linha.to_json(), 200
        except RuntimeError as e:
            return {"mensagem": f"Erro interno {str(e)}"}, 500
    
    def delete(self, id):
        try:
            linha = LinhaModel.find_by_id(id)
            if not linha:
                return {"mensagem": "Linha não encontrada"}, 400
            linha.delete()
            return {"mensagem": "Linha excluída com sucesso"}, 200
        except RuntimeError as e:
            return {"mensagem": f"Erro interno {str(e)}"}, 500


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
        required=True,
        help="Este campo não pode estar vazio"
    )
    data_parser.add_argument("status",
        type=str,
        required=True,
        help="Este campo não pode estar vazio"
    )

    def post(self):
        try:
            data = LinhaListResource.data_parser.parse_args()
            numero = data["numero"]
            linha = LinhaModel.find_by_numero(numero)
            if linha:
                return {"mensagem": f"Linha {numero} já existente"}, 400
            
            linha = LinhaModel(**data)

            linha.upsert()
            return linha.to_json(), 201
        except RuntimeError as e:
            return {"mensagem": f"Erro interno {str(e)}"}, 500

    def get(self):
        try:
            linhas = LinhaModel.get_all()
            if not linhas:
                return {"mensagem": "Não há linhas cadastradas na base"}, 400
            return {"linhas": linhas}, 200
        except RuntimeError as e:
            return {"mensagem": f"Erro interno {str(e)}"}, 500