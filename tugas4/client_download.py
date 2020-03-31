import socket

def download(sock, command, fileName):
    Data = command+" "+fileName
    sock.send(Data.encode('utf-8'))
    sock.shutdown(socket.SHUT_WR)

    data = sock.recv(1024)
    if data == b'File tidak ada':
        print("File tidak ada")
    else:
        f = open("Client/"+fileName, 'wb')
        while (data):
            f.write(data)
            data = sock.recv(1024)
        print("Download Berhasil")
        f.close()
    print("Closing Download Process")
