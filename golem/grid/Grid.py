#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Grid:
	_size = [10, 10]

	_grid = []

	_objects = []

	def setSize(self, size):
		self._size = size
		self._createGrid()
		return self

	def _createGrid(self):
		self._grid = [[None] * self._size[1]] * self._size[0]

	def getGrid(self):
		return self._grid
