import socket

def getHtmlPage(name):
	try:
		f = open('html/'+name+'.html')
	except:
		return getHtmlPage('error404')
	return f.read()

def sendPage(socket, name):
	page = getHtmlPage(name)
	socket.send("HTTP/1.1 200 OK\nContent-Type: text/html; charset=UTF-8\nContent-Length: "+str(len(page))+"\n\n")
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
		if ("GET" in requestClient): #if request from client is GET
			sendPage(clientSocket, 'index')
			print requestClient
		clientSocket.close()
