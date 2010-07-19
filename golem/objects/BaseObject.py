#!/usr/bin/env python
#-*- coding:utf-8 -*-
from libs.i18n import *

class ObjectException(BaseException):
	pass

class BaseObject:
	name = ''
	speed = 5

	moveable = False

	_image = None

	_visible = False

	_position = [0, 0]


	_grid = None


	def __init__(self):
		pass

	def setGrid(self, grid):
		self._grid = grid

	def setPosition(self, position):
		if self.moveable:
			if(self._grid.goTo(self, position)):
				self._position = position
		else:
			raise ObjectException(_('Object is not moveable')), self


	def getPosition(self):
		return {'x':self._position[0], 'y':self._position[1]}
