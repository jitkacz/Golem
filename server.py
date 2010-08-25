import socket
import os
import datetime
import Cookie

IDCounter = 0

def getHtmlPage(name):
  try:     
    f = open('html/'+name+'.html', 'r')
  except:
    return getHtmlPage('error404')
  return f.read()

def sendPage(request, socket, name):
  page = getHtmlPage(name)
  newClient = 0;
  for line in request.split('\n'): #Check id ID is already known
    if ("Cookie:" in line):
      if ("Golem-ID" in line):
        page = "<html><head><title>Golem - Test Cookie</title></head><body><p>"+line+"</p></body></html>" #HTML page for DEBUG view ID in browser
        print "Client is already known!"
        newClient = 0
        break
      else: 
        newClient = 1
    else:
      newClient = 1
  if (newClient == 1): #If client is new
    global IDCounter
    expiration = datetime.datetime.now() + datetime.timedelta(hours=1)
    HTTPHead = "HTTP/1.1 200 OK\nContent-Type: text/html; charset=UTF-8\nSet-Cookie: Golem-ID="+str(IDCounter)+"; expires="+expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")+"\nContent-Length: "+str(len(page))+"\n\n"
    print "Client with ID "+str(IDCounter)+" was added!"
    IDCounter += 1
  else: #If client is already known
    HTTPHead = "HTTP/1.1 200 OK\nContent-Type: text/html; charset=UTF-8\nContent-Length: "+str(len(page))+"\n\n"   
  socket.send(HTTPHead) #Send actual header and HTML page
  socket.send(page)

if __name__=="__main__":   
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
	 if ("GET" in requestClient): #If request from client is GET
	   sendPage(requestClient, clientSocket, 'index')
	 clientSocket.close()
