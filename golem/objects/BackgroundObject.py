#!/usr/bin/env python
#-*- coding:utf-8 -*-

import objects.GroupOfObjects

class BackgroundObject(objects.GroupOfObjects):
	"""
	Class to create many objects to show it as a background
	"""

	def drawObjects(self):
		self.positions = []
		width, height = self._grid.getSize()

		for x in range(width):
			for y in range(height):
				self.positions.append((x, y))

		objects.GroupOfObjects.drawObjects(self)
