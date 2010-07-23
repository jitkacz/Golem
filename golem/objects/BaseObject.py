#!/usr/bin/env python
#-*- coding:utf-8 -*-
from libs.i18n import *

class ObjectException(BaseException):
	pass

class BaseObject(object):
<<<<<<< HEAD
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

=======
>>>>>>> 824af7d... Collisions
	name = ''
	speed = 0

	moveable = False
	position = [0, 0]

	_image = None
	_visible = True
	_grid = None

<<<<<<< HEAD

<<<<<<< HEAD
	def __init__(self, grid=None, image=None, position=(0,0)):
=======
	def __init__(self, grid=None, position=(0,0)):
>>>>>>> 42eb8a9... BaseObject documentation
		"""
		To create new instance of BaseObject.
		"""
		# TODO - check if grid is instance of Grid
		if grid:
			self.setGrid(grid, position)
=======
	_visible = True

	position = [0, 0]
>>>>>>> 824af7d... Collisions

<<<<<<< HEAD
		if image:
			self.setImage(image)

=======
>>>>>>> 42eb8a9... BaseObject documentation
	def setGrid(self, grid, position=(0,0)):
		"""
		Assignment object to grid.
		"""

		# TODO - check if grid is instance of Grid
		self._grid = grid

<<<<<<< HEAD
		if self._grid.addObject(self, position):
			self.position = position
		else:
<<<<<<< HEAD
			return False

<<<<<<< HEAD
<<<<<<< HEAD
	def setGrid(self, grid):
=======
	def getGrid(self):
		return self._grid

	def setGrid(self, grid, position=(0,0)):
		# TODO - check if grid is instance of Grid
>>>>>>> 3a9514f... Documentation to Grid
=======
	def __init__(self, grid=None, position=(0,0)):
		# TODO - check if grid is instance of Grid
		if grid:
			self.setGrid(grid, position)

	def setGrid(self, grid, position=(0,0)):
		# TODO - check if grid is instance of Grid
>>>>>>> 824af7d... Collisions
		self._grid = grid
=======
	def getGrid(self):
		return self._grid
>>>>>>> 5ead219ebd17b91bee4f0d293874d7b597615e63
=======
			raise ObjectException(
				_('Object cant be located to position (%(x)d, %(y)d)' % {'x' : position[0], 'y' : position[1]})
			)

	def getGrid(self):
		return self._grid
>>>>>>> 42eb8a9... BaseObject documentation

<<<<<<< HEAD
	def setPosition(self, position, y=None):
		"""
		Change objects position. If object is not moveable
		it will raise an exception.
		"""
		if type(position) is int:
=======
		if self._grid.addObject(self, position):
			self._setPosition(position)
		else:
			raise ObjectException(_('Object cant be located to position (%(x)d, %(y)d)' % {'x' : position[0], 'y' : position[1]}))

	def _setPosition(self, position, y=None):
		if position is int:
>>>>>>> 824af7d... Collisions
			position = (position, y)
		return position

	def setPosition(self, position, y=None):
		position = self._setPosition(position, y)

		if self.moveable:
<<<<<<< HEAD
			if self._grid.goTo(self, position):
				self.position = position
				return True
			else:
<<<<<<< HEAD
				return False
=======
				raise ObjectException(
					_('Object cant be transported to (%(x)d, %(y)d)' % {'x' : position[0], 'y' : position[1]})
				)
>>>>>>> 42eb8a9... BaseObject documentation
=======
			if(self._grid.goTo(self, position)):
				self.position = position
				return True
			else:
				raise ObjectException(_('Object cant be transported to (%(x)d, %(y)d)' % {'x' : position[0], 'y' : position[1]}))
>>>>>>> 824af7d... Collisions
		else:
			raise ObjectException(_('Object is not moveable'))

	def getPosition(self):
		return (self.position[0], self.position[1])
<<<<<<< HEAD

	def setImage(self, image):
		self._image = image

	def getImage(self):
		return self._image


=======
>>>>>>> 824af7d... Collisions
