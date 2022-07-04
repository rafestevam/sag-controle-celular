from cellphoneauth import auth_required
from flask_restful import Resource, reqparse
from models.centro_custo import CentroCustoModel
from flask.json import jsonify

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
                return {"message": f"Centro de Custo não encontrado."}, 400
            return  centro_custo.to_json()
        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500
    
    def put(self, id):
        try:
            centro_custo = CentroCustoModel.find_by_id(id)
            if not centro_custo:
                return {"message": f"Centro de Custo não encontrado."}, 400
            
            data = CentroCustoResource.data_parser.parse_args()
            centro_custo.cc_nome = data["cc_nome"]
            centro_custo.upsert()
            return  centro_custo.to_json()
        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500

    def delete(self, id):
        try:
            centro_custo = CentroCustoModel.find_by_id(id)
            if not  centro_custo:
                {"message": "Centro de Custo não encontrado."}, 400
            centro_custo.delete()
            return {"message": "Centro de Custo excluído com sucesso"}, 200
        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500


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
            # centros_custo = CentroCustoModel.paginate(per_page=1, page=5, errors_out=False)
            if centros_custo:
                return centros_custo, 200
            return {"message": "Não há centros de custo cadastrados na base"}, 400
        except RuntimeError as error:
            return {"message": f"Erro interno: {str(error)}"}, 500
        
    def post(self):
        try:
            data = CentroCustoResourceList.data_parser.parse_args()
            cc_cod = data["cc_cod"]
            centro_custo = CentroCustoModel.find_by_cc_cod(cc_cod)
            if centro_custo:
                return {"message": f"Centro de Custo {cc_cod} já existente."}, 400

            centro_custo = CentroCustoModel(**data)   
            centro_custo.upsert()
            return  centro_custo.to_json(), 201
        except RuntimeError as error:
            return {"message": f"Erro interno: {str(error)}"}, 500
        # except Exception as e:
        #     return {"message": f"Erro interno {str(e)}"}, 500
        
class CentroCustoResourceListPaginated(Resource):
    def get(self, page_num):
        try:
            # centros_custo = CentroCustoModel.get_all()
            centros_custo = CentroCustoModel.get_all_paginated(page_num)
            if centros_custo:
                return centros_custo, 200
            return {"message": "Não há centros de custo cadastrados na base"}, 400
        except RuntimeError as error:
            return {"message": f"Erro interno: {str(error)}"}, 500

class CentroCustoResourcePages(Resource):
    def get(self):
        try:
            ccPages = CentroCustoModel.get_number_of_pages()
            if ccPages:
                return {"pages": ccPages}, 200
            return {"message": "Não há centros de custo cadastrados na base"}, 400
        except RuntimeError as error:
            return {"message": f"Erro interno: {str(error)}"}, 500
