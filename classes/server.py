#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re
import os, socket, datetime

from classes.client import Client

HTTP_HEADER = "HTTP/1.1 200 OK\nContent-Type: text/html; charset=UTF-8\nSet-Cookie: Golem-ID=%i;expires=%s\nContent-Length: %s\n\n"

class Server(object):
	status = False
	pathToHTML = 'html'

	def __init__(self, host="localhost", port=8080):
		self.clients = []
		self.IDCounter = 0

		self._createSocket(host, port)

	def _createSocket(self, host, port):
		self.socket = socket.socket()
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.socket.bind((host, port))

	def __del__(self):
		self.socket.close()

	def start(self):
		self.status = True
		self.socket.listen(1)

		self._run()

	def _run(self):
		while self.status:
			print "Server wait for client"

			socket, client = self.waitForClient()
			print "Client %s (#%i) was connected" % (client[0], client[1])

			clientID = self.getClientID(self.recvData(socket, 1024))
			if (clientID >= 0):
				#TODO - If client have cookie, but server havent his client instance (server restarted and cookies dont expired)
				clientInstance = self.findClient(clientID)

				if clientInstance:
					print "Client with ID %i is already known" % (clientID)
					HTMLPage = self.getHTMLFile('index')
					self.sendPage(socket, HTMLPage)
				else:
					self.addClient(socket)
					print "Client was added to list"

			print ""
			socket.close()

	def stop(self):
		self.status = False
		self.socket.listen(0)

	def waitForClient(self):
		return self.socket.accept()

	def sendPage(self, socket, page):
		expiration = datetime.datetime.now() + datetime.timedelta(hours=1)
		socket.send(HTTP_HEADER % (self.IDCounter, expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST"), str(len(page))))
		socket.send(page)

	def recvData(self, socket, size):
		return socket.recv(size)

	def getClientID(self, clientRequest):
		"""
		Function parse ID from HTTP head.

		@TODO Maybe, it will be better and easier, when it'll be match by
		regular expresion (module re - http://docs.python.org/library/re.html)
		"""

		lines = clientRequest.split('\n')

		print lines

		for line in lines:
			if "Cookie: Golem-ID" in line:
				return int(line[17]+line[18])

		return False


	def addClient(self, socket):
		"""
		Function adds new client instance to servers clientList
		"""

		self.IDCounter += 1
		self.clients.append(Client(self.IDCounter))

		HTMLPage = self.getHTMLFile('added')

		self.sendPage(socket, HTMLPage)

	def getHTMLFile(self, file):
		try:
			page = open(os.path.normpath(os.path.join(self.pathToHTML, file+'.html')))
			return page.read()
		except:
			if file!='error404':
				return self.getHTMLFile('error404')
			return "Error"

	def delClient(self):
		pass

	def findClient(self, ID):
		"""
		Find and return client instance from servers clientList
		"""
		for client in self.clients:
			if client.ID == ID:
				return client

		return False

	def checkRequest(self, clientRequest):
		"""
		Read request from skript from browser
		"""
		pass

	def printClients(self):
		for client in self.clients:
			print client.ID
