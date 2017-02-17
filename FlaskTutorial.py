from flask import Flask
from flask_login import LoginManager
from db import Database

app = Flask(__name__)
app.config.from_object('config')

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
lm.login_message = 'Please Sign In'
lm.login_message_category = "info"

db = Database()
db.connect()

import views
import errorhandler
