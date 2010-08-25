#!/usr/bin/env python
#-*- coding:utf-8 -*-

class BaseApp(object):
	grid = None
	viewer = None

	def __init__(self):
		self.init()

	def init(self):
		pass

	def setCollisions(self):
		pass

	def setEvents(self):
		pass

	def beforeRun(self):
		pass

	def run(self):
		self.setEvents()

		self.beforeRun()
		self.viewer.start()
		self.afterRun()

		self.beforeQuit()
		self.quit()

	def afterRun(self):
		pass

	def beforeQuit(self):
		pass

	def quit(self):
		self.viewer.stop()
		try:
			self.grid.tTimer.cancel()
		except:
			pass


