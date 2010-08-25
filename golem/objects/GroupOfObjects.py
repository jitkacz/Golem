#!/usr/bin/env python
#-*- coding:utf-8 -*-

import objects.BaseObject

class GroupOfObjects(object):
	"""
	Class to create many objects to show it as a background
	"""

	_grid = None
	_image = None

	count = 0
	positions = None

	def __init__(self, grid=None, image=None, **params):
		self._objects = []

		if grid:
			self.setGrid(grid)

		if image:
			self.setImage(image)

	def __setattr__(self, name, value):
		self.__dict__[name] = value
		for o in self._objects:
			o.set({name:value})

	def setGrid(self, grid):
		self._grid = grid
		self.drawObjects()

	def id(self):
		return self

	def drawObjects(self):
		if not self.positions:
			self.positions = []
			for i in range(self.count):
				self.positions.append(self._grid.randomPosition())

		if not type(self.positions) is list:
			self.positions = self.positionsToList(self.positions)

		for position in self.positions:
			o = objects.BaseObject(grid=self._grid, image=self._image, position=position)
			o.uid = self.id()
			self._objects.append(o)

	def positionsToList(self, str):
		positions = str.split(';')
		for i, position in enumerate(positions):
			if not ',' in position:
				positions.pop(i)
				continue

			positions[i] = [int(n) for n in position.split(',')]

		return positions

	def set(self, values):
		if not type(values) is dict:
			return False

		self.__dict__.update(values)
		self.count = int(self.count)
		self.setGrid(self._grid)

	def setImage(self, image):
		self._image = image

		for o in self._objects:
			o.setImage(image)

