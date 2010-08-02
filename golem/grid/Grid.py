#!/usr/bin/env python
#-*- coding:utf-8 -*-

#import grid.findWay
import time
from random import randint

from grid.Collisions import Collisions
from grid.Collision import Collision
from grid.Changes import Changes

from grid.createGrid import createGrid
from grid.findWay import findWay

class Grid(object):
	"""
	Class to create a grid for saving objects.

	How to create new grid
	----------------------
	>> mygrid = Grid() # with default size 10x10
	>> mygrid.setSize([5, 3]) # change grid size to 5x3

	Size of a grid is possible to set within initialization
	>> mygrid = Grid([5, 3])

	"""

	viewer = None

	Collisions = None
	Collision = None
	Changes = None

	_size = [0, 0]
	_grid = []
	_objects = []

	def __init__(self, size=[10,10]):
		"""	Create new instance of Grid. """
		self.Collisions = Collisions()
		self.Collision = Collision
		self.Changes = Changes()

		self.setSize(size)

	def setSize(self, size):
		""" Set new size of grid and refresh objects at grid. """
		# TODO - check if is size list or tuple
		# TODO - add new parametr like in BaseObject.setPosition(position, y=None)

		self._size = size
		self._createGrid(size)
		self._refreshGrid()

		return self

	def _createGrid(self, size):
		self._grid = createGrid(size)

	def _refreshGrid(self):
		"""
		Function to refresh objects positions on a grid.
		It is called after re-size grid.
		"""
		pass

	def getSize(self):
		return self._size

	def getGrid(self):
		return self._grid

	def getObjects(self):
		return self._objects

	def addObject(self, object, position):
		"""
		Function to add object to grid. If object has not set
		variable grid as instance of this grid, it will be set.
		"""

		if object.getGrid() != self:
			return self._setObjectsGrid(object, position)

		self._objects.append(object)

		if self.teleport(object, position):
			return True

		return False

	def _setObjectsGrid(self, object, position):
		"""
		Set this instance of grid to object.
		"""
		try:
			object.setGrid(self, position)
		except:
			return False
		return True

	def goTo(self, object, position):
		"""
		Function to transport the object along the shortest way.
		"""
		start = object.getPosition()
		table = self.Collisions.getPatencyOfGridList(object, self._objects, self._size)
		finish = position

		# TODO - make some manager of changes on grid and of the speed of objects
		#print findWay(start, finish, table)

		# TODO - replace it by findWay
		return self.teleport(object, position)

	def teleport(self, object, position):
		"""
		Function to transport object to some place without
		looking for any way - only teleport it.
		"""
		try:
			objectsOnPosition = self._grid[position[0]][position[1]]
		except IndexError:
			return False

		if objectsOnPosition:
			if self.Collisions.checkCollisions(object, objectsOnPosition):
				try:
					self._cleanObjectFromOldPosition(object.getPosition())
				except:
					pass
			else:
				return False

		self._moveObjectToPosition(object, position)
		return True

	def _moveObjectToPosition(self, object, position):
		"""
		Change object position - remove it from old and append
		to the new.
		"""

		oldPos = object.getPosition()

		for i, o in enumerate(self._grid[oldPos[0]][oldPos[1]]):
			if o==object:
				self._grid[oldPos[0]][oldPos[1]][i] = None

		self._cleanPosition(position)
		self._grid[position[0]][position[1]].append(object)
		object.position = position

	def _cleanPosition(self, position):
		"""
		Remove all 'None' items from position
		"""

		for i, pos in enumerate(self._grid[position[0]][position[1]]):
			if not pos:
				self._grid[position[0]][position[1]].pop(i)

	def randomPosition(self):
		"""
		Generate random position. It doesn't check anything.
		"""

		x = randint(0, self._size[0]-1)
		y = randint(0, self._size[1]-1)

		return x, y
