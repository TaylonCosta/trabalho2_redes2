from threading import Thread
import socket
import datetime as dt


class ThreadCliente(Thread):

    def __init__(self, addr):
        Thread.__init__(self)
        self.host = addr[0]
        self.porta = addr[1]
        print("Nova conexao de " + str(self.host) + ", na porta " + str(self.porta))

    def run(self):
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)
            str = ("hora de antendimento: %s:%s" % (dt.datetime.now().hour, dt.datetime.now().minute))
            conn.sendall(str.encode('ascii'))


HOST = '127.0.0.1'
PORTA = 65432
BUFFER = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORTA))
    threads = []

    while True:
        s.listen(4)
        print("server up")
        conn, addr = s.accept()
        n_thread = ThreadCliente(addr)
        n_thread.start()
        threads.append(n_thread)
