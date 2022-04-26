from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_session import Session
from db import db

# Importação das configs da aplicação
import app_config

# Importação dos Models
from models.centro_custo import CentroCustoModel
from models.funcionario import FuncionarioModel
from models.linha import LinhaModel
from models.aparelho import AparelhoModel

# Importação dos Resources
from resources.hello import HelloResource
from resources.centro_custo import CentroCustoResource, CentroCustoResourceList
from resources.funcionario import FuncionarioResource, FuncionarioListResource
from resources.linha import LinhaResource, LinhaListResource
from resources.aparelho import AparelhoResource, AparelhoListResource

app = Flask(__name__) # Inicializando API
CORS(app)

# Importação das configurações
app.config.from_object(app_config)
Session(app)

# Inicializando a API Restful
api = Api(app)

# Inicializando DB
db.init_app(app)
# Criação das tabelas do banco SQLite
@app.before_first_request
def create_tables():
    db.create_all()

# Roteamento dos recursos da API
api.add_resource(HelloResource, '/hello')
api.add_resource(CentroCustoResource, '/cc/<string:id>')
api.add_resource(CentroCustoResourceList, '/cc')
api.add_resource(FuncionarioResource, '/funcionarios/<string:id>')
api.add_resource(FuncionarioListResource, '/funcionarios')
api.add_resource(LinhaResource, '/linhas/<string:id>')
api.add_resource(LinhaListResource, '/linhas')
api.add_resource(AparelhoResource, '/aparelhos/<string:id>')
api.add_resource(AparelhoListResource, '/aparelhos')

# Inicialização da app Python
if __name__ == '__main__':
    app.run(port=5000, debug=True)
