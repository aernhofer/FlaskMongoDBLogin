from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, BooleanField, SelectField
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
    #my_choices = [('1', 'Choice1'), ('2', 'Choice2'), ('3', 'Choice3')]
    #birthyear = SelectField(u'Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    #recaptcha = RecaptchaField()
