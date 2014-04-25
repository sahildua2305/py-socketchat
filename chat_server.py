#!/usr/bin/python
import socket, select

def broadcast_data(sock, message):
	#don't send message to the master and the  client who has sent the data
	for socket in CONNECTION_LIST:
		if socket != server_socket and socket != sock:
			try:
				socket.send(message)
			except :
				socket.close()
				CONNECTION_LIST.remove(socket)

if __name__ == "__main__":
	CONNECTION_LIST = []
	RECV_BUFFER = 4096
	PORT = 5000
	
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.listen(10)
	
	CONNECTION_LIST.append(server_socket)
	print "Chat server started on port " + str(PORT)
	
	while 1:
		#get the list of sockets which are ready to be read through select
		read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])
		
		for sock in read_sockets:
			if sock == server_socket: #new connection
				s, addr = server_socket.accept()
				CONNECTION_LIST.append(s)
				print "Client (%s, %s) connected" % addr
				
				broadcast_data(s, "[%s:%s] entered the chat room\n" % addr)
			
			else: #incoming message from some client
				try:
					data = sock.recv(RECV_BUFFER)
					if data:
						broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)
				except :
					broadcast_data(sock, "Client (%s, %s) is offline" % addr)
					print "Client (%s, %s) is offline" % addr
					sock.close()
					CONNECTION_LIST.remove(sock)
					continue
	
	server_socket.close()
