#!/usr/bin/env python
#-*- coding:utf-8 -*-

class BaseControl(object):
	events = {}

	def __init__(self, app):
		self.app = app
		self.setEvents()

	def setEvents(self):
		pass

	def setObject(self, object):
		self.object = object

	def getList(self):
		return self.events
