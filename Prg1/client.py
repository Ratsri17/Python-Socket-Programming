import socket
# import the socket library

port = 12345
host = '127.0.0.1'
# port number and host must be same in client side and server side.

while True:
    s = socket.socket()
    # socket object s is created for client side

    s.connect((host, port))
    # establish the connection between host and port

    print s.recv(1024)
    # Whatever data is being sent by the server that data is received by the client using recv() function and argument in the function   is the size of data received.

    s.close()
    # Closes the client side connection.

