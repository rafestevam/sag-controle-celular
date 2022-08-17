from flask_restful import Resource
from models.funcionario import FuncionarioModel
from composer.documento import DocumentComposer

class DocumentResource(Resource):

    def get(self, id):
        try:
            funcionario =  FuncionarioModel.find_by_id(id)
            if not funcionario:
                return {"message": "Funcionário não encontrado"}
            
            DocumentComposer.cria_documento(funcionario)

            return {"message": "Termo de Responsabilidade gerado com sucesso"}, 200

        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500