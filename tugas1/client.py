import socket

#Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to the port
server_address = ('localhost', 31000)
print(f"connection to {server_address}")
sock.connect(server_address)

try:
    #Send data
    message = 'PEMROGRAMAN JARINGAN TEKNIK INFORMATIKA'
    print(f"sending {message}")
    sock.sendall(message.encode())
    #Look the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(64)
        amount_received += len(data)
        print(f"{data}")
finally:
    print("Selesai mengirimkan pesan.")
    sock.close()