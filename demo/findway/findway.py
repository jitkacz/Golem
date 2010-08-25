#!/usr/bin/env python
#-*- coding:utf-8 -*-

import golem.apps.AppFromConfigFile

def moveGolemOnClick(viewer=None, control=None, **p):
	pos = viewer.getMousePosition()
	control.object.setPosition(pos)

class FindWayApp(golem.apps.AppFromConfigFile):
	config = 'findway.cfg'

	def init(self):
		pass

	def saveEvents(self):
		self.viewer.events['onButtonDown'] = moveGolemOnClick


if __name__=='__main__':
	game = FindWayApp()
	game.run()
	game.quit()
