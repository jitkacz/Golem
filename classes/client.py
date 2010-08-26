#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Client(object):
	def __init__(self, ID, expiration, IP): 
		self.ID = ID
		self.IP = IP
		self.expiration = expiration
