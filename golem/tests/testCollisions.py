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
		self.secondary = objects.MoveableObject(self.grid, position=(1, 0))

	def test_createPrimitiveTrueCollision(self):
		self.grid = grid.Grid()

		collision = self.grid.Collision(self.primary, self.secondary, result=True)
		self.grid.Collisions.append(collision)
		# TODO - It is possible you some method assertTrue, I havent documentation
		self.assertEqual(
			True,
			self.primary.setPosition(self.secondary.getPosition())
		)

	def test_createPrimitiveFalseCollision(self):
		collision = self.grid.Collision(self.primary, self.secondary, result=False)
		self.grid.Collisions.append(collision)

		if not self.primary.setPosition(self.secondary.getPosition()):
			self.assertEqual(True, True)
		else:
			self.assertEqual(True, False)

	def test_checkingEmptyCollision(self):
		# TODO - It is possible you some method assertTrue, I havent documentation
		self.assertEqual(
			True,
			self.grid.Collisions.checkCollisions(self.primary, self.secondary)
		)

	def test_checkingEmptyCollisions(self):
		# TODO - It is possible you some method assertTrue, I havent documentation
		list = []
		for i in range(10):
			list.append(objects.MoveableObject(self.grid))

		self.assertEqual(
			True,
			self.grid.Collisions.checkCollisions(self.primary, list)
		)

	def test_checkPatencyOfGridList_FalseCollision(self):
		collision = self.grid.Collision(self.primary, self.secondary, result=False)
		self.grid.Collisions.append(collision)

		gridPatency = [[100], [0], [100]]

		self.assertEqual(
			self.grid.Collisions.getPatencyOfGridList(self.primary, self.grid.getObjects(), self.grid.getSize()),
			gridPatency
		)

	def test_checkPatencyOfGridList_SlowedDownCollision(self):
		collision = self.grid.Collision(self.primary, self.secondary, result=True, speed=50)
		self.grid.Collisions.append(collision)

		gridPatency = [[100], [50], [100]]

		self.assertEqual(
			self.grid.Collisions.getPatencyOfGridList(self.primary, self.grid.getObjects(), self.grid.getSize()),
			gridPatency
		)

	def test_CollisionsInGridArentEqual(self):
		gridA = grid.Grid()
		gridB = grid.Grid()

		gridA.Collisions.append(grid.Collision(1,2))

		self.assertNotEqual(
			gridA.Collisions.getCollisions(),
			gridB.Collisions.getCollisions()
		)
