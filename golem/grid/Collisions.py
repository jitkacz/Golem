#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy

class Collisions(object):
	"""
	Static class to saving collisions and get them
	"""

	_collisions = {}

<<<<<<< HEAD
	def __init__(self):
		self._collisions = {}

	def append(self, collision):
=======
	def appendCollision(self, collision):
>>>>>>> 9407e1d... Add Collisions functionality
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

		if type(secondaryObjects) != list:
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
		patency = numpy.zeros(size, dtype=int)+100
		return patency.tolist()

	def _getCollisionSpeed(self, collision):
		if not collision.canGoThrough:
			return 0
		else:
			return collision.speed

<<<<<<< HEAD
	def getCollisions(self):
		return self._collisions

=======
# change Collisions to only-static
Collisions = Collisions()


class Collision(object):
	"""
	Public class for creating types of collisions.
	"""

    # Instances of objects
	primaryObject = None
	secondaryObject = None

	# boolean, if primary object can go through cell with secondary object
	canGoThrough = True

	# speed in %
	speed = 100

	def __init__(self, primaryObject, secondaryObject, canGoThrough=True, speed=100):
		"""
		To creating new collision and append it to
		Collisions dictionary.
		"""
		self.primaryObject = primaryObject
		self.secondaryObject = secondaryObject

		self.setCanGoThrough(canGoThrough)
		self.setSpeed(speed)

		Collisions.appendCollision(self)

	def setCanGoThrough(self, value):
		"""
		Functions to set if collision can be passed or not.
		"""
		if type(value) is bool:
			self.canGoThrough = value
		return self

	def setSpeed(self, speed):
		"""
		Function to set speed in percentage.

		=  0	is the same as setCanGoThrough(False)
		< 100	is for retardation
		= 100	is for default objects speed
		> 100	is for speed up

		"""
		if type(speed) is int:
			self.speed = speed
		return self

	def onCollision(self):
		"""
		Function which is called within collision.
		It can do lot of things. For example destroy one of
		objects, change objects images etc.
		"""
		pass
>>>>>>> 9407e1d... Add Collisions functionality
