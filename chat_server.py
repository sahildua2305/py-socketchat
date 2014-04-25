#get the list of sockets which are ready to be read through select
read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])

def broadcast_data(sock, message):
	#don't send message to the master and the  client who has sent the data
	for socket in CONNECTION_LIST:
		if socket != server_socket and socket != sock:
			try:
				socket.send(message)
			except:
				socket.close()
				CONNECTION_LIST.remove(socket)


