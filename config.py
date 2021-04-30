import os
##configurations
class Config:

    QUOTE_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgres://wndbojhqkiiyek:a29346c05fb07d9efe91783783e33cb48b8ab5dff4e265286a0c048510aa7f88@ec2-54-163-254-204.compute-1.amazonaws.com:5432/d4h31g4gsvd4of'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADED_PHOTOS_DEST ='app/static/photos'



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://wndbojhqkiiyek:a29346c05fb07d9efe91783783e33cb48b8ab5dff4e265286a0c048510aa7f88@ec2-54-163-254-204.compute-1.amazonaws.com:5432/d4h31g4gsvd4of'
    DEBUG = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

config_options = {
'development':DevConfig,
'production':ProdConfig
}