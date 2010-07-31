#!/usr/bin/env python
#-*- coding:utf-8 -*-

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
