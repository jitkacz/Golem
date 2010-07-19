#!/usr/bin/env python
#-*- coding:utf-8 -*-

from libs.i18n import *

import unittest
import HTMLTestRunner

import objects.BaseObject
import grid

class TestBaseObject(unittest.TestCase):
	def setUp(self):
		self.object = objects.BaseObject()
		self.grid = grid.Grid().setSize([20,20])
		self.object.setGrid(self.grid)

	def test_moveObject(self):
		self.object.moveable = True
		self.object.setPosition([10, 1])

if __name__ == '__main__':
	HTMLTestRunner.main()
