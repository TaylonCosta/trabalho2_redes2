import socket
import datetime as dt

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            str = ("Oi cliente, tudo bem? Obrigado pela mensagem. Minha hora e : %s:%s" % (dt.datetime.now().hour, dt.datetime.now().minute))
            conn.sendall(str.encode('ascii'))