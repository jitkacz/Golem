#!/usr/bin/env python
#-*- coding:utf-8 -*-

from grid.findWay import findWay

class Timer(object):
	grid = None

	_time = 0

	_objectsLast = {}
	_queue = {}
	_changes = []

	def __init__(self, grid):
		# TODO - check grid instance
		self.grid = grid

	def add(self, object, position):
		"""
		Adding move to Timer.
		"""

		self._queueClean(object)

		if not self._objectsLast.has_key(object):
			self._objectsLast[object] = 0

		time = self._time

		start = object.getPosition()
		table = self.grid.Collisions.getPatencyOfGridList(object, self.grid.getObjects(), self.grid.getSize())

		way = findWay(start, position, table)

		if not way:
			return False

		for cell in way:
			self._appendToQueue(object, time, cell)
			self._objectsLast[object] = time
			time = self._objectsLast[object] + self.plusTime(object, cell)

		return True

	def _queueClean(self, object):
		for move in self._queue:
			for i, objects in enumerate(self._queue[move]):
				if objects[0]==object:
					del self._queue[move][i]

	def plusTime(self, object, position):
		"""
		Function to add time by objects speed
		"""
		time = int((self.grid.fps / object.speed) / (self.grid.getCellSpeed(object, position) / 100.0))


		if time==0:
			time = 1

		return time

	def _appendToQueue(self, object, time, position):
		"""
		Adding new position to queue by time
		"""
		if not self._queue.has_key(time):
			self._queue[time] = []

		self._queue[time].append((object, position))

	def check(self):
		"""
		Checking moves saved in the queue by actually time.
		"""
		#print self._time, sorted(self._queue)[0]

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
		self.addChange(object.getPosition(), position)

		self.grid._moveObjectToPosition(object, position)

	def addChange(self, *positions):
		for position in positions:
			self._changes.append(position)

	def pullChanges(self):
		ret = self._changes
		self._changes = []

		return ret
