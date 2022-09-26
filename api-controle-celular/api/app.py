from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api
from flask_session import Session
from flask_jwt_extended import JWTManager
from db import db

# Importação das configs da aplicação
import app_config

# Importação dos Models
from models.centro_custo import CentroCustoModel
from models.funcionario import FuncionarioModel
from models.linha import LinhaModel
from models.aparelho import AparelhoModel
from models.user import UserModel

# Importação dos Resources
from resources.hello import HelloResource
from resources.centro_custo import CentroCustoResource, CentroCustoResourceList, CentroCustoResourceListPaginated, CentroCustoResourcePages
from resources.funcionario import FuncionarioResource, FuncionarioListResource
from resources.linha import LinhaResource, LinhaListResource
from resources.aparelho import AparelhoResource, AparelhoListResource
from resources.user import UserLogin, UserRegister

# Importação dos Resources para Bulk Loading
from resources.bulk_centro_custo import BulkCentroCusto
from resources.bulk_aparelho import BulkAparelho
from resources.bulk_linha import BulkLinha
from resources.bulk_funcionario import BulkFuncionario

# Importação do Resource para composição do Termo de Responsabilidade
from resources.compose_documento import DocumentResource

app = Flask(__name__) # Inicializando API
CORS(app)

# Importação das configurações
app.config.from_object(app_config)
Session(app)

# Secret Key da App para JWT
app.secret_key = 'hrRgZRuVK98E9rBs'
#app.secret_key = secrets.SystemRandom().getrandbits(128)

# Inicializando a API Restful
api = Api(app)

# Inicializando DB
db.init_app(app)
# Criação das tabelas do banco SQLite
@app.before_first_request
def create_tables():
    db.create_all()

# Determinação do JWT
jwt = JWTManager(app)

# Adicionando infos adicionais ao Token JWT
@jwt.additional_claims_loader
def add_claims_to_jwt(identity):
    user = UserModel.find_by_id(identity)
    if user:
        return {
            "name": user.name,
            "username": user.username
        }

# Tratamento de erros do Token JWT
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return (
        jsonify({"message": "O token foi expirado.", "error": "token_expired"}), 401
    )

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return(
        jsonify({"message": "Token inválido.", "error": "invalid_token"}), 401
    )

@jwt.unauthorized_loader
def missing_token_callback(error):
    return (
        jsonify({"message": "A requisição não contém um token de acesso.", "error": "authorization_required"}), 401
    )

# Roteamento dos recursos da API
api.add_resource(HelloResource, '/hello')
api.add_resource(CentroCustoResource, '/cc/<string:id>')
api.add_resource(CentroCustoResourceList, '/cc')
api.add_resource(CentroCustoResourceListPaginated, '/cc/<int:page_num>')
api.add_resource(CentroCustoResourcePages, '/cc/pages')
api.add_resource(FuncionarioResource, '/funcionarios/<string:id>')
api.add_resource(FuncionarioListResource, '/funcionarios')
api.add_resource(LinhaResource, '/linhas/<string:id>')
api.add_resource(LinhaListResource, '/linhas')
api.add_resource(AparelhoResource, '/aparelhos/<string:id>')
api.add_resource(AparelhoListResource, '/aparelhos')
api.add_resource(BulkCentroCusto, '/bulk/cc')
api.add_resource(BulkAparelho, '/bulk/aparelhos')
api.add_resource(BulkLinha, '/bulk/linhas')
api.add_resource(BulkFuncionario, '/bulk/funcionarios')
api.add_resource(DocumentResource, '/compose/<string:id>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')

# Inicialização da app Python
if __name__ == '__main__':
    app.run(port=5000, debug=True)
