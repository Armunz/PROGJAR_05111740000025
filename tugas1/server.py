import socket
import select


#Create a TCP/IP Socket
#AF_INET = Address Family, metode paling aman   #SOCK_STREAM = TCP Socket, #SOCK_DGRAM = UDP Socket
#Untuk menjalankan 3 port sekaligus, ada 3 socket yang harus dibuat

socket_list = []
for port in range(31000, 31003):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', port)
    # Bind the socket to the port
    sock.bind(server_address)
    # Listen for incoming connections
    sock.listen(1)
    socket_list.append(sock)

while True:
    print("waiting for connection")
    readable,_,_ = select.select(socket_list, [], [])
    ready_server = readable[0]
    # Wait for a connection
    connection, client_address = ready_server.accept()
    while True:
        data = connection.recv(64)
        print(f"received{data}")

        if data:
            print("Sending back data")
            connection.sendall(data)
        else:
            print(f"no more data from {client_address}")
            break
    #Clean up the connection
    connection.close()
