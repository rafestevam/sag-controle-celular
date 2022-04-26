from flask_restful import Resource, request
from cellphoneauth import auth_required

class HelloResource(Resource):
    # @auth_required
    def get(self):
        return {"message": "Hello from controle celular!"}, 200