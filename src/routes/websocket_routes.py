from .websocket import websocket

class websocket_routes(websocket):
    
    def __init__(self, socket_client_list = []):
        super().__init__(socket_client_list)
        
    # RUTAS
    def echo(self, ws):       
        def callback(data, ws):
            print("mensaje recibido", data)
            ws.send(data)
            
        self.struct_default(ws, callback)
    
    def clock(self, ws):
        def callback(data, ws):
            print("mensaje recibido", data)
            
        self.struct_default(ws, callback)
        
    def list_client(self):
        clientes = self.socket_client_list
        n_clientes = len(clientes)
        print("clientes: ", n_clientes )
        return f"Clientes {n_clientes}"
    
    def miruta_supabase_insert(self, ws):
        def callback(data, ws):
            print("mensaje recibido", data)
            
            if data == 'insert':
                self.send_event_insert_user_supabase()
            
        self.struct_default(ws, callback)

    def miruta_search_transport(self, ws):
        def callback(data, ws):
            print("mensaje recibido", data)

            # El cliente ha contacto un servicio
            if data['opc'] == 'contract_service':
                vehiculo = data['vehiculo']
                id_service = data['id']
                current_position = data['current_position']
                client = data['client']

                self.contract_service( vehiculo, id_service, current_position, client )

            
            
        self.struct_default(ws, callback)
        