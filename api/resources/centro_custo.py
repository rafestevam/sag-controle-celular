from cellphoneauth import auth_required
from flask_restful import Resource, reqparse
from models.centro_custo import CentroCustoModel

class CentroCustoResource(Resource):
    data_parser = reqparse.RequestParser()
    data_parser.add_argument("cc_nome",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )

    def get(self, id):
        try:
            centro_custo = CentroCustoModel.find_by_id(id)
            if not centro_custo:
                return {"mensagem": f"Centro de Custo não encontrado."}, 400
            return  centro_custo.to_json()
        except RuntimeError as e:
            return {"mensagem": f"Erro interno {str(e)}"}, 500
    
    def put(self, id):
        try:
            centro_custo = CentroCustoModel.find_by_id(id)
            if not centro_custo:
                return {"mensagem": f"Centro de Custo não encontrado."}, 400
            
            data = CentroCustoResource.data_parser.parse_args()
            centro_custo.cc_nome = data["cc_nome"]
            centro_custo.upsert()
            return  centro_custo.to_json()
        except RuntimeError as e:
            return {"mensagem": f"Erro interno {str(e)}"}, 500

    def delete(self, id):
        try:
            centro_custo = CentroCustoModel.find_by_id(id)
            if not  centro_custo:
                {"mensagem": "Centro de Custo não encontrado."}, 400
            centro_custo.delete()
            return {"mensagem": "Centro de Custo excluído com sucesso"}, 200
        except RuntimeError as e:
            return {"mensagem": f"Erro interno {str(e)}"}, 500


class CentroCustoResourceList(Resource):
    data_parser = reqparse.RequestParser()
    data_parser.add_argument("cc_cod",
        type=int,
        required=True,
        help="Este campo não deve estar vazio"
    )
    data_parser.add_argument("cc_nome",
        type=str,
        required=True,
        help="Este campo não deve estar vazio"
    )

    def get(self):
        try:
            centros_custo = CentroCustoModel.get_all()
            if centros_custo:
                return {"centros_custo": centros_custo}, 200
            return {"mensagem": "Não há centros de custo cadastrados na base"}, 400
        except RuntimeError as error:
            return {"mensagem": f"Erro interno: {str(error)}"}, 500
        
    def post(self):
        try:
            data = CentroCustoResourceList.data_parser.parse_args()
            cc_cod = data["cc_cod"]
            centro_custo = CentroCustoModel.find_by_cc_cod(cc_cod)
            if centro_custo:
                return {"mensagem": f"Centro de Custo {cc_cod} já existente."}, 400

            centro_custo = CentroCustoModel(**data)   
            centro_custo.upsert()
            return  centro_custo.to_json(), 201
        except RuntimeError as error:
            return {"mensagem": f"Erro interno: {str(error)}"}, 500
        # except Exception as e:
        #     return {"mensagem": f"Erro interno {str(e)}"}, 500
        
