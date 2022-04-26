from db import db
import uuid
import sys

class FuncionarioModel(db.Model):
    __tablename__ = "funcionarios"

    id = db.Column(db.String, primary_key=True)
    nome = db.Column(db.String)
    nome_social = db.Column(db.String)
    admissao = db.Column(db.String)
    data_nascimento = db.Column(db.String)
    cargo = db.Column(db.String)
    rg = db.Column(db.String)
    cpf = db.Column(db.String)

    # Relacionamento 1:N - Centros Custo -> Funcionarios
    centros_custo_id = db.Column(db.String, db.ForeignKey("centros_custo.id"))
    centros_custo = db.relationship("CentroCustoModel")

    aparelhos = db.relationship("AparelhoModel", lazy="dynamic", back_populates="funcionario")

    def __init__(self, nome, nome_social, admissao, data_nascimento, cargo, rg, cpf, centro_custo_id):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.nome_social = nome_social
        self.admissao = admissao
        self.data_nascimento = data_nascimento
        self.cargo = cargo
        self.rg = rg
        self.cpf = cpf
        self.centros_custo_id = centro_custo_id

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "nome_social": self.nome_social,
            "admissao": self.admissao,
            "data_nascimento": self.data_nascimento,
            "cargo": self.cargo,
            "rg": self.rg,
            "cpf": self.cpf,
            "centro_custo_id": self.centros_custo_id,
            "aparelhos": [aparelho.to_json() for aparelho in self.aparelhos.all()]
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
            funcionario = cls.query.filter_by(id=id).first()
            return funcionario
        except:
            error = sys.exc_info()[1]
            raise error

    @classmethod
    def find_by_cpf(cls, cpf):
        try:
            funcionario = cls.query.filter_by(cpf=cpf).first()
            return funcionario
        except:
            error = sys.exc_info()[1]
            raise error

    @classmethod
    def get_all(cls):
        try:
            return [funcionario.to_json() for funcionario in cls.query.all()]
        except:
            error = sys.exc_info()[1]
            raise error
