import socket
import datetime

class Server:
  def __init__(self, host, port):
    self.socket = socket.socket()
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.socket.bind((host, port))
    self.clients = []
    self.IDCounter = 0
     
  def __del__(self): 
    self.socket.close()
    
  def Start(self): 
    self.socket.listen(1)
    
  def Stop(self): 
    self.socket.listen(0)
    
  def WaitForClient(self): 
    return self.socket.accept()
   
  def SendPage(self, head, page, clientSocket):
    clientSocket.send(head)
    clientSocket.send(page)
  
  def RecvData(self, clientSocket, size): 
    return clientSocket.recv(size)
  
  def GetClientID(self, clientRequest): #Function parse ID from HTTP head or return -1
    ID = "";
    for line in clientRequest.split('\n'):
      if ("Cookie: Golem-ID" in line):
        ID = int(line[17]+line[18])    
        break
    if (len(str(ID)) == 0):
      return -1
    return ID
        
  
  def AddClient(self, clientSocket): #Function add new client instance to servers clientList
    self.clients += [Client(self.IDCounter)]
    expiration = datetime.datetime.now() + datetime.timedelta(hours=1)
    HTMLPage = GetHTMLFile('added')
    HTTPHead = "HTTP/1.1 200 OK\nContent-Type: text/html; charset=UTF-8\nSet-Cookie: Golem-ID="+str(self.IDCounter)+"; expires="+expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")+"\nContent-Length: "+str(len(HTMLPage))+"\n\n"
    self.IDCounter += 1
    self.SendPage(HTTPHead, HTMLPage, clientSocket)
  
  def DelClient(self): 
    pass
   
  def FindClient(self, ID): #Find and return client instance from servers clientList
    for client in self.clients:
      if (client.ID == ID):
        return client
    return -1
  
  def CheckRequest(self, clientRequest): #Read request from skript from browser
    pass
    
  def PrintClients(self):
    for client in self.clients:
      print client.ID      

class Client: 
  def __init__(self, ID):
    self.ID = ID

def GetHTMLFile(file):
  try:
    page = open('C:\\Python26\\HTMLPages\\'+file+'.html')
  except:
    return GetHTMLFile('Error404')
  return page.read()

  
if __name__ == "__main__":
  server = Server('', 8080)
  server.Start()
  
  print "Server started!"
  while 1:
    print "Server wait for client"
    clientSocket, client = server.WaitForClient()
    print "Client ", client, " was connected"
    clientID = server.GetClientID(server.RecvData(clientSocket, 1024))
    if (clientID >= 0):
      #TODO - If client have cookie, but server havent his client instance (server restarted and cookies dont expired)
      clientInstance = server.FindClient(clientID)
      if (clientInstance != -1):
        print "Client with ID ", clientID, " is already known"
        HTMLPage = GetHTMLFile('index')
        HTTPHead = "HTTP/1.1 200 OK\nContent-Type: text/html; charset=UTF-8\nContent-Length: "+str(len(HTMLPage))+"\n\n"
        server.SendPage(HTTPHead, HTMLPage, clientSocket)
    else:
      server.AddClient(clientSocket)
      print "Client was added to list"
    clientSocket.close()
    print ""
  print "Server stop!"
  clientSocket.close()
    
  
  