import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
s.send(b"lel\n")
print(s.recv(1024))
s.close()
