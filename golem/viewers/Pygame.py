#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Pygame(object):
	"""
	A module for rendering game by Pygame.
	"""

	import pygame

	size = []
	cellSize = []

	bg = (0, 0, 0)

	screen = None

	status = False

	grid = None
	drawGrid = False
	gridColor = (0, 0, 0)

	events = {}

	images = {}
	imagesRect = {}

	clock = None

	def __init__(self, grid=None, size=[200, 200], bg=(0,0,0), cellSize=None):
		self.bg = bg
		self.size = size
		self.cellSize = cellSize

		if grid:
			self.setGrid(grid)

	def setGrid(self, grid):
		self.grid = grid

		if self.cellSize:
			self.setSizeByCell(self.cellSize)
		else:
			self.setSize(self.size)

	def setSizeByCell(self, cellSize):
		if type(cellSize) is int:
			cellSize = [cellSize]*2

		self.cellSize = cellSize
		cels, rows = self.grid.getSize()
		self.setSize([cellSize[0]*cels, cellSize[1]*rows])

	def setSize(self, size):
		self.size = size

		cols, rows = self.grid.getSize()
		self.cellSize = [(self.size[0]/cols), (self.size[1]/rows)]

	def start(self):
		self.status = True
		self._run()

	def stop(self):
		self.status = False

	def _run(self):
		self.pygame.init()
		self.screen = self.pygame.display.set_mode(self.size)
		self.screen.fill(self.bg)

		while self.status:
			self._checkEvents()

			if self.drawGrid:
				self._drawGrid()

			self._drawObjects()

			self.pygame.display.flip()

	def _drawGrid(self):
		cols, rows = self.grid.getSize()

		for i in range(rows-1):
			posY = self.cellSize[1]*(i+1)
			self.pygame.draw.line(self.screen, self.gridColor, (0, posY), (self.size[0], posY))

		for i in range(cols-1):
			posX = self.cellSize[0]*(i+1)
			self.pygame.draw.line(self.screen, self.gridColor, (posX, 0), (posX, self.size[1]))

	def _drawObjects(self):
		for position in self.grid.Timer.pullChanges():
			for object in self.grid.getObjects(pos=position):
				image = object.getImage()
				if image:
					key = str(object)+image

					if not key in self.images:
						try:
							self.images[key] = self.pygame.image.load(image)
						except:
							raise IOError('Image '+image+' was not found.')
						self.imagesRect[key] = self.images[key].get_rect()

					self.imagesRect[key].left = self.cellSize[0]*position[0]
					self.imagesRect[key].top = self.cellSize[1]*position[1]

					self.screen.blit(self.images[key], self.imagesRect[key])

		self.pygame.time.wait(100)


	def _checkEvents(self):
		for event in self.pygame.event.get():
			code = event.type

			if event.type==self.pygame.KEYUP:
				code = event.key

			if self.events.has_key(code):
				self.events[code]()

	def getMousePosition(self):
		x, y = self.pygame.mouse.get_pos()

		return (x//self.cellSize[0], y//self.cellSize[1])





