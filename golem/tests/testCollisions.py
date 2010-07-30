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
<<<<<<< HEAD
<<<<<<< HEAD
		self.secondary = objects.MoveableObject(self.grid, position=(1, 0))
=======
		self.secondary = objects.MoveableObject(self.grid, (1, 0))
>>>>>>> 902d453... Some tests
=======
		self.secondary = objects.MoveableObject(self.grid, position=(1, 0))
>>>>>>> 5ead219... Lot of fixes

	def test_createPrimitiveTrueCollision(self):
		self.grid = grid.Grid()

<<<<<<< HEAD
<<<<<<< HEAD
		collision = self.grid.Collision(self.primary, self.secondary, canGoThrough=True)
=======
		collision = grid.Collision(self.primary, self.secondary, canGoThrough=True)
>>>>>>> 902d453... Some tests
=======
		collision = self.grid.Collision(self.primary, self.secondary, canGoThrough=True)
>>>>>>> 5ead219... Lot of fixes
		# TODO - It is possible you some method assertTrue, I havent documentation
		self.assertEqual(
			True,
			self.primary.setPosition(self.secondary.getPosition())
		)

	def test_createPrimitiveFalseCollision(self):
<<<<<<< HEAD
<<<<<<< HEAD
		collision = self.grid.Collision(self.primary, self.secondary, canGoThrough=False)
		self.grid.Collisions.append(collision)
		self.grid.Collisions.getCollisions()

		if not self.primary.setPosition(self.secondary.getPosition()):
=======
		self.grid = grid.Grid()
		collision = grid.Collision(self.primary, self.secondary, canGoThrough=False)

		try:
			self.primary.setPosition(self.secondary.getPosition())
		except:
>>>>>>> 902d453... Some tests
=======
		collision = self.grid.Collision(self.primary, self.secondary, canGoThrough=False)
		self.grid.Collisions.append(collision)
		self.grid.Collisions.getCollisions()

		if not self.primary.setPosition(self.secondary.getPosition()):
>>>>>>> 5ead219... Lot of fixes
			self.assertEqual(True, True)
		else:
			self.assertEqual(True, False)

	def test_checkingEmptyCollision(self):
		# TODO - It is possible you some method assertTrue, I havent documentation
		self.assertEqual(
			True,
<<<<<<< HEAD
<<<<<<< HEAD
			self.grid.Collisions.checkCollisions(self.primary, self.secondary)
=======
			grid.Collisions.checkCollisions(self.primary, self.secondary)
>>>>>>> 902d453... Some tests
=======
			self.grid.Collisions.checkCollisions(self.primary, self.secondary)
>>>>>>> 5ead219... Lot of fixes
		)

	def test_checkingEmptyCollisions(self):
		# TODO - It is possible you some method assertTrue, I havent documentation
		list = []
		for i in range(10):
			list.append(objects.MoveableObject(self.grid))

		self.assertEqual(
			True,
<<<<<<< HEAD
<<<<<<< HEAD
			self.grid.Collisions.checkCollisions(self.primary, list)
		)

	def test_checkPatencyOfGridList_FalseCollision(self):
		collision = self.grid.Collision(self.primary, self.secondary, canGoThrough=False)
		self.grid.Collisions.append(collision)
=======
			grid.Collisions.checkCollisions(self.primary, list)
		)

	def test_checkPatencyOfGridList_FalseCollision(self):
		collision = grid.Collision(self.primary, self.secondary, canGoThrough=False)
>>>>>>> 902d453... Some tests
=======
			self.grid.Collisions.checkCollisions(self.primary, list)
		)

	def test_checkPatencyOfGridList_FalseCollision(self):
		collision = self.grid.Collision(self.primary, self.secondary, canGoThrough=False)
		self.grid.Collisions.append(collision)
>>>>>>> 5ead219... Lot of fixes

		gridPatency = [[100], [0], [100]]

		self.assertEqual(
<<<<<<< HEAD
<<<<<<< HEAD
			self.grid.Collisions.getPatencyOfGridList(self.primary, self.grid.getObjects(), self.grid.getSize()),
=======
			grid.Collisions.getPatencyOfGridList(self.primary, self.grid.getObjects(), self.grid.getSize()),
>>>>>>> 902d453... Some tests
=======
			self.grid.Collisions.getPatencyOfGridList(self.primary, self.grid.getObjects(), self.grid.getSize()),
>>>>>>> 5ead219... Lot of fixes
			gridPatency
		)

	def test_checkPatencyOfGridList_SlowedDownCollision(self):
<<<<<<< HEAD
<<<<<<< HEAD
		collision = self.grid.Collision(self.primary, self.secondary, canGoThrough=True, speed=50)
		self.grid.Collisions.append(collision)
=======
		collision = grid.Collision(self.primary, self.secondary, canGoThrough=True, speed=50)
>>>>>>> 902d453... Some tests
=======
		collision = self.grid.Collision(self.primary, self.secondary, canGoThrough=True, speed=50)
		self.grid.Collisions.append(collision)
>>>>>>> 5ead219... Lot of fixes

		gridPatency = [[100], [50], [100]]

		self.assertEqual(
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
			grid.Collisions.getPatencyOfGridList(self.primary, self.grid.getObjects(), self.grid.getSize()),
			gridPatency
		)
>>>>>>> 902d453... Some tests
=======
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
>>>>>>> 5ead219... Lot of fixes
