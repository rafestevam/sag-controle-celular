from flask_restful import Resource, reqparse
from models.aparelho import AparelhoModel

class AparelhoResource(Resource):
    data_parse = reqparse.RequestParser()
    data_parse.add_argument("status",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )
    data_parse.add_argument("funcionario_id",
        type=str,
        required=False
    )
    data_parse.add_argument("linha_id",
        type=str,
        required=False
    )

    def get(self, id):
        try:
            aparelho = AparelhoModel.find_by_id(id)
            if not aparelho:
                return {"mensagem": "Aparelho não encontrado"}, 400
            return aparelho.to_json(), 200
        except RuntimeError as e:
            return {"mensagem": f"Erro interno {str(e)}"}, 500

    def put(self, id):
        try:
            data = AparelhoResource.data_parse.parse_args()
            aparelho = AparelhoModel.find_by_id(id)
            if not aparelho:
                return {"mensagem": "Aparelho não encontrado"}, 400
            
            aparelho.status = data["status"]
            if data["funcionario_id"]:
                aparelho.funcionario_id = data["funcionario_id"]
            if data["linha_id"]:
                aparelho.linha_id = data["linha_id"]
            
            aparelho.upsert()
            return aparelho.to_json(), 200
        except RuntimeError as e:
            return {"mensagem": f"Erro interno {str(e)}"}, 500

    def delete(self, id):
        try:
            aparelho = AparelhoModel.find_by_id(id)
            if not aparelho:
                return {"mensagem": "Aparelho não encontrado"}, 400
            aparelho.delete()
            return {"mensagem": "Aparelho excluído com sucesso"}, 200
        except RuntimeError as e:
            return {"mensagem": f"Erro interno {str(e)}"}, 500


class AparelhoListResource(Resource):
    data_parser = reqparse.RequestParser()
    data_parser.add_argument("imei",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("imei_2",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("fabricante",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("marca",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("modelo",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("numero_serie",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("status",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("funcionario_id",
        type=str,
        required=True,
        help="O aparelho deve ser atribuído a um funcionário"
    )

    def post(self):
        try:
            data = AparelhoListResource.data_parser.parse_args()
            imei = data["imei"]
            aparelho = AparelhoModel.find_by_imei(imei)
            if aparelho:
                return {"mensagem": f"Aparelho com IMEI {imei} já cadastrado"}, 400
            
            aparelho = AparelhoModel(**data)

            aparelho.upsert()
            return aparelho.to_json(), 201
        except RuntimeError as e:
            return {"mensagem": f"Erro interno {str(e)}"}, 500

    def get(self):
        try:
            aparelhos = AparelhoModel.get_all()
            if aparelhos:
                return aparelhos, 200
            return {"mensagem": "Não há aparelhos cadastrados na base"}, 400
        except RuntimeError as e:
            return {"mensagem": f"Erro interno {str(e)}"}, 500
