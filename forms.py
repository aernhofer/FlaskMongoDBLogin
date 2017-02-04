from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from wtforms.widgets import PasswordInput


class LoginForm(FlaskForm):
    #openid = StringField('openid')
    remember_me = BooleanField('remember_me', default=False)
    email = StringField('email')
    password = StringField('password', widget=PasswordInput(hide_value=False))