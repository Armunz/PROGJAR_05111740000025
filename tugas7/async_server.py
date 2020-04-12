import socket
import time
import sys
import asyncore
from httpscratch import httpServerScratch

httpserver = httpServerScratch()

class ProcessTheClient(asyncore.dispatcher_with_send):
	def handle_read(self):
		data = self.recv(1024)
		if data:
			# print(data)
			d = data.decode()
			if d[-4:] == '\r\n\r\n':
				hasil = httpserver.proses(d)
				hasil = hasil + '\r\n\r\n'
				self.send(hasil.encode())
			# print(d)
			# self.send()
		self.close()

class Server(asyncore.dispatcher):
	def __init__(self,portnumber):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set_reuse_addr()
		self.bind(('0.0.0.0', portnumber))
		self.listen(5)
		print ("running on port {}" . format(portnumber))

	def handle_accept(self):
		pair = self.accept()
		if pair is not None:
			sock, addr = pair
			print(sys.stderr, 'connection from', repr(addr))
			ProcessTheClient(sock)

def main():
	portnumber=10001
	try:
		portnumber=int(sys.argv[1])
	except:
		pass
	svr = Server(portnumber)
	asyncore.loop()

if __name__=="__main__":
	main()

