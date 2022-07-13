from flask import render_template, request, redirect, url_for, flash, session, abort
from flask_login import current_user, login_required, login_user, logout_user

from main import app


@app.route('/')
def website_homepage():
    if current_user.is_anonymous:
        return redirect(url_for('users.login'))

    return render_template('sunbeds_app.html')
