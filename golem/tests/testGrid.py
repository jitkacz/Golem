#!/usr/bin/env python
#-*- coding:utf-8 -*-

import unittest, random
import grid

from libs.i18n import *

class TestGrid(unittest.TestCase):
	def setUp(self):
		self.grid = grid.Grid()

	def test_setSize(self):
		x = random.randint(1000,2000)
		y = random.randint(1000,2000)

		self.grid.setSize([x, y])

		self.assertEqual(
			len(self.grid.getGrid()),
			x
		)

		self.assertEqual(
			len(self.grid.getGrid()[0]),
			y
		)

	def test_gridsArentEqual(self):
		self.assertNotEqual(
			grid.Grid(),
			grid.Grid()
		)






