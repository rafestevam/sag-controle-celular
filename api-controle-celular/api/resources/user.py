from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import safe_str_cmp
from passlib.hash import pbkdf2_sha256
from models.user import UserModel
from blocklist import BLOCKLIST

class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="O campo USUARIO é obrigatório"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="O campo PASSWORD é obrigatório"
    )

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()
        username = data["username"]
        password = data["password"]

        user = UserModel.find_by_username(username)
        if user and pbkdf2_sha256.verify(password, user.password):
            access_token = create_access_token(identity=user.id)
            #refresh_token = create_refresh_token(user.id)
            return {
                'access_token': access_token
            }, 200

        return {'message': 'Credenciais inválidas'}, 401

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="O campo USUARIO é obrigatório"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="O campo PASSWORD é obrigatório"
    )
    parser.add_argument('name',
        type=str,
        required=True,
        help="O campo NAME é obrigatório"
    )

    @classmethod
    def post(cls):
        data = cls.parser.parse_args()
        username = data["username"]

        if UserModel.find_by_username(username):
            return {"message": f"O usuário {username} já existe na base"}, 409
        
        user = UserModel(
            username=data["username"],
            password=pbkdf2_sha256.hash(data["password"]),
            name=data["name"]
        )
        user.upsert()
        return {"message": f"Usuário {username} criado com sucesso!"}, 201

class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message": "Usuário deslogado com sucesso."}, 200




