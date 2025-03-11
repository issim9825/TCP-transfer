#import socket module
from socket import *
import sys # In order to terminate the program


#Prepare a server socket
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
try:
    serverSocket.bind(('', serverPort))
    print("Ready to receive")
except error as e:
    print(f"Bind failed, Error : {e}")
    sys.exit
serverSocket.listen(1)

while True:
    #Establish the connection print('Ready to serve...') connectionSocket, addr =
    connectionSocket, addr = serverSocket.accept()
    print('Ready to serve...')
    try:
        # Receive message from GET-request
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        # Read filename from GET-request
        outputdata = f.read()
        
        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())

        #Close client socket
        connectionSocket.close()
        
# Close server socket
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
