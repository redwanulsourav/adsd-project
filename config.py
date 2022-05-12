import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'KEY'
    SQLALCHEMY_DATABASE_URI = 'mysql://redwanul:abcd1234@localhost/orders'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SEND_FILE_MAX_AGE_DEFAULT = 0
