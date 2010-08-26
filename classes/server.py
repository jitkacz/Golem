#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, socket, datetime
import threading

from classes.client import Client

HTTP_HEADER_WITH_COOKIE = "HTTP/1.1 200 OK\nContent-Type: text/html; charset=UTF-8\nSet-Cookie: Golem-ID=%i;expires=%s\nContent-Length: %s\n\n"
HTTP_HEADER_WITHOUT_COOKIE = "HTTP/1.1 200 OK\nContent-Type: text/html; charset=UTF-8\nContent-Length: %s\n\n"
REQUESTS = ['command', 'render', 'message']

class Server(object):
	status = False
	pathToHTML = 'html'

	def __init__(self, host="localhost", port=8080):
		self.clients = []
		self.activeThreads = []
		self.IDCounter = 1 

		self._createSocket(host, port)

	def _createSocket(self, host, port):
		self.socket = socket.socket()
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.socket.bind((host, port))

	def __del__(self):
		self.socket.close()

	def start(self):
		self.status = True
		self.addClientSemaphore = threading.Semaphore(1)
		self.socket.listen(1)

		self._run()

	def _run(self):
		while self.status:
			#print "Server wait for client"

			socket, client = self.waitForClient()
			self.activeThreads.insert(0, threading.Thread(None, self.clientOperation, client[0], (socket, client)))
			self.activeThreads[0].start()
			self.checkForInactiveClients()
			#self.printClients()
	
	def checkRequest(self, clientRequest): 
		"""
		Read request from skript from browser
		"""
		lines = clientRequest.split('\n')
		
		for line in lines:
			if "HTTP" in line: #TODO - Parse Command type and Command text from HTTP head
				for command in REQUESTS:
					if command in line: #TODO - Request for render or command
						print line
						return line
				return self.getHTMLFile('index')
			
	
	def clientOperation(self, socket, client):
		"""
		Powerful client request
		"""
		#print "Client %s (#%i) was connected" % (client[0], client[1])
			
		clientRequest = self.recvData(socket, 1024)
		clientID = self.getClientID(clientRequest)
		
		if (clientID):
			clientInstance = self.findClient(clientID)
			
			if clientInstance:
				#print "Client with ID %i is already known" % (clientID)
				HTMLPage = self.checkRequest(clientRequest)
				self.sendPage(socket, HTTP_HEADER_WITHOUT_COOKIE % (str(len(HTMLPage))), HTMLPage)
			else:
				#print "Client with ID %i is expired and deleted" % (clientID)
				HTMLPage = self.getHTMLFile('expired')
				expiration = datetime.datetime.now() - datetime.timedelta(days=1)
				self.sendPage(socket, HTTP_HEADER_WITH_COOKIE % (clientID, expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST"), str(len(HTMLPage))), HTMLPage)
		else:
			self.addClientSemaphore.acquire()
			self.addClient(socket, client)
			self.addClientSemaphore.release()
			#print "Client was added to list"
		
		socket.close()
		for thread in self.activeThreads:
			if thread.name == client[0]:
				self.activeThreads.remove(thread)
	
	def stop(self):
		self.status = False
		self.socket.listen(0)
		del self.addClientSemaphore

	def waitForClient(self):
		return self.socket.accept()

	def sendPage(self, socket, head, page):
		socket.send(head)
		socket.send(page)

	def recvData(self, socket, size):
		return socket.recv(size)

	def getClientID(self, clientRequest):
		"""
		Function parse ID from HTTP head.
		"""

		lines = clientRequest.split('\n')
		
		for line in lines:
			if "Cookie: Golem-ID" in line:
				return int(line[17:])

		return False
    		
	def addClient(self, socket, client):
		"""
		Function adds new client instance to servers clientList
		"""
		#TODO - IDCounter overflow (when server is online for a long time) - Low priority
		expiration = datetime.datetime.now() + datetime.timedelta(hours=1) 
		self.clients.append(Client(self.IDCounter, expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST"), client[0]))

		HTMLPage = self.getHTMLFile('index')
    
		self.sendPage(socket, HTTP_HEADER_WITH_COOKIE % (self.IDCounter, expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST"), str(len(HTMLPage))), HTMLPage)
		self.IDCounter += 1

	def getHTMLFile(self, file):
		try:
			page = open(os.path.normpath(os.path.join(self.pathToHTML, file+'.html')))
			return page.read()
		except:
			if file != 'error404':
				return self.getHTMLFile('error404')
			return "Error"

	def delClient(self, client):
		self.clients.remove(client)

	def findClient(self, ID):
		"""
		Find and return client instance from servers clientList
		"""
		
		for client in self.clients: 
			if client.ID == ID:
				return client

		return False
	
	def checkForInactiveClients(self):
		expiration = datetime.datetime.now()
		for client in self.clients:		
			if client.expiration <= expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST"):
				self.delClient(client)
	
	def printClients(self):
		for client in self.clients:
			print client.ID, " - ", client.expiration, " - ", client.IP