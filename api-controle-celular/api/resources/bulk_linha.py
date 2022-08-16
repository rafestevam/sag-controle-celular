from flask import request
from flask_restful import Resource, reqparse
from parsers.linha import LinhaParser
import os
import app_config
import werkzeug

class BulkLinha(Resource):

    def post(self):
        try:
            uploaded_file = request.files['file']
            if uploaded_file.filename:
                file_path = os.path.join(app_config.UPLOAD_FOLDER, uploaded_file.filename)
                uploaded_file.save(file_path)
                LinhaParser.parseCSV(file_path)
                os.remove(file_path)
                return {"message": "Carga de Linhas efetuada com sucesso"}, 200
            else:
                return {"message": "Defina um arquivo para a realização da carga em lote"}, 400
        except RuntimeError as e:
            return {"message": f"Erro interno: {str(e)}"}, 500
