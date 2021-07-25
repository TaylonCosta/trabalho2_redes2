import socket
import datetime as dt

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    s.bind((HOST, PORT))

    while True:
        
        s.settimeout(5.0)
        data = s.recvfrom(1024)

        if not data:
            break

        str = ("Oi cliente, tudo bem? Obrigado pela mensagem. Minha hora e : %s:%s" % (dt.datetime.now().hour, dt.datetime.now().minute))

        s.sendto(str.encode('ascii'), (data[1][0], data[1][1]))

        print(data[0])