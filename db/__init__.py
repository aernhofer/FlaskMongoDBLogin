from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from datetime import datetime

class Database():

    bcrypt = Bcrypt(None)
    dbClient = MongoClient('192.168.1.88',27017)


    def connect(self):
        #print(dbClient.database_names())
        self.db = self.dbClient.users
        self.users = self.db.users

    def register(self,email,passwd):
        password_hash = self.bcrypt.generate_password_hash(passwd)

        user = {
        "email": email,
        "password": password_hash
        }

        self.users.insert_one(user)

    def login(self,email,passwd):

        if ( self.users.find({"email": email}).count() == 0 ):
            print ("User %s not found" % email)
            logged_in = False
        else:
            cursor = self.db.users.find_one({"email": email})
            password = self.bcrypt.check_password_hash(cursor['password'],passwd)

        if ( password == True ):
            print ("Password accepted, authentication succesful")
            logged_in = True
        else:
            print ("Password rejected. Login failed")
            logged_in = False

        return logged_in

#db = Database()
#db.connect()
#print(db.login('qwe@gmail.com','qwe'))