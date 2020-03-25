import socket
from client_download import download
from client_upload import upload
from client_list import list


while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 2005)
    print(f"connecting to {server_address}")
    sock.connect(server_address)

    print("command menu : \ndownload\nupload\nlist\nexit")
    command = input("enter command : ")
    if (command=='download'):
        filename = input("enter namefile : ")
        download(sock,command,filename)
        sock.close()
    elif (command=='upload'):
        filename = input("enter namefile : ")
        upload(sock,command,filename)
        sock.close()
    elif (command=='list'):
        list(sock,command)
        sock.close()
    elif (command == 'exit'):
        exit()
    else:
        print("ERRCMD")