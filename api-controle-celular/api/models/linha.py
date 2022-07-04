from db import db
from sqlalchemy.orm import backref
import uuid
import sys

class LinhaModel(db.Model):
    __tablename__ = 'linhas'

    id = db.Column(db.String, primary_key=True)
    ddd = db.Column(db.String)
    numero = db.Column(db.String)
    classificacao = db.Column(db.String)
    status = db.Column(db.String)

    # Relacionamento 1:N - Funcionarios -> Linhas
    funcionario_id = db.Column(db.String, db.ForeignKey("funcionarios.id"))
    #funcionarios = db.relationship("FuncionarioModel", backref=backref("linhas", uselist=False))

    def __init__(self, ddd, numero, classificacao, status, funcionario_id):
        self.id = str(uuid.uuid4())
        self.ddd = ddd
        self.numero = numero
        self.classificacao = classificacao
        self.status = status
        self.funcionario_id = funcionario_id

    def to_json(self):
        return {
            "id": self.id,
            "ddd": self.ddd,
            "numero": self.numero,
            "classificacao": self.classificacao,
            "status": self.status,
            "funcionario_id": self.funcionario_id
        }

    def upsert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            error = error = sys.exc_info()[1]
            raise RuntimeError(error)

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
            error = error = sys.exc_info()[1]
            raise RuntimeError(error)

    @classmethod
    def find_by_id(cls, id):
        try:
            linha = cls.query.filter_by(id=id).first()
            return linha
        except:
            error = error = sys.exc_info()[1]
            raise RuntimeError(error)

    @classmethod
    def find_by_numero(cls, numero):
        try:
            linha = cls.query.filter_by(numero=numero).first()
            return linha
        except:
            error = error = sys.exc_info()[1]
            raise RuntimeError(error)

    @classmethod
    def get_all(cls):
        try:
            return [linha.to_json() for linha in cls.query.all()]
        except:
            error = error = sys.exc_info()[1]
            raise RuntimeError(error)

    