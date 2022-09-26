from db import db
from sqlalchemy.orm import backref
import uuid

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)

    def __init__(self, username, password, name):
        self.id = str(uuid.uuid4())
        self.username = username
        self.password = password
        self.name = name

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "name": self.name
        }

    def upsert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            error = error = sys.exc_info()[1]
            raise RuntimeError(error)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

