from flask import Blueprint, request

main = Blueprint('api', __name__)
v1 = Blueprint('v1', __name__, url_prefix='/v1')
miruta = Blueprint('miruta', __name__, url_prefix='/miruta')

@miruta.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return {
            "id": 1,
            "loging": True
        }
    else:
        return {
            "id": 1,
            "loging": False
        }

# registrar la v1
main.register_blueprint(v1)
v1.register_blueprint(miruta)

