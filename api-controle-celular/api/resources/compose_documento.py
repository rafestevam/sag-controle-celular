from flask_restful import Resource
from models.funcionario import FuncionarioModel
from composer.documento import DocumentComposer

class DocumentResource(Resource):

    def get(self, id):
        try:
            funcionario =  FuncionarioModel.find_by_id(id)
            if not funcionario:
                return {"message": "Funcionário não encontrado"}

            if((funcionario.aparelhos.count() == 0) and (funcionario.linhas.count() == 0)):
                return {"message": "Funcionário não tem Aparelhos e/ou Linhas atribuídos"}, 400
            
            DocumentComposer.cria_documento(funcionario)

            return {"message": "Termo de Responsabilidade gerado com sucesso"}, 200

        except RuntimeError as e:
            return {"message": f"Erro interno {str(e)}"}, 500