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
	gridColor = (255, 255, 255)

	events = {}

	images = {}
	imagesRect = {}

	clock = None

	def __init__(self, grid, size=[200, 200], bg=(0,0,0), cellSize=None):
		self.pygame.init()

		self.grid = grid
		self.bg = bg

		self.setSize(size)

		if cellSize:
			self._setSizeByCell(cellSize)

		self.screen = self.pygame.display.set_mode(self.size)

	def _setSizeByCell(self, cellSize):
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
		for position in self.grid.Timer.pullChanges(): #self.grid.getObjects(): #self.grid.getChanges():
			for object in self.grid.getObjects(pos=position):
				if not object:
					continue

				image = object.getImage()
				key = str(object)+image

				posX, posY = object.getPosition()

				if not key in self.images:
					try:
						self.images[key] = self.pygame.image.load(image)
					except:
						raise IOError('Image was not found')
					self.imagesRect[key] = self.images[key].get_rect()

				self.imagesRect[key].left = self.cellSize[0]*posX
				self.imagesRect[key].top = self.cellSize[1]*posY

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





