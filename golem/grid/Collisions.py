#!/usr/bin/env python
#-*- coding:utf-8 -*-

from createGrid import createGridForCollisions

class Collisions(object):
	"""
	Class to saving collisions and get them
	"""

	def __init__(self):
		self._collisions = {}

	def append(self, collision):
		"""
		To append an instance of collision to dictionary.
		"""

		if self._collisions.has_key(collision.primaryObjectID):
			self._collisions[collision.primaryObjectID].append(collision)
		else:
			self._collisions[collision.primaryObjectID] = [collision]


	def checkCollisions(self, primaryObject, secondaryObjects):
		"""
		This function returns True if the primary object can go through
		a cell where are the secondary objects. If it can not, function
		returns False.
		"""

		if not self._collisions.has_key(primaryObject.id()):
			return True

		if not type(secondaryObjects) is list:
			secondaryObjects = [secondaryObjects]

		secondaryObjects = self.objectsInstancesToIDs(secondaryObjects)

		for collision in self._collisions[primaryObject.id()]:
			if (collision.secondaryObjectID in secondaryObjects) and \
				(not collision.result):
					return False

		return True

	def objectsInstancesToIDs(self, objects):
		ret = []
		for o in objects:
			ret.append(o.id())
		return ret

	def getPatencyOfGridList(self, primaryObject, objects, gridSize):
		"""
		This function returns a grid with informations about
		patency of cells. Patency is number (bigger or equal to 0).
		If patency is set to 0, then primary object can go through
		this cell.
		"""

		if not self._collisions.has_key(primaryObject.id()):
			return [[100]*gridSize[1]]*gridSize[0]

		# create empty patency grid
		patency = self._createEmptyPatencyGrid(gridSize)

		collisionsSpeed = {}
		for collision in self._collisions[primaryObject.id()]:
			collisionsSpeed[collision.secondaryObjectID] = self.getCollisionSpeed(collision)

		# checking all objects and saving their patency
		for object in objects:
			if collisionsSpeed.has_key(object.id()):
				pos = object.getPosition()

				# saving the smallest patency
				if patency[pos[0]][pos[1]] > collisionsSpeed[object.id()]:
					patency[pos[0]][pos[1]] = collisionsSpeed[object.id()]

		return patency

	def _createEmptyPatencyGrid(self, size):
		"""
		Function creates empty grid with values set to 100.
		"""
		return createGridForCollisions(size)

	def getCollisionSpeed(self, collision):
		if not collision.result:
			return 0
		else:
			return collision.speed

	def getCollisions(self):
		return self._collisions

	def runOnCollision(self, object, objects):
		if not self._collisions.has_key(object.id()):
			return False

		for collision in self._collisions[object.id()]:
			if (collision.secondaryObjectID in objects):
				collision.onCollision(primary=object, secondary=collision.secondaryObject)


