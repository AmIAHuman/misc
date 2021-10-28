import socket

host = ""
port = 0

def read(sock):
  return sock.recv(1024)

def send(sock, message):
  sock.send(message)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
