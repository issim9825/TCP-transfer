from socket import *
import _thread as thread 
import time
import sys

def now():
    '''returns time of day'''
    return time.ctime(time.time())

def handleClient(connection):
    '''
    Description:
    a client handler function that receives a GET-request,
    reads the filename and sends HTTP header line into socket.
    Sends 404 Not Found if file is not in the directory
    Arguments:
    connection: holds the connectionSocket connected to server
    Returns: void
    '''
    try:
        # Receive message from GET-request
        message = connection.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        # Read filename from GET-request
        outputdata = f.read()

        # Send HTTP header line into socket
        connection.send("HTTP/1.1 200 OK\r\n".encode())
        connection.send("Content-Type: text/html\r\n\r\n".encode())

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connection.send(outputdata[i].encode())
        connection.send("\r\n".encode())

    except IOError:
        # Send response message for file not found
        connection.send("HTTP/1.1 404 Not Found\r\n".encode())
        connection.send("Content-Type: text/html\r\n\r\n".encode())
        connection.send("<html><body><h1>404 Not Found</h1></body></html>\r\n".encode())
    finally:
        # Close client socket
        connection.close()


def main():
    '''
    Description:
    creates a server socket, listens for new connections,
    and spawns a new thread whenever a new connection join
    '''
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
        try:
            #Establish the connection print('Ready to serve...') connectionSocket, addr =
            connectionSocket, addr = serverSocket.accept()
            print(f'Server connected by {addr}\nat {now()}')
            print('Ready to serve...')
            thread.start_new_thread(handleClient, (connectionSocket,))
        except:
            break #End loop if interrupted
        
    # Close server socket
    serverSocket.close()
    sys.exit() #Terminate the program after sending the corresponding data

if __name__ == "__main__": main()