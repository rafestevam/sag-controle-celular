from db import db
import uuid
import sys

class LinhaModel(db.Model):
    __tablename__ = 'linhas'

    id = db.Column(db.String, primary_key=True)
    ddd = db.Column(db.String)
    numero = db.Column(db.String)
    classificacao = db.Column(db.String)
    status = db.Column(db.String)

    def __init__(self, ddd, numero, classificacao, status):
        self.id = str(uuid.uuid4())
        self.ddd = ddd
        self.numero = numero
        self.classificacao = classificacao
        self.status = status

    def to_json(self):
        return {
            "id": self.id,
            "ddd": self.ddd,
            "numero": self.numero,
            "classificacao": self.classificacao,
            "status": self.status
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

    