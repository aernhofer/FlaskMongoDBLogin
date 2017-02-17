from flask_bcrypt import Bcrypt
from hashlib import md5

class User():

    def __init__(self, email, lastLogin):
        self.email = email
        self.lastLogin = lastLogin

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

    def avatar(self, size):
        return 'https://www.gravatar.com/avatar/%s?d=monsterid&r=x&s=%d' % (md5(self.email.encode('utf-8')).hexdigest(), size)
