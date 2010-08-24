#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
from libs.RepeatTimer import RepeatTimer

from random import randint

from grid.Collisions import Collisions
from grid.Collision import Collision
from grid.Timer import Timer

from grid.createGrid import createGrid

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
	Timer = None
	tTimer = None # thread of timer

	fps = 300

	_grid = []
	_objects = []

	def __init__(self, size=[10,10]):
		"""	Create new instance of Grid. """
		self.setSize(size)

		self.Collisions = Collisions()
		self.Collision = Collision
		self.Timer = Timer(self)

		self.tTimer = RepeatTimer(1.0/self.fps, self.Timer.check)
		self.tTimer.start()

	def __del__(self):
		""" Canceling threads """
		self.tTimer.cancel()

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

	def getObjects(self, pos=None):
		if pos:
			self._cleanPosition(pos)
			return sorted(self._grid[pos[0]][pos[1]], key=lambda o: o.weight)

		return sorted(self._objects, key=lambda o: o.weight)

	def addObject(self, object, position):
		"""
		Function to add object to grid. If object has not set
		variable grid as instance of this grid, it will be set.
		"""

		if object.getGrid() != self:
			return self._setObjectsGrid(object, position)

		self._objects.append(object)
		self.Timer.addChange(position)

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

		if not self.checkPosition(position):
			return False

		return self.Timer.add(object, position)

	def checkPosition(self, position):
		if position[0]<0 or position[1]<0:
			return False

		if position[0]>=self._size[0] or position[1]>=self._size[1]:
			return False

		return True


	def teleport(self, object, position):
		"""
		Function to transport object to some place without
		looking for any way - only teleport it.
		"""
		try:
			objectsOnPosition = self._grid[position[0]][position[1]]
		except IndexError:
			return False

		if not self.checkPosition(position):
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
		object.position = position

		for i, o in enumerate(self._grid[oldPos[0]][oldPos[1]]):
			if o==object:
				self._grid[oldPos[0]][oldPos[1]][i] = None

		self._grid[position[0]][position[1]].append(object)
		self._cleanPosition(position)


	def _cleanPosition(self, position):
		"""
		Remove all 'None' items from position
		"""

		for i, pos in enumerate(self._grid[position[0]][position[1]]):
			if not pos:
				self._grid[position[0]][position[1]].pop(i)

	def randomPosition(self, ban=[]):
		"""
		Generate random position. It doesn't check anything.
		"""

		x = randint(0, self._size[0]-1)
		y = randint(0, self._size[1]-1)

		if (x, y) in ban:
			return self.randomPosition(ban=ban)

		return x, y

	def randomObjectPosition(self, object):
		"""
		Generate correct random position for object
		"""
		patency = self.Collisions.getPatencyOfGridList(object, self.getObjects(), self.getSize())

		p = 0
		while p==0:
			pos = self.randomPosition()
			p = patency[pos[0]][pos[1]]

		return pos

	def getCellSpeed(self, object, position):
		"""
		Return speed of object on the cell
		"""
		try:
			collisions = self.Collisions.getCollisions()[object]
		except:
			return 100

		slower = -1
		objects = self.getObjects(position)

		for collision in collisions:
			if collision.secondaryObject in objects:
				speed = self.Collisions.getCollisionSpeed(collision)

				if speed<slower or slower==-1:
					slower = speed

		if slower==-1:
			slower = 100

		return slower




