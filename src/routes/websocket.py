import json
import time, datetime
import uuid

class websocket:
	socket_client_list = None
	# random_uuid = uuid.uuid4()
	
	def __init__(self, socket_client_list = []):
		self.socket_client_list = socket_client_list
		
	
	def addClient(self, ws):
		print("entro...")
		self.socket_client_list.append(ws)
	
	def removeClient(self, ws):
		print("salio")
		self.socket_client_list.remove(ws)                    
	
	def reset_service(self):
		for client in self.socket_client_list:
			self.removeClient(client)
		self.socket_client_list = []
		
	def struct_default(self, ws, callback):
		self.addClient(ws)
		while True:
			data = ws.receive()
			callback(data, ws)
			if data == 'stop':
				break
		self.removeClient(ws)
		
	# daemon
	def send_time(self):
		while True:
			time.sleep(1)
			clients = self.socket_client_list.copy()
			for client in clients:
				try:
					client.send(json.dumps({
						'text': datetime.datetime.now().strftime(
							'%Y-%m-%d %H:%M:%S')
					}))
				except:
					self.removeClient(client)
	
	# remove client desconnect
	def remove_client_desconnect(self):
		while True:
			time.sleep(30)
			clients = self.socket_client_list.copy()
			for client in clients:
				try:
					client.send("")
				except:
					self.removeClient(client)
	
	def send_event_insert_user_supabase(self):
		clients = self.socket_client_list.copy()
		for client in clients:
			try:
				client.send(
					json.dumps(
						{
							'event': 'insert',
							'table': 'users',
						}
					)
				)
			except:
				self.removeClient(client)

	def contract_service(self, vehiculo, id_service, current_position, client ):
		clients = self.socket_client_list.copy()
		for client in clients:
			try:
				client.send(
					json.dumps(
						{
							'event': 'contract_service',
							'client': client,
							'vehiculo': vehiculo,
							'id_service': id_service,
							'current_position': current_position,
						}
					)
				)
			except:
				self.removeClient(client)
