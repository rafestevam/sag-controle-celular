from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from parsers.funcionario import FuncionarioParser
import os
import app_config
import werkzeug

class BulkFuncionario(Resource):

    @jwt_required()
    def post(self):
        try:
            uploaded_file = request.files['file']
            if uploaded_file.filename:
                file_path = os.path.join(app_config.UPLOAD_FOLDER, uploaded_file.filename)
                uploaded_file.save(file_path)
                FuncionarioParser.parseCSV(file_path)
                os.remove(file_path)
                return {"message": "Carga de Funcionários efetuada com sucesso"}, 200
            else:
                return {"message": "Defina um arquivo para a realização da carga em lote"}, 400
        except RuntimeError as e:
            return {"message": f"Erro interno: {str(e)}"}, 500