import threading


class daemon_websocket:      
    
    def addService(self, callback):
        t = threading.Thread(target=callback)
        t.daemon = True
        t.start()
        
