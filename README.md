# Instructions

Below are the instructions for how to run the code in corresponding tasks.

## Task 1

Run `python3 webserver.py` in the terminal.  
Then go to https://localhost:12000 to get the 404 message.  
Go to https://localhost:12000/index.html to get the index-file from the servers filedirectory.

## Task 2

Run `python3 webserver.py` in one terminal.  
Run `python3 client.py -i 'localhost' -p 12000 -f index.html` in another terminal to get the HTTP headers and content of the index-file.

Run `python3 client.py -i 'localhost' -p 12000 -f <non-existing file>` to get the 404 message as output.

## Task 3

Run `python3 multi-server.py` in terminal.  
Then test the server as described in [Task 1](#task-1) and [Task 2](#task-2)

## Task 4

The screenshots and traces are placed in the Mininet-directory.  
Use the program simpletopo.py to get the mininet-terminals up and running.  
Run the server in h3, set up listening on r2, and make the client call from h1.
