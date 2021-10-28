import socket

host = ""
port = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(10)
while True:
  conn, addr = s.accept()
  
