from flask import Flask
from flask_login import LoginManager

from Users.User import User
from db import Database

app = Flask(__name__)
app.config.from_object('config')

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

db = Database()
db.connect()

@lm.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve
    """
    user1 = User('asd@gmail.com','asd')
    user2 = User('qwe@gmail.com', 'qwe')

    users = [user1,user2]

    for user in users:
        if(user.get_id() == user_id):
            return user

    return None

import views