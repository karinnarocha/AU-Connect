import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'Alliance@Spring2023'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir, 'aep.db')
    