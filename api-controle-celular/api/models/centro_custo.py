from db import db
from sqlalchemy.orm import backref
from sqlalchemy.orm.collections import attribute_mapped_collection
import uuid
import sys

class CentroCustoModel(db.Model):
    __tablename__ = 'centros_custo'

    id = db.Column(db.String, primary_key=True)
    cc_cod = db.Column(db.String)
    cc_nome = db.Column(db.String)

    # Relacionamento 1:N - Centros de Custo -> Funcionarios
    #funcionarios = db.relationship("FuncionarioModel", lazy="dynamic", viewonly=True)
    funcionarios = db.relationship("FuncionarioModel", backref=backref("centros_custo", uselist=False), lazy="dynamic", collection_class=attribute_mapped_collection("id"))

    def __init__(self, cc_cod, cc_nome):
        self.id = str(uuid.uuid4())
        self.cc_cod = cc_cod
        self.cc_nome = cc_nome
        # self.funcionarios = funcionarios

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
            return [centro_custo.to_json() for centro_custo in cls.query.order_by(CentroCustoModel.cc_cod)]
        except:
            error = sys.exc_info()[1]
            raise RuntimeError(error)

    @classmethod
    def get_all_paginated(cls, num_page):
        try:
            pages = cls.query.paginate(per_page=10, error_out=True).pages
            if num_page <= pages:
                return [centro_custo.to_json() for centro_custo in cls.query.paginate(per_page=10, page=num_page, error_out=True).items]
            else:
                raise RuntimeError(f'O número total de páginas ({pages}) foi extrapolado')
        except:
            error = sys.exc_info()[1]
            raise RuntimeError(error)

    @classmethod
    def get_number_of_pages(cls):
        try:
            pages = cls.query.paginate(per_page=10, error_out=True).pages
            return pages
        except:
            error = sys.exc_info()[1]
            raise RuntimeError(error)