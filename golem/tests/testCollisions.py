#!/usr/bin/env python
#-*- coding:utf-8 -*-

from libs.i18n import *

import unittest

import objects.BaseObject
import grid


class testCollisons(unittest.TestCase):
	primary = None
	secondary = None

	def setUp(self):
		self.grid = grid.Grid([3, 1])

		self.primary = objects.MoveableObject(self.grid)
		self.secondary = objects.MoveableObject(self.grid, (1, 0))

	def test_createPrimitiveTrueCollision(self):
		self.grid = grid.Grid()

		collision = grid.Collision(self.primary, self.secondary, canGoThrough=True)
		# TODO - It is possible you some method assertTrue, I havent documentation
		self.assertEqual(
			True,
			self.primary.setPosition(self.secondary.getPosition())
		)

	def test_createPrimitiveFalseCollision(self):
		self.grid = grid.Grid()
		collision = grid.Collision(self.primary, self.secondary, canGoThrough=False)

		try:
			self.primary.setPosition(self.secondary.getPosition())
		except:
			self.assertEqual(True, True)
		else:
			self.assertEqual(True, False)

	def test_checkingEmptyCollision(self):
		# TODO - It is possible you some method assertTrue, I havent documentation
		self.assertEqual(
			True,
			grid.Collisions.checkCollisions(self.primary, self.secondary)
		)

	def test_checkingEmptyCollisions(self):
		# TODO - It is possible you some method assertTrue, I havent documentation
		list = []
		for i in range(10):
			list.append(objects.MoveableObject(self.grid))

		self.assertEqual(
			True,
			grid.Collisions.checkCollisions(self.primary, list)
		)

	def test_checkPatencyOfGridList_FalseCollision(self):
		collision = grid.Collision(self.primary, self.secondary, canGoThrough=False)

		gridPatency = [[100], [0], [100]]

		self.assertEqual(
			grid.Collisions.getPatencyOfGridList(self.primary, self.grid.getObjects(), self.grid.getSize()),
			gridPatency
		)

	def test_checkPatencyOfGridList_SlowedDownCollision(self):
		collision = grid.Collision(self.primary, self.secondary, canGoThrough=True, speed=50)

		gridPatency = [[100], [50], [100]]

		self.assertEqual(
			grid.Collisions.getPatencyOfGridList(self.primary, self.grid.getObjects(), self.grid.getSize()),
			gridPatency
		)
