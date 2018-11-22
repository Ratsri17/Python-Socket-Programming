import socket
# import the socket library

s = socket.socket()
# Created the object 's' of function socket() of socket library

print "Socket Succesfully Created"
# Denotion for successful object creation

port = 12345
# using a random port > 1023 as port number ranges from 0 - 65535 and 0 - 1023 are reserved so a specfic port has to be choosen above the range.

host = '127.0.0.1'
# address of the client computer for local server

s.bind((host, port))
# It binds address and port number to socket and it denotes that the server is now ready to accept the request from client

print "Socket binded to %s " %(port)
# Denotion of successful binding of port and host and printing the port number as well.

s.listen(5)
# Server is in listening mode i.e. the server is ready to be in the communication with the client.

print "socket is listening"
# Denotion for the server is in listen mode

while True:
	c , addr = s.accept()
	# When the client requests for connection to the server then the server accept the request using function s.accept().
	# This function returns tuple c and addr where c is the new socket object used for sending-receiving data on the connection and 	addr is the address bound to the socket on client side connection.

	print "Got connection from" , addr
	# Prints the host name and port number

	c.send("Hello World")
	# Sending data to the client
	
	c.close()
	# Close the connection from the client
