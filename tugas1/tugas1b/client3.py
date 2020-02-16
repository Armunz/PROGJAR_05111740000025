import socket

#Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to the port
server_address = ('localhost', 31000)
print(f"connection to {server_address}")
sock.connect(server_address)

try:
    #Send data
    #message = 'PEMROGRAMAN JARINGAN TEKNIK INFORMATIKA'
    request = input('Isikan nama file: ')
    print(f"sending {request}")
    sock.sendall(request.encode())
    f = open("Hasil_request", "wb")
    while True:
        data = sock.recv(64)
        if data:
            f.write(data)
        else:
            f.close()
            print(f"no more data from {server_address}")
            break
finally:
    print("Selesai mengirimkan pesan.")
    sock.close()