#!/usr/bin/env python
#-*- coding:utf-8 -*-

from libs.i18n import *

import unittest

import objects.BaseObject
import grid

class testBaseObject(unittest.TestCase):
	def setUp(self):
		self.object = objects.BaseObject()
		self.grid = grid.Grid().setSize([10,10])
		self.object.setGrid(self.grid)

	def test_objectsArentEqual(self):
		secondObject = objects.BaseObject()
		self.assertNotEqual(self.object, secondObject)

	def test_locateToGrid(self):
		pass

	def test_moveObject(self):
		self.object.moveable = True
		self.object.setPosition([5, 5])

