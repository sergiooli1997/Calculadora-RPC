from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()


    class MyFuncs:
        def add(self, x, y):
            return x + y

        def res(self, x, y):
            return x - y

        def mul(self, x, y):
            return x * y

        def div(self, x, y):
            if y != 0:
                return x / y


    server.register_instance(MyFuncs())

    # Run the server's main loop
    server.serve_forever()
