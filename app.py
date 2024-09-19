from flask import Flask, render_template, request
#from flask_sock import Sock
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS

# Routes
from src.routes import web, api, auth
#from src.routes.websocket_routes import websocket_routes as wsr

# config app
from config import config

# daemons
#from src.services.daemonWebsocket import daemon_websocket as daemon_ws

#sock = Sock()

app = Flask(__name__)
configuration = config['development']

# Configuration
app.config.from_object(config)
CORS(app, resources={r"/*": {'origins': '*'}})
socketio = SocketIO(app, logger=True, engineio_logger=True, cors_allowed_origins="*")

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


# websocket
'''
sock.init_app(app)
websocket_route = wsr([])
daemon_websocket = daemon_ws()

@sock.route('/echo')
def wsr_echo(ws):
	websocket_route.echo(ws)
	
@sock.route('/clock')
def wsr_clock(ws):
	websocket_route.clock(ws)

@app.route('/websocket_list_clients')
def wsr_list_client():
	return websocket_route.list_client()

@sock.route('/miruta/supbase/insert')
def wsr_miruta_supabase_insert(ws):
	websocket_route.miruta_supabase_insert(ws)

@sock.route('/miruta/search_transport')
def wsr_miruta_search_transport(ws):
	websocket_route.miruta_search_transport(ws)

@sock.route('/miruta/search_transport')
def wsr_miruta_search_transport(ws):
	websocket_route.miruta_search_transport(ws)

'''


# services
#daemon_websocket.addService(websocket_route.send_time)
#daemon_websocket.addService(websocket_route.remove_client_desconnect)

users = list()

@socketio.on('connect')
def connect():
	socket_id = request.sid
	users.append(socket_id)
	print(socket_id)
	print("client has connect")
	emit("connect", {"socket_id": socket_id})
	#emit("connect", {"data": f"id: {socket_id} is connected"}, broadcast=True)

@socketio.on('disconnect')
def disconnect():
	socket_id = request.sid
	users.remove(socket_id)
	print("client disconnect")
	emit("disconnect", {"data": f"id: {socket_id} disconnected"})

@socketio.on('client')
def miruta_client(data):
	socket_id = request.sid
	print(socket_id)
	print(data)
	emit("client", {"socket_id": socket_id})

@socketio.on('drive')
def miruta_drive(data):
	socket_id = request.sid
	print(socket_id)
	print(data)
	emit("drive", {"socket_id": socket_id})

'''
@socketio.on('client')
def miruta_client(data):
	print(socket.id)
	print(data)

@socketio.on('miruta/drive', namespace='/drive')
def miruta_client(data):
	print(socket.id)
	print(data)


@socketio.on_error('miruta/client') # handles the '/client' namespace
def error_handler_client(e):
	print("error connect socket")
	print(e)

'''

if __name__ == "__main__":
	#from waitress import serve
	#serve(app, host=config_app.HOST, port=config_app.PORT)
	#app.run()
	socketio.run(app)