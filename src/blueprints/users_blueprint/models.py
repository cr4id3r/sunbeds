from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash

# from database import db
from src.datastore.db_connection import Base


class User(Base):
    __tablename__ = 'User'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    email = Column(String(120))
    username = Column(String(50))
    password = Column(String(350))
    email_auth_hash = Column(String(120))

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def has_role(self, rolename):
        for role in self.roles:
            if role.name == rolename:
                return True
        return False

    def __repr__(self):
        return self.username


# Flask-Login User Object Wrapper
class FLUserWrapper(object):
    def __init__(self, user):
        self._user = user

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self._user.id


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d