#!/usr/bin/env python
#-*- coding:utf-8 -*-
from libs.i18n import *

class ObjectException(BaseException):
	pass

class BaseObject(object):
	name = ''
	speed = 0

	moveable = False

	_image = None

	_visible = True

	position = [0, 0]


	_grid = None


	def __init__(self, grid=None, position=(0,0)):
		# TODO - check if grid is instance of Grid
		if grid:
			self.setGrid(grid, position)

	def setGrid(self, grid, position=(0,0)):
		# TODO - check if grid is instance of Grid
		self._grid = grid

		if self._grid.addObject(self, position):
			self._setPosition(position)
		else:
			raise ObjectException(_('Object cant be located to position (%(x)d, %(y)d)' % {'x' : position[0], 'y' : position[1]}))

	def _setPosition(self, position, y=None):
		if position is int:
			position = (position, y)
		return position

	def setPosition(self, position, y=None):
		position = self._setPosition(position, y)

		if self.moveable:
			if(self._grid.goTo(self, position)):
				self.position = position
				return True
			else:
				raise ObjectException(_('Object cant be transported to (%(x)d, %(y)d)' % {'x' : position[0], 'y' : position[1]}))
		else:
			raise ObjectException(_('Object is not moveable'))

	def getPosition(self):
		return (self.position[0], self.position[1])
