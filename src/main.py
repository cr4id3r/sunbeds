from flask import Flask
from flask_login import LoginManager

from blueprints.users_blueprint.utils import get_user, UserClass
from src.blueprints.users_blueprint.views import app as users_blueprint
from src.datastore.db_connection import Base, db
from utils.server.logging_utils import configure_logging_server
from utils.server.urls_utils import check_actual_urls

configure_logging_server()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'labambanera'
app.register_blueprint(users_blueprint)

Base.metadata.create_all(db)

login_manager = LoginManager()
login_manager.init_app(app)

#Import handlers
import handlers

check_actual_urls(app)


@login_manager.user_loader
def load_user(user_id):
    found_user = get_user(id=user_id)
    if found_user:
        found_user = found_user.__dict__
        UserObject = UserClass(found_user['username'], found_user['id'], active=True)
        return UserObject
