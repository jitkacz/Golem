#!/usr/bin/env python
#-*- coding:utf-8 -*-

import golem.apps.AppFromConfigFile

class SnakeApp(golem.apps.AppFromConfigFile):
	config = 'snake.cfg'

	def init(self):
		pass



if __name__=='__main__':
	game = SnakeApp()
	game.run()
	game.quit()
