from socket import *
import argparse as ap


parser = ap.ArgumentParser(description="Check for specified server-ip (-i) and port-numper (-p)")
# Add the arguments
parser.add_argument("-i", "--server", help="Servers host name", type=str)
parser.add_argument("-p", "--port", help="Port server is listening on", type=int)
parser.add_argument("-f", "--file", help="Filename the server shall return")

args = parser.parse_args()

# Initiate variables
serverName = args.server
serverPort = args.port
filename = args.file

# Prepare client socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Send argumented file to server
request = f"GET /{filename} HTTP/1.1\r\nHost: {serverName}\r\nConnection: close\r\n\r\n"
clientSocket.send(request.encode())

response = ''
# Receive response
while True:
    chunk = clientSocket.recv(1024).decode()
    if not chunk:
        break
    response += chunk


print("From server : ", response)

# Close client socket
clientSocket.close()
