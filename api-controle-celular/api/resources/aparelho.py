from flask_restful import Resource, reqparse
from flask_cors import cross_origin
from models.aparelho import AparelhoModel
from models.linha import LinhaModel

class AparelhoResource(Resource):
    data_parser = reqparse.RequestParser()
    data_parser.add_argument("imei",
        type=str,
        required=False,
    )
    data_parser.add_argument("imei_2",
        type=str,
        required=False,
    )
    data_parser.add_argument("fabricante",
        type=str,
        required=False,
    )
    data_parser.add_argument("marca",
        type=str,
        required=False,
    )
    data_parser.add_argument("modelo",
        type=str,
        required=False,
    )
    data_parser.add_argument("numero_serie",
        type=str,
        required=False,
    )
    data_parser.add_argument("acessorios",
        type=str,
        required=False
    ),
    data_parser.add_argument("status",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("funcionario_id",
        type=str,
        # required=True,
        # help="O aparelho deve ser atribuído a um funcionário"
    )
    # data_parser.add_argument("linha_id",
    #     type=str,
    #     required=True,
    #     help="Uma linha deve ser atribuída a um aparelho"
    # )

    @cross_origin()
    def get(self, id):
        try:
            aparelho = AparelhoModel.find_by_id(id)
            if not aparelho:
                return {"message": "Aparelho não encontrado"}, 400
            return aparelho.to_json(), 200
        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500

    @cross_origin()
    def put(self, id):
        try:
            data = AparelhoResource.data_parser.parse_args()
            aparelho = AparelhoModel.find_by_id(id)
            if not aparelho:
                return {"message": "Aparelho não encontrado"}, 400

            aparelho.imei = data["imei"]
            aparelho.imei_2 = data["imei_2"]
            aparelho.fabricante = data["fabricante"]
            aparelho.marca = data["marca"]
            aparelho.modelo = data["modelo"]
            aparelho.numero_serie = data["numero_serie"]
            aparelho.acessorios = data["acessorios"]
            aparelho.status = data["status"]
            last_funcionario_id = aparelho.funcionario_id
            # if data["funcionario_id"]:
            aparelho.funcionario_id = data["funcionario_id"]
            # if data["linha_id"]:
            # aparelho.linha_id = data["linha_id"]
            if (aparelho.linha and (data["funcionario_id"] != last_funcionario_id)):
                linha = LinhaModel.find_by_id(aparelho.linha.id)
                linha.last_funcionario_id = last_funcionario_id
                # linha.funcionario.id = data["funcionario_id"]
                linha.upsert()
            
            aparelho.upsert()
            return aparelho.to_json(), 200
        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500

    @cross_origin()
    def delete(self, id):
        try:
            aparelho = AparelhoModel.find_by_id(id)
            if not aparelho:
                return {"message": "Aparelho não encontrado"}, 400
            if aparelho.funcionario_id:
                return {"message": "Aparelho está atribuído a um funcionário"}, 400
            if aparelho.linha:
                return {"message": "Aparelho está atribuído a uma linha"}, 400
            aparelho.delete()
            return {"message": "Aparelho excluído com sucesso"}, 200
        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500


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
    data_parser.add_argument("acessorios",
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
        # required=True,
        # help="O aparelho deve ser atribuído a um funcionário"
    )
    # data_parser.add_argument("linha_id",
    #     type=str,
    #     required=True,
    #     help="Uma linha deve ser atribuída a um aparelho"
    # )

    # @cross_origin()
    def post(self):
        try:
            data = AparelhoListResource.data_parser.parse_args()
            imei = data["imei"]
            aparelho = AparelhoModel.find_by_imei(imei)
            if aparelho:
                return {"message": f"Aparelho com IMEI {imei} já cadastrado"}, 400

            status = data["status"]
            funcionario = data["funcionario_id"]
            if status == "em uso" and not funcionario:
                return {"message": "Para status 'Em Uso', o aparelho deve estar atribuído a um funcionário"}, 400
            
            aparelho = AparelhoModel(**data)

            aparelho.upsert()
            return aparelho.to_json(), 201
        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500

    # @cross_origin()
    def get(self):
        try:
            aparelhos = AparelhoModel.get_all()
            if aparelhos:
                return aparelhos, 200
            return {"message": "Não há aparelhos cadastrados na base"}, 400
        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500
