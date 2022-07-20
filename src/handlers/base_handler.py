from flask import render_template, request, redirect, url_for, flash, session, abort, g
from flask_login import current_user, login_required, login_user, logout_user

from blueprints.users_blueprint.utils import get_user, UserClass
from datastore.db_connection import get_session
from main import app, login_manager


@app.route('/')
def website_homepage():
    if current_user.is_anonymous:
        return redirect(url_for('users.login'))

    return render_template('sunbeds_app.html')


@app.before_request
def before_request():
    g.db_session = get_session()


@login_manager.user_loader
def load_user(user_id):
    found_user = get_user(id=user_id)
    if found_user:
        found_user = found_user.__dict__
        UserObject = UserClass(found_user['username'], found_user['id'], active=True)
        return UserObject