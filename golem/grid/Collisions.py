#!/usr/bin/env python
#-*- coding:utf-8 -*-

from createGrid import createGridForCollisions

class Collisions(object):
	"""
	Static class to saving collisions and get them
	"""

	_collisions = {}

	def __init__(self):
		self._collisions = {}

	def append(self, collision):
		"""
		To append an instance of collision to dictionary.
		"""

		if self._collisions.has_key(collision.primaryObject):
			self._collisions[collision.primaryObject].append(collision)
		else:
			self._collisions[collision.primaryObject] = [collision]

	def checkCollisions(self, primaryObject, secondaryObjects):
		"""
		This function returns True if the primary object can go through
		a cell where are the secondary objects. If it can not, function
		returns False.
		"""

		if not self._collisions.has_key(primaryObject):
			return True

		if not type(secondaryObjects) is list:
			secondaryObjects = [secondaryObjects]

		for collision in self._collisions[primaryObject]:
			if (collision.secondaryObject in secondaryObjects) and \
				(not collision.canGoThrough):
					return False

		return True

	def getPatencyOfGridList(self, primaryObject, objects, gridSize):
		"""
		This function returns a grid with informations about
		patency of cells. Patency is number (bigger or equal to 0).
		If patency is set to 0, then primary object can go through
		this cell.
		"""

		if not self._collisions.has_key(primaryObject):
			return [[100]*gridSize[1]]*gridSize[0]

		# create empty patency grid
		patency = self._createEmptyPatencyGrid(gridSize)

		collisionsSpeed = {}
		for collision in self._collisions[primaryObject]:
			collisionsSpeed[collision.secondaryObject] = self._getCollisionSpeed(collision)

		# checking all objects and saving their patency
		for object in objects:
			if collisionsSpeed.has_key(object):
				pos = object.getPosition()

				# saving the smallest patency
				if patency[pos[0]][pos[1]] > collisionsSpeed[object]:
					patency[pos[0]][pos[1]] = collisionsSpeed[object]

		return patency

	def _createEmptyPatencyGrid(self, size):
		"""
		Function creates empty grid with values set to 100.
		"""
		return createGridForCollisions(size)

	def _getCollisionSpeed(self, collision):
		if not collision.canGoThrough:
			return 0
		else:
			return collision.speed

	def getCollisions(self):
		return self._collisions
