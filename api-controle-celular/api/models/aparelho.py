from db import db
from sqlalchemy.orm import backref
import uuid
import sys

class AparelhoModel(db.Model):
    __tablename__ = 'aparelhos'

    id = db.Column(db.String, primary_key=True)
    imei = db.Column(db.String)
    imei_2 = db.Column(db.String)
    fabricante = db.Column(db.String)
    marca = db.Column(db.String)
    modelo = db.Column(db.String)
    numero_serie = db.Column(db.String)
    acessorios = db.Column(db.String)
    status = db.Column(db.String)

    # Relacionamento 1:N - Funcionarios -> Aparelhos
    funcionario_id = db.Column(db.String, db.ForeignKey("funcionarios.id"))
    #funcionario = db.relationship("FuncionarioModel", backref=backref("aparelhos", uselist=False))

    # Relacionamento 1:1 - Linhas -> Aparelhos
    linha = db.relationship("LinhaModel", uselist=False, backref="aparelhos")
    # linha_id = db.Column(db.String, db.ForeignKey("linhas.id"))

    def __init__(self, imei, imei_2, fabricante, marca, modelo, numero_serie, acessorios, status, funcionario_id):
        self.id = str(uuid.uuid4())
        self.imei = imei
        self.imei_2 = imei_2
        self.fabricante = fabricante
        self.marca = marca
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.acessorios
        self.status = status
        self.funcionario_id = funcionario_id
        # self.linha = self.linha.to_json()

    def to_json(self):
        linha = None
        if self.linha:
            linha = self.linha.to_json()

        return {
            "id": self.id,
            "imei": self.imei,
            "imei_2": self.imei_2,
            "fabricante": self.fabricante,
            "marca": self.marca,
            "modelo": self.modelo,
            "numero_serie": self.numero_serie,
            "acessorios": self.acessorios,
            "status": self.status,
            "funcionario_id": self.funcionario_id,
            "linha": linha
            # "linha": self.linha.to_json() or None
        }

    def upsert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            error = sys.exc_info()[1]
            raise RuntimeError(error)
    
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
            error = sys.exc_info()[1]
            raise RuntimeError(error)

    @classmethod
    def find_by_id(cls, id):
        try:
            aparelho = cls.query.filter_by(id=id).first()
            return aparelho
        except:
            error = sys.exc_info()[1]
            raise RuntimeError(error)

    @classmethod
    def find_by_imei(cls, imei):
        try:
            aparelho = cls.query.filter_by(imei=imei).first()
            return aparelho
        except:
            error = sys.exc_info()[1]
            raise RuntimeError(error)

    @classmethod
    def get_all(cls):
        try:
            return [aparelho.to_json() for aparelho in cls.query.all()]
        except:
            error = sys.exc_info()[1]
            raise RuntimeError(error)