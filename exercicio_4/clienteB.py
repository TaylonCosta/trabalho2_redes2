import socket
import datetime as dt

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    str = ("Cliente B, hora da requisicao: %s:%s" % (dt.datetime.now().hour, dt.datetime.now().minute))
    s.sendto(str.encode('ascii'), (HOST, PORT))
    data, addr = s.recvfrom(1024)

print(data)
