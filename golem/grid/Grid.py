#!/usr/bin/env python
#-*- coding:utf-8 -*-

#import grid.findWay
import grid.Collisions

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


	_size = [0, 0]
	_grid = []
	_objects = []

	def __init__(self, size=[10,10]):
		"""	Create new instance of Grid. """
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
		self._grid = []

		for i in range(size[0]):
			row = []

			for j in range(size[1]):
				row.append([None])

			self._grid.append(row)

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

	def printGrid(self):
		"""
		Show grid as a text table. Objects are showed as five
		chars of their place in memory

		It is very ugly function, in next commit I will remove it.
		"""
		string = "\t"
		for i in range(self._size[0]):
			string += str(i)+"\t"
		print string

		for i in range(self._size[1]):
			string = str(i)+"\t"
			for j in range(self._size[0]):
				cell = self._grid[j][i]
				if not cell[0] and len(cell)==1:
					cell = ''
				else:
					cell = str(cell)[-7:-2]
				string += cell + "\t"
			print string

	def goTo(self, object, position):
		"""
		Function to transport the object along the shortest way.
		"""
		#grid.Collisions.getPatencyOfGridList(object, self._objects, self._size)
		# TODO - replace it by findWay
		return self.teleport(object, position)

	def teleport(self, object, position):
		"""
		Function to transport object to some place without
		looking for any way - only teleport it.
		"""
		objectsOnPosition = self._grid[position[0]][position[1]]

		if objectsOnPosition:
			if grid.Collisions.checkCollisions(object, objectsOnPosition):
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
