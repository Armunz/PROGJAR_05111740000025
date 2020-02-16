import socket
import select

#Create a TCP/IP Socket

#membuat list socket untuk menampung list socket dari server
socket_list = []
#membuat port dari 41000 sampai 41002
for port in range(41000, 41003):
    # AF_INET = Address Family, metode paling aman   #SOCK_STREAM = TCP Socket, #SOCK_DGRAM = UDP Socket
    # Untuk menjalankan 3 port sekaligus, ada 3 socket yang harus dibuat
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.43.164', port)
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
        #f = open('received_file', 'wb')
        if data:
            #f.write(data)
            print("Sending back data")
            connection.sendall(data)
        else:
            #f.close()
            print(f"no more data from {client_address}")
            break
    #Clean up the connection
    connection.close()
