from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from parsers.aparelho import AparelhoParser
import os
import app_config
import werkzeug

class BulkAparelho(Resource):

    @jwt_required()
    def post(self):
        try:
            uploaded_file = request.files['file']
            if uploaded_file.filename:
                file_path = os.path.join(app_config.UPLOAD_FOLDER, uploaded_file.filename)
                uploaded_file.save(file_path)
                AparelhoParser.parseCSV(file_path)
                os.remove(file_path)
                return {"message": "Carga de Aparelhos efetuada com sucesso"}, 200
            else:
                return {"message": "Defina um arquivo para a realização da carga em lote"}, 400
        except RuntimeError as e:
            return {"message": f"Erro interno: {str(e)}"}, 500
            