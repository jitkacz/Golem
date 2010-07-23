#!/usr/bin/env python
#-*- coding:utf-8 -*-

#import grid.findWay
import grid.Collisions

class Grid(object):
	_size = [10, 10]

	_grid = []

	_objects = []

	def __init__(self, size=[10,10]):
		self.setSize(size)

	def printGrid(self):
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

	def getSize(self):
		return self._size

	def setSize(self, size):
		self._size = size
		self._createGrid()
		return self

	def _createGrid(self):
		self._grid = []
		for i in range(self._size[0]):
			row = []
			for j in range(self._size[1]):
				row.append([None])
			self._grid.append(row)

	def getGrid(self):
		return self._grid

	def addObject(self, object, position):
		self._objects.append(object)

		if self.teleport(object, position):
			return True
		return False

	def getObjects(self):
		return self._objects

	def goTo(self, object, position):
		# TODO - replace it by findWay
		grid.Collisions.getPatencyOfGridList(object, self._objects, self._size)
		return self.teleport(object, position)

	def teleport(self, object, position):
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
		self._cleanPosition(position)
		self._grid[position[0]][position[1]].append(object)
		object.position = position

	def _cleanPosition(self, position):
		for i, pos in enumerate(self._grid[position[0]][position[1]]):
			if not pos:
				self._grid[position[0]][position[1]].pop(i)
