from flask import Flask
from config import Config
from config import basedir
from flask_login import LoginManager
import pymongo

app = Flask(__name__, static_folder='static')
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'login_view_method'

from app import routes

@login.user_loader
def  load_admin(id):
    return {}


# Mongo database
client = pymongo.MongoClient("mongodb+srv://rsourave:<password>@cluster0.m125c.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.orders