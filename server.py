import socket
from socketserver import TCPServer, StreamRequestHandler


class Handler(StreamRequestHandler):
    def handle(self):
        data = self.rfile.readline()
        self.wfile.write(data)

senv = TCPServer((socket.gethostname(), 1234), Handler)
senv.serve_forever()
senv.shutdown()
