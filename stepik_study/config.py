import os


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SECRET_KEY = 'my-super-secret-phrase-I-dont-tell-this-to-nobody'
    SQLALCHEMY_TRACK_MODIFICATIONS = False