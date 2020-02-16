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
    filename = 'pesan.txt'
    f = open(filename, 'rb')
    l = f.read(64)
    while(l):
        print(f"sending {message}")
        sock.sendall(l)
finally:
    print("Selesai mengirimkan pesan.")
    sock.close()