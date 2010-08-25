import socket

host = ''
port = 8080

serverSocket = socket.socket()
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((host, port))
serverSocket.listen(1)

while 1:
  print "Wait for client"
  clientSocket, client = serverSocket.accept()
  print client, " is connected!"
  requestClient = clientSocket.recv(1024) 
  if ("GET" in requestClient): #if request from client is GET
    clientSocket.send("HTTP/1.1 200 OK\nContent-Type: text/html; charset=UTF-8\nContent-Length: 71\n\n") #HTML head
    clientSocket.send("<html><head><title>Golem</title></head><body><p>GOLEM</p></body></html>") #HTML page
  clientSocket.close()
       
                                                                                                            