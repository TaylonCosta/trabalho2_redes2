import socket
import datetime as dt

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    str = ("Oi servidor, tudo bem? Minha hora e: %s:%s" % (dt.datetime.now().hour, dt.datetime.now().minute))
    s.sendall(str.encode('ascii'))
    data = s.recv(1024)

print(repr(data))
