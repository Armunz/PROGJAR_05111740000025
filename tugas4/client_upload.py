import socket
import os

def upload(sock, command, fileName):
    if os.path.isfile("Client/" + fileName):
        data = "split" + command + " " + fileName
        print("Sending: " + fileName)
        file = open("Client/" + fileName, "rb")
        data_encode = data.encode('utf-8')
        datasend = file.read() + data_encode
        print(datasend)
        sock.send(datasend)
        sock.shutdown(socket.SHUT_WR)
        hasil = sock.recv(1024).decode()
        print(hasil)
    else:
        print("File tidak ada")

    print("Closing Upload Process")