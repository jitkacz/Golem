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

<<<<<<< HEAD
	def setGrid(self, grid):
=======
	def getGrid(self):
		return self._grid

	def setGrid(self, grid, position=(0,0)):
		# TODO - check if grid is instance of Grid
>>>>>>> 3a9514f... Documentation to Grid
		self._grid = grid

	def setPosition(self, position, y=None):
		if position is int:
			position = (position, y)

		if self.moveable:
			if(self._grid.goTo(self, position)):
				self._position = position
			else:
				raise ObjectException(_('Object cant be transported to (%i, %i)', position[0], position[1]))
		else:
			raise ObjectException(_('Object is not moveable'))


	def getPosition(self):
		return {'x':self._position[0], 'y':self._position[1]}
