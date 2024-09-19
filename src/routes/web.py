from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

main = Blueprint('web', __name__)


@main.route('/', methods=['GET'])
def index():
    try:
        return render_template('pages/index.html')
    except TemplateNotFound:
        abort(404)

@main.route('/hello')
def hello():
    return '<p>Hello, World!</p>'

@main.route('/websocket')
def websocket():
    return render_template('pages/test_websocket.html')

@main.route('/websocket_clock')
def websocket_clock():
    return render_template('pages/test_websocket_clock.html')
