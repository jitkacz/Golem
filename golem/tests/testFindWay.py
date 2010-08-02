#!/usr/bin/env python
#-*- coding:utf-8 -*-

from libs.i18n import *

import unittest

from grid.findWay import findWay

class testFindWay(unittest.TestCase):
	def setUp(self):
		pass

	def test_finishIsBlocked(self):
		table = [[100, 100, 0]]
		start = [0,0]
		finish = [2,0]

		self.assertEqual(
			findWay(start, finish, table),
			False
		)

	def test_cleanWay(self):
		table = [[100, 100, 100]]
		start = [0,0]
		finish = [2,0]

		self.assertEqual(
			findWay(start, finish, table),
			[[1, 0], [2, 0]]
		)

	def test_way1(self):
		table = [
		[100, 100, 100, 100],
		[100, 100, 100, 100],
		[100, 100, 100, 100],
		[100, 100, 100, 100],
		]
		start = [0,0]
		finish = [3,3]

		self.assertEqual(
			findWay(start, finish, table),
			[[1, 0], [1, 1], [2, 1], [2, 2], [3, 2], [3, 3]]
		)

	def test_way2(self):
		table = [
		[100,   0, 100, 100],
		[100,   0, 100, 100],
		[100,   0, 100, 100],
		[100, 100, 100, 100],
		]
		start = [0,0]
		finish = [3,3]

		self.assertEqual(
			findWay(start, finish, table),
			[[0, 1], [0, 2], [0, 3], [1, 3], [2, 3], [3, 3]]
		)

	def test_way3(self):
		table = [
		[100,  10, 100, 100],
		[100, 120, 100, 100],
		[100,  10, 100, 100],
		[100, 100, 100, 100],
		]
		start = [0,0]
		finish = [3,3]

		self.assertEqual(
			findWay(start, finish, table),
			[[0, 1], [1, 1], [2, 1], [2, 2], [3, 2], [3, 3]]
		)

	def test_way4(self):
		table = [
		[100,  200, 100, 100],
		[100,  10, 100, 100],
		[  0,  10, 100, 100],
		[100, 100, 100, 100],
		]
		start = [0,0]
		finish = [3,3]

		self.assertEqual(
			findWay(start, finish, table),
			[[1, 0], [2, 0], [2, 1], [2, 2], [3, 2], [3, 3]]
		)

	def test_way5(self):
		table = [
		[100,  100, 100, 100],
		[100,    0,   0, 100],
		[  0,    0, 100, 100],
		[100,    0,   0,   0],
		]
		start = [0,0]
		finish = [2,2]

		self.assertEqual(
			findWay(start, finish, table),
			[[1, 0], [2, 0], [3, 0], [3, 1], [3, 2], [2, 2]]
		)

	def test_way6(self):
		table = [
		[  0,    0,   0,   0,   0,   0,   0, 100],
		[  0,  100, 100, 100, 100,   0,   0, 100],
		[100,  100,   0,   0, 100, 100,   0, 100],
		[  0,    0,   0,   0,   0, 100, 100, 100],
		]
		start = [0,2]
		finish = [7,0]

		self.assertEqual(
			findWay(start, finish, table),
			[[1, 2], [1, 1], [2, 1], [3, 1], [4, 1], [4, 2], [5,2], [5,3], [6,3], [7,3], [7,2], [7,1], [7,0]]
		)

	def test_way6(self):
		table = [
		[  0,    0,   0,   0,   0,   0,   0, 100],
		[  0,  100, 100, 100, 100,   0,   0, 100],
		[100,  100,   0,   0, 100, 100,   0, 100],
		[  0,  100, 100, 100, 100, 100, 100, 100],
		]
		start = [0,2]
		finish = [7,0]

		self.assertEqual(
			findWay(start, finish, table),
			[[1, 2], [1, 3], [2, 3], [3, 3], [4, 3], [5,3], [6,3], [7,3], [7,2], [7,1], [7,0]]
		)




