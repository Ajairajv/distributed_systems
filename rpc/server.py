import xmlrpc.server

class MyFuncs:
    def add(self, x, y):
        return x + y
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(MyFuncs())
server.serve_forever()
