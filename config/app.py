import os
from flask import Flask

SECRET_KEY=os.urandom(24).hex()
FLASK_ENV=os.environ.get('FLASK_ENV')
HOST=os.environ.get('HOST')
PORT=os.environ.get('PORT')

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = SECRET_KEY or 'dev_key'
    )

    return app