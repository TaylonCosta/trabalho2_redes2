from threading import Thread
import socket
import datetime as dt


class ThreadCliente(Thread):

    def __init__(self, host, porta, data):
        Thread.__init__(self)
        self.host = host
        self.porta = porta
        self.data = data
        print("Nova conexao de " + str(self.host) + ", na porta " + str(self.porta))

    def run(self):
        while True:
            if not self.data:
                break
            print(self.data)
            str = ("hora de antendimento: %s:%s" % (dt.datetime.now().hour, dt.datetime.now().minute))
            s.sendto(str.encode('ascii'), (self.host, self.porta))
            break


HOST = '127.0.0.1'
PORTA = 65432
BUFFER = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORTA))
    threads = []

    while True:
        data = s.recvfrom(1024)
        n_thread = ThreadCliente(data[1][0], data[1][1], data[0])
        n_thread.start()
        threads.append(n_thread)