#!/usr/bin/env python
#-*- coding:utf-8 -*-
from libs.i18n import *

class ObjectException(BaseException):
	pass

class BaseObject(object):
	"""
	BaseObject is parent of all objects. In default it
	isnt moveable, but it is visible.

	How to create new BaseObject
	----------------------------
	>> myobject = BaseObject()

	If you have an instance of Grid, you can localizate it:
	>> mygrid = Grid()
	>> myobject = BaseObject(grid=mygrid, position=[4,2])

	To move with BaseObject, you must set it moveable first
	(or create this object as MoveableObject):
	>> myobject.setPosition(2, 3) # WRONG!

	>> myobject.moveable = True
	>> myobject.setPosition(2, 3) # CORRECT

	If you dont want to set object moveable, you must use Grid
	method teleport():
	>> mygrid.teleport(myobject, [1,3])

	"""

	name = ''
	speed = 0

	moveable = False
	position = [0, 0]

	_image = None
	_visible = True
	_grid = None


	def __init__(self, grid=None, image=None, position=(0,0)):
		"""
		To create new instance of BaseObject.
		"""
		# TODO - check if grid is instance of Grid
		if grid:
			self.setGrid(grid, position)

		if image:
			self.setImage(image)

	def setGrid(self, grid, position=(0,0)):
		"""
		Assignment object to grid.
		"""

		# TODO - check if grid is instance of Grid
		self._grid = grid

		if self._grid.addObject(self, position):
			self.position = position
		else:
			return False

	def getGrid(self):
		return self._grid

	def setPosition(self, position, y=None):
		"""
		Change objects position. If object is not moveable
		it will raise an exception.
		"""
		if type(position) is int:
			position = (position, y)

		if self.moveable:
			if self._grid.goTo(self, position):
				return True
			else:
				return False
		else:
			raise ObjectException(_('Object is not moveable'))

	def getPosition(self):
		return (self.position[0], self.position[1])

	def setImage(self, image):
		self._image = image

	def getImage(self):
		return self._image


