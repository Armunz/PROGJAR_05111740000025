from socket import *
import socket
import threading
import logging

from file_machine import fileMachine

pm = fileMachine()

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        data = b''
        while True:
            data_client = self.connection.recv(1024)
            if not data_client:
                break
            data += data_client
            if data:
                dd = b'a'
                if (len(data.split(b'split', 1)) == 2):
                    dd, data = data.split(b'split', 1)
                d = data.decode()
                cstring = d.split(" ")
                command = cstring[0].strip()
                hasil = pm.proses(d, dd)
                if(command == "download"):
                    self.connection.sendall(hasil)
                elif(command == "upload"):
                    self.connection.sendall(hasil.encode())
                elif(command == "list"):
                    self.connection.sendall(hasil.encode())
            else:
                break
        self.connection.close()


class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('127.0.0.1', 2005))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)


def main():
    print("Server is running")
    svr = Server()
    svr.start()


if __name__ == "__main__":
    main()

