from db import db
import uuid
import sys

class CentroCustoModel(db.Model):
    __tablename__ = 'centros_custo'

    id = db.Column(db.String, primary_key=True)
    cc_cod = db.Column(db.String)
    cc_nome = db.Column(db.String)

    funcionarios = db.relationship("FuncionarioModel", lazy="dynamic", viewonly=True)

    def __init__(self, cc_cod, cc_nome):
        self.id = str(uuid.uuid4())
        self.cc_cod = cc_cod
        self.cc_nome = cc_nome

    def to_json(self):
        return {
            "id": self.id, 
            "cc_cod": self.cc_cod, 
            "cc_nome": self.cc_nome, 
            "funcionarios": [funcionario.to_json() for funcionario in self.funcionarios.all()]
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
    def find_by_cc_cod(cls, cc_cod):
        try:
            cc = cls.query.filter_by(cc_cod=cc_cod).first()
            return cc
        except:
            error = sys.exc_info()[1]
            raise RuntimeError(error)

    @classmethod
    def find_by_id(cls, id):
        try:
            cc = cls.query.filter_by(id=id).first()
            return cc
        except:
            error = sys.exc_info()[1]
            raise RuntimeError(error)

    @classmethod
    def get_all(cls):
        try:
            return [centro_custo.to_json() for centro_custo in cls.query.all()]
        except:
            error = sys.exc_info()[1]
            raise RuntimeError(error)