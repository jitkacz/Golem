#!/usr/bin/env python
#-*- coding:utf-8 -*-

from grid.findWay import findWay

class Timer(object):
	grid = None

	_time = 0

	_objectsLast = {}
	_queue = {}

	def __init__(self, grid):
		# TODO - check grid instance
		self.grid = grid

	def add(self, object, position):
		"""
		Adding move to Timer.
		"""

		if not self._objectsLast.has_key(object):
			self._objectsLast[object] = 0

		time = self._objectsLast[object]

		start = object.getPosition()
		table = self.grid.Collisions.getPatencyOfGridList(object, self.grid.getObjects(), self.grid.getSize())

		way = findWay(start, position, table)

		if not way:
			return False

		for cell in way:
			self._appendToQueue(object, time, position)
			time = self._objectsLast[object] + self.plusTime(object)

		self._objectsLast[object] = time

	def plusTime(self, object):
		"""
		Function to add time by objects speed
		"""
		return self.grid.fps * object.speed

	def _appendToQueue(self, object, time, position):
		"""
		Adding new position to queue by time
		"""
		if not self._queue.has_key(time):
			self._queue[time] = []

		self._queue[time].append([object, position])

	def check(self):
		"""
		Checking moves saved in the queue by actually time.
		"""
		if self._queue.has_key(self._time):
			self._apply()

		self._time += 1

	def _apply(self):
		"""
		Applying moves saved in the queue
		"""
		moves = self._queue[self._time]

		for move in moves:
			self._move(move[0], move[1])

		del self._queue[self._time]

	def _move(self, object, position):
		"""
		Moving with the objects
		"""
		self._moveObjectToPosition(object, position)
