#!/usr/bin/env python
#-*- coding:utf-8 -*-

import golem.apps.AppFromConfigFile

class FindWayApp(golem.apps.AppFromConfigFile):
	config = 'findway.cfg'

	def beforeRun(self):
		self.objectRelocate(self._objects['golem'])
		self.objectRelocate(self._objects['food'])

	def setEvents(self):
		self.viewer.events['onButtonDown'] = self.moveGolemOnClick

	def setCollisions(self):
		self.collisions['objectRelocate'] = self.objectRelocate
		self.collisions['golemAteFood'] = self.golemAteFood

	def moveGolemOnClick(self, control=None, **p):
		pos = self.viewer.getMousePosition()
		control.object.setPosition(pos)

	def golemAteFood(self, primary=None, secondary=None, **params):
		while not self.grid.teleport(secondary, self.grid.randomPosition([secondary.getPosition])):
			pass

	def objectRelocate(self, primary=None, **params):
		while not self.grid.teleport(primary, self.grid.randomPosition([primary.getPosition])):
			pass


if __name__=='__main__':
	game = FindWayApp()
	game.run()
	game.quit()
