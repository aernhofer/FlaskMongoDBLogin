from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired
from wtforms.widgets import PasswordInput


class LoginForm(FlaskForm):
    #openid = StringField('openid')
    remember_me = BooleanField('remember_me', default=False)
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', widget=PasswordInput(hide_value=False))

class RegisterForm(FlaskForm):
    vname = StringField('vname')
    nname = StringField('nname')
    email = StringField('email', validators=[DataRequired()])
    password = StringField('password', widget=PasswordInput(hide_value=False))