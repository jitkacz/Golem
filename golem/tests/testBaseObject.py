#!/usr/bin/env python
#-*- coding:utf-8 -*-

from libs.i18n import *

import unittest

import objects.BaseObject
import grid

class testBaseObject(unittest.TestCase):
	def setUp(self):
		self.object = objects.BaseObject()
		self.grid = grid.Grid().setSize([400,400])
		self.object.setGrid(self.grid)

<<<<<<< HEAD
<<<<<<< HEAD
	def test_objectsArentEqual(self):
=======
	def test_objectsIsntEqual(self):
>>>>>>> 824af7d... Collisions
=======
	def test_objectsArentEqual(self):
>>>>>>> 5ead219... Lot of fixes
		"""
		check
		"""
		secondObject = objects.BaseObject()
		self.assertNotEqual(self.object, secondObject)

	def test_locateToGrid(self):
		pass

	def test_moveObject(self):
		self.object.moveable = True
		for i in range(400):
			self.object.setPosition([i, i])

