import socket

def list(sock,command):
    sock.send(command.encode('utf-8'))
    sock.shutdown(socket.SHUT_WR)

    data = sock.recv(1024).decode()
    hasil=data
    while (data):
        data = sock.recv(1024).decode()
        hasil+=data
    print("List file pada Server : ")
    print(hasil)

    print("Closing List Process")