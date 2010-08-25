#!/usr/bin/env python
#-*- coding:utf-8 -*-

from classes.server import Server

if __name__ == "__main__":
	server = Server('', 8080)

	print "Server started!"

	server.start()
	clientSocket.close()

	print "Server stop!"


