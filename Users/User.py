from flask_bcrypt import Bcrypt


class User():

    def __init__(self, email):
        self.email = email

    Bcrypt(None)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email

    @staticmethod
    def validate_login(password_hash, password):
        return Bcrypt(None).check_password_hash(password_hash,password)