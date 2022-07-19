from flask_login import UserMixin

from blueprints.users_blueprint.models import User
from datastore.db_connection import session


def get_user(**kwargs):
    users = session.query(User)
    for attr_element, attr_value in kwargs.items():
        users = users.filter(getattr(User, attr_element) == attr_value)

    found_user = users.scalar()

    return found_user if found_user else None


class UserClass(UserMixin):
    def __init__(self, name, id, active=True):
        self.name = name
        self.id = id
        self.active = active

    def is_active(self):
        return self.active
