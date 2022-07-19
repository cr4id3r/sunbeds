from flask_wtf import FlaskForm
from sqlalchemy import select
from wtforms import TextAreaField, PasswordField, validators, BooleanField, HiddenField, EmailField
from wtforms.validators import DataRequired

from .models import User
from .utils import get_user
from ...datastore.db_connection import session


class LoginForm(FlaskForm):
    email = EmailField('Email Address', [
        DataRequired()
    ])
    password = PasswordField('Password', [
        DataRequired()
    ])


    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        form_validation = FlaskForm.validate(self)
        if not form_validation:
            return False

        user = get_user(email=self.email.data)

        if user is None:
            self.email.errors.append('Email not registered')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True


class RegistrationForm(FlaskForm):
    email = EmailField('Email Address', [
        DataRequired()
    ])
    password = PasswordField('New Password', [
        DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)

    def validate(self):

        form_validation = FlaskForm.validate(self)
        if not form_validation:
            return False

        stmt = select(User).where(User.email == self.email.data)
        user = session.execute(stmt).first()
        if user is not None:
            self.email.errors.append('Email is already registered')
            return False

        return True


class EmailAuthInitiateForm(FlaskForm):
    email = EmailField('Email Address', [
        DataRequired()
    ])

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        form_validation = FlaskForm.validate(self)
        if not form_validation:
            return False

        user = User.query.filter_by(email=self.email.data).first()
        if user is None:
            self.email.errors.append('Email is not registered')
            return False

        self.user = user
        return True

