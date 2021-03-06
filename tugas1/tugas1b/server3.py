import socket
import select
import os

#Create a TCP/IP Socket

#membuat list socket untuk menampung list socket dari server
socket_list = []
#membuat port dari 31000 sampai 31002
for port in range(31000, 31003):
    # AF_INET = Address Family, metode paling aman   #SOCK_STREAM = TCP Socket, #SOCK_DGRAM = UDP Socket
    # Untuk menjalankan 3 port sekaligus, ada 3 socket yang harus dibuat
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', port)
    # Bind the socket to the port
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)
    #Memasukkan socket ke dalam socket_list
    socket_list.append(sock)

while True:
    print("waiting for connection")
    #mengambil socket_list dan memasukkannya ke dalam readable
    readable,_,_ = select.select(socket_list, [], [])
    #mengambil server yang telah siap
    ready_server = readable[0]
    # Wait for a connection
    connection, client_address = ready_server.accept()
    while True:
        data = connection.recv(64)
        print(f"received{data}")
        if data:
            f = open(data, "rb")
            l = os.path.getsize(data)
            file_request = f.read(l)
            print("Sending the file request")
            connection.sendall(file_request)
            f.close()
            connection.shutdown(socket.SHUT_RDWR)
        else:
            print(f"File has been sent to {client_address}")
            break
    #Clean up the connection
    connection.close()
