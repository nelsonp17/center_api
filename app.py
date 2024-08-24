from flask import Flask, render_template

# Routes
from src.routes import web, api, auth

#from src import init_app
from config import config

app = Flask(__name__)
configuration = config['development']

# Configuration
app.config.from_object(config)

# Blueprints
app.register_blueprint(web.main, url_prefix="/")
app.register_blueprint(api.main, url_prefix="/api")
app.register_blueprint(auth.main, url_prefix="/auth")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 500 status explicitly
    return render_template('pages/500.html'), 500

if __name__ == "__main__":
    #from waitress import serve
    #serve(app, host=config_app.HOST, port=config_app.PORT)
    app.run()