import os

#SECRET_KEY=os.urandom(24).hex()
FLASK_ENV=os.environ.get('FLASK_ENV')
HOST=os.environ.get('HOST')
PORT=os.environ.get('PORT')

'''
from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = SECRET_KEY or 'dev_key'
    )

    return app
'''

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'f917399ab27701bda889f1170e7bdda3334c407660c265fb'

class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    "SOCK_SERVER_OPTIONS": {
        'ping_interval': 30, # Envía paquetes de ping a los clientes en el intervalo solicitado en segundos. Establezca esta opción None(predeterminada)
        'max_message_size': None # El tamaño máximo permitido para un mensaje, en bytes, o Nonesin límite.
    }
}